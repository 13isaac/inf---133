from zeep import Client

client=Client(
    "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"
)
result=client.service.NumberToWords(5)
numberTO= client.service.NumberToDollars(0.5)
print(result)
print(numberTO)