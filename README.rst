===============================
npm-package-validator
===============================

.. image:: https://travis-ci.com/romnnn/npm-package-validator.svg?branch=master
        :target: https://travis-ci.com/romnnn/npm-package-validator
        :alt: Build Status

.. image:: https://img.shields.io/pypi/v/npm_package_validator.svg
        :target: https://pypi.python.org/pypi/npm_package_validator
        :alt: PyPI version

.. image:: https://img.shields.io/github/license/romnnn/npm-package-validator
        :target: https://github.com/romnnn/npm-package-validator
        :alt: License

.. image:: https://codecov.io/gh/romnnn/npm-package-validator/branch/master/graph/badge.svg
        :target: https://codecov.io/gh/romnnn/npm-package-validator
        :alt: Test Coverage

""""""""

This python package allows you to validate npm package names.
It is a python implementation of the official `npm/validate-npm-package-name <https://github.com/npm/validate-npm-package-name>`_ package for javascript.

.. code-block:: console

    $ pip install npm_package_validator

CLI Usage
----------

.. code-block:: console

    $ npm_package_validator my-package

Programmatic usage
-------------------

Validate an npm package name like this:

.. code-block:: python

    import npm_package_validator
    # Fails! Uppercase is not allowed for new packages
    assert npm_package_validator.valid_new_package('MY-package')

However, upper case once has been allowed and you can also validate old, existing packages:

.. code-block:: python
    
    assert npm_package_validator.valid_old_package('MY-package')  # Succeeds!

When using the CLI, you can use the ``--old`` flag.
 
If you want to know whats wrong with a name, use:

.. code-block:: python

    from npm_package_validator.validate import validate_package
    errors, warnings = validate_package('MY-package')
    print("Errors: %s" % ", ".join(errors))
    print("Warnings: %s" % ", ".join(warnings))

A valid new package name must have neither ``errors`` nor ``warnings``.
Existing packages can have ``warnings``, 
as the npm validation rules have become stricter over time.

Credits
--------

This package is a port from the official `npm/validate-npm-package-name <https://github.com/npm/validate-npm-package-name>`_

Development
-----------

For detailed instructions see `CONTRIBUTING <CONTRIBUTING.rst>`_.

Tests
~~~~~~~
You can run tests with

.. code-block:: console

    $ invoke test
    $ invoke test --min-coverage=90     # Fail when code coverage is below 90%
    $ invoke type-check                 # Run mypy type checks

Linting and formatting
~~~~~~~~~~~~~~~~~~~~~~~~
Lint and format the code with

.. code-block:: console

    $ invoke format
    $ invoke lint

All of this happens when you run ``invoke pre-commit``.

Note
-----

This project is still in the alpha stage and should not be considered production ready.
