import json
import sys
from pathlib import Path

from elasticsearch import Elasticsearch


def login():
    print('Connecting to elastic search...')
    path_to_project_root = Path(__file__).resolve().parent.parent.parent
    path_to_credentials = Path.joinpath(path_to_project_root, 'elastic_search\\credentials.json')
    # Read credentials
    with open(path_to_credentials) as file:
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
