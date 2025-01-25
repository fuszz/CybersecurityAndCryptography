## Problem z podmanem (wymiana na Dockera)

https://medium.com/@nocerainfosec/docker-on-parrot-os-security-5-3-a-fresh-and-foolproof-installation-guide-5d8e9cd9e159

## Podniesienie kontenera z docker-compose podanym w pliku

`docker compose -f <nazwa_pliku_z_docker_compose>.yml up`

# XSS ([lab8.pdf]())

**Payloady** (a raczej ich kawałki w JS)

- `alert("Jakiś tekst")` → wyświetla okienko popup z treścią w nawiasach

- `document.cookie` → jeśli nie ustawiono flagi `HttpOnly`, wyświetla cookie

- `<script>`Kod w JS`</script>` → nesting skryptu w php/html

## Zadanie 9.1

![Zadanie 2](/home/filip/Dokumenty/Studia/Informatyka/CybersecurityAndCryptography/screenshots/XSS/zadanie2.png)

- wchodzimy na serwer `localhost:9091/admin/index.php`

- dane do logowania są w docker compose: `admin:password`

- przechodzimy do tworzenia nowej ankiety

- w nazwie wpisujemy payload, np `a'<script>alert(document.cookie)</script>`

- przechodzimy do podglądu ankiety. Pojawia się okienko, ale puste. To dlatego, że w cookie jest ustawiona flaga `HttpOnly: true`

## Zadanie 9.2

![Zadanie 3](/home/filip/Dokumenty/Studia/Informatyka/CybersecurityAndCryptography/screenshots/XSS/zadanie3.png)

- wchodzimy na serwer `localhost:9092/admin/index.php`

- `admin:password`

- sytuacja dokładnie taka sama jak powyżej

## Zadanie 9.3

![](/home/filip/.config/marktext/images/2025-01-24-17-42-56-image.png)

- wchodzimy na serwer `localhost:9094/admin/index.php`

- `admin:password`

- WRÓCIĆ DO TEGO CUDEŃKA

## Zadanie 9.4

![](/home/filip/.config/marktext/images/2025-01-24-17-59-43-image.png)

- `docker run -dp 9094:80 mazurkatarzyna/cwe-79-ex4:latest`

- Uruchamiamy aplikację na porcie 9094 localhosta

- Ustawiamy dane (np. a: a: a: a) i uruchamiamy instalację. Kontener o dziwo nie padł. 

- Przygotowujemy podatny plik z kodem .js. 
