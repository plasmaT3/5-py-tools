import customtkinter as ctk
import requests

def localizar():
    ip = entrada.get()
    try:
        info = requests.get(f"http://ip-api.com/json/{ip}").json()
        resultado.configure(text=f"{info['city']}, {info['country']}")
    except:
        resultado.configure(text="Erro na localização")

ctk.set_appearance_mode("Light")
app = ctk.CTk()
app.geometry("320x180")
app.title("Rastreador de IP")

entrada = ctk.CTkEntry(app, placeholder_text="Digite o IP", width=250)
entrada.pack(pady=10)

ctk.CTkButton(app, text="Localizar", command=localizar).pack(pady=5)
resultado = ctk.CTkLabel(app, text="")
resultado.pack(pady=10)

app.mainloop()
