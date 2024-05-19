# setup.py

from setuptools import setup, find_packages

setup(
    name="test_crm_utils",
    version="0.1.0",
    description="A simple package to interact with a CRM system.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/lucko515/test_crm_utils",
    author="Luka Anicin",
    author_email="luka.anicin@example.com",
    license="MIT",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        # Add any dependencies here
    ],
)
