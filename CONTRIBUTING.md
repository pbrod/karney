# Contributing

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

## Types of Contributions

### Report Bugs

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

### Write Documentation

You can never have enough documentation! Please feel free to contribute to any
part of the documentation, such as the official docs, docstrings, or even
on the web in blog posts, articles, and such.

### Submit Feedback

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

## Get Started!

Ready to contribute? Here's how to set up `karney` for local development.

1. Download a copy of `karney` locally.
2.  Install `pdm`:

    ```console
    $ pip install pdm
    ```

3.  Install `karney` and its development dependencies:

    ```console
    $ pdm install -dG dev
    ```

4.  Use `git` (or similar) to create a branch for local development and make your changes:

    ```console
    $ git checkout -b name-of-your-bugfix-or-feature
    ```

5.  When you're done making changes, check that your changes conform to any code formatting requirements and pass any tests:

    ```console
    $ pdm check-style
    $ pdm run pytest --doctest-modules
    ```

6. Commit your changes with conventional commit messages:
    When you make changes to the codebase, follow the "Angular" conventional commit message format. This format is specified in your `pyproject.toml` and is crucial for `python-semantic-release` to determine the version bump. The structure of a commit message is:

    ```
    <type>(<scope>): <subject>
    ```

    *   `<type>`: This is the most important part for versioning. Based on your configuration, the following types will trigger a release:
        *   `feat`: A new feature (triggers a **minor** release, e.g., 1.0.10 -> 1.1.0)
        *   `fix`: A bug fix (triggers a **patch** release, e.g., 1.0.10 -> 1.0.11)
        *   `perf`: A code change that improves performance (triggers a **patch** release)
    *   Other allowed types like `build`, `chore`, `ci`, `docs`, `style`, `refactor`, and `test` will be included in the changelog but will not trigger a version bump on their own.

7.  Open a pull request.

## Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include additional tests if appropriate.
2. If the pull request adds functionality, the docs should be updated.
3. The pull request should work for all currently supported operating systems and versions of Python.

## Code of Conduct

Please note that the `karney` project is released with a
Code of Conduct. By contributing to this project you agree to abide by its terms.