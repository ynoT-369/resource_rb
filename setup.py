import setuptools


def _requires_from_file(filename):
    return open(filename).read().splitlines()


# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()

setuptools.setup(
    name="flask-test-api-ms",
    version="1.0.0",
    author="Rock Group",
    author_email="ds@gmail.com",
    description="Books",
    # long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://confluence..com/BOOKS",
    install_requires=_requires_from_file("requirements.txt"),
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
    ],
)
