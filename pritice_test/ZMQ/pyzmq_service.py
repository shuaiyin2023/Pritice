import time
import zmq


# 服务器
connect = zmq.Context()
soket = connect.socket(zmq.REP)
soket.bind("tcp://*:5555")


while True:
    message = soket.recv()
    print("这是服务端···\n")
    print("Received message: {}".format(message))
    time.sleep(1)

    soket.send(b"World")


