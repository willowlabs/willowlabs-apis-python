import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="willowlabs",
    version="1.0.0",
    author="Willow Labs AS",
    description="A Python package for accessing the Willow Labs APIs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/willowlabs/willowlabs-apis-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
