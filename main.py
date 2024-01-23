from src.do_sparql_query import do_sparql_query

def main():
    q1 = "How old is Donald Knuth"
    print(f"{q1}: {do_sparql_query(q1)}")
    q2 = "How old is Radia Perlman"
    print(f"{q2}: {do_sparql_query(q2)}")
    q3 = "What is the birth name of Donal Knuth ?"
    print(f"{q3}: {do_sparql_query(q3)}")



if __name__ == '__main__':
    main()