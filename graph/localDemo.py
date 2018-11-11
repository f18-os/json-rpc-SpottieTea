from node import *

leaf1 = node("leaf1")
leaf2 = node("leaf2")

root = node("root", [leaf1, leaf1, leaf2])

print("graph before increment")
root.show()

# do this increment remotely: (using the server)
increment(root)

print("graph after increment")
root.show()

#pass this tree through json-rpc--the server---then perform a function and send it back. You can make it increment, but it cooould have additional functions...!

