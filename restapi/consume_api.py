import requests

""" data = {
    "nombre": "empresaA",
    "contactoEmail": "ted@gmail.com",
    "ingresos": 300,
    "egresos": 100,
} """

data = {
    "nombre": "empresaB",
    "contactoEmail": "rod@gmail.com",
    "ingresos": 400,
    "egresos": 150,
}

""" response = requests.head("http://localhost:5000/empresa/0") """
""" response = requests.get("http://localhost:5000/empresa/1") """
""" response = requests.post("http://localhost:5000/empresa/1") """
""" response = requests.put("http://localhost:5000/empresa/0", data=data) """
""" response = requests.patch("http://localhost:5000/empresa/2", data=data) """
response = requests.delete("http://localhost:5000/empresa/2")
print(response)
if response.status_code == 200:
    dataJson = response.json()
    print(dataJson)
