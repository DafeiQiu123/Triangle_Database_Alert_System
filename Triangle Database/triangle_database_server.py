import socket
import pymysql.cursors

# Create a socket object
server_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('2603:7000:4040:3c00:9156:dede:b92f:9678', 12345)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

print('Server is listening on {}:{}'.format(*server_address))

# Establish a connection to the MySQL database
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='',
                       db='triangle_accounting',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)

while True:
    print('Waiting for a client connection...')
    client_socket, client_address = server_socket.accept()

    print('Connected to client:', client_address)

    # Receive data from the client
    data = client_socket.recv(1024).decode('utf-8')
    print('Received data:', data)

    # Execute an SQL query
    cursor = conn.cursor()
    query = "SELECT * FROM customer"
    cursor.execute(query)

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Send the result back to the client
    response = '\n'.join([str(row) for row in rows])
    response = 'hello caiyuan'
    client_socket.sendall(response.encode('utf-8'))

    # Close the cursor and client socket
    cursor.close()
    client_socket.close()
