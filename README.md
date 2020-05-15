# Neo4j tutorial

A neo4j testing playground.

## Installation

The neo4j python driver can be installed via cmd by entering one of the following:

```
pip install neo4j
conda install -c conda-forge py2neo
```

* neo4j is the official neo4j driver.
* py2neo is a community python package with more features, but doesn't fully support the enterprise edition yet.

### Local machine

1. Download the community (free) version and unpack it into a folder of your choice: https://neo4j.com/download-center/#community

2. To run the database server, open cmd in the folder (left click the empty part of the address bar in explorer and enter cmd) and enter in cmd:

```
bin\neo4j console
```

Use ctrl c to exit.

In case of "error: missing JVM", download and install JRE or JDK (JRE but with developer tools) of the appropriate version (ver 11 for neo4j 4.0.4) here: https://www.oracle.com/java/technologies/javase-downloads.html

You might also need to enter path for java.exe into windows environmental variables. Java can normally be found at:

```
C:\Program Files\Java\jre_or_jdk-version\bin
```

Then run the cmd command again. For more, see: https://neo4j.com/docs/operations-manual/current/installation/windows/

The neo4j web app can now be accessed using a web browser at localhost:7474. (shields down)

#### Plugin installation

1. Download the plugin from the same place you got the community edition: https://neo4j.com/download-center/#community

2. Unpack the .jar file into neo4j's plugins folder.

3. Navigate to the conf folder and open neo4j.conf in notepad. Find the following line, remove the # from the following line and add gds.* to it:

```
dbms.security.procedures.unrestricted=gds.*
```

In addition, it is necessary to add gds.* to the whitelist if you use one:

```
dbms.security.procedures.whitelist=apoc.coll.*,apoc.load.*,gds.*
```

4. Restart the neo4j server. You may now use the plugin apis from the browser interface.

### Bitnami neo4j community edition on AWS

1. Spin up an AWS EC2 instance by choosing the appropriate BitNami neo4j AMI from this list: https://bitnami.com/stack/neo4j/cloud/aws/amis

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

To remove the added ip from the known hosts list, use:

```
ssh-keygen -R server_ip_address
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

The community edition of neo4j only allows 1 database, so any additional will require usage of images.

When importing data into neo4j without python, the data must be located in neo4j_path/import/

Neo4j commands are case sensitive.

### Neo4j admin

Neo4j admin is a tool used to manage the neo4j instance. It can be accessed on the local machine using cmd from the neo4j folder and entering:

```
bin\neo4j-admin
```

For ec2 servers, connect tot he server and enter:

```
neo4j-admin
```

Commands found here: https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin/

### Cypher shell

Cypher shell is used to run queries to the neo4j database. It can be accessed while connected to the ec2 server by entering:

```
cypher-shell
```

The application username and password are used to log into the database. Use ctrl z to exit.

Commands found here: https://neo4j.com/docs/operations-manual/current/tools/cypher-shell/
