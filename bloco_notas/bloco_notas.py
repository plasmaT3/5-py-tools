import customtkinter as ctk
from tkinter.filedialog import asksaveasfilename

def salvar():
    arquivo = asksaveasfilename(defaultextension=".txt")
    if arquivo:
        with open(arquivo, "w") as f:
            f.write(textbox.get("1.0", "end"))

ctk.set_appearance_mode("Light")
app = ctk.CTk()
app.geometry("400x300")
app.title("Bloco de Notas")

textbox = ctk.CTkTextbox(app, width=380, height=200)
textbox.pack(pady=10)

ctk.CTkButton(app, text="Salvar", command=salvar).pack(pady=5)

app.mainloop()
