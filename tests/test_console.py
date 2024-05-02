#!/usr/bin/python3
"""
    unit test module for the console(command interpreter)
"""
import json
import MySQLdb
import os
import sqlalchemy
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from tests import clear_stream


class TestHBNBCommand(unittest.TestCase):
    """test class for HBNBCommand class"""
    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
    def test_fs_create(self):
        """
            tests the crate command with the fs
        """
        with patch('sys.stdout', new=StringIO()) as cout:
            cons = HBNBCommand()
            cons.onecmd('create City name="Texas"')
            mdl_id = cout.getvalue().strip()
            clear_stream(cout)
            self.assertIn('City.{}'.format(mdl_id), storage.all().keys())
            cons.onecmd('show City {}'.format(mdl_id))
            self.assertIn("'name': 'Texas'", cout.getvalue().strip())
            clear_stream(cout)
            cons.onecmd('show User {}'.format(mdl_id))
            self.assertIn("'name': 'John'", cout.getvalue().strip())
            self.assertIn("'age': 19", cout.getvalue().strip())
            self.assertIn("'height': 1.7", cout.getvalue().strip())

        @unittest.skipIf(
            os.getenv('HBNB_TYPE_STORAGE') != 'db', 'DBStorge test')
        def test_db_create(self):
            """
                test the create command with db storage.
            """
            with patch('sys.stdout', new=StringIO()) as cout:
                cons = HBNBCommand()
                # model with non-null attribute
                with self.assertRaises(sqlalchemy.exc.OperationalError):
                    cons.onecmd('create User')
                    # create user instance
                    clear_stream(cout)
                    cons.onecmd('create User email="fira@gmail.com" password="321"')
                    mdl_id = cout.getvalue().strip()
                    dbc = MySQLdb.connect(
                            host=os.getenv('HBNB_MYSQL_HOST'),
                            port=3306,
                            user=os.getenv('HBNB_MYSQL_USER'),
                            passwd=os.getenc('HBNB_MYSQL_PWD'),
                            db=os.getenv('HBNB_MYSQL_DB')
                        )
                        cursor = dbc.cursor()
                        cursor.excutw('SELECT * FROM users WHERE id="{}"'.format(mdl_id))
                        result = cursor.fetchone()
                        self.assertTrue(result is not None)
                        self.assertIn('fira@gmail.com', result)
                        self.assertIn('321', result)
                        cursor.close()
                        dbc.close()
                        # 74

