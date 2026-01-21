#building our project as the pacage itself
from setuptools import find_packages,setup

def get_requirements(filepath:str):
    '''
    it will return the list of packages that need to be install
    '''
    requirements=[]
    with open(filepath) as f:
        requirements=f.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')

    return requirements



setup(
    name='mlproject',
    version='0.0.1',
    author='abhishek',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)