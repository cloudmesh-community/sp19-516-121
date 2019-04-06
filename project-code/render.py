from flask import Flask, jsonify, render_template, render_template_string
from flask import jsonify
import oyaml as yaml



def show():

    with open("workflow.yaml", "r") as stream:
        data = yaml.load(stream)

    tasks = data["tasks"]
    for task in tasks:
        print(task)

    nodes = []
    edges = []

    for task in tasks:
        nodes.append({'id': task, 'label': task})

    nodes.append({'id': 'start', 'label': 'start'})
    nodes.append({'id': 'end', 'label': 'end'})

    flows = data["flow"].split("|")
    for flow in flows:
        arrows = flow.split(";")

        for i in range(0, len(arrows) - 1):
            edges.append({'from': arrows[i], 'to': arrows[i + 1], "arrows": 'to'})

    return render_template("home.html", nodes=nodes, edges=edges)


def update(workflow):
    flow = workflow.get("flowyaml", None)
    data = yaml.load(flow)
    with open('workflow.yaml', 'w') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)
    show()
