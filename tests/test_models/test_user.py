#!/usr/bin/python3
"""
Contains the TestUserDocs classes
"""

from datetime import datetime
import inspect
import models
from models import user
from models.base_model import BaseModel
import pep8
import unittest
User = user.User
from os import getenv, remove

storage = getenv("HBNB_TYPE_STORAGE", "fs")


class TestUserDocs(unittest.TestCase):
    """Tests to check the documentation and style of User class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.user_f = inspect.getmembers(User, inspect.isfunction)

    def test_pep8_conformance_user(self):
        """Test that models/user.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_user(self):
        """Test that tests/test_models/test_user.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_user_module_docstring(self):
        """Test for the user.py module docstring"""
        self.assertIsNot(user.__doc__, None,
                         "user.py needs a docstring")
        self.assertTrue(len(user.__doc__) >= 1,
                        "user.py needs a docstring")

    def test_user_class_docstring(self):
        """Test for the City class docstring"""
        self.assertIsNot(User.__doc__, None,
                         "User class needs a docstring")
        self.assertTrue(len(User.__doc__) >= 1,
                        "User class needs a docstring")

    def test_user_func_docstrings(self):
        """Test for the presence of docstrings in User methods"""
        for func in self.user_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestUser(unittest.TestCase):
    """Test the User class"""
    @classmethod
    def setUpClass(cls):
        """Sets up unittest"""
        cls.new_user = User()
        cls.new_user.email = "email@gmail.com"
        cls.new_user.password = "password"
        cls.new_user.firt_name = "Mel"
        cls.new_user.last_name = "Ng"

    @classmethod
    def tearDownClass(cls):
        """Tears down unittest"""
        del cls.new_user
        try:
            remove("file.json")
        except FileNotFoundError:
            pass

    def test_User_dbtable(self):
        """Check if the tablename is correct"""
        self.assertEqual(self.new_user.__tablename__, "users")

    def test_User_inheritance(self):
        """tests that the User class Inherits from BaseModel"""
        self.assertIsInstance(self.new_user, BaseModel)

    def test_User_attributes(self):
        """Test the user attributes exist"""
        self.assertTrue("email" in self.new_user.__dir__())
        self.assertTrue("first_name" in self.new_user.__dir__())
        self.assertTrue("last_name" in self.new_user.__dir__())
        self.assertTrue("password" in self.new_user.__dir__())

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_email(self):
        """Test the type of name"""
        name = getattr(self.new_user, "email")
        self.assertIsInstance(name, str)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_first_name(self):
        """Test the type of name"""
        name = getattr(self.new_user, "first_name")
        self.assertIsInstance(name, str)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_last_name(self):
        """Test the type of last_name"""
        name = getattr(self.new_user, "last_name")
        self.assertIsInstance(name, str)

    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_type_password(self):
        """Test the type of password"""
        name = getattr(self.new_user, "password")
        self.assertIsInstance(name, str)
