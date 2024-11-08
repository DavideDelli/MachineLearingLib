import tkinter as tk
from tkinter import messagebox
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

# Caricamento dati dal file CSV
data = pd.read_csv("./Datasets/milano.csv", delimiter=";")

# Conversione colonne necessarie a float
data['Loc_min'] = data['Loc_min'].str.replace(",", ".").astype(float)
data['Loc_max'] = data['Loc_max'].str.replace(",", ".").astype(float)
data['Anno'] = data['Anno'].astype(int)

# Calcolo del prezzo medio d'affitto per mq
data['Affitto_medio'] = (data['Loc_min'] + data['Loc_max']) / 2

# Creazione del modello di regressione
scaler = StandardScaler()
features = ['Sup_NL_loc', 'Loc_min', 'Loc_max', 'Anno', 'Stato']
X = scaler.fit_transform(data[features])
y = data['Affitto_medio']

model = LinearRegression()
model.fit(X, y)

# Funzione di previsione
def prevedi():
    try:
        # Parametri inseriti dall'utente
        superficie = float(entry_superficie.get())
        anno = int(entry_anno.get())
        quartiere = entry_quartiere.get()
        tipologia = entry_tipologia.get()
        stato = entry_stato.get()

        # Filtraggio dei dati in base ai criteri
        filtro = (
            (data['Zona'] == quartiere) &
            (data['Descr_Tipologia'] == tipologia) &
            (data['Stato'] == stato)
        )
        data_filtrata = data[filtro]

        if data_filtrata.empty:
            messagebox.showerror("Errore", "Nessun dato disponibile per i criteri specificati!")
            return

        # Previsione dell'affitto per l'anno e la superficie selezionati
        X_nuovo = scaler.transform([[superficie, anno]])
        previsione = model.predict(X_nuovo)[0]

        messagebox.showinfo(
            "Previsione",
            f"L'affitto previsto per una casa di {superficie} mq a {quartiere} "
            f"({tipologia}, {stato}) nel {anno} è: {previsione:.2f} €/mq"
        )
    except ValueError:
        messagebox.showerror("Errore", "Inserisci valori numerici validi per superficie e anno.")

# Interfaccia grafica con Tkinter
root = tk.Tk()
root.title("Previsione Affitto Casa a Milano")

# Campi di input
tk.Label(root, text="Superficie (mq):").pack()
entry_superficie = tk.Entry(root)
entry_superficie.pack()

tk.Label(root, text="Anno:").pack()
entry_anno = tk.Entry(root)
entry_anno.pack()

tk.Label(root, text="Quartiere (es: B01):").pack()
entry_quartiere = tk.Entry(root)
entry_quartiere.pack()

tk.Label(root, text="Tipologia (es: Abitazioni civili):").pack()
entry_tipologia = tk.Entry(root)
entry_tipologia.pack()

tk.Label(root, text="Stato di conservazione (es: OTTIMO):").pack()
entry_stato = tk.Entry(root)
entry_stato.pack()

tk.Button(root, text="Prevedi Affitto", command=prevedi).pack()

root.mainloop()
