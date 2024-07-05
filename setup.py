from setuptools import setup,find_packages


HYPEN_E_DOT = '-e .'


author_name = 'GuruHemendra'
author_email = 'guruhemendraputhuru@gmail.com'
version = '0.0.1'
name = 'Text Summarization'


def get_requirements(file_path :str)-> list[str]:

    requirements = []

    with open(file_path,'r') as file_obj:

        lines = file_obj.readlines()
        requires = [ req.strip() for req in lines]

        if HYPEN_E_DOT in requirements:
            requires.remove(HYPEN_E_DOT)
        
        for req in requires:
            req = req.replace('[',"['")
            req = req.replace(']',"']")
            requirements.append(req)

    return requirements
    

requirement_file_path = './requirements.txt'

setup(
    name = name,
    version = version,
    author = author_name,
    author_email = author_email,
    packages = find_packages(),

)

