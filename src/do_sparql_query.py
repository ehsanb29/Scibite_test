import requests
import pprint
from datetime import datetime, date

def do_sparql_query(question: str):

    # connect to the API by requests library
    # results, prop = dbpedia_api_by_requests(question)

    # connect to the API by SPARQLWrapper library
    results, prop = dbpedia_api_by_sparqlwrapper(question)
    return extract_output(results=results, prop=prop)


def dbpedia_api_by_requests(question: str):
    '''Make a Restful request and send to dbpedia API
        by requests library
    param: 
        question: a question in natural language
    return: 
        response: the response in json format
        prop: the property taht shows type of the question 
    '''

    # set api_endpoint
    url = "http://dbpedia.org/sparqll"

    # Pars question to create sparql query
    query, prop = make_query(question)

    # Set the response format to headers
    headers = {'Accept': 'application/json'}

    # Set the query as a pyload for API
    payload = {'query': query}

    # Send a RESTful request to the api_endpoint address, query and the output format we expect
    response = requests.get(url=url, params=payload, headers=headers)

    # Check if the request was successful (status code 200) or print the response code and the reason
    if response.status_code == 200:
        # Return json-encoded content of reponse
        return response.json()['results']['bindings'], prop
    else:
        print(f"API returns an error code '{response.status_code}' for this reason: {response.reason}")


def dbpedia_api_by_sparqlwrapper(question: str):
    '''Make connection to dbpedia api endpoint
        using SPARQLWrapper library
    param: 
        question: a question in natural language
    return: 
        response: the response in json format
        prop: the property that shows type of the question 
    '''
    from SPARQLWrapper import SPARQLWrapper, SPARQLExceptions

    # Create and SPRQLWrapper instance with dbpedia endpoint
    spql = SPARQLWrapper("http://dbpedia.org/sparql")

    # Make query based on input question (Question parsing)
    query, prop = make_query(question)

    # Set query for SPARQLwrapper instance
    spql.setQuery(query)

    # Set the return format
    spql.setReturnFormat('json')

    try:
        # Run the query and return the response
        response = spql.query().convert()
        # response = spql.queryAndConvert()
        # pprint(qry_res)
        return response['results']['bindings'], prop
    # Handle possible error
    except SPARQLExceptions.QueryBadFormed as e:
        print(f"SPARQL query is badly formed: {e}")
        exit(0)
    except SPARQLExceptions.EndPointNotFound as e:
        print(f"SPARQL endpoint not found: {e}")
        exit(0)
    except SPARQLExceptions.EndPointInternalError as e:
        print(f"SPARQL endpoint internal error: {e}")
        exit(0)


def make_query(question: str):
    '''Make Sparql query form natural language question
    param: 
        question: a question in natural language
    return: 
        query: Sparql query
        prop: the property that shows type of the question 
    '''
    name = ""
    prop = ""

    #  
    if "donald knuth" in question.lower() or "donal knuth" in question.lower():
        name = "Donald_Knuth"
    elif "radia perlman" in question.lower():
        name = "Radia_Perlman"
    
    if "how old" in question.lower():
        prop = "dob"
        query = f"SELECT  ?dob FROM <http://dbpedia.org> WHERE {{dbr:{name} dbp:birthDate ?dob .}}"
    elif "birth name" in question.lower():
        prop = "name"
        query = f"""SELECT  ?p ?name 
        FROM <http://dbpedia.org> 
        WHERE {{dbr:{name}?p ?name . FILTER (?p IN (dbp:birthname, dbp:birthName) ) }}"""

    return query, prop


def extract_output(results: any, prop: str):
    '''extrcat the output data form Json data
    param:
        results: Json data responded by the api
        prop: the property that shows type of the question 
    return:
        output: the answer for the input question
    '''
    # extract the response data
    for result in results:
        if prop == 'name':
            # print(result[prop]['value'])
            output = result[prop]['value']
        if prop == 'dob':
            # convert birthdate value to date type
            birth_date = datetime.strptime(result[prop]['value'], '%Y-%M-%d').date()
            # retrive current date
            curren_date = date.today()
            # calculate age
            age = curren_date.year - birth_date.year
            output = age
    return output