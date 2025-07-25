# CHANGELOG

## v1.1.0 (2025-07-21)

### Feature

* feat: New minor release ([`a147f2e`](https://github.com/pbrod/karney/commit/a147f2ec3724804b299c6ccec9c61e53480c8b03))

* feat: Added pdm scripts

Summary of scripts added:
build-docs-XXX: Build the documentation in the docs folder
lock_XXXX: Generates a lock file
format: Runs ruff to format the source code
check-style: Runs ruff to check the coding style of the source code. ([`380973f`](https://github.com/pbrod/karney/commit/380973f2ffd22654b8046f883c2a4d1c40da5cd6))

### Fix

* fix: Updated CI-CD.yml ([`17d968f`](https://github.com/pbrod/karney/commit/17d968fb4f022096cad614a695aeb23b1f345699))

### Unknown

* fix (util.py): Fixed doctests on numpy&gt;=2 strings ([`66202cc`](https://github.com/pbrod/karney/commit/66202cc1b6934074e88a7168893a8a584f217c0c))

* docs (LICENSE): Updated licence. ([`3013992`](https://github.com/pbrod/karney/commit/3013992b25a02cdd22a52dc028ec44d71beb493e))

* docs (CONTRIBUTING.md): Detailed the commit message format. ([`0922f5b`](https://github.com/pbrod/karney/commit/0922f5b5d80afe94ea2a4dbd14e5e5e854805ea9))

* refactor (geodesic.py, util.py): Rewrite unnecessary generators as dict comprehensions ([`276417e`](https://github.com/pbrod/karney/commit/276417eed99fb25a3ef6adc863a6a4f537ae6be0))

* feat (karney): Removed support for python 3.8 and added for python 3.13 ([`de013ec`](https://github.com/pbrod/karney/commit/de013ec2971a31b908b8d0a70bb0864c68f4be85))

* docs (geodesic.py): Minor typo

Fixes issue #1 ([`0c0e220`](https://github.com/pbrod/karney/commit/0c0e2200c340dcad3070972465919e2b772ea89c))

* refactor (karney): Changed build backend from Poetry to PDM (Python Development Master)

* pyproject.toml: Modified to follow PEP 621 for project metadata and to use PDM for dependency management and build configuration.
* .github/workflows/CI-CD.yml: The GitHub Actions workflow is updated to use PDM for installing dependencies and running tests and builds.
* .readthedocs.yml: The Read the Docs configuration is changed to use PDM for installing dependencies to build the documentation.
* CONTRIBUTING.md: The setup instructions for contributors is updated to reflect the change to PDM.
* poetry.lock: This file is deleted. PDM will generate a pdm.lock file to lock dependencies.
* PUBLISHING.md: This file is added to document how to publish a new release of the `karney` library. ([`a861bcc`](https://github.com/pbrod/karney/commit/a861bcc6295e0805336dc5b7b1c868a35ebd2f56))

## v1.0.10 (2024-09-30)

### Fix

* fix: Allow numpy&gt;=2.0 ([`7b3cd1c`](https://github.com/pbrod/karney/commit/7b3cd1c46bcaacd885e6c27532568b3b04efddbc))

### Unknown

* Attempt to remove warnings when running workflows/CI-CD.yml ([`63562d9`](https://github.com/pbrod/karney/commit/63562d9328b1166b389552036b590ee40c15af5d))

## v1.0.9 (2024-09-30)

### Fix

* fix: Made numpy requirement less strict. ([`72dcb55`](https://github.com/pbrod/karney/commit/72dcb5573f1768892fb81809ec4deb2797a49192))

### Refactor

* refactor: CI-CD.yml ([`62e6f9c`](https://github.com/pbrod/karney/commit/62e6f9cc01bf6f51baeeef0194ae06174a384538))

* refactor: CI-CD.yml ([`250dd75`](https://github.com/pbrod/karney/commit/250dd75b43c6552560e2d296eee5d879697d2ecb))

* refactor: CI-CD.yml ([`1486e32`](https://github.com/pbrod/karney/commit/1486e327e0a5f4a21a87c4ab416d6417164d1206))

* refactor: CI-CD.yml ([`ee1f66d`](https://github.com/pbrod/karney/commit/ee1f66d95c6d5d7b90f097c3e14864882e1b08db))

* refactor: CI-CD.yml ([`aa8ce41`](https://github.com/pbrod/karney/commit/aa8ce41788df891453a8d6729921213ef15f15d8))

* refactor: workflows/CI-CD.yml so it will not try to test-publish an already published relase ([`72bd9eb`](https://github.com/pbrod/karney/commit/72bd9eb110a679044824864bc7e9563f4853ebae))

### Test

* test: Added doctest to workflows/CI-CD.yml and deleted workflows/publish.yml and workflows/testpublish.yml ([`1ff7318`](https://github.com/pbrod/karney/commit/1ff7318d5010c277beb53e616ac4990feaa4e023))

### Unknown

* * fix: Made numpy requirement more strict for python 3.12 ([`896e8ee`](https://github.com/pbrod/karney/commit/896e8eed465c30d058986cbe7e9839fc6f53b42c))

* Attempt 2 on resolving python and numpy requirements ([`5a69ad9`](https://github.com/pbrod/karney/commit/5a69ad974c0cebd367ea78fdebe242db2bca9883))

* Attempt to resolve python and numpy requirements ([`c0144cb`](https://github.com/pbrod/karney/commit/c0144cb8163c2beaa6c0deb45261215b1fa7e148))

* refactor CI-CD.yml ([`1166226`](https://github.com/pbrod/karney/commit/1166226a878652e0752ae01f87540956d304919d))

## v1.0.8 (2024-09-11)

### Fix

* fix: Removed fragile determination of package version in __init__.py ([`b1a8f00`](https://github.com/pbrod/karney/commit/b1a8f0063948f1af81d9885b50dc1725b72e2f9b))

## v1.0.7 (2024-09-11)

### Fix

* fix: Added CODECOV_TOKEN to CI-CD.yml and PyPi version to README.md ([`d3a9984`](https://github.com/pbrod/karney/commit/d3a9984046e7efb01593cfb98696853f9f387733))

## v1.0.6 (2024-09-11)

### Fix

* fix: Yet another attempt to fix workflows/CI-CD.yml ([`e6e88e2`](https://github.com/pbrod/karney/commit/e6e88e2e155206db3b6317ee61610c4d049159ea))

## v1.0.5 (2024-09-11)

### Fix

* fix: Another attempt to fix workflows/CI-CD.yml ([`fb9c7b8`](https://github.com/pbrod/karney/commit/fb9c7b85f70ba8a2eae57df08d5d9bf79b700825))

## v1.0.4 (2024-09-11)

### Fix

* fix: Another attempt to fix workflows/CI-CD.yml ([`386be8e`](https://github.com/pbrod/karney/commit/386be8ed5d7bdd31e7cfe9fbff6bb55f737b5d79))

## v1.0.3 (2024-09-10)

### Build

* build: updated CI-CD.yml ([`fdc518c`](https://github.com/pbrod/karney/commit/fdc518cea533782f7438fb6f6a17c40855a0a3d2))

* build: updated CI-CD.yml ([`73603b5`](https://github.com/pbrod/karney/commit/73603b5b181f22773048a752b2e670cea33e9719))

* build: Update CI-CD.yml ([`dca15d8`](https://github.com/pbrod/karney/commit/dca15d8df1a66d901aad4c3c72ef90eacae7b7b7))

* build: Updated CI-CD.yml ([`5cd9385`](https://github.com/pbrod/karney/commit/5cd938599857383f72faebea52fd0013b6e9e737))

* build: Renamed CI-tests.yml to CI-CD.yml ([`68f73d7`](https://github.com/pbrod/karney/commit/68f73d76c8843c8d327fd448350112275002c067))

* build: test new build workflow ([`22db731`](https://github.com/pbrod/karney/commit/22db731ee7d6362dbeb8f81c7ede1880cf272d88))

### Documentation

* docs: Cleaned up CHANGELOG.md ([`d93dc71`](https://github.com/pbrod/karney/commit/d93dc7174d0794b5ad2fd7204efe54182b0141f3))

### Fix

* fix:  testpublish.yml ([`fb94a1f`](https://github.com/pbrod/karney/commit/fb94a1f0614ac1b3437550d2b2c37ac0e9bef56f))

* fix: Added testpublish.yml ([`88774cd`](https://github.com/pbrod/karney/commit/88774cd50e64148a7d94d9738382ab258cf5586d))

### Unknown

* Fix: publish.yml ([`c9229c3`](https://github.com/pbrod/karney/commit/c9229c3844a5607029c1be5c01ed426fc9718583))

* Build: Update and rename CI-CD.yml to CI-tests.yml ([`547ea07`](https://github.com/pbrod/karney/commit/547ea07329e6bf674872a2153e3b55f5af318a1b))

* Build: Updated pyproject.toml ([`94ebcac`](https://github.com/pbrod/karney/commit/94ebcac613c124645be642c0c301e11fd2edfaa0))

* Update CI-CD.yml

Fix: Fixed a bug in build in CI_CD.yml file ([`f201056`](https://github.com/pbrod/karney/commit/f201056cf149a4371a46b9795d5f32086d846351))

* Update and rename CI-tests.yml to CI-CD.yml

Build:  Added automatic build and deployment ([`9579cf0`](https://github.com/pbrod/karney/commit/9579cf045dadd88e984526a6ddcf9704ab292e25))

* Updated CI-tests.yml ([`a135653`](https://github.com/pbrod/karney/commit/a135653054b0259b477d1424cbb49b5d5addb192))

* Update publish.yml ([`ff6e9ac`](https://github.com/pbrod/karney/commit/ff6e9ac6471d7d2f48fa311b25f889f323e48c86))

* Updated README.md ([`0c3aee1`](https://github.com/pbrod/karney/commit/0c3aee10b5a39517ccb67bea37bcaa7129709553))

* Rename python-package.yml to CI-tests.yml ([`afdac19`](https://github.com/pbrod/karney/commit/afdac195ae70f910006a7de3fae363a89cddb752))

* Update python-package.yml ([`43a866e`](https://github.com/pbrod/karney/commit/43a866e0b764dadc9224a32cf73951c369468f16))

* Update python-package.yml ([`391cb6e`](https://github.com/pbrod/karney/commit/391cb6e26e5e46177a25303c34a7f20c6f2b73b6))

* Updated path to documentation ([`e2a7137`](https://github.com/pbrod/karney/commit/e2a713758cde5cf5b66062cc37d73b91be783a3a))

* Updated README.md ([`dc8f1e2`](https://github.com/pbrod/karney/commit/dc8f1e2dca1361c5bc258fec3331740a2e5a2c64))

* Update python-package.yml

Added python 3.12 to test matrix ([`328f417`](https://github.com/pbrod/karney/commit/328f41786838455ae252ac7dfd9ee708e9b471ee))

* updated poetry.lock and pyproject.toml ([`554d9cb`](https://github.com/pbrod/karney/commit/554d9cb97b22503dcfd642104880757da4a58471))

* Added ruff to dev dependencies ([`5e417e6`](https://github.com/pbrod/karney/commit/5e417e6a5b93bcd9dfd459ef3ddf0b26ef9e5709))

* Update python-package.yml ([`50cd0b2`](https://github.com/pbrod/karney/commit/50cd0b26cfe16c1f007f6b62190d7494fd4929da))

* Update python-package.yml

Simplified install of dependencies ([`3a66ea0`](https://github.com/pbrod/karney/commit/3a66ea03577ec4bc1a4983812573f20422ea26bd))

* Update python-package.yml ([`7ac1bd0`](https://github.com/pbrod/karney/commit/7ac1bd0abc592b63f488b7dac71145a05c98467a))

* Update python-package.yml ([`13d0102`](https://github.com/pbrod/karney/commit/13d0102e67dfdfa7ec2b8c752b6da5c9efabd2fd))

* Added workflow status to README.md ([`3260bfc`](https://github.com/pbrod/karney/commit/3260bfcbe1ccb1a9544fc3491458208f81d9d322))

* Update python-package.yml ([`4f00848`](https://github.com/pbrod/karney/commit/4f00848702a004bf908df8407527065e9d4de27b))

* Update python-package.yml ([`52e9c8a`](https://github.com/pbrod/karney/commit/52e9c8a9b8c95442325cb0e6002a71a211260be9))

* Create python-package.yml ([`753a4fd`](https://github.com/pbrod/karney/commit/753a4fdf66c9a852db5543e7055564798f364a68))

* Added doc image and version image to README.md ([`d521b66`](https://github.com/pbrod/karney/commit/d521b66f4164a707d5985810c1fccd3cc70bcbd4))

* Create publish.yml ([`44bbd7f`](https://github.com/pbrod/karney/commit/44bbd7f2af81c6bb31729743a70ea0eb4dd2bd94))

* Attempt 7 ([`517de81`](https://github.com/pbrod/karney/commit/517de81670d49137f3e6611e32c07a3053eea5c7))

* Attempt 6 ([`bb67800`](https://github.com/pbrod/karney/commit/bb67800be117450d5e30008828b5667cf8545e96))

* Attempt 5 ([`f81617b`](https://github.com/pbrod/karney/commit/f81617b63aeb97eaf70022054e3f54d53de9d42d))

* Another attempt to make readthedocs work... ([`7c831f7`](https://github.com/pbrod/karney/commit/7c831f7f26027b0c3419b471c821aba2614da9d3))

* Try to explicitly install myst-nb ([`425f07c`](https://github.com/pbrod/karney/commit/425f07c92718ac1db4befa78cab810badded1ed4))

* Updated to python 3.12 ([`b609e47`](https://github.com/pbrod/karney/commit/b609e47b7adba26d73d6e1bb40779845b0df09b0))

* Another attempt to fix the readthedocs.yml file. ([`4542c49`](https://github.com/pbrod/karney/commit/4542c49c732d99f162f9777b5d5924026429c25d))

* Updated readthedocs.yml ([`c380d9b`](https://github.com/pbrod/karney/commit/c380d9be97dabff4e140cc08462377e423db1c06))

* Added stacklevel=2 to warnings.warn
Added ruff linter to pyproject.toml
pep8 ([`01f2583`](https://github.com/pbrod/karney/commit/01f25835fa4e6b85d7881e744aecf9fa559701e6))

* v1.0.2 ([`1a4671b`](https://github.com/pbrod/karney/commit/1a4671bab182e45276b74258b6093c36602ed445))

## v1.0.2 (2024-02-12)

### Build

* build: .coverage and .lock updated ([`710bcc2`](https://github.com/pbrod/karney/commit/710bcc2349c7cc014b976c1ca2c255148dec360b))

### Fix

* fix(license): Fixed license and poetry.lock file. ([`eb4b9f3`](https://github.com/pbrod/karney/commit/eb4b9f3ba29e59457f5bb538f284d9eee5e5fde2))

## v1.0.1 (2024-02-09)

### Build

* build: Prepare for release v1.0.1 ([`4f1d6e3`](https://github.com/pbrod/karney/commit/4f1d6e3c59630db5797774e6d3cc8123192a007f))

* build: Added Python Semantic Release to pyproject.toml ([`7795cee`](https://github.com/pbrod/karney/commit/7795cee546658c1a218224603e762ef3525f08a8))

* build: add PSR as dev dependency ([`f2dbf42`](https://github.com/pbrod/karney/commit/f2dbf429d2dc28499d53f4f196f8ff57668b81de))

### Documentation

* docs: Updated header in CHANGELOG.md ([`8a8c29a`](https://github.com/pbrod/karney/commit/8a8c29a9c25f6b8133c38b9c723376165c4918fe))

### Unknown

* Release v1.0.1 ([`49c44bd`](https://github.com/pbrod/karney/commit/49c44bd4edef505fc25ae45663d2361d833b9c89))

## v1.0.0 (2024-02-09)

### Unknown

* Initial package setup with translated code from Matlab to Python. ([`285d6e3`](https://github.com/pbrod/karney/commit/285d6e3e1062df3fa29ade430a22a731812c3d5a))
