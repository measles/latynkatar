import nox

nox.options.sessions = ["black", "flake8", "mypy", "test"]


@nox.session(tags=("tests", "lint"))
def black(session):
    session.install("black")
    session.run("black", "--check", "tests/", "src/", "noxfile.py")


@nox.session(tags=("tests", "lint"))
def ruff(session):
    session.install("ruff")
    session.run("ruff", "format", "tests/", "src/", "noxfile.py")
    session.run("ruff", "check", "tests/", "src/", "noxfile.py")


@nox.session
def black_diff(session):
    session.install("black")
    session.run("black", "--diff", "tests/", "src/", "noxfile.py")


@nox.session
def blacked(session):
    session.install("black")
    session.run("black", "tests", "src", "noxfile.py")


@nox.session(tags=("tests", "lint"))
def flake8(session):
    session.install("flake8", "flake8-pyproject")
    session.run("flake8", ".", "--count", "--exclude", ".nox,.venv")


@nox.session(tags=("tests", "lint"))
def mypy(session):
    session.install("mypy")
    session.run("mypy", "-p", "src.latynkatar")


@nox.session(tags=("tests"))
def test(session):
    session.install("pytest", "pytest-html")
    session.run(
        "python3",
        "-m",
        "pytest",
        "tests",
        "-lvv",
        "-ra",
        "--html=report.html",
        "--self-contained-html",
    )
