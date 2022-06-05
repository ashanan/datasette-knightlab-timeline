from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-knightlab-timeline",
    description="A Datasette plugin to create timelines using the TimelineJS library.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Avner Shanan",
    url="https://github.com/ashanan/datasette-knightlab-timeline",
    project_urls={
        "Issues": "https://github.com/ashanan/datasette-knightlab-timeline/issues",
        "CI": "https://github.com/ashanan/datasette-knightlab-timeline/actions",
        "Changelog": "https://github.com/ashanan/datasette-knightlab-timeline/releases",
    },
    license="Apache License, Version 2.0",
    classifiers=[
        "Framework :: Datasette",
        "License :: OSI Approved :: Apache Software License"
    ],
    version=VERSION,
    packages=["datasette_knightlab_timeline"],
    entry_points={"datasette": ["knightlab_timeline = datasette_knightlab_timeline"]},
    install_requires=["datasette"],
    extras_require={"test": ["pytest", "pytest-asyncio"]},
    package_data={
        "datasette_knightlab_timeline": ["static/*", "templates/*"]
    },
    python_requires=">=3.7",
)
