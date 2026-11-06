# AIN7301 – Python Programming

Welcome to the practical workspace for **AIN7301 – Python Programming** in the
Master in Artificial Intelligence & Applied Data Science program.

## Project purpose

This workspace contains small, focused examples for learning Python and a
fictional UAE retail dataset for practice. The Week 1 examples use Python's
standard library, so no third-party package is needed to run them.

The included `sales.csv` is **synthetic educational data**. It does not describe
real businesses, customers, or transactions.

## Prerequisites

- Windows 10 or later
- Python 3.10 or later (this workspace was checked with Python 3.12.8)
- Visual Studio Code
- The Microsoft **Python** extension for VS Code
- Git (optional, but useful for tracking your work)

Download Python from [python.org](https://www.python.org/downloads/). During
installation on Windows, enable **Add python.exe to PATH** if that option is
shown.

## Set up the environment

The project virtual environment is named `.venv`. It keeps this workspace's
Python packages separate from other projects and from system Python.

From the workspace folder, activate it in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can run Python without activating:

```powershell
.\.venv\Scripts\python.exe --version
```

To install packages listed in `requirements.txt`:

```powershell
python -m pip install -r requirements.txt
```

There are no third-party dependencies required for the initial Week 1
fundamentals. `print`, variables, conditions, loops, functions, and CSV/file
handling used here are provided by Python's **standard library**. Packages such
as NumPy, pandas, Matplotlib, Seaborn, Requests, scikit-learn, and Jupyter are
third-party libraries; add them only when a later session requires them.

## Select the interpreter in VS Code

1. Install the Microsoft **Python** extension if it is not already installed.
2. Open this project folder in VS Code.
3. Press `Ctrl+Shift+P`, run **Python: Select Interpreter**, and select the
   interpreter inside `.venv`.
4. The workspace settings point to `.venv` by default. In the integrated
   terminal, environment activation is enabled.

The Python extension provides interpreter selection and Python support. Pylance
provides Python diagnostics and analysis; the Black Formatter extension enables
the configured Python format-on-save behavior.

## Run a Python file

With the virtual environment activated:

```powershell
python .\Week_01_Python_Fundamentals\01_hello_world.py
```

Or, without activation:

```powershell
.\.venv\Scripts\python.exe .\Week_01_Python_Fundamentals\01_hello_world.py
```

## Verify the environment

From the workspace folder, run:

```powershell
python .\environment_check.py
```

Without activation, use:

```powershell
.\.venv\Scripts\python.exe .\environment_check.py
```

The check reports the Python executable and pip status, and identifies which
optional learning libraries are present. Missing optional libraries do not
prevent the Week 1 standard-library exercises from running.

## Project structure

```text
AIN7301_Python_Programming/
├── .gitignore
├── .vscode/
│   └── settings.json
├── README.md
├── requirements.txt
├── environment_check.py
├── Week_01_Python_Fundamentals/
│   ├── 01_hello_world.py
│   ├── 02_comments_and_syntax.py
│   ├── 03_variables.py
│   ├── 04_data_types.py
│   ├── 05_operators.py
│   ├── 06_conditional_statements.py
│   ├── 07_loops.py
│   ├── 08_functions.py
│   ├── 09_file_handling.py
│   ├── 10_debugging.py
│   └── data/
│       └── sales.csv
├── Week_02_Data_Structures/
├── Week_03_Data_Analysis/
├── Week_04_APIs_and_Data_Collection/
└── Week_05_Final_Project/
```

Future-week folders are intentionally empty until their course material is
provided.

## Troubleshooting

- **`python` is not recognized:** use the `.venv` executable shown above, or
  reinstall Python from python.org and enable the PATH option.
- **The wrong Python version is selected:** use **Python: Select Interpreter**
  and choose `.venv`; reopen the terminal after changing interpreters.
- **PowerShell says script execution is disabled:** do not change a system-wide
  policy for this course. Run the `.venv\Scripts\python.exe` directly instead.
- **A future import reports `ModuleNotFoundError`:** check the package name in
  `requirements.txt`, then install it into this environment with
  `python -m pip install package-name`.
- **CSV file cannot be found:** open the project folder as the VS Code
  workspace. The file-handling example builds the CSV path relative to its own
  location.
