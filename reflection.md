# Reflection – Lab 5: Static Code Analysis

In this lab, I learned how to use Bandit, Pylint, and Flake8 to identify and fix security vulnerabilities, code quality issues, and style violations in Python code.

Bandit helped me identify security risks such as unsafe use of `eval()`, weak hashing with MD5, insecure random number generation, shell command execution, and hardcoded credentials. I fixed these issues by using safer alternatives such as SHA-256, the `secrets` module, and Python's built-in file handling.

Pylint helped me improve code quality by identifying missing docstrings, naming convention problems, unused variables, and other coding practices that needed improvement. After making the changes, I achieved a score of 9.64/10.

Flake8 helped me identify formatting problems, including whitespace errors, long lines, and unused imports. After correcting these issues, the final Flake8 report showed no style violations.

Overall, this lab taught me that static code analysis is an important part of software development. It helps detect potential problems before a program is executed and encourages writing safer, cleaner, and more maintainable code. I also learned that using multiple analysis tools provides a more complete evaluation of a program.