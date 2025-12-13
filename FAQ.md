# ❓ FAQ - Najczęściej Zadawane Pytania

## Ogólne

### 1. Czym jest ta aplikacja?
Aplikacja wykorzystuje uczenie maszynowe (Machine Learning) do przewidywania rocznych kosztów ubezpieczenia na życie na podstawie Twoich danych demograficznych i zdrowotnych.

### 2. Czy aplikacja jest darmowa?
Tak! Aplikacja jest całkowicie darmowa i open-source. Kod źródłowy jest dostępny na GitHubie.

### 3. Czy moje dane są bezpieczne?
Tak! Aplikacja działa lokalnie na Twoim komputerze. Dane nie są wysyłane nigdzie do internetu ani przechowywane.

### 4. W jakiej walucie są ceny?
Ceny są w USD (dolarach amerykańskich), ponieważ model został wytrenowany na danych z amerykańskiego rynku ubezpieczeń.

## Instalacja i Uruchamianie

### 5. Jakie są wymagania systemowe?
- Python 3.8 lub nowszy (zalecane 3.9-3.11)
- 4GB RAM (minimum)
- 2GB wolnego miejsca na dysku
- System: Windows, macOS lub Linux

### 6. Jak zainstalować aplikację?
```bash
# 1. Sklonuj repozytorium
git clone https://github.com/Lukasz6855/prognoza-cen-ubezpieczen.git

# 2. Wejdź do folderu
cd prognoza-cen-ubezpieczen

# 3. Zainstaluj zależności
pip install -r requirements.txt

# 4. Wytrenuj model (tylko pierwszy raz!)
python trenowanie_modelu.py

# 5. Uruchom aplikację
streamlit run aplikacja.py
```

### 7. Ile czasu zajmuje trenowanie modelu?
Trenowanie modelu zajmuje zwykle 5-10 minut, w zależności od mocy Twojego komputera. Musisz to zrobić tylko raz!

### 8. Czy muszę trenować model za każdym razem?
NIE! Trenowanie modelu wykonujesz tylko raz. Model jest zapisywany do pliku i później tylko wczytywany.

### 9. Aplikacja nie otwiera się w przeglądarce. Co robić?
Otwórz ręcznie: http://localhost:8501 w przeglądarce.

### 10. Port 8501 jest zajęty. Co robić?
Użyj innego portu:
```bash
streamlit run aplikacja.py --server.port 8502
```

## Używanie Aplikacji

### 11. Jakie dane muszę wprowadzić?
- Wiek (18-100 lat)
- Płeć (Mężczyzna/Kobieta)
- Wzrost (w centymetrach)
- Waga (w kilogramach)
- Liczba dzieci (0-5)
- Czy palisz papierosy (Tak/Nie)
- Region zamieszkania

### 12. Co to jest BMI i jak jest obliczane?
BMI (Body Mass Index) to wskaźnik masy ciała obliczany jako: **waga / (wzrost w metrach)²**
Aplikacja oblicza go automatycznie na podstawie Twojej wagi i wzrostu.

### 13. Jak działają suwaki w sekcji porównania?
Możesz zmieniać różne parametry (wagę, liczbę dzieci, status palacza, region) i natychmiast widzieć jak te zmiany wpływają na koszt ubezpieczenia.

### 14. Czy mogę zapisać wyniki?
Obecnie aplikacja nie ma wbudowanej funkcji zapisu. Możesz zrobić screenshot lub skopiować wyniki ręcznie.

### 15. Dlaczego palenie tak bardzo wpływa na cenę?
Palenie jest największym czynnikiem ryzyka dla ubezpieczycieli. Palarze mogą płacić nawet 50-70% więcej!

## Techniczne

### 16. Jaki model ML jest używany?
Aplikacja automatycznie porównuje wiele modeli regresji (Random Forest, XGBoost, LightGBM, etc.) i wybiera najlepszy według metryki MAE.

### 17. Skąd pochodzą dane treningowe?
Dane pochodzą z datasetu "insurance" wbudowanego w bibliotekę PyCaret. Zawiera 1338 rekordów rzeczywistych danych ubezpieczeniowych.

### 18. Co to jest PyCaret?
PyCaret to biblioteka Python do automatycznego uczenia maszynowego (AutoML). Automatycznie porównuje i stroi modele ML.

### 19. Czy mogę zobaczyć kod?
Tak! Cały kod jest dostępny na GitHubie. Wszystkie nazwy zmiennych i funkcji są po polsku, z komentarzami.

### 20. Czy mogę użyć własnych danych do trenowania?
Tak, ale wymagałoby to modyfikacji pliku `trenowanie_modelu.py`. Twoje dane muszą mieć takie same kolumny jak dataset "insurance".

## Błędy i Problemy

### 21. Błąd: "ModuleNotFoundError: No module named 'pycaret'"
Zainstaluj zależności:
```bash
pip install -r requirements.txt
```

### 22. Błąd: "Nie znaleziono wytrenowanego modelu"
Wytrenuj model przed uruchomieniem aplikacji:
```bash
python trenowanie_modelu.py
```

### 23. Błąd podczas instalacji PyCaret
PyCaret wymaga Python 3.8-3.11. Sprawdź wersję:
```bash
python --version
```

### 24. Aplikacja jest wolna
- Pierwsza predykcja może trwać kilka sekund (ładowanie modelu)
- Kolejne predykcje są szybkie
- Upewnij się, że masz wystarczającą ilość RAM

### 25. Trenowanie modelu wywaliło się
- Sprawdź czy masz stabilne połączenie z internetem (do pobrania danych)
- Upewnij się, że masz min. 4GB RAM
- Spróbuj ponownie - czasami to pomaga

## Funkcjonalności

### 26. Czy aplikacja obsługuje wprowadzanie danych głosem?
W obecnej wersji nie, ale biblioteki do tego są już zainstalowane w requirements.txt. To planowana funkcja na przyszłość.

### 27. Czy mogę eksportować wyniki do PDF?
Nie w obecnej wersji. To możliwe rozszerzenie na przyszłość.

### 28. Czy aplikacja działa offline?
Tak, po jednorazowym zainstalowaniu i wytrenowaniu modelu aplikacja działa całkowicie offline.

### 29. Czy mogę zmienić język aplikacji na angielski?
Obecnie aplikacja jest tylko po polsku. Funkcja multi-language to planowane rozszerzenie.

### 30. Czy aplikacja jest dokładna?
Aplikacja daje **szacunkowe** prognozy na podstawie danych treningowych. Rzeczywiste ceny ubezpieczeń zależą od wielu innych czynników i mogą się różnić.

## Rozwój i Wsparcie

### 31. Jak mogę pomóc w rozwoju?
- Zgłaszaj błędy przez Issues na GitHubie
- Proponuj nowe funkcje
- Wysyłaj Pull Requesty z poprawkami/ulepszeniami
- Dziel się projektem z innymi

### 32. Znalazłem błąd. Co robić?
Otwórz Issue na GitHubie: https://github.com/Lukasz6855/prognoza-cen-ubezpieczen/issues

### 33. Mam pomysł na nową funkcję
Świetnie! Dodaj go jako Feature Request w Issues na GitHubie.

### 34. Czy mogę użyć tego kodu w moim projekcie?
Tak! Projekt jest na licencji MIT - możesz go używać i modyfikować.

### 35. Kto stworzył tę aplikację?
Aplikacja została stworzona przez Łukasza ([@Lukasz6855](https://github.com/Lukasz6855)) jako projekt edukacyjny/demonstracyjny.

## Uczenie i Nauka

### 36. Czy mogę używać tego projektu do nauki?
Absolutnie! Projekt jest idealny do nauki:
- Python
- Streamlit
- Machine Learning (PyCaret)
- Data Science
- Wizualizacji danych

### 37. Gdzie mogę dowiedzieć się więcej o ML?
- Dokumentacja PyCaret: https://pycaret.org/
- Kursy Python na Coursera/Udemy
- Dokumentacja Streamlit: https://docs.streamlit.io/

### 38. Czy kod jest dobrze skomentowany?
Tak! Każda linia kodu ma komentarz wyjaśniający co robi. Idealne dla początkujących.

### 39. Jakie inne projekty mogę zrobić na tej bazie?
- Prognoza cen domów
- Prognoza wynagrodzeń
- Analiza ryzyka kredytowego
- Przewidywanie churn klientów
- I wiele innych!

### 40. Gdzie mogę zadać więcej pytań?
- Otwórz Issue na GitHubie z tagiem [question]
- Sprawdź dokumentację w plikach README.md i NOTATKI_TECHNICZNE.md

---

## 🆘 Nie znalazłeś odpowiedzi?

Jeśli Twoje pytanie nie jest na tej liście:
1. Sprawdź [README.md](README.md)
2. Sprawdź [NOTATKI_TECHNICZNE.md](NOTATKI_TECHNICZNE.md)
3. Otwórz Issue na GitHubie
4. Opisz problem szczegółowo (system, wersja Python, komunikat błędu)

---

**Ostatnia aktualizacja:** 12 grudnia 2025
