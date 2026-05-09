# Page 16

## C++ Learning Notes

### 1.1 — Statements and the Structure of a Program

#### Chapter Introduction

This chapter introduces several essential concepts required to understand how C++ programs are structured.\
The concepts are introduced at a basic level and will be explored in more depth in later chapters.

The goal of this chapter is to understand how simple C++ programs are constructed and how they execute.

By the end of this chapter, you should be able to write simple C++ programs and understand their structure.

***

## Statements

A computer program is a sequence of instructions that tells the computer what actions to perform.

A **statement** is an instruction that causes the program to perform some action.

Statements are the most common type of instruction in C++ programs because they represent the **smallest independent unit of computation**.

Statements function similarly to sentences in natural language.\
Just as sentences express ideas in English, statements express actions in a program.

Most C++ statements end with a **semicolon ( ; )**.

Example statement:

```
std::cout << "Hello world!";
```

Important point:

A single high-level language statement may compile into **multiple machine language instructions**.

***

#### Types of Statements in C++

C++ supports several types of statements:

* Declaration statements
* Expression statements
* Jump statements
* Compound statements
* Selection statements (conditionals)
* Iteration statements (loops)
* Try blocks (exception handling)

These will be studied in detail later.

***

## Functions

Statements in C++ are usually grouped together into units called **functions**.

A **function** is a collection of statements that execute sequentially from top to bottom.

Functions are used to perform specific tasks within a program.

Example tasks a function might perform:

* Determining the larger of two numbers
* Calculating a student's grade
* Printing information to the console

Functions are one of the most important organizational tools in programming.

***

## The main Function

Every C++ program must contain a special function named **main**.

Rule:

Every C++ program must contain exactly one function called **main**.

The **main function** acts as the entry point of the program.

When a program is executed:

1. Execution begins at the start of the `main` function.
2. Statements inside `main` execute sequentially.
3. When the last statement of `main` finishes, the program terminates.

Example structure of a minimal program:

```
int main()
{

}
```

***

## Function Naming Convention

When referring to functions in writing, parentheses are often added to the name.

Example:

```
main()
calculateGrade()
printEmployee()
```

This notation distinguishes functions from other entities such as variables.

In programming terminology, the name of a function (or variable, type, etc.) is called its **identifier**.

***

## Characters and Text

Early computers primarily handled numerical calculations and data processing.

As computing evolved, computers became important tools for written communication.

The basic unit of written communication is the **character**.

A **character** is a single written symbol such as:

```
a
2
$
=
```

Characters are generated when keys are pressed on a keyboard and can be displayed on a screen.

***

#### Text and Strings

A sequence of characters forms **text**.

In programming, a sequence of characters is called a **string**.

Example of text:

```
Hello world
```

C++ programs themselves are written as **plain text files**.

Plain text contains only standard characters without formatting such as bold or italics.

***

#### Control Characters

Computers also support **control characters**, which perform special actions instead of displaying visible symbols.

Examples:

| Character | Function                    |
| --------- | --------------------------- |
| Tab       | Inserts spacing             |
| Backspace | Deletes previous character  |
| Escape    | Special control instruction |

These characters control formatting or system behavior.

***

## Dissecting the Hello World Program

Example program:

```
#include <iostream>

int main()
{
    std::cout << "Hello world!";
    return 0;
}
```

Explanation of each line:

***

#### Line 1

```
#include <iostream>
```

This is a **preprocessor directive**.

It tells the compiler to include the **iostream library**.

The iostream library enables input and output operations such as printing text to the console.

Without this line, the compiler would not recognize `std::cout`.

***

#### Line 2

Blank line.

This line exists only to improve readability.\
The compiler ignores blank lines.

***

#### Line 3

```
int main()
```

This line defines the **main function**.

`int` indicates the function returns an integer value.

***

#### Lines 4 and 7

```
{
}
```

Curly braces define the **function body**.

All statements inside these braces belong to the function.

***

#### Line 5

```
std::cout << "Hello world!";
```

This statement outputs text to the console.

Components involved:

`std::cout`\
Standard output stream used for printing characters.

`<<`\
Insertion operator used to send data to the output stream.

`"Hello world!"`\
A string literal containing the text to be printed.

***

#### Line 6

```
return 0;
```

This is a **return statement**.

It ends the function and sends a value back to the operating system.

Returning `0` indicates that the program executed successfully.

***

#### Program Output

When this program is executed, the console displays:

```
Hello world!
```

***

## Syntax

In any language, rules determine how elements must be arranged.

These rules are called **syntax**.

Example of incorrect English syntax:

"My house painted is blue"

The sentence contains correct words but in an incorrect arrangement.

Programming languages also have strict syntax rules.

C++ programs must follow these rules exactly.

***

## Syntax Errors

A **syntax error** occurs when code violates the syntax rules of the language.

Example with missing semicolon:

```
std::cout << "Hello world!"
return 0;
```

Compiler error example:

```
error: expected ';' after expression
```

The compiler stops compilation when a syntax error is detected.

The program cannot run until the error is fixed.

***

#### Compiler Error Location

Sometimes the compiler reports an error on the line **after the actual mistake**.

Example:

If a semicolon is missing on line 5, the compiler might report an error on line 6.

Reason:

The compiler only detects the issue when it encounters the next unexpected token.

Therefore, when debugging syntax errors:

If the reported line looks correct, check the **previous line**.

***

## Key Concepts Summary

Statement - A single instruction that performs an action in a program.

Function - A group of statements executed sequentially to perform a task.

Main Function - The entry point of every C++ program.

Character - A single symbol such as a letter, number, or punctuation mark.

String - A sequence of characters forming text.

Syntax - The rules that determine how code must be written.

Syntax Error - An error that occurs when code violates language syntax rules.

C++ Standard Library - A collection of prewritten functionality (such as input/output, containers, algorithms, etc.) that programmers can use in their programs.

***
