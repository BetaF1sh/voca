from setuptools import setup, find_packages
import voca

with open("README.md") as f:
    long_description = f.read()

setup(
    name="voca-gorae",
    version=voca.__version__,
    description="A printable vocabulary exam generator for Amgigore",
    long_description=long_description,
    classifiers=[
        "Environment :: Console",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6"
    ],
    keywords="printable, vocabulary, exam, generator",
    author="Muhun Kim",
    author_email="iam@muhun.kim",
    url="https://github.com/BetaF1sh/voca",
    license="MIT",
    packages=find_packages(),
    entry_points={"console_scripts": ["voca = voca.voca:command_line_runner"]},
    install_requires=["pandas", "flask"],
)
