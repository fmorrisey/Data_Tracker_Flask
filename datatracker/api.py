import json
import requests
from types import SimpleNamespace


class api:
    def __init__(self):
        self.__init__ = True


    def requests_NameSpace(apiUrl): #Handle errors gracefully
        response = requests.get(apiUrl)
        json_data = json.loads(response.content, object_hook=lambda d: SimpleNamespace(**d)) \
            if response and response.status_code == 200 else None
        print(type(json_data))
        return json_data  # Returns a List / technically a class


    def requests_JSONDict(apiUrl): #Handle errors gracefully
        response = requests.get(apiUrl)
        json_data = response.json() \
            if response and response.status_code == 200 else None
        print(type(json_data))
        return json_data  # Returns a Dict / sorta


    def requests_byid(apiUrl):  # Handle errors gracefully
        response = requests.get(apiUrl)
        json_data = json.loads(response.content, object_hook=lambda d: SimpleNamespace(**d)) \
            if response and response.status_code == 200 else None
        print(type(json_data))
        return json_data  # Returns a List

