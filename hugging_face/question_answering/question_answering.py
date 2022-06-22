import json

from transformers import pipeline

from elastic_search.utilities.login import login
from utilities.es_search import search_es


def question_answer(question="Was ist ein duales Studium"):
    main(question=question)


def main(question):
    index_name = get_index_name()
    es = login()
    get_relevant_results_from_elasticsearch(es_connection=es, index_name=index_name, question=question)
    extract_answer()
    write_answer_to_json()


def get_index_name():
    with open('../../elastic_search/utilities/index_config.json') as file:
        index_name = json.load(file)[0]['index_name']
        return index_name


def get_relevant_results_from_elasticsearch(es_connection, index_name, question):
    global question_text, es_answers
    question_text = question
    es_answers = search_es(es_instance=es_connection, index_name=index_name, question_text=question_text,
                           number_of_results=10)
    # print(f'Question: {question_text}')
    # print(f'Query Duration: {es_answers["took"]} milliseconds')
    # print('Title, Relevance Score:')
    # [(hit['_source']['document_title'], hit['_score']) for hit in es_answers['hits']['hits']]


def extract_answer():
    global best_answer
    # Define QA Pipeline
    qas = pipeline(
        model='deutsche-telekom/bert-multi-english-german-squad2',
        task='question-answering'
        )
    # Get the best answer according to Happy face' score from
    # the 10 most relevant database entry's according to elastic search
    best_answer = {'score': 0}
    for hit in es_answers['hits']['hits']:
        answer = qas(
            question=question_text,
            context=hit['_source']['document_text']
            )
        if answer['score'] > best_answer['score']:
            best_answer = answer
    # print(best_answer)


def write_answer_to_json():
    # Write the answer to a JSON file
    answer_dict = dict([
        ("question", question_text),
        ("answer", best_answer["answer"]),
        ("score", best_answer['score']),
        ('link', es_answers['hits']['hits'][0]['_source']['link'])
        ])
    # Write answer to a JSON file
    with open('answer.json', 'w') as file:
        json.dump(answer_dict, file, ensure_ascii=False)


if __name__ == '__main__':
    main()
