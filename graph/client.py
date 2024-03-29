# minimalistic client example from 
# https://github.com/seprich/py-bson-rpc/blob/master/README.md#quickstart
from node import *
import socket
from bsonrpc import JSONRpc
from bsonrpc.exceptions import FramingError
from bsonrpc.framing import (
	JSONFramingNetstring, JSONFramingNone, JSONFramingRFC7464)    
    
def convertVal(graph):

    vals = {}

    for c in graph.children:
        vals.update({c.name: c.val})
        convertVal(c)

    return vals    


leaf1 = node("leaf1")
leaf2 = node("leaf2")

root = node("root", [leaf1, leaf1, leaf2])

print("graph before increment")
root.show()

vals = convertVal(root)

print(vals)

# Cut-the-corners TCP Client:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 50001))

rpc = JSONRpc(s,framing_cls=JSONFramingNone)
server = rpc.get_peer_proxy()
# Execute in server:
result = server.increment(vals) #asking server for the swapper method to be performed; waits for the server to give an input back
# result:              "!dlroW olleH"

vals = result

print(vals)
    
print("graph after increment")
root.show()

print(server.nop({1:[2,3]}))

rpc.close() # Closes the socket 's' also
