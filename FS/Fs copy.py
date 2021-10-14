import json, requests
import socket
from flask import Flask, request

app = Flask(__name__)

@app.route('/fibonacci', methods = ['GET'])

def fibonacci():
    number = request.args['number']
    result = calculate_fibonacci_number(number)
    return str(result)

def calculate_fibonacci_number(number):
    number = int(number)
    if number <= 2:
        return 1
    return calculate_fibonacci_number(number - 1) + calculate_fibonacci_number(number - 2)
#   if n <= 1:  
#       return n  
#   else:  
#       return(FibRecursion(n-1) + FibRecursion(n-2))  
 #nterms = int(input("Enter the terms? "))  # take input from the user
  
#if nterms <= 0:  # check if the number is valid 
#   print("Please enter a positive integer")  
#else:  
#   print("Fibonacci sequence:")  
#   for i in range(nterms):  
#       print(FibRecursion(i))

#def FibOutput():
#    number = int(request.args('number'))
#    output = Fibonacci(number)
#    return - str(output)

@app.route('/register', methods=['PUT'])
def registration():
    content = request.get_json()
    hostname = content.get('hostname')
    ip = content.get('ip')
    as_ip = content.get('as_ip')
    as_port = int(content.get('as_port'))
    register_json = {'TYPE': 'A', 'NAME': hostname, 'VALUE': ip, 'TTL': 10}

    client_socket = socket(AF_INET, SOCK_DGRAM)
    
    client_socket.sendto(json.dumps(register_json).encode(), (as_ip, as_port))
    response_message, server_address = client_socket.recvfrom(2048)
    return 'successfully registered', status.HTTP_201_CREATED
    
app.run(host='0.0.0.0', port = 9090,debug=True)


#Hostname=request.args('hostname')
#   As_IP=request.args('as_IP')
#  As_port=request.args('as_port')
# IP=request.args('ip')

#    dictionary = {"type":"A", "Hostname":Hostname,"value":IP, "TTL":10}
#    serverSocket = socket(AF_INET, SOCK_DGRAM)
#    serverSocket.sendto(dictionary).encode(), (As_IP, As_port))
#    response_message, client_address = client_socket.recvfrom(2048)
#    return 'successfully registered', status.HTTP_201_CREATED
