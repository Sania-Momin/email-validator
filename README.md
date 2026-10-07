# Email Validator in Python

A simple Python program built to validate email address syntax based on custom structural and formatting rules.

## Features

The script checks whether an entered email address satisfies the following criteria:

- **Minimum Length:** Email must be at least 6 characters long.
- **Starting Character:** Must start with an alphabetic letter (`a-z`, `A-Z`).
- **`@` Symbol Check:** Must contain exactly one `@` symbol.
- **Domain Extension Position:** Must have a `.` dot at either the 3rd or 4th position from the end (e.g., `.com`, `.in`).
- **Forbidden Characters & Formatting:**
  - No whitespace/spaces allowed.
  - No uppercase letters allowed (must be lowercase).
  - No unapproved special characters (only letters, numbers, `_`, `.`, and `@` are permitted).
