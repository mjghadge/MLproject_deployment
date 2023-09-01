# responsible for creating ML application as package and we deploy it 

from setuptools import find_packages, setup
from typing import List

# -e . in requirements.txt will automatically trigger setup.py file
HYPEN_E_DOT = "-e ."

def get_requirement(file_path:str)->List[str]:
    """ This function will return the list of requirements 
    Args:
        file_path (str): _description_
    Returns:
        List[str]: _description_
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # to remove next line
        requirements = [req.replace("\n","") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
             requirements.remove(HYPEN_E_DOT)
             
    return requirements

setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Mayur',
    author_email= 'mjghadge9007@gmail.com',
    packages= find_packages(),
    install_requires = get_requirement('requirements.txt'),
    
)