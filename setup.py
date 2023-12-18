import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "dataproject"
AUTHOR_USER_NAME = "banti9021"
SRC_REPO = "mlproject2"
AUTHOR_EMAIL = "nbanti943@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Fixed attribute name

    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",  # Fixed URL
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),  # Fixed attribute name
)