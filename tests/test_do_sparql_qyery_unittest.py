import unittest
from src.do_sparql_query import do_sparql_query

class TestClass(unittest.TestCase):
    def test_do_sparql_query(self):
        self.assertTrue(do_sparql_query("How old is Donald Knuth") == 85)
        self.assertTrue(do_sparql_query("How old is Radia Perlman") == 72)
        self.assertTrue(do_sparql_query("What is the birth name of Donal Knuth ?") == "Donald Ervin Knuth")