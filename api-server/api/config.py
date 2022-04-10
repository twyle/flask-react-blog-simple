"""
Empty module docstring
"""
import os


class BaseConfig():
    """
    Empty class docstring
    """

    SECRET_KEY = os.environ['SECRET_KEY']
    DEBUG = False
    TESTING = False
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class DevelopmentConfig(BaseConfig):
    """
    Empty class docstring
    """

    DEBUG = True
    TESTING = True


class ProductionConfig(BaseConfig):
    """
    Empty class docstring
    """

    DEBUG = False
    TESTING = False
