# 5-py-tools

Coleção de 5 miniaplicativos feitos em **Python** com **interfaces gráficas modernas**, utilizando a biblioteca `customtkinter`.

## 🧰 Ferramentas incluídas

1. **Calculadora Moderna**
   - Operações básicas com interface de botões.
2. **Conversor de Moeda (USD → BRL)**
   - Consulta taxa de câmbio em tempo real.
3. **Gerador de Senhas**
   - Gera senhas seguras com controle de tamanho.
4. **Bloco de Notas**
   - Editor simples com opção de salvar arquivo `.txt`.
5. **Rastreador de IP**
   - Mostra localização aproximada com base no IP informado.

## 💻 Tecnologias utilizadas

- [Python 3](https://www.python.org/)
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- [Requests](https://pypi.org/project/requests/) (para APIs)

## 📦 Como usar

1. Instale as dependências:
   ```bash
   pip install customtkinter requests

2. Execute o script desejado:

   python nome_do_arquivo.py

Exemplo:

   python calculadora_moderna.py

☁️ Como clonar e testar

   git clone https://github.com/seu-usuario/5-py-tools.git
   cd 5-py-tools
   python calculadora_moderna/calculadora_moderna.py

🔖 Licença
Este projeto é livre para uso pessoal ou acadêmico. Contribuições são bem-vindas!
---
## Imagens

import os

# Caminho da raiz do projeto
caminho = '.'

pastas = [f for f in os.listdir(caminho) if os.path.isdir(os.path.join(caminho, f))]

imagens = [f"{pasta}.png" for pasta in pastas]

with open('imagens_readme.md', 'w', encoding='utf-8') as f:
    for img in imagens:
        if os.path.isfile(os.path.join(caminho, img)):
            f.write(f"![{img}]({img})\n\n")

print("Arquivo imagens_readme.md criado com os links das imagens.\n")

print("Para adicionar as imagens no git, rode os comandos abaixo:\n")
for img in imagens:
    if os.path.isfile(os.path.join(caminho, img)):
        print(f"git add {img}")

## 👤 Autor

**Juan Carlos**

- 🇧🇷 Desenvolvedor independente em Anápolis - GO
- 💼 Projetos voltados para automações e ferramentas gráficas em Python
- 🔗 GitHub: [@plasmaT3](https://github.com/plasmaT3)

---


