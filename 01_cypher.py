import json
import py2neo as p2n

with open(r'.\boto3\keys.json') as f:
    keys = json.load(f)

gdb = p2n.Graph(
    user=keys['user'],
    password=keys['password']
)
