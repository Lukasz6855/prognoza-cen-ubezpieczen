# 🏥 Prognoza Cen Ubezpieczeń na Życie

Aplikacja do przewidywania opłaty za ubezpieczenie na życie z użyciem Machine Learning.

## � Dokumentacja

- 📖 [README.md](README.md) - Główna dokumentacja (czytasz ją teraz)
- 🚀 [QUICKSTART.md](QUICKSTART.md) - Szybki start krok po kroku- 📂 [STRUKTURA.md](STRUKTURA.md) - Struktura projektu i mapa plików- 📝 [NOTATKI_TECHNICZNE.md](NOTATKI_TECHNICZNE.md) - Szczegóły techniczne
- ❓ [FAQ.md](FAQ.md) - Najczęściej zadawane pytania

## �📋 Opis projektu

Aplikacja wykorzystuje uczenie maszynowe (PyCaret) do przewidywania rocznych kosztów ubezpieczenia na życie na podstawie danych demograficznych użytkownika. Aplikacja oferuje:

- 📝 Formularz do wprowadzania danych osobowych
- 🤖 Predykcję kosztów ubezpieczenia przy użyciu modelu ML
- 💡 Personalizowane podpowiedzi jak obniżyć koszty
- 📊 Interaktywne porównanie scenariuszy ze suwakami
- 📈 Wizualizacje i wykresy porównawcze

## 🚀 Funkcje

### Główne funkcjonalności:
1. **Formularz danych klienta:**
   - Wiek
   - Płeć
   - Wzrost i waga (z automatycznym obliczeniem BMI)
   - Liczba dzieci
   - Status palacza
   - Region zamieszkania

2. **Predykcja kosztów:**
   - Wykorzystanie wytrenowanego modelu ML
   - Wyświetlanie przewidywanej rocznej opłaty w USD

3. **Podpowiedzi personalizowane:**
   - Analiza danych użytkownika
   - Konkretne sugestie jak obniżyć koszty
   - Oszacowanie potencjalnych oszczędności

4. **Porównanie scenariuszy:**
   - Interaktywne suwaki do zmiany parametrów
   - Tabela porównawcza
   - Wykres słupkowy
   - Obliczanie różnic procentowych

## 🛠️ Technologie

- **Python 3.8+**
- **Streamlit** - interfejs użytkownika
- **PyCaret** - automatyczne uczenie maszynowe
- **Pandas** - przetwarzanie danych
- **Plotly** - wizualizacje interaktywne
- **Scikit-learn** - ML backend

## 📦 Instalacja

### 1. Sklonuj repozytorium:
```bash
git clone https://github.com/Lukasz6855/prognoza-cen-ubezpieczen.git
cd prognoza-cen-ubezpieczen
```

### 2. Zainstaluj wymagane biblioteki:
```bash
pip install -r requirements.txt
```

## 🎯 Użytkowanie

### Krok 1: Wytrenowanie modelu

Przed pierwszym użyciem aplikacji musisz wytrenować model:

```bash
python trenowanie_modelu.py
```

Ten skrypt:
- Wczytuje dane z datasetu "insurance"
- Porównuje różne modele regresji
- Wybiera najlepszy model
- Stroi hiperparametry
- Zapisuje model jako `najlepszy_model_ubezpieczenia.pkl`

**Uwaga:** Trenowanie może potrwać kilka minut!

### Krok 2: Uruchomienie aplikacji

Po wytrenowaniu modelu uruchom aplikację Streamlit:

```bash
streamlit run aplikacja.py
```

Aplikacja otworzy się w przeglądarce pod adresem `http://localhost:8501`

## 📁 Struktura projektu

```
prognoza-cen-ubezpieczen/
│
├── aplikacja.py              # Główna aplikacja Streamlit
├── trenowanie_modelu.py      # Skrypt do trenowania modelu
├── pomocnicze.py             # Funkcje pomocnicze
├── requirements.txt          # Zależności projektu
├── README.md                 # Dokumentacja (ten plik)
└── najlepszy_model_ubezpieczenia.pkl  # Wytrenowany model (generowany)
```

## 🎨 Funkcje pomocnicze

### `pomocnicze.py` zawiera:
- `generuj_podpowiedzi()` - generuje personalizowane porady
- `oblicz_bmi()` - oblicza wskaźnik masy ciała
- `interpretuj_bmi()` - interpretuje wartość BMI
- `konwertuj_plec_na_angielski()` - konwersja płci PL→EN
- `konwertuj_palacz_na_angielski()` - konwersja statusu palacza PL→EN
- `utworz_ramke_danych_dla_predykcji()` - przygotowanie danych dla modelu
- `sformatuj_kwote()` - formatowanie kwot
- `oblicz_roznice_procentowe()` - obliczanie różnic %
- `wyswietl_metryki_porownawcze()` - wyświetlanie metryk w Streamlit

## 📊 Dane

Aplikacja wykorzystuje wbudowany dataset **"insurance"** z biblioteki PyCaret, który zawiera:
- **1338 rekordów** danych ubezpieczeniowych
- **7 kolumn**: age, sex, bmi, children, smoker, region, charges

## 🔍 Model ML

Aplikacja automatycznie:
1. Porównuje wszystkie dostępne modele regresji w PyCaret
2. Wybiera model z najniższym MAE (Mean Absolute Error)
3. Stroi hiperparametry wybranego modelu
4. Zapisuje najlepszy model do pliku

## 💡 Przykład użycia

1. Wprowadź swoje dane w formularzu (wiek, płeć, wzrost, wagę, etc.)
2. Kliknij "🔮 Przewiduj koszt ubezpieczenia"
3. Zobacz przewidywany koszt
4. Sprawdź podpowiedzi jak obniżyć koszt
5. Użyj suwaków aby zobaczyć jak zmiany wpływają na cenę

## ⚠️ Uwagi

- Model został wytrenowany na danych amerykańskich, więc ceny są w USD
- Aplikacja ma charakter edukacyjny i demonstracyjny
- Rzeczywiste ceny ubezpieczeń zależą od wielu dodatkowych czynników

## 🤝 Autor

Łukasz - [@Lukasz6855](https://github.com/Lukasz6855)

## 📝 Licencja

Ten projekt jest dostępny na licencji MIT.

## 🙏 Podziękowania

- [PyCaret](https://pycaret.org/) - za fantastyczną bibliotekę AutoML
- [Streamlit](https://streamlit.io/) - za prosty framework do tworzenia aplikacji
- [Plotly](https://plotly.com/) - za interaktywne wykresy
