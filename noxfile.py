import nox

nox.options.sessions = ["black", "test"]


@nox.session(tags=("tests"))
def black(session):
    session.install("black")
    session.run("black", "--check", "tests/", "src/", "noxfile.py")


@nox.session
def black_diff(session):
    session.install("black")
    session.run("black", "--diff", "tests/", "src/", "noxfile.py")


@nox.session
def blacked(session):
    session.install("black")
    session.run("black", "tests", "src", "noxfile.py")


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
