# Flask React Blog
> This is a simple Blog built with React and Flask.

[![NPM Version][npm-image]][npm-url]
[![Build Status][travis-image]][travis-url]
[![Downloads Stats][npm-downloads]][npm-url]
[![security: bandit][bandit-image]][bandit-url]
[[![Imports: isort][isort-image]][isort-url]
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

This Blog app enables a blogger to add new blog posts or view published blog posts.

![](header.png)

## Installation

### Clone the [Flask React Blog repo](https://github.com/twyle/flask-react-blog-simple.git)

```sh
git clone https://github.com/twyle/flask-react-blog-simple.git
```

### Navigate into the cloned repo

```sh
cd flask-react-blog-simple
```

### Create a Python3 Virtual Environment.

OS X & Linux:

```sh
python3 -m venv venv
```

Windows:

```sh
python3 -m venv venv
```

### Activate the Virtual Environment.

OS X & Linux:

```sh
source venv/bin/activate
```

Windows:

```sh
venv\\Scripts\\Activate
```

### Install the Project dependencies.

```sh
make install
```

### Run the application.

```sh
make run
```

## Usage example

A few motivating and useful examples of how your product can be used. Spice this up with code blocks and potentially more screenshots.

_For more examples and usage, please refer to the [Wiki][wiki]._

## Development setup

Here is how to setup your development environment incase you want to play around with this project.

### Install the development dependencies (make sure you have set up the virtual environment as stated above and are in the project folder)

```sh
make install-dev
```

### Run the unit tests

```sh
make test
```

## Release History

## v0.2.0 (2022-04-06)

### Feat

- added the front-end.

## v0.1.0 (2022-04-06)

### Fix

- fixed the tag versioning.
- fixed the workflow deployments.
- added the app-dir directive.

### Feat

- added new divide functionality
- added the header photo.
- renamed the workflows.
- initial commit.


## Meta

Lyle Okoth – [@lylethedesigner](https://twitter.com/lylethedesigner) on twitter – [lyle okoth](https://medium.com/@lyle-okoth) on medium, and my email is lyceokoth@gmail.com

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/twyle/github-link](https://github.com/twyle/)

## Contributing

1. Fork it https://github.com/twyle/flask-react-blog-simple/fork
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki
[bandit-image]: https://img.shields.io/badge/security-bandit-yellow.svg
[bandit-url]: https://github.com/PyCQA/bandit
[isort-image]: https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336
[isort-url]: https://pycqa.github.io/isort/