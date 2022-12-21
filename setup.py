from setuptools import find_packages,setup

from typing import List

REQUIREMENT_FILE_NAME="requirements.txt"
HYPHEN_E_DOT = "-e ."  #-e . install source code(sensor) as libarary so that trigger the setup.py file.


def get_requirements()->List[str]:
    
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        print(requirement_list)
    requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
    #print(requirement_list)
    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
    return requirement_list



setup(
    name="sensor",
    version="0.0.2",
    author="iSudhir",
    author_email="sudhich1208@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements(),
)

