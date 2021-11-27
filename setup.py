import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="coinonpy", 
    version="0.0.1",
    author="Lukas Yoo, Brayden Jo",
    author_email="jonghun.yoo@outlook.com, brayden.jo@outlook.com",
    description="CoinOne Python Wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sharebook-kr/coinonepy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)