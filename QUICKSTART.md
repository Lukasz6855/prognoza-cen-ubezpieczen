# 🚀 Szybki Start

## Krok po kroku - uruchomienie aplikacji

### 1️⃣ Instalacja zależności

```bash
pip install -r requirements.txt
```

Czekaj aż wszystkie biblioteki zostaną zainstalowane (może zająć kilka minut).

### 2️⃣ Trenowanie modelu

**WAŻNE:** Ten krok jest wymagany tylko raz, przed pierwszym użyciem aplikacji!

```bash
python trenowanie_modelu.py
```

Co się dzieje podczas trenowania:
- ⏳ Ładowanie danych (1338 rekordów)
- 🔄 Porównywanie różnych modeli ML (~5-10 minut)
- ⚙️ Strojenie najlepszego modelu
- 💾 Zapisywanie modelu do pliku `.pkl`

### 3️⃣ Uruchomienie aplikacji

```bash
streamlit run aplikacja.py
```

Aplikacja automatycznie otworzy się w przeglądarce!

---

## 🎯 Jak używać aplikacji

### Krok 1: Wypełnij formularz
- Wprowadź swój wiek (18-100 lat)
- Wybierz płeć
- Podaj wzrost i wagę (BMI oblicza się automatycznie)
- Wybierz liczbę dzieci
- Zaznacz czy palisz
- Wybierz region zamieszkania

### Krok 2: Kliknij "Przewiduj koszt"
Zobaczysz:
- 💰 Przewidywany roczny koszt ubezpieczenia w USD
- 💡 Personalizowane podpowiedzi jak obniżyć koszt
- 📊 Sekcję porównania scenariuszy

### Krok 3: Eksperymentuj z suwakami
W sekcji "Porównanie scenariuszy":
- Zmień wagę, liczbę dzieci, status palacza, region
- Zobacz jak to wpływa na cenę
- Sprawdź różnicę w tabeli i wykresie

---

## 📝 Przykładowe dane testowe

### Scenariusz 1: Młody niepalący
- Wiek: 25
- Płeć: Mężczyzna
- Wzrost: 180 cm
- Waga: 75 kg
- Dzieci: 0
- Palacz: Nie
- Region: northeast

### Scenariusz 2: Palący z nadwagą
- Wiek: 45
- Płeć: Mężczyzna
- Wzrost: 175 cm
- Waga: 95 kg
- Dzieci: 2
- Palacz: Tak
- Region: southeast

Spróbuj obu scenariuszy i zobacz różnicę w cenie!

---

## ❓ Rozwiązywanie problemów

### Problem: "Nie znaleziono wytrenowanego modelu"
**Rozwiązanie:** Uruchom najpierw `python trenowanie_modelu.py`

### Problem: Błąd podczas instalacji PyCaret
**Rozwiązanie:** 
```bash
pip install --upgrade pip
pip install pycaret==3.1.0
```

### Problem: Streamlit nie otwiera się w przeglądarce
**Rozwiązanie:** Otwórz ręcznie: http://localhost:8501

### Problem: Błędy podczas trenowania modelu
**Rozwiązanie:** Upewnij się, że masz Python 3.8 lub nowszy:
```bash
python --version
```

---

## 🎓 Dodatkowe informacje

- Model trenuje się raz i zapisuje do pliku - nie musisz tego powtarzać
- Możesz zatrzymać aplikację: `Ctrl+C` w terminalu
- Aplikacja działa lokalnie - dane nie są wysyłane nigdzie
- Ceny są w USD (dataset amerykański)

---

## 🆘 Potrzebujesz pomocy?

Otwórz issue na GitHubie: https://github.com/Lukasz6855/prognoza-cen-ubezpieczen/issues
