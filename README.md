# Python testing examples

### Introduction

This is a simple project to demostrate the Page Object Model implementation with Pytest for Web UI validation testing.

### Libraries

Install all the libraries with the following command

```console
pip install -r requirements.txt
```

### How to

To run ui tests in parallel use this command:

```console
pytest -n auto -m "not serial"
```

With this call, pytest will spawn a number of workers processes equal to the number of available CPUs, and distribute the tests randomly across them.

To run api tests serial use this command:

```console
export API_TOKEN=<your-api-token-here> && python -m pytest -n0 -m "serial"
```
