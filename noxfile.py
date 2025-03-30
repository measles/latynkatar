"""Тэсты і іншая аўтаматызацыя для праекта."""

import sys
import nox
import toml

nox.options.sessions = ["ruff", "black", "flake8", "pylint", "mypy", "pytest"]


@nox.session(tags=("tests", "lint"))
def ruff(session):
    """Фарматаванне і статычныя тэсты ruff."""
    session.install("ruff")
    session.run("ruff", "format", "tests/", "src/", "noxfile.py")
    session.run("ruff", "check", "tests/", "src/", "noxfile.py")


@nox.session(tags=("tests", "lint"))
def black(session):
    """Праверка фарматавання коду праз black."""
    session.install("black")
    session.run("black", "--check", "tests/", "src/", "noxfile.py")


@nox.session
def black_diff(session):
    """паказвае што ў кодзе змяніў бы black."""
    session.install("black")
    session.run("black", "--diff", "tests/", "src/", "noxfile.py")


@nox.session
def blacked(session):
    """Фарматуе код па правілах black."""
    session.install("black")
    session.run("black", "tests", "src", "noxfile.py")


@nox.session(tags=("tests", "lint"))
def pylint(session):
    """Правярае код з дапамогай pylint."""
    session.install("pylint", "nox", "toml")
    session.run("pylint", "tests/", "src/", "noxfile.py")


@nox.session(tags=("tests", "lint"))
def flake8(session):
    """Правярае код з дапамогай flake8."""
    session.install("flake8", "flake8-pyproject")
    session.run("flake8", ".", "--count", "--exclude", ".nox,.venv")


@nox.session(tags=("tests", "lint"))
def mypy(session):
    """Правярае пазначэнне і супадзенне тыпаў праз mypy."""
    session.install("mypy")
    session.run("mypy", "-p", "src.latynkatar")


@nox.session(tags=("tests",))
def pytest(session):
    """Юніттэсты з pytest."""
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


@nox.session
def set_version(_):
    """Змяніць версію пакета."""
    with open("pyproject.toml", "r", encoding="utf-8") as config_file:
        config = toml.load(config_file)

    config["project"]["version"] = sys.argv[-1].split("/")[-1]

    with open("pyproject.toml", "w", encoding="utf-8") as config_file:
        toml.dump(config, config_file)
