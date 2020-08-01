import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
menu = True
while menu == True:
    server = input(str('Enter your Designated IP: '))
    Done = False
    while Done == False:
        portnum = input(str('Enter the port number you want to check: '))
        try:
            s.connect((server,portnum))
            print('Port',portnum,'is open')
            print('\n')
        except:
            print('Port',portnum,'is closed')
            print('\n')
        go = input(str('Enter y to continue entering ports or n to enter a new ip: '))
        if go == "y":
            Done = False
            Menu = False
        elif go == "n":
            Done = True
            Menu = True
