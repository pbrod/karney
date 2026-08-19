# Changelog


## [1.1.1] - 2026-08-19

### 📚 Documentation

- Refresh contribution guide.
- Refresh publishing and release documentation.

### 🎨 Styling

- Format code with Ruff.
- Replace unnecessary `dict()` calls with dictionary literals.

### 🏗️ CI/CD

- Modernize CI and release workflows.

### ⚙️ Maintenance

- Add conda recipe.
- Simplify Read the Docs configuration.
- Refresh `.gitignore`.
- Remove tracked `.coverage` file.

### ♻️ Refactoring

- Remove hardcoded MyPy Python version.


## [1.1.0] - 2025-07-21

### 🚀 Features

- Added PDM scripts for:
  - Building HTML, LaTeX, and PDF documentation.
  - Generating platform-specific lock files.
  - Formatting source code with Ruff.
  - Checking source-code style with Ruff.
- Dropped support for Python 3.8.
- Added support for Python 3.13.

### 🐛 Bug Fixes

- Fixed doctests for NumPy 2.x string formatting.
- Updated CI/CD workflow configuration.

### ♻️ Refactoring

- Replaced unnecessary generators with dictionary comprehensions.
- Migrated the project from Poetry to PDM.
- Updated project metadata to follow PEP 621.
- Replaced Poetry dependency management with PDM.
- Updated GitHub Actions workflows and Read the Docs configuration to use PDM.

### 📚 Documentation

- Added `PUBLISHING.md`.
- Updated `CONTRIBUTING.md`.
- Updated license information.
- Fixed a typo in `geodesic.py` (issue #1).

### ⚙️ Maintenance

- Removed `poetry.lock`.
- Added lock-file based dependency management.
- Modernized project configuration and development workflow.

## [1.0.10] - 2024-09-30

### 🐛 Bug Fixes

- Added support for NumPy 2.x.
- Relaxed NumPy version requirements where appropriate.
- Improved compatibility across supported Python versions.

### 🏗️ CI/CD

- Refined CI/CD workflows.
- Improved release automation reliability.
- Added doctest execution to continuous integration.
- Resolved issues related to publishing previously released versions.

## [1.0.8] - 2024-09-11

### 🐛 Bug Fixes

- Removed fragile package version detection from `__init__.py`.
- Added Codecov integration.
- Updated PyPI metadata and badges.

## [1.0.3] - 2024-09-10

### ⚙️ Build System

- Added automated build and deployment workflows.
- Introduced GitHub Actions based CI/CD.
- Added Python 3.12 to the test matrix.
- Added Ruff to development dependencies.
- Simplified dependency installation and build configuration.

### 🐛 Bug Fixes

- Fixed publishing and test-publishing workflows.
- Resolved build issues in CI/CD workflows.

### 📚 Documentation

- Cleaned up the changelog.
- Updated README badges and documentation links.
- Improved Read the Docs configuration.

### ⚙️ Maintenance

- Updated `pyproject.toml` and lock files.
- Added workflow status badges.
- Improved packaging and dependency management.

## [1.0.2] - 2024-02-12

### 🐛 Bug Fixes

- Fixed license metadata and lock-file configuration.

### ⚙️ Build System

- Updated coverage and lock files.

## [1.0.1] - 2024-02-09

### ⚙️ Build System

- Added Python Semantic Release integration.
- Added release automation tooling.
- Prepared the project for automated releases.

### 📚 Documentation

- Updated changelog formatting.

## [1.0.0] - 2024-02-09

### 🚀 Features

- Initial release of Karney.
- Added a Python implementation of Karney's geodesic algorithms translated from MATLAB.