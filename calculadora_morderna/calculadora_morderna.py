import customtkinter as ctk
import requests

def converter():
    try:
        valor = float(entrada.get())
        r = requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()
        taxa = r['rates']['BRL']
        resultado.configure(text=f"R$ {valor * taxa:.2f}")
    except:
        resultado.configure(text="Erro na conversão")

ctk.set_appearance_mode("Light")
app = ctk.CTk()
app.geometry("300x200")
app.title("Conversor USD-BRL")

entrada = ctk.CTkEntry(app, placeholder_text="Valor em USD", width=200)
entrada.pack(pady=10)

ctk.CTkButton(app, text="Converter", command=converter).pack(pady=5)
resultado = ctk.CTkLabel(app, text="")
resultado.pack(pady=10)

app.mainloop()
