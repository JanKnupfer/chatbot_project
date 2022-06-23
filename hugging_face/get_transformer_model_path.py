import json
import sys
from pathlib import Path


def get_transformer_model_path():
    path_to_project_root = Path(__file__).resolve().parent.parent
    path_to_credentials = Path.joinpath(path_to_project_root, 'hugging_face\\transformer_model.json')
    # Read credentials
    with open(path_to_credentials) as file:
        data = json.load(file)
        model_name = data['model']
        is_local = data['local']

    if not model_name:
        sys.exit("No transformer model path found! You need to set the path in tranformer_model.json!")

    if is_local:
        # Todo add location of local model
        model_path = Path.joinpath(path_to_project_root, "PATH", model_name)
        return model_path

    return model_name


if __name__ == '__main__':
    get_transformer_model_path()
