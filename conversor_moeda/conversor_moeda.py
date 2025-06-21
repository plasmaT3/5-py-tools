import customtkinter as ctk
import requests

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Lista das principais moedas
MOEDAS = [
    "USD", "EUR", "BRL", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", "INR",
    "MXN", "RUB", "ZAR", "KRW", "TRY", "SEK", "NZD"
]

class ConversorMoedas(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Conversor de Moedas")
        self.geometry("400x300")
        self.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        self.label_valor = ctk.CTkLabel(self, text="Valor:", font=("Roboto", 16))
        self.label_valor.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.entry_valor = ctk.CTkEntry(self, font=("Roboto", 16))
        self.entry_valor.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.label_moeda_origem = ctk.CTkLabel(self, text="De:", font=("Roboto", 16))
        self.label_moeda_origem.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.combo_origem = ctk.CTkComboBox(self, values=MOEDAS, font=("Roboto", 14))
        self.combo_origem.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        self.combo_origem.set("USD")  # valor padrão

        self.label_moeda_destino = ctk.CTkLabel(self, text="Para:", font=("Roboto", 16))
        self.label_moeda_destino.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.combo_destino = ctk.CTkComboBox(self, values=MOEDAS, font=("Roboto", 14))
        self.combo_destino.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
        self.combo_destino.set("BRL")  # valor padrão

        self.botao_converter = ctk.CTkButton(self, text="Converter", command=self.converter)
        self.botao_converter.grid(row=3, column=0, columnspan=2, pady=20)

        self.label_resultado = ctk.CTkLabel(self, text="", font=("Roboto", 18))
        self.label_resultado.grid(row=4, column=0, columnspan=2, pady=10)

        # Configura coluna 1 para expandir (entrada e combos)
        self.grid_columnconfigure(1, weight=1)

    def converter(self):
        valor_texto = self.entry_valor.get()
        moeda_origem = self.combo_origem.get()
        moeda_destino = self.combo_destino.get()

        try:
            valor = float(valor_texto)
            if valor < 0:
                raise ValueError("Valor deve ser positivo.")
        except ValueError:
            self.label_resultado.configure(text="Por favor, insira um valor numérico válido.", text_color="red")
            return

        # Usa API pública para obter taxa de câmbio
        url = f"https://api.exchangerate.host/convert?from={moeda_origem}&to={moeda_destino}&amount={valor}"
        try:
            resposta = requests.get(url)
            dados = resposta.json()
            if dados.get("success"):
                resultado = dados.get("result")
                self.label_resultado.configure(
                    text=f"{valor:.2f} {moeda_origem} = {resultado:.2f} {moeda_destino}",
                    text_color="white"
                )
            else:
                self.label_resultado.configure(text="Erro ao obter a taxa de câmbio.", text_color="red")
        except Exception:
            self.label_resultado.configure(text="Erro na conexão com a API.", text_color="red")

if __name__ == "__main__":
    app = ConversorMoedas()
    app.mainloop()
