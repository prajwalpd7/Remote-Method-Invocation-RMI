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



##Run the following in 3 terminals:
python -m Pyro4.naming
python client.py
python server.py
