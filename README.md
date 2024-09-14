# Python `.pyc` Decompiler with Chainlit Interface

This project demonstrates how to decompile Python `.pyc` files back into human-readable Python source code using the Chainlit chat interface. It leverages Python's `uncompyle6` library to reverse the compilation process and display the result in a chat interface.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [How to Use](#how-to-use)
- [Project Structure](#project-structure)

## Overview

This project uses **Python 3.12** for the Chainlit interface and general project development but requires **Python 3.8** for compiling `.py` files into `.pyc` files. This is because the `uncompyle6` library can only decompile `.pyc` files created with Python 3.8.

Once the `.pyc` file is uploaded to the Chainlit interface, the project decompiles it into readable Python source code and displays it in the chat.

## Prerequisites

1. **Python 3.12**: Main Python version for running Chainlit and other functionality.
2. **Python 3.8**: Required to compile `.py` files into `.pyc` files.
3. **Manual installation of required libraries**:
   - `chainlit`
   - `uncompyle6` (installed separately for both Python 3.12 and Python 3.8)

You must manually install the required libraries for each version of Python. For example:

### For Python 3.12
```bash
pip install chainlit
pip install uncompyle6
```
### For Python 3.8
```bash
python3.8 -m pip install uncompyle6
```
## How to Use

### 1. Compile Python `.py` File to `.pyc`

Before you can decompile a `.pyc` file, you must first compile a Python `.py` file using **Python 3.8**. This is because `uncompyle6` only supports decompiling `.pyc` files created by Python 3.8.

To compile a Python file into a `.pyc` file, use the following command:

```bash
python3.8 -m compileall your_script.py
```
This will generate a `.pyc` file in the `__pycache__` directory, typically named like `your_script.cpython-38.pyc`.
### 1. Run the Chainlit Interface

Ensure that you have **Python 3.12** installed and that the required libraries are installed for this version. Then, run the Chainlit interface by executing:

```bash
chainlit run app.py
```
### 3. Upload `.pyc` File

- Once the Chainlit interface is running, you will be prompted to upload a `.pyc` file.
- Navigate to the `__pycache__` directory where your compiled `.pyc` file is located (it should be something like `your_script.cpython-38.pyc`).
- Upload the `.pyc` file using the Chainlit interface.

### 4. View Decompiled Code

- After uploading the `.pyc` file, the app will decompile the bytecode and display the human-readable Python source code directly in the chat window.
- You can review the decompiled code or use it for debugging purposes.

### 5. Manually Install Libraries

Since this project does not use a `requirements.txt` file, you need to manually install all required libraries for both Python 3.12 and Python 3.8.

#### For Python 3.12 (Used for Running Chainlit):
```bash
pip install chainlit
pip install uncompyle6
```
## Project Structure

The project has the following structure:
```
.
├── app.py              # Main application file for the Chainlit interface
├── decompile.py        # Contains the decompilation logic using uncompyle6
└── __pycache__         # Directory where the compiled .pyc files will be stored
```

### Description of Files:
- **app.py**: This file contains the Chainlit interface logic. It prompts users to upload a `.pyc` file, calls the decompilation function from `decompile.py`, and displays the decompiled source code.
- **decompile.py**: This file defines the `decompile_pyc()` function, which uses `uncompyle6` to decompile `.pyc` files and returns the decompiled source code as a string.
- **__pycache__/**: This directory is where Python stores the compiled `.pyc` files. After compiling a `.py` file with Python 3.8, the resulting `.pyc` file is saved here.
- **chainlit.md**: Project documentation that explains how to set up, use, and run the project.
