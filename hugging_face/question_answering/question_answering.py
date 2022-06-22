import json
from pathlib import Path

from transformers import pipeline

from elastic_search.utilities.login import login
from hugging_face.question_answering.utilities.es_search import search_es


def question_answer(question):
    return main(question=question)


def main(question="Gibt es die Möglichkeit eines Auslandssemesters?"):
    index_name = get_index_name()
    es = login()
    answer_count = get_relevant_results_from_elasticsearch(es_connection=es, index_name=index_name, question=question)
    if answer_count <= 0:
        return {

            }
    extract_answer()
    # write_answer_to_json()
    return get_json()


def get_index_name():
    path_to_project_root = Path(__file__).parent.parent.parent
    path_to_index_config = Path.joinpath(path_to_project_root, 'elastic_search\\utilities\\index_config.json')
    with open(path_to_index_config) as file:
        index_name = json.load(file)[0]['index_name']
        return index_name


def get_relevant_results_from_elasticsearch(es_connection, index_name, question):
    print('getting relevant database entries...')
    global question_text, es_answers
    question_text = question
    es_answers = search_es(
        es_instance=es_connection,
        index_name=index_name,
        question_text=question_text,
        number_of_results=10
        )
    # print(f'Question: {question_text}')
    # print(f'Query Duration: {es_answers["took"]} milliseconds')
    # print('Title, Relevance Score:')
    # [(hit['_source']['document_title'], hit['_score']) for hit in es_answers['hits']['hits']]
    answer_count = es_answers["hits"]["total"]["value"]
    print(f'got {answer_count} database entries')
    return answer_count


def extract_answer():
    print('looking for best answer...')
    global best_answer, best_answer_index
    # Define QA Pipeline
    qas = pipeline(
        model='deutsche-telekom/bert-multi-english-german-squad2',
        task='question-answering'
        )
    # Get the best answer according to Happy face' score from
    # the 10 most relevant database entry's according to elastic search
    best_answer = {'score': 0}
    best_answer_index = 0
    index = 0
    for hit in es_answers['hits']['hits']:
        index += 1
        answer = qas(
            question=question_text,
            context=hit['_source']['document_text']
            )
        if answer['score'] > best_answer['score']:
            best_answer = answer
            best_answer_index = index
    # print(best_answer)
    print('best answer found')


def get_json():
    answer = {
        'question': question_text,
        'answer': best_answer["answer"],
        'score': best_answer['score'],
        'link': ''
        }

    if 'link' in es_answers['hits']['hits'][best_answer_index]['_source']:
        answer['link'] = es_answers['hits']['hits'][best_answer_index]['_source']['link']

    return json.dumps(answer)


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
    print(main())
