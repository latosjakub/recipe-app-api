"""
Test custom Django managment commands.
"""
from unittest.mock import patch
#for mock behavior of the db 
from psycopg2 import OperationalError as Psycopg2Error
#One of possibilites we can get trying to connect to the db before db get ready

from django.core.management import call_command
# call_command enables to call commands 
from django.db.utils import OperationalError
#One of possibilites we can get trying to connect to the db before db get ready
from django.test import SimpleTestCase
#Base case class

#Mock a behavior of database
#Command that we will mocking 

@patch('core.management.commands.wait_for_db.Command.check')
class CommandsTest(SimpleTestCase):
    """Test commands."""

    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for database if database ready."""
        patched_check.return_value = True
        # it it is setting if db is on or not 
        call_command('wait_for_db')

        patched_check.assert_called_once_with(databases=['default'])

    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):

        patched_check.side_effect = [Psycopg2Error] * 2 + [OperationalError] * 3 + [True]

        call_command('wait_for_db')

        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_once_with(databases=['default'])