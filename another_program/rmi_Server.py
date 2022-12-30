import Pyro4

@Pyro4.expose
class Calculator(object):
    def add(self, n1, n2):
        return n1+n2
    def sub(self, n1, n2):
        return n1-n2

daemon = Pyro4.Daemon.serveSimple({Calculator: 'Calculator', }, host="localhost",port=8000,ns=False,verbose=True) # make a Pyro daemon
ns = Pyro4.localhost()   # find the name server
server = Calculator()
uri = daemon.register(server)  # register the maker as a Pyro object
ns.register('calculation_Server', uri)    # register the object with a name in the name server
print("READY.Calculator Server..")
daemon.requestLoop()                   # start the event loop of the server to wait for calls