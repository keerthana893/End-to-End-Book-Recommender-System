# now only we are starting the proper project setup...by doing modular coding,in different components

from setuptools import find_packages,setup

with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()
    
REPO_NAME="ML Based Books Recommender System"
AUTHOR_USER_NAME="KEERTHANA"
SRC_REPO="books_recommender"
LIST_OF_REQUIREMENTS=["streamlit==1.32.0",
    "pandas",
    "numpy",
    "scikit-learn",
    "pyyaml",
    "altair==5.2.0"]

setup(
    name=SRC_REPO,
    version="0.0.1",
    author="KEERTHANA",
    description="A small local packages for ML based books recommendations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/keerthana893/End-to-End-Book-Recommender-System",
    author_email="keerthana93k@gmail.com",
    packages=find_packages(),# this will look for constructor file,wherever it is present and will consider that as a and set that up as a local package
    license="MIT",
    python_requires=">=3.9",
    install_requires=[]
)

# to execute this file and set that package up as a local package, we need to type "-e . " in requirement .txt file, this will execute the 
# setup.py file and set up the local package in our system.