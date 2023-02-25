# Python testing examples

### Introduction

This is a simple project to demostrate the Page Object Model implementation with Pytest for Web UI validation testing.

### Libraries

Install all the libraries with the following command

```console
pip install -r requirements.txt
```

### How to

To run this project you could clone this repo and run this command:

```console
python -m pytest
```

To run tests in parallel run this command:

```console
python -m pytest -n auto
```

With this call, pytest will spawn a number of workers processes equal to the number of available CPUs, and distribute the tests randomly across them.
