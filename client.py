import socket
import  sys

host = 'localhost'
port = 9000
buffer = 1024

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host, port))

while True:
    helloMsg = mysock.recv(1024)
    print helloMsg

    file_list = mysock.recv(1024)
    print file_list
    while True:

        file_name = raw_input('Enter the file name: ')
        send_file_name_to_Server = mysock.send(file_name)

        file_Data = mysock.recv(buffer)
        #print fileData
        if not file_Data:
            break
        f1 = open(file_name, 'wb')
        f1.write(file_Data)
        f1.close()
        question = raw_input('Do you wish to continue ? (Y/N) >')
        send_to_server = mysock.send(question)
        if question == 'Y':
            continue
        else:
            exit()


mysock.close()
print 'Connection Closed'