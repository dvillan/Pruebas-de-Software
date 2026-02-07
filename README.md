# Software Testing and Quality Assurance repo 
David Emmanuel Villanueva Martinez

This repo uses uv as package manager, uv is an extremely fast package and project manager and acts as replacement to other tools like pip, pipx, venv, etc.

You can find the instructions for installing uv in: https://docs.astral.sh/uv/

## Usage

### Running scripts using UV package manager 
The first step is to syncronize the environment using: 
```bash
uv sync
```
This will update all necessary libraries and packages needed for the project 

Then we can start running project scripts with: 
```bash
uv run computeStatistics.py
```

### Validation Testing 

This project has testing functionality using Pytest library, it's a simple way to validate results "on the fly", it only supports testing convertNumbers.py script for the moment, you can run tests using: 

```bash
uv run pytest test_conver_numbers.py 
```


