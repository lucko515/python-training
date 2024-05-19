# Test CRM Utils

A simple package to interact with a toy CRM.

## Installation

```bash
pip install test-crm-utils
```

NOTE: Create `requirements.txt` if you have any dependencies (for this example, we'll keep it empty).

#### Step 1: Build the Package

Make sure you have `setuptools` and `wheel` installed:

```bash
pip install setuptools wheel
```

Build the package:

```bash
python setup.py sdist bdist_wheel
```

#### Step 2: Upload the Package to PyPI

First, install `twine`:

```bash
pip install twine
```

Upload the package to PyPI:

```bash
twine upload dist/*
```

You will be prompted to enter your PyPI username and password. After successful upload, your package will be available on PyPI.

### Summary

By following these steps, you will have created a simple Python package for interacting with Salesforce, built the package, and uploaded it to PyPI. This is a practical exercise for Salesforce employees to understand Python packaging and distribution.

If you need any further customization or additional features for the package, let me know!