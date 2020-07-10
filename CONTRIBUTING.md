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
  - [Creating a new release](#creating-a-new-release)

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

Unsure where to start? Try taking a look at issues labeled [![good first issue](https://img.shields.io/github/labels/bsoyka/passwd/good%20first%20issue)](https://github.com/bsoyka/passwd/labels/good%20first%20issue).

#### Formatting and testing

First, make sure you have all the dev dependencies installed:

```console
$ python -m pip install -r requirements.txt
```

This project uses [`autopep8`](https://pypi.org/project/autopep8/) for formatting. To format a file:

```console
$ autopep8 --in-place FILENAME.py
```

This project also uses [`pytest`](https://pypi.org/project/pytest/) for testing. To run all the tests:

```console
$ pytest
```

#### Adding tests

To add tests, create a `test_*.py` file in the `tests/` directory. Follow the format of the previous files and see [this section](#formatting-and-testing) to learn how to run the tests.

## Creating a new release

This checklist is for maintainers when preparing a new release to GitHub and PyPI.

- [ ] Use `bump2version` to update the version string in all files.

```console
$ bumpversion patch
```

- [ ] Use the [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format to add notes to the `CHANGELOG.md` file. Use the new version string generated in the previous step.
- [ ] Reinstall the package for local development with the new version number.

```console
$ python -m pip install -e .
```

- [ ] Run all the tests.

```console
$ pytest
```

- [ ] Commit the changelog and version bump changes
- [ ] Push to GitHub
- [ ] Create a release on GitHub using [this template](https://github.com/bsoyka/passwd/releases/new?tag=vMAJOR.MINOR.PATCH&title=Concise%20release%20title&body=%23%23%23%20Added%0A-%20Release%20notes%20%28copy%20from%20CHANGELOG.md%29). The tag should be named `v{version_string}`. Making a release will automatically push the release to PyPI.
