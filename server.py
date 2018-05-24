import socket
from thread import *
import os.path

host = 'localhost'
port = 9000
folder_location = '/Users/Downloads/'

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
mysock.bind((host, port))
print 'Socket binding complete'
mysock.listen(5)
print 'Socket Listening'


def client_thread(conn):

    while True:
        conn.send('Hi... I am server.\n')

        send_file_names(conn)
        data = conn.recv(1024)
        print data
        download_file(conn, data)
        receive = conn.recv(1024)
        if receive == 'N':
            exit()
        else:
            continue


def send_file_names(conn):

    file_names = os.listdir(folder_location)
    conn.sendall('Files available to download: %s\n' % file_names)
    #print file_names


def download_file(conn, data):

    f1 = open('/Users/sufyjakate/Downloads/Pyes/%s' % data, 'rb')
    f2 = f1.read()
    conn.sendall(f2)


while True:
    conn, address = mysock.accept()
    start_new_thread(client_thread, (conn,))


conn.close()
mysock.close()
