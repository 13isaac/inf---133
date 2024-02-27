from zeep import Client

client=Client('http://localhost:8000')
result=client.service.Saludar(nombre="Isaac")
sumaDos=client.service.SumaDosNumeros(a=3,b=2)
palindromo=client.service.CadenaPalindromo(palabra="Ana")
print(result)
print(sumaDos)
print(palindromo)