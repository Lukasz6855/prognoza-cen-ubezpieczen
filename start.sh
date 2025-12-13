#!/bin/bash

# Skrypt do szybkiego uruchomienia aplikacji
# Ten skrypt sprawdza czy model istnieje, jeśli nie - trenuje go, a następnie uruchamia aplikację

echo "🏥 Prognoza Cen Ubezpieczeń - Skrypt startowy"
echo "=============================================="
echo ""

# Sprawdzenie czy istnieje wytrenowany model
if [ -f "najlepszy_model_ubezpieczenia.pkl" ]; then
    echo "✅ Model został już wytrenowany"
    echo ""
    echo "🚀 Uruchamiam aplikację Streamlit..."
    streamlit run aplikacja.py
else
    echo "⚠️  Nie znaleziono wytrenowanego modelu"
    echo ""
    echo "📚 Trenuję model (to może zająć kilka minut)..."
    python trenowanie_modelu.py
    
    # Sprawdzenie czy trenowanie się powiodło
    if [ $? -eq 0 ]; then
        echo ""
        echo "✅ Trenowanie zakończone sukcesem!"
        echo ""
        echo "🚀 Uruchamiam aplikację Streamlit..."
        streamlit run aplikacja.py
    else
        echo ""
        echo "❌ Błąd podczas trenowania modelu"
        echo "Sprawdź czy wszystkie zależności są zainstalowane:"
        echo "pip install -r requirements.txt"
        exit 1
    fi
fi
