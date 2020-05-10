# Neo4j tutorial

A neo4j testing playground.

## Installation

The neo4j python driver can be installed via cmd by entering one of the following:

```
pip install neo4j
pip install py2neo
```

* neo4j is the official neo4j driver.
* py2neo is a community python package with more features, but doesn't fully support the enterprise edition yet.

### Local machine

1. Download the community (free) version and unpack it into a folder of your choice: https://neo4j.com/download-center/#community

2. To run the database server, open cmd in the folder (left click the empty part of the address bar in explorer and enter cmd) and enter in cmd:

```
bin\neo4j console
```

Use ctrl + c to exit.

In case of "error: missing JVM", download and install JRE or JDK (JRE but with developer tools) of the appropriate version (ver 11 for neo4j 4.0.4) here: https://www.oracle.com/java/technologies/javase-downloads.html

You might also need to enter path for java.exe into windows environmental variables. Java can normally be found at:

```
C:\Program Files\Java\jre_or_jdk-version\bin
```

Then run the cmd command again. For more, see: https://neo4j.com/docs/operations-manual/current/installation/windows/

3. Visit the neo4j web app using a web browser at localhost:7474. (shields down)

### Bitnami neo4j community edition on AWS

1. Spin up an AWS EC2 instance by choosing the appropriate BitNami neo4j AMI from this list https://bitnami.com/stack/neo4j/cloud/aws/amis

2. Download the .pem key.

3. git bash (install on computer if not already present) in the folder with the key and type:

```
chmod 400 keyname.pem
```

which gives the user permission to read the file (4) and no permissions (0) to the group and everyone else.

4. Connect to the aws instance using the following command:

```
ssh -i keyname.pem bitnami@aws_instance_public_dns
```

We also need the application login username and password. To get this, enter the following command when connected to the server:

```
cat ./bitnami_credentials
```

Alternatively, right clicking the AWS instance in AWS console > instance settings > get system log will open a window that contains the username and password. This has to be done 24hrs from first boot.

To end the connection, enter:

```
exit
```

## Issuing commands

To determine the edition and version of the neo4j instance, open the cypher shell and enter:

```
call dbms.components() yield name, versions, edition unwind versions as version return name, version, edition;
```

### Neo4j admin

Neo4j admin is a tool used to manage the neo4j instance. It can be accessed after connecting to the ec2 server and entering:

```
neo4j-admin command
```

Commands found here: https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/

### Cypher shell

Cypher shell is used to run queries to the neo4j database. It can be accessed while connected to the ec2 server by entering:

```
cypher-shell
```

The application username and password are used to log into the database. Use ctrl z to exit.

Commands found here: https://neo4j.com/docs/operations-manual/current/tools/cypher-shell/
