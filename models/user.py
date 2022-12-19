#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """To represent a User.
    Attributes:
        email (str): The User email.
        password (str): The User password.
        first_name (str): The User first name.
        last_name (str): The User last name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
