#!/usr/bin/python3
"""
Contains the TestDBStorageDocs and TestDBStorage classes
"""

from datetime import datetime
import inspect
import models
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pep8
import unittest
DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


class TestDBStorage(unittest.TestCase):
    """Test the DBStorage class functionality with MySQL"""

    @classmethod
    def setUpClass(cls):
        """Setup test objects to be used by the test methods"""
        models.storage.reload()
        cls.state = State(name="California")
        cls.city = City(state_id=cls.state.id, name="San Francisco")
        models.storage.new(cls.state)
        models.storage.new(cls.city)
        models.storage.save()

    @classmethod
    def tearDownClass(cls):
        """Clean up resources after tests are done"""
        models.storage.delete(cls.city)
        models.storage.delete(cls.state)
        models.storage.save()

    def test_get(self):
        """Test the `get` method returns specific object by class and id"""
        state = models.storage.get(State, self.state.id)
        self.assertEqual(state.id, self.state.id)

    def test_get_none(self):
        """Test the `get` method returns None
        when no matching object is found"""
        self.assertIsNone(models.storage.get(State, "fake-id"))

    def test_count(self):
        """Test the `count` method counts all objects in storage"""
        initial_count = models.storage.count()
        new_state = State(name="California")
        models.storage.new(new_state)
        models.storage.save()
        self.assertEqual(models.storage.count(), initial_count + 1)
    
    def test_count_specific_class(self):
        """Test the `count` method with a class name argument"""
        state_count_before = models.storage.count(State)
        new_state = State(name="Arizona")
        models.storage.new(new_state)
        models.storage.save()
        state_count_after = models.storage.count(State)
        self.assertEqual(state_count_after, state_count_before + 1)
        models.storage.delete(new_state)
        models.storage.save()


class TestDBStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """Test that models/engine/db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """Test tests/test_models/test_db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_db_storage_module_docstring(self):
        """Test for the db_storage.py module docstring"""
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test for the DBStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

    def test_dbs_func_docstrings(self):
        """Test for the presence of docstrings in DBStorage methods"""
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""
    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_returns_dict(self):
        """Test that all returns a dictionaty"""
        self.assertIs(type(models.storage.all()), dict)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_no_class(self):
        """Test that all returns all rows when no class is passed"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_new(self):
        """test that new adds an object to the database"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_save(self):
        """Test that save properly saves objects to file.json"""
