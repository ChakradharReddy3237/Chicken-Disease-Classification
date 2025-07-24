import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

__version__ = "0.0.1"

REPO_NAME = "Chicken-Disease-Classification"
AUTHOR_USER_NAME = "ChakradharReddy3237"
AUTHOR_EMAIL = "chakradharreddyponnavolu@gmail.com"
SRC_REPO = "cnnClassifier"  

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small package for Chicken Disease Classification using CNN",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)