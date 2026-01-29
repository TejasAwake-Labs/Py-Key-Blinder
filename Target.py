from multiprocessing.connection import Listener

R =Listener(('localhost',5000)).accept()
while True:
    Data = R.recv()
    print(Data)

