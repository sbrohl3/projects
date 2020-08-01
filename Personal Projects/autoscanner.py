import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
done = False

while done == False:
    server = input('Please input your server IP Address: ')
    portnumlow = int(input('Please input your lowest Port to scan: '))
    portnumhigh = int(input('Please input your highest Port to scan: '))
    print('\n')

    for ports in range(portnumlow,portnumhigh + 1):
        try:
            s.connect((server,ports))
            print('Port',ports,'is open')
            print('\n')
        except:
            print('Port',ports,'is closed')
            print('\n')
