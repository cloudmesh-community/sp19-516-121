
from flask import Flask, jsonify, render_template, render_template_string
from flask_restful import Api, Resource, reqparse
import connexion

app = connexion.App(__name__, specification_dir="./")


# Read the yaml file to configure the endpoints
app.add_api("server.yaml")

# create a URL route in our application for "/"
@app.route("/")
def home():
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
        {id: 1, label: 'Node 1'},
        {id: 2, label: 'Node 2'},
        {id: 3, label: 'Node 3'},
        {id: 4, label: 'Node 4'},
        {id: 5, label: 'Node 5'}
    ]);

    // create an array with edges
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

    return render_template_string(content)



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)


