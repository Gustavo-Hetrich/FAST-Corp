from pynput.mouse import Button, Controller as mousecontrol
from pynput.keyboard import Key, Listener, Controller
import subprocess
import time
from colored import Fore, Back, Style

keyboard = Controller()
mouse = mousecontrol()

titulo = (rf""" {Fore.red}
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

{Style.reset}Framework de Assistência ao Suporte Técnico Corporativo """)

while True:
    print(titulo)
    inicio = input(f'\n Quer iniciar a configuração? \n (1) Checklist \n (2) Limpar Temps \n Favor digitar uma das opções \n \n')


    # Checklist
    if inicio == '1':
        modelo = input(f'\n Qual seria o modelo do notebook? \n (1)Acer (2)Outro (3...)Voltar \n Favor digitar uma das opções \n \n')
        # Acer
        if modelo == '1':
            print('Iniciando configuração do Acer')
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
           
            print('\n Checklist Concluido')
            

        # Outro
        if modelo == '2':
            # Atualização
            print('\n Atualizando Windows...')
            keyboard.press(Key.cmd)
            keyboard.release(Key.cmd)
            time.sleep(5)
            keyboard.type('atualizações')
            time.sleep(5)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            time.sleep(20)
            for i in range(0,3):
                keyboard.press(Key.tab)
                keyboard.release(Key.tab)
                time.sleep(1)
            time.sleep(5)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            time.sleep(10)
            # GPUPDATE
            print('\n Realizando GPUPDATE...')
            keyboard.press(Key.cmd)
            keyboard.release(Key.cmd)
            time.sleep(2)
            keyboard.type('gpupdate /force /boot /sync')
            time.sleep(2)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            time.sleep(20)
            # Ativação Administrador
            print('\n Ativando Administrador...')
            keyboard.press(Key.cmd)
            keyboard.press('r')
            time.sleep(2)
            keyboard.release(Key.cmd)
            keyboard.release('r')
            time.sleep(4)
            keyboard.tap(Key.backspace)
            keyboard.type('Y:\SUPORTE TECNICO\Corporativo\Macros\Bot Format\Ativador Admin')
            time.sleep(2)
            keyboard.press(Key.ctrl)
            keyboard.press(Key.shift)
            keyboard.press(Key.enter)
            keyboard.release(Key.ctrl)
            keyboard.release(Key.shift)
            keyboard.release(Key.enter)
            time.sleep(60)
            # Instalação Cortex, Global, Netskope
            print('\n Instalando Programas...')
            keyboard.press(Key.cmd)
            keyboard.press('r')
            time.sleep(2)
            keyboard.release(Key.cmd)
            keyboard.release('r')
            time.sleep(4)
            keyboard.tap(Key.backspace)
            keyboard.type('Y:\SUPORTE TECNICO\Corporativo\Macros\Bot Format\Rede\executar')
            time.sleep(4)
            keyboard.tap(Key.enter)
            print('\n Checklist Concluido')

    #Limpar Temps
    if inicio == '2':
        print('\nLimpando Temps...')
        keyboard.press(Key.cmd)
        keyboard.press('r')
        time.sleep(0.5)
        keyboard.release(Key.cmd)
        keyboard.release('r')
        time.sleep(2)
        keyboard.tap(Key.backspace)
        # https://stackoverflow.com/questions/10716803/batch-file-to-perform-start-run-temp-and-delete-all - fonte do Bat
        keyboard.type('Y:\SUPORTE TECNICO\Corporativo\Macros\Bot Format\Clear.bat')
        time.sleep(2)
        keyboard.press(Key.ctrl)
        keyboard.press(Key.shift)
        keyboard.press(Key.enter)
        keyboard.release(Key.ctrl)
        keyboard.release(Key.shift)
        keyboard.release(Key.enter)
        print('\nTemps limpas')

    print('\n')     
    print('-' * 50)
