import requests
url = "http://localhost:8000"

response = requests.get(f"{url}/posts")
print("----------muestra todas las publicaciones----------")
print(response.text)

#----------------------------------
response_2 = requests.get(f"{url}/posts/2")
print("----------muestra la publicacion 2----------")
print(response_2.text)

#----------------------------------

nuevo_post={
        "title": "Mi experiencia como DEV",
        "content": "ta muy duro aprender todo en un semestre",
    }
response_new = requests.post(f"{url}/posts", json=nuevo_post)#(url, json=mi_pizza, headers=headers)
print("----------nuevo post----------")
print(response_new.text)

#---------------------------------
response = requests.get(f"{url}/posts")
print("----------muestra todas las publicaciones----------")
print(response.text)
