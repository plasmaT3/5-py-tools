import customtkinter as ctk
import string, random

def gerar_senha():
    chars = string.ascii_letters + string.digits + string.punctuation
    tamanho = int(slider.get())
    senha = ''.join(random.choice(chars) for _ in range(tamanho))
    resultado.configure(text=senha)

ctk.set_appearance_mode("Light")
app = ctk.CTk()
app.geometry("300x200")
app.title("Gerador de Senhas")

slider = ctk.CTkSlider(app, from_=8, to=32, number_of_steps=24)
slider.set(12)
slider.pack(pady=10)

ctk.CTkButton(app, text="Gerar Senha", command=gerar_senha).pack(pady=5)
resultado = ctk.CTkLabel(app, text="")
resultado.pack(pady=10)

app.mainloop()
