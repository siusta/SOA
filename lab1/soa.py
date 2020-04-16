from osa import Client

cl = Client("http://localhost:8088/mockApiPortSoap11?WSDL")
reg_call = cl.service.registerCall(" ")
res = cl.service.results(" ")
print("Name: " + reg_call.name)
print("Note: " + reg_call.note)