import customtkinter as ctk
import requests
import webbrowser

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class LocalizadorIP(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Localizador de IP")
        self.geometry("400x250")
        self.resizable(False, False)

        self.ip = None
        self.latitude = None
        self.longitude = None

        self.create_widgets()

    def create_widgets(self):
        self.label_ip = ctk.CTkLabel(self, text="Seu IP:", font=("Roboto", 16))
        self.label_ip.pack(pady=(20, 5))

        self.entry_ip = ctk.CTkEntry(self, font=("Roboto", 16), width=250)
        self.entry_ip.pack(pady=5)
        self.entry_ip.configure(state="readonly")

        self.botao_descobrir = ctk.CTkButton(self, text="Descobrir meu IP", command=self.descobrir_ip)
        self.botao_descobrir.pack(pady=10)

        self.botao_mapa = ctk.CTkButton(self, text="Mostrar no Google Maps", command=self.abrir_mapa, state="disabled")
        self.botao_mapa.pack(pady=10)

        self.label_status = ctk.CTkLabel(self, text="", font=("Roboto", 14))
        self.label_status.pack(pady=10)

    def descobrir_ip(self):
        self.label_status.configure(text="Buscando seu IP...")
        try:
            resposta = requests.get("https://api.ipify.org?format=json", timeout=5)
            resposta.raise_for_status()
            self.ip = resposta.json().get("ip")
            self.entry_ip.configure(state="normal")
            self.entry_ip.delete(0, "end")
            self.entry_ip.insert(0, self.ip)
            self.entry_ip.configure(state="readonly")
            self.label_status.configure(text="Buscando localização do IP...")

            self.buscar_localizacao()
        except Exception as e:
            self.label_status.configure(text=f"Erro ao obter IP: {e}")

    def buscar_localizacao(self):
        try:
            url = f"https://ipapi.co/{self.ip}/json/"
            resposta = requests.get(url, timeout=5)
            resposta.raise_for_status()
            dados = resposta.json()

            self.latitude = dados.get("latitude")
            self.longitude = dados.get("longitude")

            if self.latitude and self.longitude:
                self.label_status.configure(text=f"Localização encontrada: {self.latitude}, {self.longitude}")
                self.botao_mapa.configure(state="normal")
            else:
                self.label_status.configure(text="Não foi possível obter localização do IP.")
                self.botao_mapa.configure(state="disabled")
        except Exception as e:
            self.label_status.configure(text=f"Erro ao obter localização: {e}")
            self.botao_mapa.configure(state="disabled")

    def abrir_mapa(self):
        if self.latitude and self.longitude:
            url_mapa = f"https://www.google.com/maps/search/?api=1&query={self.latitude},{self.longitude}"
            webbrowser.open(url_mapa)
        else:
            self.label_status.configure(text="Nenhuma localização para mostrar.")

if __name__ == "__main__":
    app = LocalizadorIP()
    app.mainloop()
