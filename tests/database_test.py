import unittest
import sys
from mock import patch, MagicMock

sys.path.append('../lib')

from database import Database


class TestPythonXL(unittest.TestCase):

	def setUp(self):
			path = '../files'
			self.x = Database(path)
			self.dummy_transaction = ['04/01/2015',' FIFTH THIRD PAID THIS ATM FEE ON YOUR BEHALF',2.0]

	def test_database_obj_without_constructor(self):
			self.assertTrue(isinstance(self.x,Database))

	def test_show_all_the_file_locations_that_will_be_uploaded(self):
			self.assertTrue(len(self.x.get_csv_file_paths_to_upload()) == 2)

	def test_database_connection(self):
			self.assertTrue(self.x.transaction_exists(self.dummy_transaction,'53').type == '53')

	def test_account_exists(self):
			self.assertTrue(self.x.get_account('53').name == '53')

	def test_upload_unique_transaction(self):
			with patch.object(self.x, 'upload_transaction', return_value='Uploaded') as mock_upload:
				self.x.upload_transaction(self.dummy_transaction,'53')

				assert len(mock_upload.call_args[0][0]) == 3
			


			

if __name__ == '__main__':
    unittest.main()