import ast
import base64
import importlib
import os
import sys
import magic
import mimetypes
import modal
from modal import App, Dict, Image
from fastapi import HTTPException
from pydantic import BaseModel
from typing import Dict, Any, Optional

app = App('code_executor_vectorshift_api') # should be able to make this dynamically set
image = modal.Image.debian_slim()
app.image = Image.debian_slim(python_version="3.11").run_commands(
    "apt-get update",
    "apt-get install -y software-properties-common",
    "apt-add-repository non-free",
    "apt-add-repository contrib",
    "apt-get install libmagic-dev -y",
).pip_install(
    "fastapi[standard]>=0.115.6",
    "pydantic-core==2.23.3",
    "pydantic==2.9.1",
    "aiohttp>=3.11.10",
    "beautifulsoup4>=4.12.3",
    "bokeh>=3.6.2",
    "exifread>=3.0.0",
    "gensim>=4.3.3",
    "imageio>=2.36.1",
    "joblib>=1.4.2",
    "librosa>=0.10.2.post1",
    "matplotlib>=3.9.3",
    "moviepy>=2.1.1",
    "nltk>=3.9.1",
    "numpy>=1.26.4",
    "opencv-python>=4.10.0.84",
    "openpyxl>=3.1.5",
    "pandas>=2.2.3",
    "paypalrestsdk>=1.13.3",
    "pillow>=10.4.0",
    "playwright>=1.49.0",
    "plotly>=5.24.1",
    "praw>=7.8.1",
    "pymongo>=4.10.1",
    "pytest>=8.3.4",
    "python-docx>=1.1.2",
    "pytz>=2024.2",
    "replicate>=1.0.4",
    "requests>=2.32.3",
    "scikit-image>=0.24.0",
    "scikit-learn>=1.5.2",
    "scipy>=1.13.1",
    "scrapy>=2.12.0",
    "scrapy-splash>=0.9.0",
    "seaborn>=0.13.2",
    "selenium>=4.27.1",
    "soundfile>=0.12.1",
    "spacy>=3.7.5",
    "splinter>=0.21.0",
    "textblob>=0.18.0.post0",
    "tornado>=6.4.2",
    "urllib3>=2.2.3",
    "xarray>=2024.11.0",
    "xlrd>=2.0.1",
    "numba==0.60.0",
    "selenium>=4.28.1",
    "webdriver-manager>=4.0.2",
    "python-magic==0.4.27",
)

class CodeExecutionRequest(BaseModel):
    api_key: str
    code: str
    function_name: Optional[str] = None
    inputs: Optional[Dict[str, Any]] = None
    input_schema: Optional[Dict[str, str]] = None
    output_schema: Optional[Dict[str, str]] = None
    
type_name_mapping = {
    'int': 'int',
    'int32': 'int',
    'Integer': 'int',
    'list': 'list',
    'List': 'list',
    'Vec': 'list',
    'vec': 'list',
    'any': 'Any',
    'Any': 'Any',
    'string': 'str',
    'str': 'str',
    'Text': 'str',
    'text': 'str',
    'Bool': 'bool',
    'bool': 'bool',
    'Dict': 'dict',
    'dict': 'dict',
    'Float': 'float',
    'float': 'float',
    'float64': 'float',
    'float32': 'float',
    'file': 'file',
    'File': 'file',
}

# Safe type mapping without using eval()
type_class_mapping = {
    'int': int,
    'str': str,
    'bool': bool,
    'float': float,
    'list': list,
    'dict': dict,
}

restricted_modules = [
    'os',
    'subprocess',
    'sys',
    'importlib',
    'builtins',
    '__main__',
    'open',
    'exec',
    'eval',
    'input',
    'raw_input',
    'cryptography',
    'inspect',
    'gc',
    'ctypes',
    'code',
    'pty',
    'signal',
    'multiprocessing',
    'threading',
]

def check_code_and_add_imports(code):
    banned_functions = [
        'os',
        'subprocess',
        'sys',
        'importlib',
        'builtins',
        '__main__',
        'open',
        'exec',
        'eval',
        'input',
        'raw_input',
        'cryptography',
        'getattr',
        'setattr',
        'delattr',
        'compile',
        '__import__',
        'globals',
        'locals',
        'breakpoint',
        'inspect',
        'gc',
        'ctypes',
        'code',
        'pty',
        'signal',
        'multiprocessing',
        'threading',
    ]

    dangerous_attributes = [
        '__globals__',
        '__builtins__',
        '__code__',
        '__dict__',
        '__class__',
        '__bases__',
        '__subclasses__',
        '__import__',
        '__loader__',
        '__spec__',
        '__build_class__',
        '__cached__',
        '__file__',
        'modules',
        'environ',
        '__wrapped__',
        'func_globals',
    ]

    import_names = set()

    tree = ast.parse(code)
    for node in ast.walk(tree):
        # Check imports
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            if isinstance(node, ast.ImportFrom):
                if node.module in banned_functions:
                    raise ValueError(
                        f"Importing from {node.module} is not allowed inside this version of Sandbox due to security reasons"
                    )
                for alias in node.names:
                    if alias.name in banned_functions:
                        raise ValueError(
                            f"Importing {alias.name} is not allowed inside this version of Sandbox due to security reasons"
                        )
            if isinstance(node, ast.Import):
                for n in node.names:
                    import_names.add(n.name)
            elif isinstance(node, ast.ImportFrom):
                import_names.add(node.module)

        # Check attribute access (obj.attr)
        if isinstance(node, ast.Attribute):
            if node.attr in banned_functions:
                raise ValueError(
                    f"Unsafe attribute {node.attr} is not allowed inside this version of Sandbox due to security reasons"
                )
            if node.attr in dangerous_attributes:
                raise ValueError(
                    f"Access to dangerous attribute {node.attr} is not allowed inside this version of Sandbox due to security reasons"
                )

        # Check function calls
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            if node.func.id in banned_functions:
                raise ValueError(
                    f"Using {node.func.id}() is not allowed inside this version of Sandbox due to security reasons"
                )

        # Check subscript access (obj['attr'] or obj[expr])
        if isinstance(node, ast.Subscript):
            # Check for string literals being used as subscript keys
            if isinstance(node.slice, ast.Constant) and isinstance(node.slice.value, str):
                key = node.slice.value
                if key in banned_functions:
                    raise ValueError(
                        f"Subscript access to '{key}' is not allowed inside this version of Sandbox due to security reasons"
                    )
                if key in dangerous_attributes:
                    raise ValueError(
                        f"Subscript access to dangerous attribute '{key}' is not allowed inside this version of Sandbox due to security reasons"
                    )

    for module in import_names:
        # print("Module found: ", module)
        if module not in sys.modules:
            importlib.import_module(module)

    return import_names

def create_safe_import(allowed_modules):
    """Create a restricted __import__ that only allows pre-validated modules"""
    # __builtins__ can be either a module or a dict depending on context
    if isinstance(__builtins__, dict):
        original_import = __builtins__['__import__']
    else:
        original_import = __builtins__.__import__

    def safe_import(name, globals=None, locals=None, fromlist=(), level=0):
        # Check if this module or its base package was validated during AST check
        base_module = name.split('.')[0]
        if name not in allowed_modules and base_module not in allowed_modules:
            raise ImportError(
                f"Dynamic import of '{name}' is not allowed. Module was not pre-approved during code validation."
            )
        # Use the real __import__ for allowed modules
        return original_import(name, globals, locals, fromlist, level)

    return safe_import

def create_safe_builtins(allowed_modules):
    """Create a restricted __builtins__ dictionary with only safe functions"""
    safe_builtins = {
        # Type constructors
        'int': int,
        'float': float,
        'str': str,
        'bool': bool,
        'list': list,
        'dict': dict,
        'tuple': tuple,
        'set': set,
        'frozenset': frozenset,
        'bytes': bytes,
        'bytearray': bytearray,

        # Iteration and sequences
        'range': range,
        'enumerate': enumerate,
        'zip': zip,
        'map': map,
        'filter': filter,
        'reversed': reversed,
        'sorted': sorted,
        'len': len,
        'slice': slice,

        # Math operations
        'abs': abs,
        'min': min,
        'max': max,
        'sum': sum,
        'round': round,
        'pow': pow,
        'divmod': divmod,

        # Type checking and conversion
        'isinstance': isinstance,
        'issubclass': issubclass,
        'type': type,
        'callable': callable,
        'hasattr': hasattr,
        'hash': hash,
        'id': id,
        'hex': hex,
        'oct': oct,
        'bin': bin,
        'ord': ord,
        'chr': chr,
        'ascii': ascii,
        'repr': repr,
        'format': format,

        # Object operations
        'iter': iter,
        'next': next,
        'all': all,
        'any': any,
        # 'dir': BLOCKED - introspection could reveal attack paths
        # 'vars': BLOCKED - returns __dict__ which could expose internals

        # Other safe builtins
        'print': print,
        'Exception': Exception,
        'ValueError': ValueError,
        'TypeError': TypeError,
        'KeyError': KeyError,
        'IndexError': IndexError,
        'AttributeError': AttributeError,
        'RuntimeError': RuntimeError,
        'StopIteration': StopIteration,
        'ZeroDivisionError': ZeroDivisionError,

        # Allow safe import through our wrapper
        '__import__': create_safe_import(allowed_modules),

        # Explicitly blocked (commented for clarity):
        # 'eval': BLOCKED
        # 'exec': BLOCKED
        # 'compile': BLOCKED
        # 'open': BLOCKED
        # 'getattr': BLOCKED (can bypass attribute checks)
        # 'setattr': BLOCKED (can modify restricted objects)
        # 'delattr': BLOCKED (can delete restricted attributes)
        # '__build_class__': BLOCKED
        # 'breakpoint': BLOCKED
    }

    return safe_builtins

def is_pydantic_serializable(value):
    """Check if the value is Pydantic serializable (a Pydantic model or a primitive type)."""
    if isinstance(value, BaseModel):
        # For Pydantic models, call `.model_dump()` to get serializable fields
        return value.model_dump()
    elif isinstance(value, (str, int, float, bool, list, dict, type(None))):
        # Primitive types are naturally serializable
        return value
    else:
        # If it's a custom object or something more complex, it may not be serializable
        return None

@app.function(secrets=[modal.Secret.from_name("modal-code-executor-api-key")])
@modal.web_endpoint(method="POST")
def main(item: CodeExecutionRequest) -> dict:
    
    """
    Executes Python code provided as a string and returns the resulting variables as a dictionary.

    Args:
        code (str): Python code to execute.

    Returns:
        dict: Dictionary containing variables defined in the code.
    """

    # raise Exception("No no this ain't happening bro")
    modal_api_key = os.environ.get('MODAL_CODE_EXECUTOR_API_KEY', '')
    if item.api_key != modal_api_key:
        raise HTTPException(status_code=401, detail="Unauthorized: Invalid token")

    code = item.code.strip()
    import_names = []
    try:
        import_names = check_code_and_add_imports(code)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    # Create a safe execution environment with restricted builtins
    exec_globals = {
        '__builtins__': create_safe_builtins(import_names),
    }
    # Add only the validated modules to the namespace
    for module in import_names:
        exec_globals[module] = sys.modules[module]
    exec_locals = {}

    # Execute code directly if no additional parameters are provided
    if not (item.function_name and item.inputs and item.input_schema and item.output_schema):
        try:
            exec(code, exec_globals, exec_locals)
            # print("Exec locals: ", exec_locals)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
        serializable_data = {}
        for key, value in exec_locals.items():
            serializable_value = is_pydantic_serializable(value)
            if serializable_value is not None:
                serializable_data[key] = serializable_value
        return {"outputs": serializable_data}

    # Validate presence of all required fields
    if not all([item.function_name, item.inputs, item.input_schema, item.output_schema]):
        raise HTTPException(status_code=400, detail="Missing required fields for function execution")

    # Validate inputs against the schema
    for key, expected_type in item.input_schema.items():
        if key not in item.inputs:
            raise HTTPException(status_code=400, detail=f"Missing input: {key}")
        type_to_check = type_name_mapping.get(expected_type, 'Any')
        if type_to_check == 'Any':
            continue
        if type_to_check == "file":
            item.inputs[key] = item.inputs[key].get("raw_bytes")
            if not item.inputs[key]:
                raise HTTPException(
                    status_code=400, detail=f"Missing content for file input: {key}"
                )
            item.inputs[key] = base64.b64decode(item.inputs[key])
            continue
        expected_class = type_class_mapping.get(type_to_check)
        if expected_class and not isinstance(item.inputs[key], expected_class):
            raise HTTPException(
                status_code=400,
                detail=f"Invalid type for input '{key}': Expected {expected_type}, got {type(item.inputs[key]).__name__}"
            )

    # Execute code
    try:
        exec(code, exec_globals, exec_locals)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    # Validate function existence
    if item.function_name not in exec_locals or not callable(exec_locals[item.function_name]):
        raise HTTPException(status_code=400, detail=f"Function '{item.function_name}' not defined in code")
    
    # Assign the global namespace to the function
    user_function = exec_locals[item.function_name]
    user_function.__globals__.update(exec_globals)

    # Call the function
    try:
        result = user_function(**item.inputs)
    except Exception as e:
        raise HTTPException(status_code=400, detail= f"Error while executing function: {str(e)}")

    # Validate outputs against the schema
    if not isinstance(result, dict):
        raise HTTPException(status_code=400, detail="Function must return a dictionary")
    
    for key, expected_type in item.output_schema.items():
        if key not in result:
            raise HTTPException(status_code=400, detail=f"Missing output: {key}")
        type_to_check = type_name_mapping.get(expected_type, 'Any')
        if type_to_check == 'Any':
            continue
        if type_to_check == "file":
            mime_type = magic.from_buffer(result[key], mime=True)
            file_extension = mimetypes.guess_extension(mime_type)
            result[key] = {
                "raw_bytes": base64.b64encode(result[key]).decode("utf-8"),
                "metadata": {
                    "name": f"File{file_extension}",
                    "mime_type": mime_type,
                },
            }
            continue
        expected_class = type_class_mapping.get(type_to_check)
        if expected_class and not isinstance(result[key], expected_class):
            raise HTTPException(
                status_code=400,
                detail=f"Invalid type for output '{key}': Expected {expected_type}, got {type(result[key]).__name__}"
            )

    return {"outputs": result}