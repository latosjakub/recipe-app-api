"""
Test custom Django managment commands.
"""
from unittest.mock import patch
#for mock behavior of the db 
from psycopg2 import OperationalError as Psycop2Error
#One of possibilites we can get trying to connect to the db before db get ready

from django.core.management import call_command
# call_command enables to call commands 
from django.db.utils import OperationalError
#One of possibilites we can get trying to connect to the db before db get ready
from django.test import SimpleTestCase
#Base case class

class CommandsTest(SimpleTestCase):
    """Test commands."""

    def test_wait_for_db_ready(self):
        """Test waiting for database if database ready."""