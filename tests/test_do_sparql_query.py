import pytest
from src.do_sparql_query import do_sparql_query

def test_do_sparql_query():
    assert do_sparql_query("How old is Donald Knuth") == 85
    assert do_sparql_query("How old is Radia Perlman") == 72
    assert do_sparql_query("What is the birth name of Donal Knuth ?") == "Donald Ervin Knuth"