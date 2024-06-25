import zmq
# 客户端
context = zmq.Context()
print("这是客户端发起的请求····\n")
print("Connecting to server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")


for i in range(10):
    print("Sending message: {}".format(i))
    socket.send(b"Hello")

    message = socket.recv()
    print("Received message: {}".format(message))
