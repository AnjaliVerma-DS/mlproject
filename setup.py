from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    with open(file_path) as file_obj:
        requirements = [req.strip() for req in file_obj.readlines()]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name="mlproject",
    version="3.10.10",
    author="Anjali Verma",
    packages=find_packages(), 
    install_requires=get_requirements("requirements.txt")
)