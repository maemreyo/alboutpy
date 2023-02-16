# Chapter 8 - Pythonic Productivity Techniques

## 1. Exploring Python Modules and Objects
- Use the built-in `dir()` function to interactively explore Python modules and classes from an interpreter session.
- The `help()` built-in lets you browse through the documentation right from your interpreter.

## 2. Isolating Project Dependencies With Virtualenv
### Virtual Environment to the Rescue
- A virtual environment allows you to separate Python dependencies by project and give you the ability to select between
different versions of the Python interpreter.
- A virtual environment is an isolated Python environment that helps you avoid version conflicts between packages and 
different versions of the Python runtime.
- As a best practice, all of your Python projects should use a virtual environment to store their dependencies.

## 3. Peeking Behind the Bytecode Curtain
- CPython executes programs by first translating them into an intermediate bytecode and then running the bytecode on a 
stackbased virtual machine.
- You can use the built-in dis module to peek behind the scenes and inspect the bytecode.
- Study up on virtual machines—it’s worth it.

