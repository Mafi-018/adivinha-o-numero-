import random
import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font
from tkinter import ttk

def iniciar_jogo():
    apresentacao_frame.pack_forget()
    jogo_frame.pack()

def reiniciar_jogo():
    global numero_secreto
    numero_secreto = random.randint(1, 100)
    historico.clear()
    historico_text.delete("1.0", tk.END)
    entrada.delete(0, tk.END)
    mensagem_label.configure(text="")
    reiniciar_button.pack_forget()
    entrada.configure(state='normal')
    botao_verificar.configure(state='normal')
    entrada.focus_set()

def verificar_tentativa():
    tentativa = entrada.get()

    if tentativa.lower() == 'desistir':
        messagebox.showinfo("Jogo de Adivinhação", f"O número secreto era: {numero_secreto}\nDesistiu do jogo. Boa  sorte n"
                                                   f"a próxima vez!")
        janela.destroy()
    else:
        try:
            tentativa = int(tentativa)
            historico.append(tentativa)
            if tentativa == numero_secreto:
                mensagem_label.configure(text=f"Parabéns! Você acertou em {len(historico)} tentativa(s)!", fg="#00FF00")
                reiniciar_button.pack()
                entrada.configure(state='disabled')
                botao_verificar.configure(state='disabled')
            elif tentativa < numero_secreto:
                mensagem_label.configure(text="Tente um número maior!", fg="#FF0000")
            else:
                mensagem_label.configure(text="Tente um número menor!", fg="#FF0000")
            entrada.delete(0, tk.END)
            entrada.focus_set()
            atualizar_historico()
        except ValueError:
            messagebox.showinfo("Jogo de Adivinhação", "Entrada inválida. Digite um número válido ou 'desistir' para sair.")

def atualizar_historico():
    historico_text.delete("1.0", tk.END)
    for i, tentativa in enumerate(historico, start=1):
        historico_text.insert(tk.END, f"{i}. {tentativa}\n")

# Configurações de estilo
background_color = "#4B0082"  # Roxo escuro
font_color = "#FFFFFF"
highlight_color = "#3D85C6"
active_color = "#90EE90"
entry_bg_color = "#FFFFFF"
entry_fg_color = "#333333"
button_bg_color = "#90EE90"
button_fg_color = "#000000"

janela = tk.Tk()
janela.title("Jogo de Adivinhação")
janela.geometry("400x500")
janela.config(bg=background_color)


# Centralizar a janela na tela
largura_janela = 400
altura_janela = 500
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
posicao_x = int(largura_tela/2 - largura_janela/2)
posicao_y = int(altura_tela/2 - altura_janela/2)
janela.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")

numero_secreto = random.randint(1, 100)
historico = []

fonte_titulo = Font(family="Arial", size=28, weight="bold")
fonte_texto = Font(family="Arial", size=14)
fonte_botao = Font(family="Arial", size=14, weight="bold")
fonte_historico = Font(family="Arial", size=12)

apresentacao_frame = tk.Frame(janela, bg=background_color)
apresentacao_frame.pack(expand=True)

jogo_frame = tk.Frame(janela, bg=background_color)

label_titulo = tk.Label(apresentacao_frame, text="Jogo de Adivinhação", font=fonte_titulo, fg=font_color, bg=background_color)
label_titulo.pack(pady=20)

label_instrucoes = tk.Label(apresentacao_frame, text="Estou pensando em um número entre 1 e 100. Tente adivinhar!", font=fonte_texto, fg=font_color, bg=background_color)
label_instrucoes.pack(pady=10)

iniciar_button = ttk.Button(apresentacao_frame, text="Iniciar Jogo", style="C.TButton", command=iniciar_jogo)
iniciar_button.pack(pady=20)

label_digite = tk.Label(jogo_frame, text="Digite um número (ou 'desistir' para sair):", font=fonte_texto, fg=font_color, bg=background_color)
label_digite.pack()

entrada = tk.Entry(jogo_frame, font=fonte_texto, width=10, bg=entry_bg_color, fg=entry_fg_color)
entrada.pack(pady=10)
entrada.focus_set()

botao_verificar = ttk.Button(jogo_frame, text="Verificar", style="C.TButton", command=verificar_tentativa)
botao_verificar.pack()

mensagem_label = tk.Label(jogo_frame, font=fonte_texto, fg=font_color, bg=background_color)
mensagem_label.pack(pady=10)

historico_frame = tk.Frame(jogo_frame, bg=background_color)
historico_frame.pack()

historico_text = tk.Text(historico_frame, font=fonte_historico, fg=font_color, bg=background_color, width=15, height=8, bd=0)
historico_text.pack(side=tk.LEFT, padx=25)

reiniciar_button = ttk.Button(jogo_frame, text="Reiniciar", style="C.TButton", command=reiniciar_jogo)
reiniciar_button.pack_forget()

# Estilo do botão
style = ttk.Style()
style.configure("C.TButton",
                font=fonte_botao,
                background=button_bg_color,
                foreground=button_fg_color,
                padding=10,
                relief=tk.RAISED,
                borderwidth=2)
style.map("C.TButton",
          background=[('active', active_color)],
          foreground=[('active', button_fg_color)])


janela.mainloop()