Team 23 - Team members:

Rupika Peela
Punith Sai Vaddi
Sriram Malladi
Prudhvi Sai Reddy Gummireddy
Mogileeswar Reddy Morramreddygari

How to run the project:

1. Get the events tweet data from twitterAPIAunthentication.py
2. Run the react app which will let you to choose the event category and location to get the tweet data based on the selection.
3. SPARQL queries are used for querying the data using Fuseki server.
4. All the owl files are generated using protege and loaded onto the Fuseki server to run the queries to generate the data using the AWS EC2 instances.

To start fuseki instances: ("brew install putty" if not already installed)

1. Go to the API folder containing the .pem file to run the instances.
2. Connect with shell instance from terminal we need to use SSH protocol(Note: Go to the project folder with .pem file before executing command):
   ssh -i "fusekitest.pem" ec2-user@ec2-35-90-139-77.us-west-2.compute.amazonaws.com
   ssh -i "fusekitest.pem" ec2-user@ec2-35-90-160-230.us-west-2.compute.amazonaws.com
   ssh -i "fusekitest.pem" ec2-user@ec2-34-215-6-96.us-west-2.compute.amazonaws.com
3. Then run these commands to start fuseki server in each terminal execute: "cd apache-jena-fuseki-4.2.0/" and :
   for instance one "./fuseki-server --file /home/ec2-user/eventdata.owl /eventdata"
   for instance one "./fuseki-server --file /home/ec2-user/tweetdata.rdf /tweetdata"
   for instance one "./fuseki-server --file /home/ec2-user/userdata.owl /userdata"
4. The 3 instances are:
   http://ec2-35-90-139-77.us-west-2.compute.amazonaws.com:3030/
   http://ec2-35-90-160-230.us-west-2.compute.amazonaws.com:3030/
   http://ec2-34-215-6-96.us-west-2.compute.amazonaws.com:3030/

Cellfie Plugin in Protege is used to generate the RDF files for the fetched data to upload it to the Fuseki server and query through the data.

YouTube Link: https://youtu.be/EhVtUIyQaGc
