from osa import Client

cl = Client("http://localhost:8088/mockApiPortSoap11?WSDL")
reg_call = cl.service.registerCall(" ")
res = cl.service.results(" ")
print(reg_call,res)