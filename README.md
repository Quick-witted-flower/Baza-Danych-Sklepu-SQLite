                Baza Danych Sklepu SQLite

Spis Treści:
    *Informacje Ogólne
    *Wykorzystane Technologie
    *Konfiguracja
    *Użytkowanie
    *Kontakt


Informacje Ogólne
    Ten projekt demonstruje, jak używać SQLite do zarządzania danymi sklepu internetowego, w tym informacjami o produktach oraz zamówieniach klientów. Tabele products i orders tworzą relację typu "jeden-do-wielu", w której każdy produkt może być częścią wielu zamówień, a każde zamówienie odnosi się do jednego produktu. Projekt ten powstał w celu zdobycia praktycznego doświadczenia z zarządzaniem bazami danych w Pythonie i ilustruje implementację systemu zamówień.

Wykorzystane Technologie
•	Python - version 3.x
•	SQLite - version 3.x
•	DB Browser for SQLite - (opcjonalnie, do zarządzania bazą danych za pomocą graficznego interfejsu)



Konfiguracja:
1.	Klonowanie repozytorium:
                bash
                git clone <repository-url>
2.	Instalacja Python 3.x oraz modułu sqlite3 (jest on domyślnie dołączony do Python).
3.	(Opcjonalnie) Zainstaluj DB Browser for SQLite, aby zarządzać bazą danych za pomocą interfejsu graficznego: Pobierz DB Browser.


Użytkowanie:
Projekt zawiera kilka funkcji użytkowych do zarządzania bazą danych, wykonywania operacji CRUD oraz obsługi relacji między tabelami. Oto kroki, jak rozpocząć:

1. Tworzenie bazy danych i nawiązywanie połączenia:
    >Uchomienie skryptu utworzy bazę danych (mydatabase.db), jeśli jeszcze nie istnieje, i nawiąże połączenie.

2. Tworzenie tabel:
    >Skrypt automatycznie tworzy dwie tabele: products i orders.
    >Tabela orders zawiera klucz obcy product_id, który łączy zamówienie z określonym produktem, tworząc relację jeden-do-wielu.

3. Wstawianie przykładowych danych:
    >Skrypt dynamicznie dodaje przykładowe produkty oraz zamówienia, demonstrując podstawowe operacje dodawania danych do bazy.

4. Operacje CRUD:
    >Insert: Dodawanie nowych produktów i zamówień.
    >Select: Pobieranie danych z tabel products lub orders na podstawie określonych kryteriów.
    >Update: Modyfikowanie danych w tabelach products lub orders.
    >Delete: Usuwanie konkretnych rekordów lub czyszczenie całych tabel.

5. Funkcje Specyficzne dla Relacji Jeden-do-Wielu:
    >Możesz przeglądać, dodawać i zarządzać danymi w bazie za pomocą DB Browser for SQLite. Otwórz plik mydatabase.db, aby zobaczyć tabelę products i orders oraz sprawdzić powiązania między danymi.

6. Uruchamianie skryptu:
    Aby uruchomić skrypt i wywołać funkcje, użyj polecenia:
                python mydatabase.py

Kontakt:
    Stworzone przez @Quick-witted-flower – w razie pytań lub uwag zapraszam do kontaktu!

