# Username Validation Automation Test Flow

A small, self-contained username validation module with an automated test
suite and a CI workflow. It has **no external dependencies** — it uses only
the Python standard library.

## Structure

```
username_validation/
├── validator.py            # Validation logic
├── tests/
│   └── test_validator.py   # Automated tests (unittest)
└── README.md
.github/workflows/username-validation-tests.yml   # CI automation
```

## Validation rules

A username is valid when it:

1. Is not empty or only whitespace.
2. Is between 3 and 20 characters long (inclusive).
3. Contains only letters, digits, and underscores.
4. Starts with a letter.
5. Does not end with an underscore.
6. Does not contain consecutive underscores.

## Usage

```python
from validator import validate_username, is_valid_username

validate_username("john_doe")   # (True, "OK")
validate_username("1abc")       # (False, "Username must start with a letter.")
is_valid_username("john__doe")  # False
```

## Running the tests locally

```bash
python -m unittest discover -s username_validation/tests -v
```

Or, if you use pytest:

```bash
pytest username_validation/tests
```

## Automation (CI)

The workflow `.github/workflows/username-validation-tests.yml` runs the test
suite automatically on every push and pull request that touches this module,
and can also be run manually from the GitHub **Actions** tab
(`workflow_dispatch`).
