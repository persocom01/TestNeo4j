# Neo4j tutorial

A neo4j testing playground.

## Installation

### Local machine

Download and install the desktop version from https://neo4j.com/download/

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

## Issuing commands

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
