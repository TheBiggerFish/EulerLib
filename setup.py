import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="EulerLib-TheBiggerFish",
    version="1.0.0",
    author="Cameron Haddock",
    author_email="clhnumber4@gmail.com",
    description="A small package with common tools for solving Project Euler problems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TheBiggerFish/EulerLib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)