def search_es(es_instance, index_name, question_text, number_of_results):
    # construct query
    query = {
        'query': {
            'match': {
                'document_text': question_text
                }
            }
        }

    response = es_instance.search(index=index_name, body=query, size=number_of_results)
    return response
