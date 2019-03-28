import js2py

import oyaml as yaml
import requests
from flask import jsonify



with open("workflow.yaml", "r") as stream:
    data = yaml.load(stream)

tasks = data["tasks"]
for task in tasks:
    print(task)

url = "http://127.0.0.1:8090/"
response = requests.get(url + "visualize/graph/" + jsonify(tasks))

def visualize(workflow):
    flows = workflow.split("|")







