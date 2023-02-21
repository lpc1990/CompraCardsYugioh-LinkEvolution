import pygetwindow as gw
import teclas
import time
import os
from tkinter import *
from tkinter import messagebox
import pyautogui
from python_imagesearch.imagesearch import imagesearch
import pygame


# Função principal, que faz o direcionamento ao personagem escolhido, além de pegar o valor do personagem
# selecionado no radiobuton e colocar na variável "personagem"
def inicio(personagem_escolhido, quantidade_packs_para_comprar):
    # Verifica se a o yugioh tá aberto. Se tiver, ele dá foco ao yugioh, e coloca o mouse encima de Modo Solo
    if gw.getWindowsWithTitle("Yu-Gi-Oh! Legacy of the Duelist : Link Evolution"):
        yugioh_aberto = gw.getWindowsWithTitle("Yu-Gi-Oh! Legacy of the Duelist : Link Evolution")[0]
        yugioh_aberto.activate()
        time.sleep(2)
        personagem = personagem_escolhido.get()
        # Faz uma pesquisa de imagem pelo "Modo solo" na janela principal, e posiciona o mouse pra lá
        pos = imagesearch("./images/modo_solo.png")
        if pos[0] != -1:
            print("position : ", pos[0], pos[1])
            pyautogui.moveTo(pos[0], pos[1])

        teclas.teclado_baixo(4)
        teclas.teclado_enter(1)

    else:
        os.startfile("yugioh.bat")
        personagem = personagem_escolhido.get()
        time.sleep(20)
        teclas.teclado_enter(1)
        time.sleep(2)
        teclas.teclado_baixo(4)
        teclas.teclado_enter(1)

    if personagem == "vovo_muto":
        time.sleep(1)
        comprar_cartas(quantidade_packs_para_comprar, personagem)
    if personagem == "mai":
        time.sleep(1)
        teclas.teclado_direita(1)
        comprar_cartas(quantidade_packs_para_comprar, personagem)
    if personagem == "bakura":
        time.sleep(1)
        teclas.teclado_direita(2)
        comprar_cartas(quantidade_packs_para_comprar, personagem)
    if personagem == "joe":
        time.sleep(1)
        teclas.teclado_direita(3)
        comprar_cartas(quantidade_packs_para_comprar, personagem)
    if personagem == "kaiba":
        time.sleep(1)
        teclas.teclado_direita(4)
        comprar_cartas(quantidade_packs_para_comprar, personagem)
    if personagem == "yugi":
        time.sleep(1)
        teclas.teclado_direita(5)
        comprar_cartas(quantidade_packs_para_comprar, personagem)

    if personagem == "alexis":
        time.sleep(1)
        teclas.teclado_baixo(1)
        comprar_cartas(quantidade_packs_para_comprar, personagem)
    if personagem == "bastion":
        time.sleep(1)
        teclas.teclado_baixo(1)
        teclas.teclado_direita(1)
        comprar_cartas(quantidade_packs_para_comprar, personagem)
    if personagem == "chazz":
        time.sleep(1)
        teclas.teclado_baixo(1)
        teclas.teclado_direita(2)
        comprar_cartas(quantidade_packs_para_comprar, personagem)
    if personagem == "syrus":
        time.sleep(1)
        teclas.teclado_baixo(1)
        teclas.teclado_direita(3)
        comprar_cartas(quantidade_packs_para_comprar, personagem)
    if personagem == "jesse":
        time.sleep(1)
        teclas.teclado_baixo(1)
        teclas.teclado_direita(4)
        comprar_cartas(quantidade_packs_para_comprar, personagem)
    if personagem == "jaden":
        time.sleep(1)
        teclas.teclado_baixo(1)
        teclas.teclado_direita(5)
        comprar_cartas(quantidade_packs_para_comprar, personagem)

    if personagem == "tetsu":
        time.sleep(1)
        teclas.teclado_baixo(2)
        comprar_cartas(quantidade_packs_para_comprar, personagem)
    if personagem == "leo_luna":
        time.sleep(1)
        teclas.teclado_baixo(2)
        teclas.teclado_direita(1)
        comprar_cartas(quantidade_packs_para_comprar, personagem)
    if personagem == "akiza":
        time.sleep(1)
        teclas.teclado_baixo(2)
        teclas.teclado_direita(2)
        comprar_cartas(quantidade_packs_para_comprar, personagem)
    if personagem == "jack":
        time.sleep(1)
        teclas.teclado_baixo(2)
        teclas.teclado_direita(3)
        comprar_cartas(quantidade_packs_para_comprar, personagem)
    if personagem == "crow":
        time.sleep(1)
        teclas.teclado_baixo(2)
        teclas.teclado_direita(4)
        comprar_cartas(quantidade_packs_para_comprar, personagem)
    if personagem == "yusei":
        time.sleep(1)
        teclas.teclado_baixo(2)
        teclas.teclado_direita(5)
        comprar_cartas(quantidade_packs_para_comprar, personagem)

    if personagem == "cathy":
        time.sleep(1)
        teclas.teclado_baixo(3)
        comprar_cartas(quantidade_packs_para_comprar, personagem)
    if personagem == "quinton":
        time.sleep(1)
        teclas.teclado_baixo(3)
        teclas.teclado_direita(1)
        comprar_cartas(quantidade_packs_para_comprar, personagem)
    if personagem == "kite":
        time.sleep(1)
        teclas.teclado_baixo(3)
        teclas.teclado_direita(2)
        comprar_cartas(quantidade_packs_para_comprar, personagem)
    if personagem == "shark":
        time.sleep(1)
        teclas.teclado_baixo(3)
        teclas.teclado_direita(3)
        comprar_cartas(quantidade_packs_para_comprar, personagem)
    if personagem == "yuma":
        time.sleep(1)
        teclas.teclado_baixo(3)
        teclas.teclado_direita(4)
        comprar_cartas(quantidade_packs_para_comprar, personagem)

    if personagem == "gong":
        time.sleep(1)
        teclas.teclado_baixo(4)
        comprar_cartas(quantidade_packs_para_comprar, personagem)
    if personagem == "zuzu":
        time.sleep(1)
        teclas.teclado_baixo(4)
        teclas.teclado_direita(1)
        comprar_cartas(quantidade_packs_para_comprar, personagem)
    if personagem == "shay":
        time.sleep(1)
        teclas.teclado_baixo(4)
        teclas.teclado_direita(2)
        comprar_cartas(quantidade_packs_para_comprar, personagem)
    if personagem == "declan":
        time.sleep(1)
        teclas.teclado_baixo(4)
        teclas.teclado_direita(3)
        comprar_cartas(quantidade_packs_para_comprar, personagem)
    if personagem == "yuya":
        time.sleep(1)
        teclas.teclado_baixo(4)
        teclas.teclado_direita(4)
        comprar_cartas(quantidade_packs_para_comprar, personagem)

    if personagem == "playmaker":
        time.sleep(1)
        teclas.teclado_baixo(5)
        comprar_cartas(quantidade_packs_para_comprar, personagem)
    if personagem == "blue":
        time.sleep(1)
        teclas.teclado_baixo(5)
        teclas.teclado_direita(1)
        comprar_cartas(quantidade_packs_para_comprar, personagem)
    if personagem == "soulburner":
        time.sleep(1)
        teclas.teclado_baixo(5)
        teclas.teclado_direita(2)
        comprar_cartas(quantidade_packs_para_comprar, personagem)
    if personagem == "varis":
        time.sleep(1)
        teclas.teclado_baixo(5)
        teclas.teclado_direita(3)
        comprar_cartas(quantidade_packs_para_comprar, personagem)
    if personagem == "ai":
        time.sleep(1)
        teclas.teclado_baixo(5)
        teclas.teclado_direita(4)
        comprar_cartas(quantidade_packs_para_comprar, personagem)


# Função que executa a compra das cartas depois de já estar no menu de compras lá no jogo
def comprar_cartas(quantidade_packs_para_comprar, personagem):
    i = 0
    while quantidade_packs_para_comprar > i:
        if i == 0:
            time.sleep(2)
            teclas.teclado_enter(1)
            valor = acabou_a_compra()
            if valor == 0:
                print(f"valor primeiro if = {valor} - Linha 208")
                time.sleep(.6)
                teclas.teclado_enter(1)
                time.sleep(.6)
                teclas.teclado_enter(1)
                time.sleep(6)
                teclas.teclado_enter(1)
                print(f"Valor do i aqui: {i} - Linha 214")
                i = i + 1
            else:
                print(f"valor primeiro else = {valor} - Linha 217")
                break
        else:
            teclas.teclado_enter(1)
            valor = acabou_a_compra()
            if valor == 0:
                print(f"valor segundo if = {valor} - Linha 224")
                time.sleep(.5)
                teclas.teclado_enter(1)
                time.sleep(.5)
                teclas.teclado_enter(1)
                time.sleep(6)
                teclas.teclado_enter(1)
                time.sleep(.5)
                print(f"Valor do i aqui: {i} - Linha 232")
                i = i + 1

            else:
                print(f"valor segundo else = {valor} - Linha 235")
                break
    time.sleep(2)
    teclas.teclado_enter(1)
    time.sleep(1)
    teclas.teclado_esc(1)
    time.sleep(3)

    if personagem == "vovo_muto":
        if i != 0:
            som_acabou_as_compras()
            valor_total_comprado = quantidade_packs_para_comprar * 200
            quantidade_de_cards_adquirido = quantidade_packs_para_comprar * 8
            messagebox.showinfo("Informações da compra", f"Foram comprados {quantidade_packs_para_comprar} packs, "
                                                         f"com o valor total de {valor_total_comprado}! \n"
                                                         f"Foram adquiridas {quantidade_de_cards_adquirido} cartas no total! ")
    else:
        if i != 0:
            som_acabou_as_compras()
            valor_total_comprado = quantidade_packs_para_comprar * 400
            quantidade_de_cards_adquirido = quantidade_packs_para_comprar * 8
            messagebox.showinfo("Informações da compra", f"Foram comprados {quantidade_packs_para_comprar} packs, "
                                                         f"com o valor total de {valor_total_comprado}! \n"
                                                         f"Foram adquiridas {quantidade_de_cards_adquirido} cartas no total! ")


# Função para a verificação se foi dado entrada em INT e se foi escolhido somente um personagem
def numero(numero, personagem_escolhido):
    personagem = personagem_escolhido.get()
    if personagem == "":
        messagebox.showwarning("Multiplas escolhas", "Escolha somente um personagem!")
    else:
        try:
            int(quantidade_packs.get())
            packs = int(quantidade_packs.get())
            inicio(personagem_selecionado, packs)

        except ValueError:
            messagebox.showwarning("Somente números!", "Por favor, digite somente números!")


# Função para verificar se aparece a mensagem de que não existem
# mais cartas para serem compradas com o personagem escolhido
def acabou_a_compra():
    pos = imagesearch("./images/compra_finalizada.png")
    if pos[0] != -1:
        valor = 1
        som_acabou_as_compras()
        messagebox.showinfo("Informações da compra", "Já foram comprados todos os packs para esse personagem!")
        return valor
    else:
        valor = 0
        return valor
        pass


# Função para parar e iniciar a música
def parar_musica():
    if musica.get_busy():
        musica.stop()
    else:
        musica.play(som, loops=10)


# início configurações do TKinter
janela = Tk()
janela.resizable(False, False)
janela.title("*** Comprando cards de Yugioh ***")
janela.iconbitmap("./images/MilleniumPuzzle.ico")

img_fundo = PhotoImage(file="images\\fundo_programa.png")
label_fundo = Label(janela, image=img_fundo)
label_fundo.pack()


# Acabou as compras!
def som_acabou_as_compras():
    musica = pygame.mixer.Channel(5)
    som = pygame.mixer.Sound("./sounds/acabou_a_compra.mp3")
    musica.play(som, loops=0)
    musica.set_volume(1)


# Iniciando a música junto com o programa
pygame.mixer.init()
musica = pygame.mixer.Channel(5)
som = pygame.mixer.Sound("./sounds/yugioh_free_duel.mp3")

musica.play(som, loops=10)
musica.set_volume(0.2)

# Cálculo para a definição do centro da tela, para o aparecimento ideal da janela do programa
# *****************************************************************
largura = 1600
altura = 900

largura_screen = janela.winfo_screenwidth()
altura_screen = janela.winfo_screenheight()

posx = ((largura_screen / 2) - (largura / 2))
posy = ((altura_screen / 2) - (altura / 2))

janela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
# *****************************************************************

# Indica o caminho da pasta das imagens usadas no sistema
pasta_de_imagens = os.path.dirname(__file__)

# *****************************************************************
# Criando os RadioButtons
personagem_selecionado = StringVar()

# ************************ RadioButon grupo 1 *******************************
rb_vovo_muto = Radiobutton(janela, text="", value="vovo_muto", variable=personagem_selecionado)
rb_vovo_muto.place(x=125, y=195)

rb_mai = Radiobutton(janela, text="", value="mai", variable=personagem_selecionado)
rb_mai.place(x=215, y=195)

rb_bakura = Radiobutton(janela, text="", value="bakura", variable=personagem_selecionado)
rb_bakura.place(x=305, y=195)

rb_joe = Radiobutton(janela, text="", value="joe", variable=personagem_selecionado)
rb_joe.place(x=395, y=195)

rb_kaiba = Radiobutton(janela, text="", value="kaiba", variable=personagem_selecionado)
rb_kaiba.place(x=485, y=195)

rb_yugi = Radiobutton(janela, text="", value="yugi", variable=personagem_selecionado)
rb_yugi.place(x=575, y=195)

# ************************ RadioButon grupo 2 *******************************
rb_alexis = Radiobutton(janela, text="", value="alexis", variable=personagem_selecionado)
rb_alexis.place(x=125, y=405)

rb_bastion = Radiobutton(janela, text="", value="bastion", variable=personagem_selecionado)
rb_bastion.place(x=215, y=405)

rb_chazz = Radiobutton(janela, text="", value="chazz", variable=personagem_selecionado)
rb_chazz.place(x=305, y=405)

rb_syrus = Radiobutton(janela, text="", value="syrus", variable=personagem_selecionado)
rb_syrus.place(x=395, y=405)

rb_jesse = Radiobutton(janela, text="", value="jesse", variable=personagem_selecionado)
rb_jesse.place(x=485, y=405)

rb_jaden = Radiobutton(janela, text="", value="jaden", variable=personagem_selecionado)
rb_jaden.place(x=575, y=405)

# ************************ RadioButon grupo 3 *******************************
rb_tetsu = Radiobutton(janela, text="", value="tetsu", variable=personagem_selecionado)
rb_tetsu.place(x=125, y=615)

rb_leo_luna = Radiobutton(janela, text="", value="leo_luna", variable=personagem_selecionado)
rb_leo_luna.place(x=215, y=615)

rb_akiza = Radiobutton(janela, text="", value="akiza", variable=personagem_selecionado)
rb_akiza.place(x=305, y=615)

rb_jack = Radiobutton(janela, text="", value="jack", variable=personagem_selecionado)
rb_jack.place(x=395, y=615)

rb_crow = Radiobutton(janela, text="", value="crow", variable=personagem_selecionado)
rb_crow.place(x=485, y=615)

rb_yusei = Radiobutton(janela, text="", value="yusei", variable=personagem_selecionado)
rb_yusei.place(x=575, y=615)

# ************************ RadioButon grupo 4 *******************************
rb_cathy = Radiobutton(janela, text="", value="cathy", variable=personagem_selecionado)
rb_cathy.place(x=1115, y=195)

rb_quinton = Radiobutton(janela, text="", value="quinton", variable=personagem_selecionado)
rb_quinton.place(x=1205, y=195)

rb_kite = Radiobutton(janela, text="", value="kite", variable=personagem_selecionado)
rb_kite.place(x=1295, y=195)

rb_shark = Radiobutton(janela, text="", value="shark", variable=personagem_selecionado)
rb_shark.place(x=1385, y=195)

rb_yuma = Radiobutton(janela, text="", value="yuma", variable=personagem_selecionado)
rb_yuma.place(x=1475, y=195)

# ************************ RadioButon grupo 5 *******************************
rb_gong = Radiobutton(janela, text="", value="gong", variable=personagem_selecionado)
rb_gong.place(x=1115, y=405)

rb_zuzu = Radiobutton(janela, text="", value="zuzu", variable=personagem_selecionado)
rb_zuzu.place(x=1205, y=405)

rb_shay = Radiobutton(janela, text="", value="shay", variable=personagem_selecionado)
rb_shay.place(x=1295, y=405)

rb_declan = Radiobutton(janela, text="", value="declan", variable=personagem_selecionado)
rb_declan.place(x=1385, y=405)

rb_yuya = Radiobutton(janela, text="", value="yuya", variable=personagem_selecionado)
rb_yuya.place(x=1475, y=405)

# RadioButon grupo 6
rb_playmaker = Radiobutton(janela, text="", value="playmaker", variable=personagem_selecionado)
rb_playmaker.place(x=1115, y=615)

rb_blue = Radiobutton(janela, text="", value="blue", variable=personagem_selecionado)
rb_blue.place(x=1205, y=615)

rb_soulburner = Radiobutton(janela, text="", value="soulburner", variable=personagem_selecionado)
rb_soulburner.place(x=1295, y=615)

rb_varis = Radiobutton(janela, text="", value="varis", variable=personagem_selecionado)
rb_varis.place(x=1385, y=615)

rb_ai = Radiobutton(janela, text="", value="ai", variable=personagem_selecionado)
rb_ai.place(x=1475, y=615)

# Criando as imaggens dos duelistas na tela principal
# ++++++++++++++++++++++++++++++++++++ Fileira 1 de duelistas ++++++++++++++++++++++++++++++++++++++
img_logo_1 = PhotoImage(file=pasta_de_imagens + "\\personagens\\1_0_2.png")
label_logo_1 = Label(janela, image=img_logo_1)
label_logo_1.place(x=10, y=50)

img_vovo_muto = PhotoImage(file=pasta_de_imagens + "\\personagens\\1_1_vovo_muto_2.png")
label_vovo_muto = Label(janela, image=img_vovo_muto)
label_vovo_muto.place(x=90, y=20)

img_mai = PhotoImage(file=pasta_de_imagens + "\\personagens\\1_2_mai_2.png")
label_mai = Label(janela, image=img_mai)
label_mai.place(x=180, y=20)

img_bakura = PhotoImage(file=pasta_de_imagens + "\\personagens\\1_3_bakura_2.png")
label_bakura = Label(janela, image=img_bakura)
label_bakura.place(x=270, y=20)

img_joe = PhotoImage(file=pasta_de_imagens + "\\personagens\\1_4_joe_2.png")
label_joe = Label(janela, image=img_joe)
label_joe.place(x=360, y=20)

img_kaiba = PhotoImage(file=pasta_de_imagens + "\\personagens\\1_5_kaiba_2.png")
label_kaiba = Label(janela, image=img_kaiba)
label_kaiba.place(x=450, y=20)

img_yugi = PhotoImage(file=pasta_de_imagens + "\\personagens\\1_6_yugi_2.png")
label_yugi = Label(janela, image=img_yugi)
label_yugi.place(x=540, y=20)

# ++++++++++++++++++++++++++++++++++++ Fileira 2 de duelistas ++++++++++++++++++++++++++++++++++++++
img_logo_2 = PhotoImage(file=pasta_de_imagens + "\\personagens\\2_0_2.png")
label_logo_2 = Label(janela, image=img_logo_2)
label_logo_2.place(x=10, y=260)

img_alexis = PhotoImage(file=pasta_de_imagens + "\\personagens\\2_1_alexis_2.png")
label_alexis = Label(janela, image=img_alexis)
label_alexis.place(x=90, y=230)

img_bastion = PhotoImage(file=pasta_de_imagens + "\\personagens\\2_2_bastion_2.png")
label_bastion = Label(janela, image=img_bastion)
label_bastion.place(x=180, y=230)

img_chazz = PhotoImage(file=pasta_de_imagens + "\\personagens\\2_3_chazz_2.png")
label_chazz = Label(janela, image=img_chazz)
label_chazz.place(x=270, y=230)

img_syrus = PhotoImage(file=pasta_de_imagens + "\\personagens\\2_4_syrus_2.png")
label_syrus = Label(janela, image=img_syrus)
label_syrus.place(x=360, y=230)

img_jesse = PhotoImage(file=pasta_de_imagens + "\\personagens\\2_5_jesse_2.png")
label_jesse = Label(janela, image=img_jesse)
label_jesse.place(x=450, y=230)

img_jaden = PhotoImage(file=pasta_de_imagens + "\\personagens\\2_6_jaden_2.png")
label_jaden = Label(janela, image=img_jaden)
label_jaden.place(x=540, y=230)

# ++++++++++++++++++++++++++++++++++++ Fileira 3 de duelistas ++++++++++++++++++++++++++++++++++++++
img_logo_3 = PhotoImage(file=pasta_de_imagens + "\\personagens\\3_0_2.png")
label_logo_3 = Label(janela, image=img_logo_3)
label_logo_3.place(x=10, y=470)

img_tetsu = PhotoImage(file=pasta_de_imagens + "\\personagens\\3_1_tetsu_2.png")
label_tetsu = Label(janela, image=img_tetsu)
label_tetsu.place(x=90, y=440)

img_leo_luna = PhotoImage(file=pasta_de_imagens + "\\personagens\\3_2_leo_luna_2.png")
label_leo_luna = Label(janela, image=img_leo_luna)
label_leo_luna.place(x=180, y=440)

img_akiza = PhotoImage(file=pasta_de_imagens + "\\personagens\\3_3_akiza_2.png")
label_akiza = Label(janela, image=img_akiza)
label_akiza.place(x=270, y=440)

img_jack = PhotoImage(file=pasta_de_imagens + "\\personagens\\3_4_jack_2.png")
label_jack = Label(janela, image=img_jack)
label_jack.place(x=360, y=440)

img_crow = PhotoImage(file=pasta_de_imagens + "\\personagens\\3_5_crow_2.png")
label_crow = Label(janela, image=img_crow)
label_crow.place(x=450, y=440)

img_yusei = PhotoImage(file=pasta_de_imagens + "\\personagens\\3_6_yusei_2.png")
label_yusei = Label(janela, image=img_yusei)
label_yusei.place(x=540, y=440)

# ++++++++++++++++++++++++++++++++++++ Fileira 4 de duelistas ++++++++++++++++++++++++++++++++++++++
img_logo_4 = PhotoImage(file=pasta_de_imagens + "\\personagens\\4_0_2.png")
label_logo_4 = Label(janela, image=img_logo_4)
label_logo_4.place(x=1000, y=50)

img_cathy = PhotoImage(file=pasta_de_imagens + "\\personagens\\4_1_cathy_2.png")
label_cathy = Label(janela, image=img_cathy)
label_cathy.place(x=1080, y=20)

img_quinton = PhotoImage(file=pasta_de_imagens + "\\personagens\\4_2_quinton_2.png")
label_quinton = Label(janela, image=img_quinton)
label_quinton.place(x=1170, y=20)

img_kite = PhotoImage(file=pasta_de_imagens + "\\personagens\\4_3_kite_2.png")
label_kite = Label(janela, image=img_kite)
label_kite.place(x=1260, y=20)

img_shark = PhotoImage(file=pasta_de_imagens + "\\personagens\\4_4_shark_2.png")
label_shark = Label(janela, image=img_shark)
label_shark.place(x=1350, y=20)

img_yuma = PhotoImage(file=pasta_de_imagens + "\\personagens\\4_5_yuma_2.png")
label_yuma = Label(janela, image=img_yuma)
label_yuma.place(x=1440, y=20)

# ++++++++++++++++++++++++++++++++++++ Fileira 5 de duelistas ++++++++++++++++++++++++++++++++++++++
img_logo_5 = PhotoImage(file=pasta_de_imagens + "\\personagens\\5_0_2.png")
label_logo_5 = Label(janela, image=img_logo_5)
label_logo_5.place(x=1000, y=260)

img_gong = PhotoImage(file=pasta_de_imagens + "\\personagens\\5_1_gong_2.png")
label_gong = Label(janela, image=img_gong)
label_gong.place(x=1080, y=230)

img_zuzu = PhotoImage(file=pasta_de_imagens + "\\personagens\\5_2_zuzu_2.png")
label_zuzu = Label(janela, image=img_zuzu)
label_zuzu.place(x=1170, y=230)

img_shay = PhotoImage(file=pasta_de_imagens + "\\personagens\\5_3_shay_2.png")
label_shay = Label(janela, image=img_shay)
label_shay.place(x=1260, y=230)

img_declan = PhotoImage(file=pasta_de_imagens + "\\personagens\\5_4_declan_2.png")
label_declan = Label(janela, image=img_declan)
label_declan.place(x=1350, y=230)

img_yuya = PhotoImage(file=pasta_de_imagens + "\\personagens\\5_5_yuya_2.png")
label_yuya = Label(janela, image=img_yuya)
label_yuya.place(x=1440, y=230)

# ++++++++++++++++++++++++++++++++++++ Fileira 6 de duelistas ++++++++++++++++++++++++++++++++++++++
img_logo_6 = PhotoImage(file=pasta_de_imagens + "\\personagens\\6_0_2.png")
label_logo_6 = Label(janela, image=img_logo_6)
label_logo_6.place(x=1000, y=470)

img_playmaker = PhotoImage(file=pasta_de_imagens + "\\personagens\\6_1_playmaker_2.png")
label_playmaker = Label(janela, image=img_playmaker)
label_playmaker.place(x=1080, y=440)

img_blue = PhotoImage(file=pasta_de_imagens + "\\personagens\\6_2_blue_2.png")
label_blue = Label(janela, image=img_blue)
label_blue.place(x=1170, y=440)

img_soulburner = PhotoImage(file=pasta_de_imagens + "\\personagens\\6_3_soulburner_2.png")
label_soulburner = Label(janela, image=img_soulburner)
label_soulburner.place(x=1260, y=440)

img_varis = PhotoImage(file=pasta_de_imagens + "\\personagens\\6_4_varis_2.png")
label_varis = Label(janela, image=img_varis)
label_varis.place(x=1350, y=440)

img_ai = PhotoImage(file=pasta_de_imagens + "\\personagens\\6_5_ai_2.png")
label_ai = Label(janela, image=img_ai)
label_ai.place(x=1440, y=440)

# Cria uma caixa de texto para a entrada da quantidade de packs para ser comprado!
quantidade_packs = Entry(janela)
quantidade_packs.place(x=775, y=375)

# Criando o botão confirmar! Aciona a função número, que valida a entrada como INT
botao_confirmar = Button(janela, text="Confirmar?", command=lambda: numero(quantidade_packs, personagem_selecionado))
botao_confirmar.place(x=800, y=400)

# Criando o botão pra parar a música
botao_parar_musica = Button(janela, text="Stop/Play Music", command=lambda: parar_musica())
botao_parar_musica.place(x=1343, y=730)

janela.mainloop()
