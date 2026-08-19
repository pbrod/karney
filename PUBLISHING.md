# Publishing

Publishing a new release of `karney` is a straightforward process based on:

- Conventional Commit messages
- `pdm-bump` for version management
- GitHub Actions release automation
- Trusted PyPI publishing

The release workflow automatically builds, verifies, and publishes the package whenever a version tag is pushed.

## Release Workflow

### 1. Complete Your Changes

Implement the desired fixes, features, documentation updates, or maintenance tasks.

Before creating a release, ensure that all checks pass:

```console
pdm format --check
pdm check-style
pdm check-types
pdm test
```

## 2. Update the Version

Use `pdm-bump` to update the project version.

### Patch Release

Examples:

- Bug fixes
- Documentation corrections
- Small maintenance changes

```console
pdm bump patch
```

Example:

```text
1.1.0 → 1.1.1
```

### Minor Release

Examples:

- New functionality
- Backward-compatible enhancements

```console
pdm bump minor
```

Example:

```text
1.1.0 → 1.2.0
```

### Major Release

Examples:

- Breaking API changes

```console
pdm bump major
```

Example:

```text
1.1.0 → 2.0.0
```

## 3. Update the Changelog

Review and update `CHANGELOG.md`.

Ensure the upcoming release section accurately summarizes:

- New features
- Bug fixes
- Refactoring
- Documentation updates
- Other noteworthy changes

## 4. Commit the Release Changes

Commit the version and changelog updates:

```console
git add .
git commit -m "chore(release): prepare v1.2.0"
```

## 5. Create and Push a Version Tag

Create a version tag matching the project version:

```console
git tag v1.2.0
```

Push both commits and tags:

```console
git push origin develop
git push origin v1.2.0
```

Or:

```console
git push origin --tags
```

## 6. Automatic Release Process

Pushing a version tag triggers the GitHub Actions release workflow.

The workflow will:

1. Build source and wheel distributions.
2. Verify that the wheel installs correctly.
3. Verify that the version does not already exist on PyPI.
4. Publish the package to PyPI using trusted publishing.
5. Optionally create a GitHub Release.

No manual upload is normally required.

## Conventional Commits

Although releases are triggered by version tags, contributors are encouraged to use Conventional Commit messages:

```text
feat(core): add support for custom ellipsoids
fix(geodesic): correct azimuth calculation near poles
docs: update installation instructions
test(core): add regression tests
```

Common commit types include:

- `feat`
- `fix`
- `docs`
- `test`
- `refactor`
- `perf`
- `ci`
- `build`
- `chore`
- `style`

These help maintain a clean project history and improve changelog generation.

## Manual Publishing

In rare situations it may be necessary to publish manually.

### Build the Package

```console
pdm build
```

This creates:

```text
dist/
├── karney-<version>.tar.gz
└── karney-<version>-py3-none-any.whl
```

### Publish to PyPI

```console
pdm publish
```

### Publish to TestPyPI

```console
pdm publish --repository testpypi
```

You will need appropriate credentials or API tokens.

## Troubleshooting

### Verify the Built Wheel

```console
python -m venv test_env

# Linux/macOS
test_env/bin/pip install dist/*.whl

# Windows*test_env\Scripts\pip install dist**.whl
```

Verify the installation:

```console
python -c "import karney; print(karney.__version__)"
```

### Release Already Exists

If the release workflow reports that the version already exists on PyPI:

1. Increment the version.
2. Create a new tag.
3. Push the new tag.

Existing PyPI releases cannot be overwritten.

## Summary

Typical release workflow:

```console
pdm bump patch
git add .
git commit -m "chore(release): prepare v1.1.1"
git tag v1.1.1
git push origin develop
git push origin v1.1.1
```

Once the tag is pushed, GitHub Actions handles the rest.
