create (N1:ToyNode {name: 'Tom'}) - [:ToyRelation {relationship: 'knows'}] -> (N2:ToyNode {name: 'Harry'}),

(N2) - [:ToyRelation {relationship: 'co-worker'}] -> (N3:ToyNode {name: 'Julian', job: 'plumber'}),

(N2) - [:ToyRelation {relationship: 'wife'}] -> (N4:ToyNode {name: 'Michele', job: 'accountant'}),

(N1) - [:ToyRelation {relationship: 'wife'}] -> (N5:ToyNode {name: 'Josephine', job: 'manager'}),

(N4) - [:ToyRelation {relationship: 'friend'}] -> (N5)

;

More code examples
==============

View the resulting graph

match (n:ToyNode)-[r]-(m) return n, r, m

==============

Delete all nodes and edges

match (n)-[r]-() delete n, r

==============

Delete all nodes which have no edges

match (n) delete n

==============

Delete only ToyNode nodes which have no edges

match (n:ToyNode) delete n

==============

Delete all edges

match (n)-[r]-() delete r

==============

Delete only ToyRelation edges

match (n)-[r:ToyRelation]-() delete r

//Selecting an existing single ToyNode node

match (n:ToyNode {name:'Julian'}) return n
