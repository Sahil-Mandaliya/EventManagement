from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

from main_app.utils.pydantic import convert_json_to_pydantic, convert_json_list_to_pydantic_list
import json

def model_to_json(model_instance, pydantic_class):
    return jsonable_encoder(db_model_to_pydantic(model_instance, pydantic_class))


def model_list_to_json(instances, pydantic_class):
    new_instances = []
    for obj in instances:
        new_instances.append(model_to_json(obj))
    
    return new_instances


def db_model_to_pydantic(instance, pydantic_model_class: BaseModel):
    # json_data = model_to_json(instance)
    # return convert_json_to_pydantic(json_data, pydantic_model_class)
   return pydantic_model_class.from_orm(instance)

def db_model_list_to_pydantic(instances, pydantic_model_class: BaseModel):
    pydantic_instances = []
    for instance in instances:
        pydantic_instances.append(db_model_to_pydantic(instance, pydantic_model_class))
    return pydantic_instances

    # json_data = model_list_to_json(instances)
    # return convert_json_list_to_pydantic_list(json_data, pydantic_model_class)