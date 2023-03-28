import json
from io import open
import os
import sys

csv_p = os.getcwd() + '/' + 'stimuli.csv'
json_p = os.getcwd() + '/stimuli.json'

def csv_to_json(csv_path, json_path, num_lists, list_id):
    try:
        with open(csv_path, encoding='utf-8') as csv_file:
            csv = csv_file.read()
    except:
        print("Could not find file to parse: " + csv_path)
        exit()

    ls = [item.split(',') for item in csv.split('\n')]
    cols = ls[0]
    d = {}
    c = {}
    for i in range(len(cols)):
        c[cols[i]] = i
    d['columns'] = c
    d['stimuli'] = {}

    for i in range(num_lists):
        d['stimuli'][list_id + str(i + 1)] = [item for item in ls if item[0] == list_id + str(i + 1)]
        if len(d['stimuli'][list_id + str(i + 1)]) == 0:
            print("Warning: empty list " + list_id + str(i + 1) + ". Please make sure you have entered your list number/prefix correctly.")
    try:
        with open(json_path, 'w') as js:
            json.dump(d, js, indent=4)
    except:
        print("Error with writing to file: " + json_path)
        exit()

csv_to_json(csv_p, json_p, 2, 'NList')
