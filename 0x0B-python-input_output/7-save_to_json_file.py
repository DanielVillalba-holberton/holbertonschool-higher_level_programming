#!/usr/bin/python3
"""module save a json file"""
import json


def save_to_json_file(my_obj, filename):
    """saves JSON in a file"""
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
        f.close()
