from os import path as os_path

from setuptools import setup, find_packages

this_directory = os_path.abspath(os_path.dirname(__file__))


def read_file(filename):
    with open(os_path.join(this_directory, filename), encoding="utf-8") as f:
        long_description = f.read()
    return long_description


def read_requirements(filename):
    return [
        line.strip()
        for line in read_file(filename).splitlines()
        if not line.startswith("#")
    ]


def get_version():
    version_file = 'imagecon/version.py'
    with open(version_file, 'r', encoding='utf-8') as f:
        exec(compile(f.read(), version_file, 'exec'))
    return locals()['__version__']


setup(
    name="imagecon",
    version=get_version(),
    description="image controller toolkit",
    author="sdhan",
    url="https://github.com/FacePerceiver/facer",
    license="MIT",
    keywords="image-control pytorch",
    project_urls={
        "Documentation": "https://github.com/FacePerceiver/facer",
        "Source": "https://github.com/FacePerceiver/facer",
        "Tracker": "https://github.com/FacePerceiver/facer/issues",
    },
    long_description=read_file("README.md"),
    long_description_content_type="text/markdown",
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=read_requirements('requirements.txt')
)
