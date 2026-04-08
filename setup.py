from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path)->List[str]:
    '''
    This functionn will return the list of requirements

    '''
    requirements =[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace('\n',"") for req in requirements]

    return requirements






setup(
name = 'CapstonMLPro',
version= '0.01',
author= 'Pradeep',
author_email='psrana344@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)