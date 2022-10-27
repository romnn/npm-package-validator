from invoke import task
from pathlib import Path
import webbrowser

ROOT_DIR = Path(__file__).parent
TEST_DIR = ROOT_DIR.joinpath("tests")
SOURCE_DIR = ROOT_DIR.joinpath("npm_package_validator")
COVERAGE_DIR = ROOT_DIR.joinpath("htmlcov")
PYTHON_DIRS = [str(d) for d in [SOURCE_DIR, TEST_DIR]]
PYTHON_FILES = [str(f) for f in ROOT_DIR.rglob("*.py")]


def _delete_file(file):
    try:
        file.unlink(missing_ok=True)
    except TypeError:
        # missing_ok argument added in 3.8
        try:
            file.unlink()
        except FileNotFoundError:
            pass


@task(help={"check": "Checks formatting without applying changes"})
def format(c, check=False):
    """Format code"""
    options = []
    if check:
        options.append("--diff")
    cmd = ["pipenv", "run", "black"]
    cmd += options
    cmd += PYTHON_FILES
    c.run(" ".join(cmd))


@task
def lint(c):
    """Lint code"""
    c.run("pipenv run flake8")


@task
def test(c, min_coverage=None):
    """Run tests"""
    pytest_options = []
    if min_coverage:
        pytest_options.append("--cov-fail-under={min_coverage}")
    c.run(f"pipenv run pytest {' '.join(pytest_options)}")


@task
def type_check(c):
    """Check types"""
    c.run("pipenv run mypy")


@task
def install_hooks(c):
    """Install pre-commit hooks"""
    c.run("pipenv run pre-commit install -t pre-commit")
    c.run("pipenv run pre-commit install -t pre-push")


@task
def pre_commit(c):
    """Run all pre-commit checks"""
    c.run("pipenv run pre-commit run --all-files")


@task(
    pre=[test],
    help=dict(
        publish="Publish the result (default False)",
        provider="The provider to publish (default codecov)",
    ),
)
def coverage(c, publish=False, provider="codecov"):
    """Create coverage report"""
    if publish:
        # Publish the results via provider (e.g. codecov or coveralls)
        c.run("pipenv run {}".format(provider))
    else:
        # Build a local report
        c.run("pipenv run coverage html -d {}".format(COVERAGE_DIR))
        webbrowser.open(COVERAGE_DIR.joinpath("index.html").as_uri())


@task
def clean_build(c):
    """Clean up files from package building"""
    c.run("rm -fr build/")
    c.run("rm -fr dist/")
    c.run("rm -fr .eggs/")
    c.run("find . -name '*.egg-info' -exec rm -fr {} +")
    c.run("find . -name '*.egg' -exec rm -f {} +")


@task
def clean_python(c):
    """Clean up python file artifacts"""
    c.run("find . -name '*.pyc' -exec rm -f {} +")
    c.run("find . -name '*.pyo' -exec rm -f {} +")
    c.run("find . -name '*~' -exec rm -f {} +")
    c.run("find . -name '__pycache__' -exec rm -fr {} +")


@task
def clean_tests(c):
    """Clean up files from testing"""
    import shutil

    _delete_file(ROOT_DIR.joinpath(".coverage"))
    shutil.rmtree(COVERAGE_DIR, ignore_errors=True)


@task(pre=[clean_build, clean_python, clean_tests])
def clean(c):
    """Runs all clean sub-tasks"""
    pass


@task(pre=[clean])
def dist(c):
    """Build source and wheel packages"""
    c.run("python setup.py sdist")
    c.run("python setup.py bdist_wheel")


@task(pre=[dist])
def release(c):
    """Make a release of the python package to pypi"""
    c.run("twine upload dist/*")
