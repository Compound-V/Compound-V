# Page 11

***

## Introduction to Programming & C++

### 1. Concepts to Understand Before Programming

Before diving into code, it is essential to understand how computers actually process instructions.

* **A Computer Program:** A sequence of instructions that directs a computer to perform specific actions in a particular order.
* **Running/Executing:** When a computer executes the actions described by these instructions, we say it is "running" or "executing" the program.
* **Explicit Instruction:** A computer will **not** execute a program on its own — it must be explicitly told to do so.

#### The Hardware Environment

Programs are executed on the computer’s hardware, which consists of the physical components that make up the system:

* **The CPU (Central Processing Unit):** Responsible for executing programs.
* **Memory (RAM):** Where programs are loaded before execution.
* **Interactive Devices:** Monitor, touchscreen, mouse, keyboard, etc., allow a person to interact with the computer.
* **Storage Devices:** Hard drives, SSDs, flash memory, etc., retain information and installed programs even when the system is turned off.

#### Software & Platforms

* **Software:** Refers to the programs that run on top of the hardware.
* **Platform:** Typically refers to the combination of hardware and software that provides an environment for other software to run (e.g., operating systems, browsers, etc.).

> **Types of Programs:**
>
> * **Platform Dependent:** Rely on the specific structure or resources of a certain platform.
> * **Portable:** Can be easily transferred between platforms. The act of modifying a program so that it runs on a different platform is called **porting**.

***

### 2. Machine Language (Machine Code)

Machine language is the native language of the computer—the binary code of 0s and 1s.

* Each instruction is composed of binary digits, or **‘bits’**.
* The number of bits in a machine instruction varies—some CPUs use fixed-size instructions (e.g., 32 bits), while others (like x86 CPUs) use variable-length instructions.
* **Incompatibility:** Each family of compatible CPUs (e.g., x86, ARM64) has its own machine code, which is not compatible with that of other CPU families.
  * This means machine code written for one CPU family cannot run on a different family!
* A CPU family is formally called an **Instruction Set Architecture (ISA)**.
  * Reference: [Comparison of instruction set architectures](https://www.google.com/url?sa=E\&q=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FComparison_of_instruction_set_architectures%23Instruction_sets)

***

### 3. Assembly Language

Assembly language is a more human-readable version of machine language.

* **Mnemonics:** Operations are represented by short names instead of binary.
  * mov — "move", an operation that copies bits from one location to another.
  * al — a specific register name on an x86 CPU (registers are fast memory locations built into the CPU).
  * Numbers can be written conveniently in decimal (97) or hexadecimal (0x61).

**Example:**

```
    mov al, 0x61
; copies the hexadecimal number 0x61 into the CPU register ‘al’.
  
```

#### The Assembler

CPUs cannot directly execute assembly language. It must be translated into machine language by a program called an **assembler**.

* This translation is straightforward because each assembly instruction typically corresponds to a specific machine instruction.
* **Variation:** Just like each CPU family has its own machine language, each also has its own assembly language.
  * There are many assembly languages—conceptually similar, but differing in supported instructions, syntax, and naming conventions.

***

### 4. Introduction to Low-Level Languages

Low-level languages are tailored to the specific Instruction Set Architecture (ISA) they are designed to run on.

**Downsides of Low-Level Languages:**

1. **Not Portable:** Programs are ISA-specific.
2. **High Difficulty:** Writing them requires detailed knowledge of the ISA.
3. **Maintenance Issues:** They are hard to read and maintain; complex programs are difficult to create because these languages provide only primitive capabilities.

***

### 5. Introduction to High-Level Languages

High-level languages were developed to overcome the limitations of low-level languages. Programs written here must be translated into machine language before they can run. This is done via **Compiling** or **Interpreting**.

#### A. Compiling

A **compiler** is a program that reads source code written in one language and translates it into another (usually lower-level) language.

* C++ programs are usually compiled.
* Most C++ compilers can also generate assembly code for inspection.
* **Executable:** The machine code output is packaged into an executable file (e.g., .exe).
* **Distribution:** Running the executable does not require the compiler to be installed on the user's machine.

**The Compiling Process:**

```
                Compiled by             Produces                 Run on               Produces
High-level   ---------------->        ----------->            ------------>          ---------> Program
language          Compiler             Executable               Hardware                        Results
  
```

#### B. Interpreting

An **interpreter** is a program that directly executes the source code without compiling it first.

* Interpreters are flexible but generally less efficient (interpretation happens every time the program runs).
* **Requirement:** The interpreter must be installed on every system where the program executes.

**The Interpreting Process:**

code Textdownloadcontent\_copyexpand\_less

```
                        Interpreted by                 Run On               Produces
High-level language -------------------->            ----------->          -----------> Program
      code                 Interpreter                 Hardware                         Results
  
```

#### C. Compiler vs. Interpreter

> **Reference:** [StackOverflow: Difference between compiled and interpreted languages](https://www.google.com/url?sa=E\&q=https%3A%2F%2Fstackoverflow.com%2Fquestions%2F38491212%2Fdifference-between-compiled-and-interpreted-languages%2F38491646%2338491646)

Neither approach has a definitive advantage over the other.

| **Compilers**                                                                             | **Interpreters**                                                             |
| ----------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **Advantage:** Analyzes entire codebase for deep optimization (faster execution).         | **Advantage:** Starts executing immediately (no compilation delay).          |
| **Advantage:** Translates high-level concepts into efficient low-level memory operations. | **Advantage:** Can apply dynamic optimizations based on runtime behavior.    |
| **Advantage:** CPU executes only program instructions (no overhead).                      |                                                                              |
| **Disadvantage:** Dynamic features (like dynamic typing) are harder to optimize.          | **Disadvantage:** Uses more memory to retain program info at runtime.        |
| **Disadvantage:** Compilation takes time (long startup for development).                  | **Disadvantage:** Slower execution (CPU runs the interpreter + the program). |

***

### 6. Modern Implementations & Hybrid Approaches

Modern runtimes often combine compilation and interpretation for better performance (Hybrid approach).

1. **Java (JVM):** First interprets bytecode, then JIT-compiles (Just-In-Time) frequently used code ("hot code") into machine code. It uses dynamic optimizations like inline caching.
2. **JavaScript Engines:** Start with interpretation for fast startup, then compile hot code for efficiency.
3. **Nature of Languages:** Languages themselves aren't inherently compiled or interpreted—it depends on their implementation.

#### The Futamura Projections

The Futamura projections show that anything that can be interpreted can, in theory, also be compiled.

> **The 3 Projections:**
>
> 1. Specializing the interpreter with a source program gives a **compiled program**.
>    * \[ interpreter + program -> executable ]
> 2. Specializing the specializer (partial evaluator) with the interpreter gives a **compiler**.
>    * \[ specializer + interpreter -> compiler ]
> 3. Specializing the specializer with itself gives a **compiler-generator**.
>    * \[ specializer + itself -> compiler-compiler ]

***

### 7. Benefits of High-Level Languages

1. **Abstraction:** Provides a high level of abstraction from the underlying architecture.
2. **Ease of Use:** Programmers do not need to know much about the specific hardware platform.
3. **Portability:** Programs can be designed to run on multiple platforms (Cross-platform).
4. **Readability:** Easier to read, write, and learn compared to assembly.

**Cross-Platform Compilation Model:**

```
              +---------------------------+
              |   High-level language     |
              |          code             |
              +---------------------------+
              /          |          \
             /           |           \
            v            v            v
+----------------+  +----------------+  +----------------+
| Compiler for   |  | Compiler for   |  | Compiler for   |
| x86 hardware   |  | PowerPC hw     |  | MIPS hardware  |
+----------------+  +----------------+  +----------------+
      |                   |                   |
      v                   v                   v
+----------------+   +----------------+   +----------------+
|  x86 executable|   | PowerPC exec.  |   | MIPS executable|
+----------------+   +----------------+   +----------------+
  
```

#### Portability Considerations

Even in high-level languages, portability is not automatic.

* **Platform-specific features:** Using OS-specific capabilities (like Windows APIs) makes your program less portable.
* **Third-party libraries:** Some libraries work only on specific systems.
* **Compiler extensions:** Using features unique to one compiler (e.g., GCC vs MSVC) can prevent code from compiling elsewhere.
* **Implementation-defined behavior:** Some C++ behaviors vary by compiler.
* **Future-proofing:** Starting with portability in mind saves time if you expand to Mac, Linux, or Consoles later.

***

### 8. Introduction to C/C++

#### History

The **C language** was developed in **1972 by Dennis Ritchie** at Bell Telephone Labs.

* **Goal:** Produce a minimalistic language that was easy to compile, allowed efficient memory access, produced efficient code, and was self-contained.
* **Success:** By 1973, it was so efficient that most of UNIX was rewritten in C.
* **Key Trait:** Excellent portability.

#### Standardization Timeline

* **1983:** ANSI formed a committee to establish a formal standard.
* **1989 (C89/ANSI C):** The first standard was released.
* **1990 (C90):** ISO adopted ANSI C with a few modifications.
* **1999 (C99):** ISO released a revised version, adopting features that had existed as compiler extensions or in C++.

