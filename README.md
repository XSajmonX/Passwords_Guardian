## Aplikacja PassGuard:
Aplikacja komputerowa ma zadanie przechowywać hasła użytkownika na lokalnym komputerze.
Dostęp do haseł jest zabezpieczony uwierzytelnieniem i autoryzacją konta użytkownika w aplikacji.
Dane konta oraz informacje o haśle są przechowywane w postaci zaszyfrowanej.
## Funkcje programu:
- Utworzenie i modyfikacja danych konta użytkownika
- Weryfikacja dwuetapowa 
  - Login oraz hasło konta aplikacji
  - Kod weryfikacyjny wysłany na pocztę
- Wszystkie dane wrażliwe są w postaci zaszyfrowanej
- Wyświetlenie danych w tabeli
- Dodanie, modyfikacja i usunięcie rekordu z hasłem
## Biblioteki Python:
- PyQt5
- pyqt5-tools
- pyinstaller
- python-dotenv
## Instalacja i Uruchomienie lokalne:
1. Sklonuj repozytorium
```
git clone https://github.com/XSajmonX/Passwords_Guardian.git
cd Passwords_Guardian
```
2. Stwórz środowisko wirtualne
```
python -m venv myenv
myenv\Scripts\activate  
```
3. Zainstaluj zależności
```
 pip install -r requirements.txt
```
4. Utwórz niezbędne pliki i katalogi
- Utwórz katalog Pass, w którym będą przechowywane hasła
- Utwórz plik .env i zdefiniuj zmienne:
kod aplikacji w Gmail oraz email, z którego będą wysyłane wiadomości
```
app_key = "aaabbbcccddd"
sender = "example@gmail.com" 
```
5. (Opcjonalne) Utwórz plik wykonywalny main.exe
```
pyinstaller --noconsole --onefile --icon=UI_design/desktop_icon.ico --hidden-import=PyQt5 main.py
```
6. Uruchom plik main.exe

## Struktura Programu

Okna aplikacji:
- `main.py` - Okno główne, pierwszy etap weryfikacji
- `new_user.py` - Tworzenie nowego użytkownika
- `verify.py` - Drugi etap weryfikacji
- `passwords_tab.py` - Panel zarządzania hasłami
- `modify.py` - Modyfikacja rekordu hasła
- `profil.py` - Modyfikacja danych konta lokalnego aplikacji

Pliki operacyjne:
- `Coder.py` - Funkcje i operacje potrzebne do szyfrowania danych
- `Decoder.py` - Funkcje i operacje potrzebne do deszyfrowania danych
- `File_operations.py` - Operacje na plikach odczyt/zapis danych o użytkowniku/jego hasłach
- `Generator.py` - Generuje unikatowe id użytkownika, kod weryfikacyjny
- `Mail.py` - Automatyzacja i wysyłanie emaili z kodem weryfikacyjnym do użytkownika

Klasy obiektów:
- `User.py` - Obiekty reprezentujące konto (login, hasło, email)
- `Record.py` - Obiekty reprezentujące hasło/usługę (usługa,login,hasło)
- `Messagebox.py` - Utworzenie komunikatów (np. potwierdzenie usunięcia hasła)

Projektowanie UI:
- `Table_style_css.py` - Określenie stylu tabeli
- `UI_design/` - Folder zawierający UI okien i ikony aplikacji

Dane wrażliwe:
- `Users.csv` - Zaszyfowane dane o użytkownikach
- `Pass/` - Folder gdzie znajdują się wszystkie hasła

Inne:
- `.gitignore` - Określa, które pliki mają być pominięte przez Gita
- `.env` - Dane serwera poczty elektronicznej
- `requirements.txt` - Potrzebne moduły
- `Documentation.pdf` - Szczegółowa dokumentacja projektu 

## Autor:
- Szymon Bęczkowski