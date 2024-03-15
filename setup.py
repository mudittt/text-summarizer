"""
No, you don't need to run the setup file (setup.py) yourself. 
The setup file is meant to be executed by tools like pip or setuptools,
     during the installation process of the package. 
When you run pip install, it automatically detects the setup file in the package directory, 
    and executes it to install the package properly.
"""

import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "text-summarizer"
AUTHOR_USER_NAME = "mudittt"
SRC_REPO = "textsummarizer"
AUTHOR_EMAIL = "mudittyagi2002@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
