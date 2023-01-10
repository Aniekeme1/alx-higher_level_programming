#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed jan 11th 2023
@author: Aniekeme Umoren
"""
import json


def from_json_string(my_str):
    """
    Convert a json string to a python object
    Arguments:
        my_obj (str): The inputed object to convert in json format
    Return:
        A Python object from json
    """
    return json.loads(my_str)
