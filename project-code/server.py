
from flask import Flask, jsonify, render_template, render_template_string
from flask_restful import Api, Resource, reqparse
import connexion
import oyaml as yaml

app = connexion.App(__name__, specification_dir="./")


# Read the yaml file to configure the endpoints
app.add_api("server.yaml")

# create a URL route in our application for "/"
@app.route("/")
def home():
    with open("workflow.yaml", "r") as stream:
        data = yaml.load(stream)

    tasks = data["tasks"]
    for task in tasks:
        print(task)

    nodes = []
    edges = []

    for task in tasks:
        nodes.append({'id': task, 'label': task})

    nodes.append({'id': 'start', 'lable': 'start'})
    nodes.append({'id': 'end', 'lable': 'end'})

    flows = data["flow"].split("|")
    for flow in flows:
        arrows = flow.split(";")

        for i in range(0, len(arrows) - 1):
            edges.append({'from': arrows[i], 'to': arrows[i + 1], "arrows": 'to'})

    return render_template("home.html", nodes=nodes, edges=edges)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)


