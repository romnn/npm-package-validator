## npm-package-validator

[![Test Status](https://github.com/romnn/npm-package-validator/workflows/test/badge.svg)](https://github.com/romnn/npm-package-validator/actions)
[![PyPI version](https://img.shields.io/pypi/v/npm_package_validator.svg)](https://pypi.python.org/pypi/npm_package_validator)
[![License](https://img.shields.io/github/license/romnn/npm-package-validator)](https://github.com/romnn/npm-package-validator)
[![Test Coverage](https://codecov.io/gh/romnn/npm-package-validator/branch/master/graph/badge.svg)](https://codecov.io/gh/romnn/npm-package-validator)

This is a python implementation of the official [`npm/validate-npm-package-name`](https://github.com/npm/validate-npm-package-name) package
for validating npm package names.

```bash
$ pip install npm_package_validator
```

#### CLI Usage

```bash
$ npm_package_validator my-package
```

#### Programmatic usage

Validate an npm package name like this:

```python
import npm_package_validator
# Fails! Uppercase is not allowed for new packages
assert npm_package_validator.valid_new_package('MY-package')
```

However, upper case names used to be allowed and so validating as an old, existing package succeeds:

```python
assert npm_package_validator.valid_old_package('MY-package')  # Succeeds!
```

When using the CLI, you can use the `--old` flag.
 
If you want to know whats wrong with a name, use:

```python
from npm_package_validator.validate import validate_package
errors, warnings = validate_package('MY-package')
print("Errors: %s" % ", ".join(errors))
print("Warnings: %s" % ", ".join(warnings))
```

A valid new package name must have neither `errors` nor `warnings`.
Existing packages can have `warnings`, as the npm validation rules have become stricter over time.

#### Acknowledgements

The official javascript implementation [`npm/validate-npm-package-name`](https://github.com/npm/validate-npm-package-name).

#### Development

All of this happens when you run ``invoke pre-commit``.
