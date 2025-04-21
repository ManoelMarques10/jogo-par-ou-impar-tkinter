# Jogo de Ímpar ou Par com interface gráfica usando Tkinter
# O jogador escolhe entre "ímpar" ou "par", digita um número entre 0 e 10
# O computador escolhe um número aleatório, e o resultado é mostrado com uma pequena animação
# Pontuação é contada em formato de "winstreak"

from tkinter import *
from PIL import Image, ImageTk
import random
from emoji import emojize

vitórias = 0

def jogo():
    try:
        global vitórias, escolha_jogador, numero_jogador, maquina

        escolha_jogador = escolhapoui.get().lower().replace("í", "i")  # Corrige acento
        numero_jogador = int(número.get())

        if numero_jogador < 0 or numero_jogador > 10:
            resultado["text"] = "Só aceitamos números entre 0 e 10."
            return

        if escolha_jogador not in ["par", "impar"]:
            resultado["text"] = "Só aceitamos 'ímpar' ou 'par'."
            return

        maquina = random.randint(0, 10)

        botão.config(state=DISABLED)  # Evita múltiplos cliques

        # Animação "Ímpar ou Par"
        resultado["text"] = "Ímpar"
        janela.after(500, lambda: resultado.config(text="Ou"))
        janela.after(1000, lambda: resultado.config(text="Par"))
        janela.after(1500, mostrar_resultado)

    except ValueError:
        resultado["text"] = "Ops, insira um número válido."

def mostrar_resultado():
    global vitórias, escolha_jogador, numero_jogador, maquina

    soma = numero_jogador + maquina
    venceu = (soma % 2 == 0 and escolha_jogador == "par") or (soma % 2 != 0 and escolha_jogador == "impar")

    if venceu:
        resultado["text"] = emojize("O jogador venceu! :sunglasses:", language="alias")
        vitórias += 1
        winstreak["text"] = emojize(f"Winstreak {vitórias} :fire:", language="alias")
    else:
        resultado["text"] = emojize("O jogador perdeu. :upside_down_face:", language="alias")
        vitórias = 0
        winstreak["text"] = f"Winstreak {vitórias}"

    resultado["text"] += f"\nVocê jogou {numero_jogador}, máquina jogou {maquina}."

    botão["text"] = "Jogar novamente"
    botão["command"] = resetar
    botão.config(state=NORMAL)

def resetar():
    escolhapoui.delete(0, END)
    número.delete(0, END)
    escolhapoui.focus()  # Foco automático no campo de escolha
    resultado["text"] = ""
    botão["text"] = "Jogar"
    botão["command"] = jogo

# === Janela ===
janela = Tk()
janela.geometry("450x450")
janela.title("Estudos Tkinter")

bg_image = Image.open("Fundo.png")
bg_image = bg_image.resize((450, 450))
bg_photo = ImageTk.PhotoImage(bg_image)

canvas = Canvas(janela, width=450, height=450)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor=NW)

frame = Frame(canvas, bg="plum")
canvas.create_window(225, 225, window=frame)

texto1 = Label(frame, text="Escolha entre 'ímpar' ou 'par'.", bg="plum", font=("Arial", 10, "bold"))
texto1.grid(column=0, row=0, padx=10, pady=10)

escolhapoui = Entry(frame, bg="plum")
escolhapoui.grid(column=0, row=1)

texto2 = Label(frame, text="Escolha um número entre 0 a 10.", bg="plum", font=("Arial", 10, "bold"))
texto2.grid(column=0, row=2, padx=10, pady=10)

número = Entry(frame, bg="plum")
número.grid(column=0, row=3)

botão = Button(frame, text="Jogar", command=jogo, bg="plum", font=("Arial", 10, "bold"), activebackground="violet")
botão.grid(column=0, row=4)

resultado = Label(frame, text="", bg="plum", fg="black", font=("Arial", 10, "bold"))
resultado.grid(column=0, row=5)

winstreak = Label(frame, text="Winstreak 0", bg="plum", font=("Arial", 10, "bold"))
winstreak.grid(column=0, row=6)

janela.mainloop()