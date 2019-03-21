import js2py

import oyaml as yaml


with open("workflow.yaml", "r") as stream:
    data = yaml.load(stream)

tasks = data["tasks"]
for task in tasks:
    print(task)


def visualize(workflow):
    flows = workflow.split("|")







