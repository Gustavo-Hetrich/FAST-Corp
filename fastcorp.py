from pynput.mouse import Button, Controller as mousecontrol
from pynput.keyboard import Key, Listener, Controller
import subprocess
import time

keyboard = Controller()
mouse = mousecontrol()

titulo = (r"""
    ______           __ 
   / ____/___ ______/ /_
  / /_  / __ `/ ___/ __/
 / __/ / /_/ (__  ) /_  
/_/    \__,_/____/\__/                         
   ______               
  / ____/___  _________ 
 / /   / __ \/ ___/ __ \
/ /___/ /_/ / /  / /_/ /
\____/\____/_/  / .___/ 
               /_/      

Framework de Assistência ao Suporte Técnico Corporativo""")


def on_release(key):
    
    if key == Key.esc:
        print('parando configuração')
        return False
while True:
    print(titulo)
    inicio = input(f'\n Quer iniciar a configuração? \n (1) Checklist \n favor digitar uma das opções \n \n')

    if inicio == '1':
        print('\n começando configuração')

        # Atualização
        print('\n Atualizando Windows...')
        keyboard.press(Key.cmd)
        keyboard.release(Key.cmd)
        time.sleep(0.5)
        keyboard.type('atualizações')
        time.sleep(0.5)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(3)
        for i in range(0,3):
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)
            time.sleep(0.5)
        time.sleep(2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(5)
        # GPUPDATE
        print('\n Realizando GPUPDATE...')
        keyboard.press(Key.cmd)
        keyboard.release(Key.cmd)
        time.sleep(0.5)
        keyboard.type('gpupdate /force /boot /sync')
        time.sleep(0.5)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(10)
        # Ativação Administrador
        print('\n Ativando Administrador...')
        keyboard.press(Key.cmd)
        keyboard.press('r')
        time.sleep(0.5)
        keyboard.release(Key.cmd)
        keyboard.release('r')
        time.sleep(1)
        keyboard.tap(Key.backspace)
        keyboard.type('Y:\SUPORTE TECNICO\Corporativo\Macros\Bot Format\Ativador Admin')
        time.sleep(0.5)
        keyboard.press(Key.ctrl)
        keyboard.press(Key.shift)
        keyboard.press(Key.enter)
        keyboard.release(Key.ctrl)
        keyboard.release(Key.shift)
        keyboard.release(Key.enter)
        time.sleep(30)
        # Instalação Cortex, Global, Netskope
        print('\n Instalando Programas...')
        keyboard.press(Key.cmd)
        keyboard.press('r')
        time.sleep(0.5)
        keyboard.release(Key.cmd)
        keyboard.release('r')
        time.sleep(2)
        keyboard.tap(Key.backspace)
        keyboard.type('Y:\SUPORTE TECNICO\Corporativo\Macros\Bot Format\Rede\executar')
        time.sleep(2)
        keyboard.tap(Key.enter)
        time.sleep(0.5)
        mouse.position = (1103, 605)
        mouse.press(Button.left)
        mouse.release(Button.left)
        keyboard.tap(Key.down)
        keyboard.tap(Key.up)
        keyboard.tap(Key.enter)
        print('\n Checklist Concluido')
        print('-' * 50)

     
