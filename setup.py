import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setuptools.setup(
    name="comspy",
    version="2022.3",
    author="SunnyLi",
    author_email="5327136@qq.com",
    description="A package that uses Python to make communication easier",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SunnyLi1106/ComsPy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "pyesytime",
    ],
    python_requires='>=3',
)