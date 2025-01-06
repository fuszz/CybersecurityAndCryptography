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
