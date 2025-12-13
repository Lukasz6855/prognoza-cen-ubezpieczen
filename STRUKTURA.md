# 📂 Struktura Projektu

```
prognoza-cen-ubezpieczen/
│
├── 📄 README.md                           # Główna dokumentacja projektu
├── 🚀 QUICKSTART.md                       # Szybki start krok po kroku
├── 📝 NOTATKI_TECHNICZNE.md               # Szczegóły techniczne i architektura
├── ❓ FAQ.md                               # Najczęściej zadawane pytania
├── 📜 LICENSE                              # Licencja MIT
│
├── 🐍 PLIKI PYTHONA:
│   ├── aplikacja.py                       # Główna aplikacja Streamlit (455 linii)
│   ├── trenowanie_modelu.py               # Skrypt trenowania modelu (149 linii)
│   ├── pomocnicze.py                      # Funkcje pomocnicze (252 linie)
│   └── demo_funkcji.py                    # Demonstracja funkcji (223 linie)
│
├── ⚙️ KONFIGURACJA:
│   ├── requirements.txt                   # Zależności Python
│   ├── .gitignore                         # Ignorowane pliki Git
│   └── .streamlit/
│       └── config.toml                    # Konfiguracja Streamlit
│
├── 🚀 SKRYPTY:
│   └── start.sh                           # Skrypt startowy (sprawdza model i uruchamia)
│
└── 🤖 GENEROWANE (po trenowaniu):
    └── najlepszy_model_ubezpieczenia.pkl  # Wytrenowany model ML

```

## 📊 Statystyki Projektu

- **Łączna liczba linii kodu:** ~1,863
- **Pliki Python:** 4 pliki, ~1,079 linii
- **Dokumentacja:** 4 pliki Markdown, ~738 linii
- **Konfiguracja:** 3 pliki
- **Skrypty pomocnicze:** 1 plik bash

## 🔄 Przepływ Pracy

```
┌─────────────────────────────────────────────────────────────────┐
│  KROK 1: INSTALACJA                                             │
│  pip install -r requirements.txt                                │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│  KROK 2: TRENOWANIE MODELU (tylko raz!)                         │
│  python trenowanie_modelu.py                                    │
│                                                                  │
│  Proces:                                                        │
│  1. Wczytanie danych insurance (1338 rekordów)                 │
│  2. Porównanie modeli ML (~5-10 min)                           │
│  3. Strojenie hiperparametrów                                  │
│  4. Zapis modelu → najlepszy_model_ubezpieczenia.pkl           │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│  KROK 3: URUCHOMIENIE APLIKACJI                                 │
│  streamlit run aplikacja.py                                     │
│  (lub ./start.sh)                                               │
│                                                                  │
│  Aplikacja otwiera się w przeglądarce (http://localhost:8501)  │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│  KROK 4: UŻYWANIE                                                │
│  1. Wypełnij formularz danymi                                   │
│  2. Zobacz predykcję kosztów                                    │
│  3. Czytaj podpowiedzi                                          │
│  4. Porównaj scenariusze (suwaki)                               │
└─────────────────────────────────────────────────────────────────┘
```

## 🎯 Kluczowe Pliki - Co Robią?

### aplikacja.py
**Główna aplikacja Streamlit**
- 🖼️ Interfejs użytkownika
- 📝 Formularz wprowadzania danych
- 🔮 Wykonywanie predykcji
- 💡 Wyświetlanie podpowiedzi
- 📊 Porównywanie scenariuszy
- 📈 Wykresy i wizualizacje

### trenowanie_modelu.py
**Trenowanie i zapis modelu**
- 📥 Wczytywanie danych insurance
- 🔍 Porównywanie ~15 modeli regresji
- ⚙️ Strojenie hiperparametrów
- 💾 Zapis najlepszego modelu

### pomocnicze.py
**Funkcje wspierające**
- 🧮 Obliczenia (BMI, różnice procentowe)
- 🔄 Konwersje PL↔EN
- 💡 Generowanie podpowiedzi
- 📊 Funkcje formatowania
- 🎨 Wyświetlanie metryk

### demo_funkcji.py
**Testy i demonstracja**
- 🧪 Testowanie funkcji pomocniczych
- 📚 Przykłady użycia
- ✅ Weryfikacja poprawności

## 📚 Dokumentacja - Dla Kogo?

| Plik | Dla Kogo | Zawiera |
|------|----------|---------|
| **README.md** | Wszyscy | Ogólny opis, instalacja, podstawowe info |
| **QUICKSTART.md** | Początkujący | Szybki start, przykłady, rozwiązywanie problemów |
| **NOTATKI_TECHNICZNE.md** | Developerzy | Architektura, API, szczegóły techniczne |
| **FAQ.md** | Wszyscy | 40 najczęstszych pytań i odpowiedzi |
| **STRUKTURA.md** | Wszyscy | Ten plik - mapa projektu |

## 🛠️ Technologie i Biblioteki

```python
# Framework UI
streamlit==1.29.0          # Interfejs użytkownika

# Machine Learning
pycaret==3.1.0             # AutoML
scikit-learn==1.3.2        # ML backend

# Przetwarzanie danych
pandas==2.0.3              # DataFrames
numpy==1.24.3              # Obliczenia numeryczne

# Wizualizacje
plotly==5.18.0             # Interaktywne wykresy

# Audio (na przyszłość)
audio-recorder-streamlit==0.0.8
speechrecognition==3.10.0
pydub==0.25.1
```

## 🎓 Nauka z Tego Projektu

Ten projekt jest świetnym materiałem do nauki:

### Python
- ✅ Struktura projektu (moduły)
- ✅ Funkcje i dokumentacja
- ✅ Dobre praktyki kodowania
- ✅ Komentarze w języku polskim

### Data Science
- ✅ Preprocessing danych
- ✅ Feature engineering (BMI)
- ✅ Model selection
- ✅ Hyperparameter tuning

### Machine Learning
- ✅ Regresja
- ✅ PyCaret (AutoML)
- ✅ Model persistence (.pkl)
- ✅ Metryki (MAE, RMSE, R²)

### Web Development
- ✅ Streamlit framework
- ✅ Interaktywne formularze
- ✅ Session state
- ✅ Plotly wykresy

### DevOps
- ✅ Git version control
- ✅ Requirements management
- ✅ Documentation
- ✅ Shell scripting

## 🚀 Możliwe Rozszerzenia

### Funkcjonalności (priorytet wysoki)
- [ ] Audio input - nagrywanie odpowiedzi głosem
- [ ] Export wyników do PDF
- [ ] Historia predykcji użytkownika
- [ ] Porównanie z innymi ubezpieczycielami

### Wizualizacje (priorytet średni)
- [ ] Wykresy rozkładu cen
- [ ] Heatmapa korelacji
- [ ] Feature importance
- [ ] Animowane przejścia

### Techniczne (priorytet niski)
- [ ] Baza danych (SQLite)
- [ ] API REST
- [ ] Testy jednostkowe
- [ ] CI/CD pipeline
- [ ] Docker container
- [ ] Deployment na cloud

### UI/UX (priorytet średni)
- [ ] Dark mode
- [ ] Multi-language (EN, DE, etc.)
- [ ] Mobile responsive
- [ ] Onboarding tutorial

## 📞 Kontakt i Wsparcie

- 🐙 **GitHub:** [@Lukasz6855](https://github.com/Lukasz6855)
- 📧 **Issues:** [github.com/Lukasz6855/prognoza-cen-ubezpieczen/issues](https://github.com/Lukasz6855/prognoza-cen-ubezpieczen/issues)
- 🌟 **Star projekt** jeśli Ci się podoba!
- 🔀 **Fork i PR** mile widziane!

---

**Wersja dokumentacji:** 1.0  
**Ostatnia aktualizacja:** 12 grudnia 2025  
**Licencja:** MIT
