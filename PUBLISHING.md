Publishing a new release of the `karney` library involves a few steps, primarily managed through git commits and automated by the `python-semantic-release` tool configured in your `pyproject.toml` file. Here’s a breakdown of the process:

### Automated Release with `python-semantic-release`

The project is configured to use `python-semantic-release`, which automates versioning, changelog generation, and package publishing based on your commit messages. This means you don't manually set the version number for a new release. Instead, the tool deduces the next version based on the types of commits you've made since the last release.

Here's how it works:

1.  **Commit Your Changes with Conventional Commit Messages**:
    When you make changes to the codebase, follow the "Angular" conventional commit message format. This format is specified in your `pyproject.toml` and is crucial for `python-semantic-release` to determine the version bump. The structure of a commit message is:

    ```
    <type>(<scope>): <subject>
    ```

    *   `<type>`: This is the most important part for versioning. Based on your configuration, the following types will trigger a release:
        *   `feat`: A new feature (triggers a **minor** release, e.g., 1.0.10 -> 1.1.0)
        *   `fix`: A bug fix (triggers a **patch** release, e.g., 1.0.10 -> 1.0.11)
        *   `perf`: A code change that improves performance (triggers a **patch** release)
    *   Other allowed types like `build`, `chore`, `ci`, `docs`, `style`, `refactor`, and `test` will be included in the changelog but will not trigger a version bump on their own.

2.  **Push to the `main` Branch**:
    The GitHub Actions workflow `CI-CD.yml` is configured to run on pushes to the `main` branch. When you push commits with the appropriate messages to `main`, the `release1` job in the workflow will be triggered.

3.  **The Release Process in GitHub Actions**:
    The `release1` job will:
    *   Check out your repository.
    *   Run `python-semantic-release`, which will:
        *   Analyze the commit messages since the last release.
        *   Determine the new version number (e.g., v1.0.11).
        *   Update the `version` in `pyproject.toml` and `src/karney/__init__.py`.
        *   Generate a `CHANGELOG.md` with the latest changes.
        *   Create a new git tag with the new version number.
        *   Push the updated `pyproject.toml`, `src/karney/__init__.py`, `CHANGELOG.md`, and the new tag to your repository.
    *   If a new release is created, the workflow will then build the package using `pdm build`.
    *   The built distributions (wheel and sdist) are then uploaded to GitHub Releases.

4.  **Publishing to PyPI**:
    The workflow includes jobs for publishing to TestPyPI and PyPI:
    *   `testpypi-publish`: This job will take the distribution files and publish them to TestPyPI. This is a good way to verify that your package works as expected before a full public release.
    *   `pypi-publish`: Once the TestPyPI publish is successful, this job will publish the package to the official Python Package Index (PyPI).

In summary, to publish a new release, you need to:

*   **Make your code changes.**
*   **Commit them with a message that follows the conventional commit format.**
*   **Push your changes to the `main` branch.**

The rest of the process is automated by your GitHub Actions workflow.

### Manual Publishing with PDM (if needed)

While your setup is automated, it's useful to know how to publish manually with PDM.

1.  **Build the package**:
    This command will create a wheel and a source distribution in the `dist/` directory.

    ```bash
    pdm build
    ```

2.  **Publish to PyPI**:
    You can publish the contents of the `dist/` directory to PyPI. You'll need to have a PyPI account and an API token.

    ```bash
    pdm publish
    ```

    You can also specify a repository, like TestPyPI:

    ```bash
    pdm publish --repository testpypi
    ```

    PDM will prompt for your username and password. For PyPI, you should use `__token__` as the username and your PyPI API token as the password.

Your current setup with `python-semantic-release` is the recommended way to handle releases for your project, as it ensures a consistent and automated process.