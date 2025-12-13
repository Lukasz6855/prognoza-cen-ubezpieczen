"""
Skrypt do trenowania modelu przewidywania kosztów ubezpieczenia na życie
Ten plik ładuje dane, porównuje modele i zapisuje najlepszy model
"""

# Import bibliotek
import pandas as pd
from pycaret.regression import *

def wczytaj_i_przygotuj_dane():
    """
    Funkcja ładująca dane insurance z pycaret.datasets
    Zwraca przygotowane dane
    """
    print("📊 Wczytuję dane insurance...")
    # Wczytanie danych wbudowanych w PyCaret
    from pycaret.datasets import get_data
    dane = get_data('insurance')
    
    # Wyświetlenie podstawowych informacji o danych
    print(f"✅ Wczytano {len(dane)} rekordów")
    print("\n📋 Pierwsze wiersze danych:")
    print(dane.head())
    print("\n📊 Informacje o danych:")
    print(dane.info())
    print("\n📈 Statystyki opisowe:")
    print(dane.describe())
    
    return dane

def przygotuj_srodowisko_pycaret(dane):
    """
    Funkcja przygotowująca środowisko PyCaret
    Ustawia parametry i inicjalizuje setup
    """
    print("\n🔧 Konfiguruję środowisko PyCaret...")
    # Inicjalizacja środowiska PyCaret (PyCaret 3.x)
    # target='charges' - kolumna którą przewidujemy (koszt ubezpieczenia)
    # session_id=123 - dla reprodukowalności wyników
    # normalize=True - normalizacja danych
    # transformation=True - transformacja danych
    # remove_outliers=True - usunięcie wartości odstających
    setup_model = setup(
        data=dane,
        target='charges',
        session_id=123,
        normalize=True,
        transformation=True,
        remove_outliers=True,
        verbose=False
    )
    
    print("✅ Środowisko PyCaret skonfigurowane!")
    return setup_model

def porownaj_modele():
    """
    Funkcja porównująca różne modele regresji
    Zwraca najlepszy model
    """
    print("\n🤖 Porównuję modele regresji...")
    print("To może zając kilka minut...\n")
    
    # Porównanie wszystkich dostępnych modeli regresji
    # sort='MAE' - sortowanie według Mean Absolute Error (im mniej tym lepiej)
    # n_select=5 - wybór 5 najlepszych modeli
    najlepsze_modele = compare_models(sort='MAE', n_select=5)
    
    print("\n✅ Porównanie modeli zakończone!")
    print(f"🏆 Najlepszy model: {type(najlepsze_modele[0]).__name__}")
    
    # Zwraca najlepszy model (pierwszy z listy)
    return najlepsze_modele[0]

def strojenie_modelu(model):
    """
    Funkcja stroiąca hiperparametry najlepszego modelu
    Zwraca dostrojony model
    """
    print("\n⚙️ Stroję hiperparametry najlepszego modelu...")
    
    # Strojenie hiperparametrów modelu
    # optimize='MAE' - optymalizacja względem Mean Absolute Error
    dostrojony_model = tune_model(model, optimize='MAE')
    
    print("✅ Strojenie zakończone!")
    return dostrojony_model

def porownaj_i_wybierz_model(model_przed, model_po):
    """
    Funkcja porównująca model przed i po strojeniu
    Zwraca lepszy model na podstawie MAE
    """
    print("\n🔍 Porównuję model przed i po strojeniu...")
    
    # Test modelu przed strojeniem
    print("\nModel PRZED strojeniem:")
    wyniki_przed = predict_model(model_przed)
    mae_przed = wyniki_przed['MAE'].iloc[0] if hasattr(wyniki_przed, 'MAE') else None
    
    # Test modelu po strojeniu
    print("\nModel PO strojeniu:")
    wyniki_po = predict_model(model_po)
    mae_po = wyniki_po['MAE'].iloc[0] if hasattr(wyniki_po, 'MAE') else None
    
    # Porównanie parametrów
    print("\n🔧 Sprawdzam czy parametry się zmieniły...")
    if model_przed.get_params() == model_po.get_params():
        print("⚠️  Parametry są identyczne - strojenie nie zmieniło modelu")
        print("   Używam modelu PRZED strojeniem (prostszy)")
        return model_przed
    else:
        print("✅ Parametry są różne - strojenie zmieniło model")
        
        # Porównanie MAE i wybór lepszego modelu
        print("\n📊 Porównuję MAE:")
        print(f"   MAE przed strojeniem: {mae_przed:.2f}")
        print(f"   MAE po strojeniu: {mae_po:.2f}")
        
        if mae_przed is not None and mae_po is not None:
            if mae_po < mae_przed:
                print(f"\n🏆 Model PO strojeniu jest lepszy (MAE: {mae_po:.2f} < {mae_przed:.2f})")
                return model_po
            else:
                print(f"\n🏆 Model PRZED strojeniem jest lepszy (MAE: {mae_przed:.2f} <= {mae_po:.2f})")
                return model_przed
        else:
            # Jeśli nie można wyciągnąć MAE, użyj modelu przed strojeniem
            print("   ⚠️ Nie można porównać MAE, używam modelu PRZED strojeniem")
            return model_przed

def ocen_model(model):
    """
    Funkcja oceniająca model na danych testowych
    Wyświetla metryki i wykresy
    """
    print("\n📊 Oceniam model...")
    
    # Ocena modelu - wyświetla różne metryki
    evaluate_model(model)
    
    print("✅ Ocena zakończona!")

def zapisz_model(model, nazwa_pliku='najlepszy_model_ubezpieczenia'):
    """
    Funkcja zapisująca wytrenowany model do pliku
    """
    print(f"\n💾 Zapisuję model do pliku {nazwa_pliku}...")
    
    # Zapisanie modelu do pliku .pkl
    save_model(model, nazwa_pliku)
    
    print(f"✅ Model zapisany jako {nazwa_pliku}.pkl")

def glowna_funkcja_trenowania():
    """
    Główna funkcja orchestrująca cały proces trenowania
    """
    print("=" * 60)
    print("🚀 START TRENOWANIA MODELU PRZEWIDYWANIA KOSZTÓW UBEZPIECZENIA")
    print("=" * 60)
    
    # Krok 1: Wczytanie danych
    dane = wczytaj_i_przygotuj_dane()
    
    # Krok 2: Przygotowanie środowiska PyCaret
    przygotuj_srodowisko_pycaret(dane)
    
    # Krok 3: Porównanie modeli
    najlepszy_model = porownaj_modele()
    
    # Krok 4: Strojenie hiperparametrów
    dostrojony_model = strojenie_modelu(najlepszy_model)
    
    # Krok 5: Porównanie i wybór finalnego modelu
    finalny_model = porownaj_i_wybierz_model(najlepszy_model, dostrojony_model)
    
    # Krok 6: Ocena modelu
    ocen_model(finalny_model)
    
    # Krok 7: Zapisanie modelu
    zapisz_model(finalny_model)
    
    print("\n" + "=" * 60)
    print("✅ TRENOWANIE ZAKOŃCZONE SUKCESEM!")
    print("=" * 60)
    print("\n📝 Następne kroki:")
    print("1. Model został zapisany jako 'najlepszy_model_ubezpieczenia.pkl'")
    print("2. Możesz teraz uruchomić aplikację Streamlit: streamlit run aplikacja.py")

# Uruchomienie głównej funkcji gdy plik jest wykonywany bezpośrednio
if __name__ == "__main__":
    glowna_funkcja_trenowania()
