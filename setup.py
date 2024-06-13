import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ ="0.0.0"

REPO_NAME = "Text-Summarization-Project"
AUTHOR_USER_NAME = "Praveenahd4" 
SRC_REPO = "textSummarization"
AUTHOR_EMAIL = "praveenahd.work@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description= " A small python package for NLP applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    package_urls={"Bug Tracker\": f\"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",},
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)