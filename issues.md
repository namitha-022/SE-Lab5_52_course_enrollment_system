# Issues Identified and Fixed

## 1. Bandit — Security Issues

The initial Bandit analysis identified the following security issues:

- **B110 — Try/Except/Pass:** Exceptions were silently ignored.
- **B307 — Use of `eval()`:** Evaluating user-provided expressions could execute unsafe code.
- **B324 — Insecure Hash Function:** MD5 was used for generating student hashes.
- **B311 — Insecure Randomness:** `random.randint()` was used to generate enrollment OTPs.
- **B605 — Shell Command Execution:** `os.system()` was used to execute a shell command.
- **B105 — Hardcoded Password/String:** A registrar authentication token was hardcoded in the source code.

### Fixes Applied

- Removed the unsafe `eval()` expression and used a numeric discount rate with validation.
- Replaced MD5 with SHA-256 for student hash generation.
- Replaced `random.randint()` with `secrets.randbelow()` for OTP generation.
- Removed shell command execution and used normal Python file handling.
- Removed the hardcoded registrar token.
- Removed the bare exception handler that silently ignored errors.

**Final result:** Bandit reported no issues identified.

## 2. Pylint — Code Quality Issues

The initial Pylint analysis identified several code quality problems:

- Missing module and function docstrings.
- Mutable default argument in the enrollment function.
- Use of a global variable for tuition tracking.
- Poor naming conventions.
- Unused imports and variables.
- Broad exception handling.
- Unsafe use of `eval()`.
- File handling and code readability issues.
- Code formatting problems.

### Fixes Applied

- Added docstrings to explain functions.
- Replaced the mutable default argument with `None` and initialized the list inside the function.
- Improved variable and function naming.
- Removed unused imports and variables.
- Removed unsafe evaluation and broad exception handling.
- Improved file handling and readability.

**Final result:** Pylint score of **9.64/10**, exceeding the target of 9.5/10.

## 3. Flake8 — Style Issues

The initial Flake8 analysis identified style violations, including:

- Unused imports.
- Lines exceeding the recommended length.
- Bare exception handling.
- Unused variables.
- Incorrect comparison with `None`.
- Missing newline at the end of the file.
- Whitespace issues.

### Fixes Applied

- Removed unused imports and variables.
- Split long lines across multiple lines.
- Corrected whitespace and formatting.
- Used `is None` for `None` comparisons.
- Added the required final newline.

**Final result:** Flake8 reported no style violations.

## Conclusion

Static code analysis was performed using Bandit, Pylint, and Flake8. The identified security, code quality, and style issues were addressed, and the final reports were generated to document the improvements.