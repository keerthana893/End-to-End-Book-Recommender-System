# it will have the common functions mostly used in development of project-->i.e read yaml file...everytime we have to read the yaml file from the
# config file itself, so we can write a function to read yaml file and return the content of yaml file in dict format,
# so that we can use it in our project,so that we don't have write that code again and again


import yaml
import sys
from books_recommender.exception.exception_handler import AppException



def read_yaml_file(file_path:str)->dict:
    """
    Reads a YAML file and returns the contents as a dictionary.
    file_path: str
    """
    try:  
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise AppException(e,sys) from e