
### Scibite Coding Challenge (Python)

[DbPedia](http://wiki.dbpedia.org/) is a structured data version of Wikipedia.  It contains a [live RESTful api](http://dbpedia.org/sparql) which allows to issue SPARQL queries and receive results in a variety of formats.
This python code gets three specific questions in natural language and returns their answers.

The code is consists of three steps: 

1. Connect to the API, send a request and get a response:
	There are two approaches by using two python libraries in this code:
	- Requests library: `dbpedia_api_by_requests()`
	- SPARQLWrapper library: `dbpedia_api_by_sparqlwrapper()`

2. Translate natural language question to Sparql query:
	- Based on this challenge description we don't need to do any clever parsing, So I have only translated the questions based on two factors: name of the person and  the property we are looking for. `make_query()`
	- Generally for this part we can use new AI models to create Sparql queries from natural language question. [HuggingFace Hub]([Hugging Face – The AI community building the future.](https://huggingface.co/)) is a platform to find a proper pretrained AI model to do this. Transformers library provides lots of pretrained ML (deep learning) models for unstructured data such as text and vision. These models can be fine tuned with a dataset for a specific reason in [Amazon Sagemaker]([Machine Learning Service, Machine Learning Ide - Amazon SageMaker - AWS](https://aws.amazon.com/sagemaker/)) as a serverless environment.

3.  Extract output from the API response:
	- We get the response from API in `JSON` format and need to find the exact value of the property that asked in the input question. Finally the answer returns as the output. `extract_output()`

### Tests:
Two python libraries are used for unit testing:
- pytest: `test_do_sparql_query.py`
- unittest: `test_do_sparql_qyery_unittest.py`

### How to run the code:
Simply run the following command:
`make`

The output shows the possible actions to install requirements, run the code and test.
Makefile Menu:
1. `make install`: Install requirements
2. `make run` : Run the script
3. `make pytest` : Run pytest on all tests
4. `make unittest` : Run unittest

Notice: Install the requirements by `make install` before run or test.
