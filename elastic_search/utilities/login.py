import json
import os
import sys

from elasticsearch import Elasticsearch


def get_root_dir():
    return os.path.abspath('readme.md').split('chatbot_project')[0] + 'chatbot_project'


def login():
    print('Connecting to elastic search...')
    # Read credentials
    with open(f'{get_root_dir()}\\elastic_search\\credentials.json') as file:
        data = json.load(file)
        elastic_user = data['username']
        elastic_password = data['password']
        elastic_url = data['url']

    if not elastic_password:
        sys.exit("No credentials found! You need to set the elastic search password in credentials.json!")

    # Configurate Elastic Search
    es = Elasticsearch(
        elastic_url,
        verify_certs=False,
        basic_auth=(elastic_user, elastic_password)
        )

    # Test connection
    if not es.ping():
        sys.exit(
            "Cannot establish connection to elastic search. Check if elastic search is running! Check if URL, user and password are set correctly in the credentials.json file!")
    else:
        print("Connection to elastic search successfully established")
        return es


if __name__ == '__main__':
    login()
