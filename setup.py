import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="BookeySearch",  # Replace with your own username
    version="0.0.1",
    author="Yaroslav Brovchenko",
    author_email="yaroslav.brovchenko@ucu.edu.ua",
    description="Bookey engine search",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/firstgenius/BOOKEY_SEARCH",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True
)
