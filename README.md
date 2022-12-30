# Remote-Method-Invocation-RMI

# Remote Method Invocation Demonstration

This project is a demonstration of Remote Method Invocation (RMI) using the Pyro - Python Remote Objects library. Pyro enables you to build distributed systems in which objects can communicate with each other over a network with minimal programming effort.

## Prerequisites

To run this project, you will need to have Python installed on your computer and have the Pyro library installed. You can install Pyro using the following command:

pip install Pyro4


## Running the Demonstration

The demonstration consists of a server script and a client script. To start the server, use the following command:

python server.py


To start the client, use the following command:

python client.py


The client will send a request to the server to invoke a method on a remote object, and the server will execute the method and return the result to the client.

## Customizing the Remote Object

You can customize the remote object by modifying the `MyClass` class in the server script. This class defines the methods that can be invoked remotely by the client. You can add additional methods or modify the existing methods as needed.

## Additional Notes

Remote Method Invocation is a powerful technique for building distributed systems, and Pyro makes it easy to get started with RMI in Python. This demonstration is just a simple example of the capabilities of RMI, and there are many other ways that RMI can be used in a variety of applications.


# Running the Pyro RMI Demonstration

To run the Pyro RMI demonstration, you will need to open three terminal windows and run the following commands in each window:

Terminal 1:
python -m Pyro4.naming

Terminal 2:
python client.py

Terminal 3:
python server.py


The `python -m Pyro4.naming` command starts the Pyro name server, which is responsible for managing the communication between the client and server. The `python client.py` command starts the client script, which sends a request to the server to invoke a method on a remote object. The `python server.py` command starts the server script, which hosts the remote object and responds to requests from the client.

With all three terminals running, you should see the client and server communicate with each other and execute the remote method.

## Additional Notes

This demonstration uses Pyro to enable remote communication between the client and server. Pyro is a powerful library for building distributed systems in Python, and this demonstration is just a simple example of the capabilities of Pyro. There are many other ways that Pyro can be used in a variety of applications.

