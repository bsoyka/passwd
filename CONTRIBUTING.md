# Contributing to passwd
:tada: First off, thanks for taking the time to contribute! :tada:

- [Contributing to passwd](#contributing-to-passwd)
  - [Code of conduct](#code-of-conduct)
  - [Ask questions on Gitter](#ask-questions-on-gitter)
  - [How to contribute](#how-to-contribute)
    - [Reporting bugs](#reporting-bugs)
    - [Suggesting enhancements](#suggesting-enhancements)
    - [Submitting a good issue](#submitting-a-good-issue)
    - [Making code contributions](#making-code-contributions)
      - [Your first contribution](#your-first-contribution)
      - [Formatting and testing](#formatting-and-testing)
      - [Adding tests](#adding-tests)

## Code of conduct
This project is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## Ask questions on Gitter
[![Gitter](https://badges.gitter.im/bsoyka/passwd.svg)](https://gitter.im/bsoyka/passwd)

If you just have a quick question, you can ask in our [Gitter room](https://gitter.im/bsoyka/passwd)! This helps keep issues on GitHub nice and tidy.

Please note that it may take a while to get a response on Gitter &mdash; please be patient!

## How to contribute
All contributions are welcome! Please make sure to read the section on [how to submit a good issue](#submitting-a-good-issue) before clicking `Submit` on GitHub.

### Reporting bugs
Bugs are tracked as GitHub [Issues](https://guides.github.com/features/issues/). You can open a new issue [right here](https://github.com/bsoyka/passwd/issues/new/choose).

### Suggesting enhancements
This includes completely new features and minor enhancements to existing code. Enhancements are also tracked as GitHub [Issues](https://guides.github.com/features/issues/). You can open a new issue [right here](https://github.com/bsoyka/passwd/issues/new/choose).

### Submitting a good issue
- Use a clear and descriptive title
- Provide code samples whenever possible (for bug reports)
  - Give [minimal, reproducible examples](https://stackoverflow.com/help/minimal-reproducible-example)
  - Use Markdown [code blocks](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax#quoting-code)
- Give as much detail as possible in as few words as possible
  - Keep it concise

### Making code contributions

#### Your first contribution
Unsure where to start? Try taking a look at these [good first issues](https://github.com/bsoyka/passwd/labels/good%20first%20issue).

#### Formatting and testing
This project uses [`autopep8`](https://pypi.org/project/autopep8/) for formatting. To format a file:

```sh
$ python -m pip install --upgrade autopep8

$ autopep8 --in-place FILENAME.py
```

This project also uses [`pytest`](https://pypi.org/project/pytest/) for testing. To run all the tests:

```sh
$ python -m pip install --upgrade pytest

$ python -m pip install -e .

$ pytest
```

#### Adding tests
To add tests, create a `test_*.py` file in the `tests/` directory. Follow the format of the previous files and see [this section](#formatting-and-testing) to learn how to run the tests.