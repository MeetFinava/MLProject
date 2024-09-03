from setuptools import setup,find_packages
from typing import List

HYPEN_DOT='-e .'
def get_requriements(file_path:str)->List[str]:
    '''
    this is function is our requriements
    '''
    requriements=[]
    with open(file_path) as file_obj:
        requriements=file_obj.readlines()
        requriements=[req.replace("\n","") for req in requriements]

        if HYPEN_DOT in requriements:
            requriements.remove(HYPEN_DOT)
    
    return requriements
    
setup(
    name='mlproject',
    version='0.0.1',    
    author='meet',
    author_email='meetfinava82868@gmail.com',
    package=find_packages(),
    install_require=get_requriements('requriements.txt')
)