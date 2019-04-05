from flask import Flask, jsonify, render_template, render_template_string
from flask import jsonify


def get_template():
    content = '''
                 <html>
    <head>
        <script type="text/javascript" src="{{ url_for('static', filename="js/vis.js")}}"></script>
        <link href="{{ url_for('static', filename="css/vis.css")}}" rel="stylesheet" type="text/css" />

        <style type="text/css">
            #mynetwork {
                width: 600px;
                height: 400px;
                border: 1px solid lightgray;
            }
        </style>
    </head>
    <body>
    <div id="mynetwork"></div>

    <script type="text/javascript">
    
       
        // create an array with nodes
         
        var nodes = new vis.DataSet([
            {{nodes}}
        ]);

        // create an array with edges
        {{ edges }}
        var edges = new vis.DataSet([
            {from: 1, to: 3},
            {from: 1, to: 2},
            {from: 2, to: 4},
            {from: 2, to: 5}
        ]);

        // create a network
        var container = document.getElementById('mynetwork');

        // provide the data in the vis format
        var data = {
            nodes: nodes,
            edges: edges
        };
        var options = {};

        // initialize your network!
        var network = new vis.Network(container, data, options);
    </script>
    </body>
    </html> 
                  '''
    return content;

def check():
    content = get_template()
    nodes= [{'id': 1, 'label': 'Node1'},
            {'id': 2, 'label': 'Node2'},
            {'id': 3, 'label': 'Node3'},
            {'id': 4, 'label': 'Node4'},
            {'id': 5, 'label': 'Node5'}]


    return render_template("home.html", nodes=nodes)


def monitor(workflow):
    flow = workflow.get("flow", None)
    tasks = workflow.get("tasks", None)