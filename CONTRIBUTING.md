# Contributing

Contributions are welcome and greatly appreciated. Every contribution, no matter how small, helps improve the project.

## Types of Contributions

### Report Bugs

If you are reporting a bug, please include:

- Your operating system and version.
- Your Python version.
- Any relevant details about your local environment.
- Detailed steps to reproduce the issue.
- The expected and actual behavior.

### Fix Bugs

Browse the GitHub issue tracker for issues labeled **bug** and **help wanted**.

### Implement Features

Browse the GitHub issue tracker for issues labeled **enhancement** and **help wanted**.

### Improve Documentation

Documentation improvements of any size are welcome, including:

- User guides
- Tutorials
- API documentation
- Docstrings
- Examples
- Blog posts and articles

### Submit Feedback

If you are proposing a new feature:

- Explain clearly what problem it solves.
- Describe how it would work.
- Keep the scope as focused as possible.
- Remember that this is a volunteer-driven project.

## Getting Started

Ready to contribute? Follow these steps to set up a local development environment.

### 1. Fork and Clone the Repository

Fork the repository on GitHub and clone your fork locally:

```console
git clone https://github.com/<your-github-username>/karney.git
cd karney
```

### 2. Install PDM

```console
pip install pdm
```

### 3. Install Dependencies

Install the package together with development dependencies:

```console
pdm install -dG test -G docs -G dev
```

### 4. Create a Branch

Create a branch for your changes:

```console
git checkout -b name-of-your-feature
```

Examples:

```console
git checkout -b fix-geodesic-edge-case
git checkout -b add-example-notebook
```

### 5. Make Your Changes

Implement your changes and add or update tests and documentation as needed.

### 6. Run Quality Checks

Before submitting a pull request, ensure that all checks pass:

```console
pdm format --check
pdm check-style
pdm check-types
pdm test
```

If any command reports an error, please resolve it before opening a pull request.

### 7. Commit Your Changes

Please use Conventional Commit messages whenever practical:

```text
<type>(<scope>): <subject>
```

Examples:

```text
feat(core): add support for custom ellipsoids
fix(geodesic): correct azimuth calculation near poles
docs: update installation instructions
test(core): add regression test for issue 42
```

Common commit types include:

- `feat` – new functionality
- `fix` – bug fixes
- `docs` – documentation updates
- `test` – test improvements
- `refactor` – code improvements without behavior changes
- `perf` – performance improvements
- `ci` – CI/CD changes
- `build` – packaging or build-system changes
- `chore` – maintenance tasks
- `style` – formatting or style-only changes

### 8. Open a Pull Request

Push your branch to GitHub and open a pull request against the `develop` branch. 
Please ensure that all tests and CI checks pass before requesting review.

## Pull Request Guidelines

Before submitting a pull request, please ensure that:

1. All tests pass.
2. All CI checks pass.
3. New functionality includes appropriate tests.
4. Public-facing functionality includes documentation updates.
5. The code works on all supported Python versions.
6. The pull request remains focused on a single topic whenever possible.

## Code Style

This project uses:

- Ruff for formatting and linting
- MyPy for static type checking
- Pytest for testing

Please follow the existing coding style and patterns used throughout the code base.

## Questions?

If you have questions, feel free to open a GitHub issue or discussion.

## Code of Conduct

This project is released with a Code of Conduct. By participating, you agree to abide by its terms.