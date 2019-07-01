import unittest
import requests

class ApiTesting(unittest.TestCase):

    def __init__(self):
        self.apiUrl=input("Enter base URL: ")
        self.resource=input("Enter resource path: ")

    def setUp(self):
        pass
    
    def test_requestAPI(self):
        pass

    def tearDown(self):
        pass