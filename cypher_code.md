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

==============

//Adding a Node Correctly

match (n:ToyNode {name:'Julian'})

merge (n)-[:ToyRelation {relationship: 'fiancee'}]->(m:ToyNode {name:'Joyce', job:'store clerk'})

//Adding a Node Incorrectly

create (n:ToyNode {name:'Julian'})-[:ToyRelation {relationship: 'fiancee'}]->(m:ToyNode {name:'Joyce', job:'store clerk'})

//Correct your mistake by deleting the bad nodes and edge

match (n:ToyNode {name:'Joyce'})-[r]-(m) delete n, r, m

//Modify a Node’s Information

match (n:ToyNode) where n.name = 'Harry' set n.job = 'drummer'

match (n:ToyNode) where n.name = 'Harry' set n.job = n.job + ['lead guitarist']

//One way to "clean the slate" in Neo4j before importing (run both lines):

match (a)-[r]->() delete a,r

match (a) delete a

==============

//Script to Import Data Set: test.csv (simple road network)

//For Windows use something like the following

//[NOTE: replace any spaces in your path with %20, "percent twenty" ]

LOAD CSV WITH HEADERS FROM "file:///C:/coursera/data/test.csv" AS line

MERGE (n:MyNode {Name:line.Source})

MERGE (m:MyNode {Name:line.Target})

MERGE (n) -[:TO {dist:line.distance}]-> (m)


//For mac OSX use something like the following

//[NOTE: replace any spaces in your path with %20, "percent twenty" ]

LOAD CSV WITH HEADERS FROM "file:///coursera/data/test.csv" AS line

MERGE (n:MyNode {Name:line.Source})

MERGE (m:MyNode {Name:line.Target})

MERGE (n) -[:TO {dist:line.distance}]-> (m)


//Script to import global terrorist data

LOAD CSV WITH HEADERS FROM "file:///Users/jsale/sdsc/coursera/data/terrorist_data_subset.csv" AS row

MERGE (c:Country {Name:row.Country})

MERGE (a:Actor {Name: row.ActorName, Aliases: row.Aliases, Type: row.ActorType})

MERGE (o:Organization {Name: row.AffiliationTo})

MERGE (a)-[:AFFILIATED_TO {Start: row.AffiliationStartDate, End: row.AffiliationEndDate}]->(o)

MERGE(c)<-[:IS_FROM]-(a);

==============

Basic Graph Operations with CYPHER

//Counting the number of nodes

match (n:MyNode)

return count(n)

//Counting the number of edges

match (n:MyNode)-[r]->()

return count(r)

//Finding leaf nodes:

match (n:MyNode)-[r:TO]->(m)

where not ((m)-->())

return m

//Finding root nodes:

match (m)-[r:TO]->(n:MyNode)

where not (()-->(m))

return m

//Finding triangles:

match (a)-[:TO]->(b)-[:TO]->(c)-[:TO]->(a)

return distinct a, b, c

//Finding 2nd neighbors of D:

match (a)-[:TO*..2]-(b)

where a.Name='D'

return distinct a, b

//Finding the types of a node:

match (n)

where n.Name = 'Afghanistan'

return labels(n)

//Finding the label of an edge:

match (n {Name: 'Afghanistan'})<-[r]-()

return distinct type(r)

//Finding all properties of a node:

match (n:Actor)

return * limit 20

//Finding loops:

match (n)-[r]->(n)

return n, r limit 10

//Finding multigraphs:

match (n)-[r1]->(m), (n)-[r2]-(m)

where r1 <> r2

return n, r1, r2, m limit 10

//Finding the induced subgraph given a set of nodes:

match (n)-[r:TO]-(m)

where n.Name in ['A', 'B', 'C', 'D', 'E'] and m.Name in ['A', 'B', 'C', 'D', 'E']

return n, r, m
