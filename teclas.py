import time
import win32api
import win32con


def click_esquerdo(numero_de_cliques):
    while numero_de_cliques > 0:
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        numero_de_cliques = numero_de_cliques - 1
        time.sleep(.1)


def teclado_enter(numero_de_cliques):
    while numero_de_cliques > 0:
        win32api.keybd_event(0x0D, 0, 0, 0)
        time.sleep(.1)
        win32api.keybd_event(0x0D, 0, win32con.KEYEVENTF_KEYUP, 0)
        numero_de_cliques = numero_de_cliques - 1
        time.sleep(.1)


def teclado_esc(numero_de_cliques):
    while numero_de_cliques > 0:
        win32api.keybd_event(0x1B, 0, 0, 0)
        time.sleep(.1)
        win32api.keybd_event(0x1B, 0, win32con.KEYEVENTF_KEYUP, 0)
        numero_de_cliques = numero_de_cliques - 1
        time.sleep(.1)


def teclado_cima(numero_de_cliques):
    while numero_de_cliques > 0:
        win32api.keybd_event(0x26, 0, 0, 0)
        time.sleep(.1)
        win32api.keybd_event(0x26, 0, win32con.KEYEVENTF_KEYUP, 0)
        numero_de_cliques = numero_de_cliques - 1
        time.sleep(.1)


def teclado_baixo(numero_de_cliques):
    while numero_de_cliques > 0:
        time.sleep(.2)
        win32api.keybd_event(0x28, 0, 0, 0)
        time.sleep(.1)
        win32api.keybd_event(0x28, 0, win32con.KEYEVENTF_KEYUP, 0)
        numero_de_cliques = numero_de_cliques - 1
        time.sleep(.1)


def teclado_esquerda(numero_de_cliques):
    while numero_de_cliques > 0:
        win32api.keybd_event(0x25, 0, 0, 0)
        time.sleep(.1)
        win32api.keybd_event(0x25, 0, win32con.KEYEVENTF_KEYUP, 0)
        numero_de_cliques = numero_de_cliques - 1
        time.sleep(.1)


def teclado_direita(numero_de_cliques):
    while numero_de_cliques > 0:
        win32api.keybd_event(0x27, 0, 0, 0)
        time.sleep(.1)
        win32api.keybd_event(0x27, 0, win32con.KEYEVENTF_KEYUP, 0)
        numero_de_cliques = numero_de_cliques - 1
        time.sleep(.1)
