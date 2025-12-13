# 📝 Notatki Techniczne

## Architektura Aplikacji

### Podział na moduły:

```
┌─────────────────────────────────────────────────────────┐
│                    APLIKACJA                            │
│                  (aplikacja.py)                         │
│  - Interfejs użytkownika Streamlit                     │
│  - Logika główna aplikacji                             │
│  - Integracja z modelem ML                             │
└─────────────────────────────────────────────────────────┘
                         │
                         │ importuje
                         ▼
┌─────────────────────────────────────────────────────────┐
│                  POMOCNICZE                             │
│                (pomocnicze.py)                          │
│  - Funkcje obliczeniowe (BMI, różnice)                 │
│  - Konwersje danych (PL/EN)                            │
│  - Generowanie podpowiedzi                             │
│  - Formatowanie wyświetlania                           │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│              TRENOWANIE MODELU                          │
│           (trenowanie_modelu.py)                        │
│  - Wczytanie danych insurance                          │
│  - Porównanie modeli regresji                          │
│  - Strojenie hiperparametrów                           │
│  - Zapis modelu do pliku                               │
└─────────────────────────────────────────────────────────┘
                         │
                         │ generuje
                         ▼
┌─────────────────────────────────────────────────────────┐
│              WYTRENOWANY MODEL                          │
│     (najlepszy_model_ubezpieczenia.pkl)                │
│  - Gotowy do użycia model ML                           │
│  - Ładowany przez aplikację                            │
└─────────────────────────────────────────────────────────┘
```

## Przepływ danych w aplikacji

1. **Wprowadzenie danych przez użytkownika**
   - Formularz Streamlit → Słownik Python

2. **Przetwarzanie danych**
   - Obliczenie BMI (pomocnicze.py)
   - Konwersja PL → EN (pomocnicze.py)
   - Utworzenie DataFrame (pomocnicze.py)

3. **Predykcja**
   - DataFrame → Model PyCaret → Przewidywana cena

4. **Wyświetlanie wyników**
   - Główna predykcja
   - Podpowiedzi (generuj_podpowiedzi)
   - Porównanie scenariuszy (suwaki)

## Struktura danych

### Dane wejściowe (formularz):
```python
{
    'wiek': int,           # 18-100
    'plec': str,           # 'Mężczyzna' / 'Kobieta'
    'wzrost': int,         # cm
    'waga': int,           # kg
    'bmi': float,          # obliczane automatycznie
    'dzieci': int,         # 0-5
    'palacz': str,         # 'Tak' / 'Nie'
    'region': str          # 'northeast', 'northwest', 'southeast', 'southwest'
}
```

### Dane dla modelu (po konwersji):
```python
DataFrame({
    'age': int,
    'sex': str,            # 'male' / 'female'
    'bmi': float,
    'children': int,
    'smoker': str,         # 'yes' / 'no'
    'region': str
})
```

### Wynik predykcji:
```python
float  # Przewidywana roczna opłata w USD
```

## Najważniejsze funkcje

### pomocnicze.py

1. **oblicz_bmi(waga_kg, wzrost_cm)**
   - Oblicza BMI = waga / (wzrost_m)²
   - Zwraca: float

2. **generuj_podpowiedzi(...)**
   - Analizuje dane użytkownika
   - Zwraca: lista słowników z podpowiedziami
   - Struktura: `{ikona, tytul, opis, potencjalne_oszczednosci}`

3. **utworz_ramke_danych_dla_predykcji(...)**
   - Tworzy DataFrame w formacie modelu
   - Zwraca: pandas.DataFrame

4. **konwertuj_plec_na_angielski(plec_po_polsku)**
   - Mapuje: Mężczyzna → male, Kobieta → female

5. **konwertuj_palacz_na_angielski(palacz_po_polsku)**
   - Mapuje: Tak → yes, Nie → no

### trenowanie_modelu.py

1. **wczytaj_i_przygotuj_dane()**
   - Ładuje dataset 'insurance' z PyCaret
   - Wyświetla statystyki

2. **porownaj_modele()**
   - Porównuje wszystkie modele regresji
   - Sortuje po MAE
   - Zwraca 5 najlepszych

3. **strojenie_modelu(model)**
   - Optymalizuje hiperparametry
   - Używa grid search

4. **zapisz_model(model, nazwa)**
   - Serializuje model do .pkl

### aplikacja.py

1. **wczytaj_model()**
   - Ładuje zapisany model .pkl
   - Sprawdza czy plik istnieje

2. **przewidz_koszt(model, dane_df)**
   - Wykonuje predykcję
   - Zwraca: float (koszt)

3. **sekcja_formularz()**
   - Renderuje formularz Streamlit
   - Zwraca: słownik z danymi

4. **sekcja_podpowiedzi(...)**
   - Wyświetla expandery z poradami

5. **sekcja_porownanie(...)**
   - Suwaki do zmiany parametrów
   - Tabela porównawcza
   - Wykres Plotly

## Metryki modelu

Model jest oceniany według:
- **MAE** (Mean Absolute Error) - główna metryka
- **RMSE** (Root Mean Square Error)
- **R² Score** (R-squared)

Modele porównywane przez PyCaret:
- Linear Regression
- Ridge Regression
- Lasso Regression
- Random Forest
- Gradient Boosting
- XGBoost
- LightGBM
- CatBoost
- i inne...

## Optymalizacje

### Wydajność:
- Model ładowany raz przy starcie aplikacji
- Dane w session_state (brak ponownych obliczeń)
- Predykcje w czasie rzeczywistym

### UX:
- Automatyczne obliczanie BMI
- Walidacja danych wejściowych
- Kolorowe metryki (delta w czerwono/zielono)
- Interaktywne wykresy Plotly

## Możliwe rozszerzenia

### 1. Obsługa audio (obecnie nieimplementowana)
- Użycie `audio-recorder-streamlit`
- Speech-to-text (SpeechRecognition)
- Wypełnianie formularza głosem

### 2. Więcej wizualizacji
- Wykresy rozkładu cen
- Heatmapa korelacji czynników
- Wykresy importance features

### 3. Eksport wyników
- PDF z predykcją
- CSV z porównaniem scenariuszy
- Email z wynikami

### 4. Baza danych
- Zapisywanie historii użytkownika
- Porównywanie z poprzednimi predykcjami
- Analytics

### 5. Multi-language
- Tłumaczenia interfejsu
- i18n support

## Zależności i wersje

Kluczowe biblioteki:
- `streamlit==1.29.0` - framework UI
- `pycaret==3.1.0` - AutoML
- `pandas==2.0.3` - manipulacja danych
- `plotly==5.18.0` - wykresy interaktywne
- `scikit-learn==1.3.2` - ML backend

## Troubleshooting

### Błąd: "Model not found"
- Uruchom `python trenowanie_modelu.py`

### Błąd podczas instalacji PyCaret
- Wymaga Python 3.8-3.11
- `pip install --upgrade pip setuptools wheel`

### Streamlit nie startuje
- Sprawdź port 8501
- Użyj `streamlit run aplikacja.py --server.port 8502`

### Długie trenowanie
- To normalne! Porównywanie modeli zajmuje 5-10 min
- Można użyć mniejszej liczby modeli (edytuj compare_models)

## Kontakt i rozwój

- Repozytorium: github.com/Lukasz6855/prognoza-cen-ubezpieczen
- Issues: zgłaszaj błędy i sugestie
- Pull Requests: mile widziane!
