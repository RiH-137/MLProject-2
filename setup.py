from setuptools import setup
from typing import List





#delaring variables for setup functions
PROJECT_NAME="housing-prediction"
VERSION="0.0.1"
AUTHOR="Rishi Ranjan"
REQUIREMENT_FILE_NAME="requirements.txt"


def get_requirements_list()->List[str]:
    
        #This function is going to return list of requirement mention in requirements.txt file.

    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()



setup(

    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description="This model can predict the house price.",
    packages=["housing"],                                                   #folder name
    install_requires=get_requirements_list()                                                                

)


# if __name__=="__main__":
#         print(get_requirements_list())