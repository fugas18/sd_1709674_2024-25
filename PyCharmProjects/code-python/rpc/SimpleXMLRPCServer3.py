from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(('localhost', 8001),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Register a function under a different name
    def soma(n):
        sum=0
        for i in range (1,n+1):
            sum =sum+i**3
        return sum

    server.register_function(soma, 'ss')

    # Run the server's main loop
    server.serve_forever()

