# Demonstrates basic cypher code creating and deleting nodes and edges.
import json
import py2neo as p2n

with open(r'.\keys.json') as f:
    keys = json.load(f)

# If the server is not specified, it appears to use bolt://localhost:7687 by
# default.
gdb = p2n.Graph(
    "bolt://localhost:7687",
    user=keys['user'],
    password=keys['password']
)

# Creates the nodes.
command = '''
create (N1:ToyNode {name: 'Tom'}) - [:ToyRelation {relationship: 'knows'}] -> (N2:ToyNode {name: 'Harry'}),
(N2) - [:ToyRelation {relationship: 'co-worker'}] -> (N3:ToyNode {name: 'Julian', job: 'plumber'}),
(N2) - [:ToyRelation {relationship: 'wife'}] -> (N4:ToyNode {name: 'Michele', job: 'accountant'}),
(N1) - [:ToyRelation {relationship: 'wife'}] -> (N5:ToyNode {name: 'Josephine', job: 'manager'}),
(N4) - [:ToyRelation {relationship: 'friend'}] -> (N5)
;
'''
print(gdb.run(command).to_table())

# Displays the graph as a table. It's much better to see it on the graph app
# using the browser.
command = '''
match (n:ToyNode)-[r]-(m) return n, r, m
'''
print(gdb.run(command).to_table())

# Deletes all nodes and edges.
command = '''
match (n)-[r]-() delete n, r
'''
print(gdb.run(command).to_table())
