import os
import json


def get_api_key_config():
    api_key_json_path = os.path.abspath(os.path.join(os.path.split(__file__)[0], "../../config/api_key.json"))
    with open(api_key_json_path, "r") as f:
        return json.load(f)

def get_model_name_config():
    model_name_json_path = os.path.abspath(os.path.join(os.path.split(__file__)[0], "../../config/model_name.json"))
    with open(model_name_json_path, "r") as f:
        return json.load(f)

def get_openai_key():
    api_key_config = get_api_key_config()
    return api_key_config.get("openai")

def get_openai_model():
    model_name_config = get_model_name_config()
    return model_name_config.get("openai_model")