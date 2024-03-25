#!/usr/bin/env python3

import hashlib
import time
from threading import Thread
from colorama import init, Fore, Style

class Animacion(Thread):
    def __init__(self):
        super().__init__()
        self.ejecutar = True

    def run(self):
        try:
            while self.ejecutar:
                for char in "|/-\\":
                    print(f'\rDeshasheando contraseña... {char}', end='', flush=True)
                    time.sleep(0.1)
        except KeyboardInterrupt:
            print("\nCancelando...")
            exit()

    def detener(self):
        self.ejecutar = False

def detectar_tipo_hash(hash_a_crackear):
    tipos_hash = {
        32: 'md5',
        40: 'sha1',
        64: 'sha256',
        56: 'sha224',
        96: 'sha384',
        128: 'sha512',
    }
    longitud_hash = len(hash_a_crackear)
    if longitud_hash in tipos_hash:
        return tipos_hash[longitud_hash]
    else:
        return None

def crackear_hash(hash_a_crackear, diccionario, animacion):
    algoritmo = detectar_tipo_hash(hash_a_crackear)
    if algoritmo:
        try:
            with open(diccionario, 'r', errors='ignore') as f:
                for linea in f:
                    palabra = linea.strip()
                    if algoritmo == 'md5':
                        hash_calculado = hashlib.md5(palabra.encode()).hexdigest()
                    elif algoritmo == 'sha1':
                        hash_calculado = hashlib.sha1(palabra.encode()).hexdigest()
                    elif algoritmo == 'sha256':
                        hash_calculado = hashlib.sha256(palabra.encode()).hexdigest()
                    elif algoritmo == 'sha224':
                        hash_calculado = hashlib.sha224(palabra.encode()).hexdigest()
                    elif algoritmo == 'sha384':
                        hash_calculado = hashlib.sha384(palabra.encode()).hexdigest()
                    elif algoritmo == 'sha512':
                        hash_calculado = hashlib.sha512(palabra.encode()).hexdigest()
                    else:
                        print("Algoritmo de hash no válido.")
                        return None
                    if hash_calculado == hash_a_crackear:
                        animacion.detener()
                        return palabra
            animacion.detener()
            return None
        except KeyboardInterrupt:
            print("\nCancelando...")
            exit()
    else:
        print("Hash no encontrado.")
        return None

def main():
    init(autoreset=True)
    print("==============================================")
    print("|                HASH CRACKER                |")
    print("|               by SamilosoSami              |")
    print("==============================================")
    hash_a_crackear = input("Introduce el hash que deseas " + Fore.YELLOW + "crackear" + Style.RESET_ALL + ": ")
    diccionario = input("Introduce la ruta al " + Fore.YELLOW + "diccionario" + Style.RESET_ALL + ": ")
    print("\nDetectando hash...")
    time.sleep(1)  
    algoritmo = detectar_tipo_hash(hash_a_crackear)
    if algoritmo:
        print(f"Hash encontrado: {algoritmo.upper()}")
    else:
        print("Hash no encontrado.")
    print("\nIniciando proceso de " + Fore.YELLOW + "crackeo" + Style.RESET_ALL + "...")
    animacion_crackeo = Animacion()
    animacion_crackeo.start()
    palabra_encontrada = crackear_hash(hash_a_crackear, diccionario, animacion_crackeo)
    animacion_crackeo.detener()
    print("\nProceso de " + Fore.YELLOW + "crackeo" + Style.RESET_ALL + " finalizado.")
    print("=============================================")
    if palabra_encontrada:
        if palabra_encontrada.lower() == "terence":
            print(f"|   La contraseña es: {Fore.GREEN}{palabra_encontrada}")
            print(f"{Fore.BLUE}Hazme un truco y desaparece macho jeje")
        else:
            print(f"|   La contraseña es: {Fore.GREEN}{palabra_encontrada}")
    else:
        print("|   No se encontró la contraseña en el " + Fore.YELLOW + "diccionario" + Style.RESET_ALL + ".")
    print("=============================================")

if __name__ == "__main__":
    main()
