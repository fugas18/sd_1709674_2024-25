import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8001')
x= int(input("um numero inteiro: "))
print(type(x))
print(s.ss(x))
print('FIM')


# Print list of available methods
print(s.system.listMethods())