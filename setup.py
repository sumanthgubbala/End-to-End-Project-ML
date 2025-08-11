
from setuptools import find_packages, setup
from typing import List

def get_requiremenst(file_path:str)->list[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

setup(
    name="MLProject",
    packages=find_packages(),
    version="0.0.1",
    description="",
    author='Sumanth',
    author_email='sumanthgubbala123@gmail.com',
    install_requires=[get_requiremenst('requirements.txt')]
)