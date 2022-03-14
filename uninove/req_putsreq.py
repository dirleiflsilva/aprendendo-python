import requests
requisicao = requests.post("https://putsreq.com/a6ZnhxrdUGZJnuXcMzVg")
print(requisicao.text)
nome = input("informe seu nome: ")
requisicao = requests.post(
    "https://putsreq.com/a6ZnhxrdUGZJnuXcMzVg?name="+nome)
print(requisicao.text)