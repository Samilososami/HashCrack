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
                    print(f'\rDeshasheando contraseÃ±a... {char}', end='', flush=True) 
                    time.sleep(0.1) 
        except KeyboardInterrupt: 
            print("\nCancelando...") 
            exit() 

    def detener(self): 
        self.ejecutar = False 

def crackear_hash(hash_a_crackear, diccionario, animacion): 
    try: 
        with open(diccionario, 'r', errors='ignore') as f: 
            for linea in f: 
                palabra = linea.strip() 
                hash_calculado = hashlib.md5(palabra.encode()).hexdigest() 
                if hash_calculado == hash_a_crackear: 
                    animacion.detener() 
                    return palabra 
        animacion.detener() 
        return None 
    except KeyboardInterrupt: 
        print("\nCancelando...") 
        exit() 

def main(): 
    init(autoreset=True) 
    print("==============================================") 
    print("|              MD5 HASH CRACKER              |") 
    print("|               by SamilosoSami              |") 
    print("==============================================") 
    hash_a_crackear = input("Introduce el hash que deseas " + Fore.YELLOW + "crackear" + Style.RESET_ALL + ": ") 
    diccionario = input("Introduce la ruta al " + Fore.YELLOW + "diccionario" + Style.RESET_ALL + ": ") 
    print("Iniciando proceso de " + Fore.YELLOW + "crackeo" + Style.RESET_ALL + "...") 
    animacion_crackeo = Animacion() 
    animacion_crackeo.start() 
    palabra_encontrada = crackear_hash(hash_a_crackear, diccionario, animacion_crackeo) 
    print("\nProceso de " + Fore.YELLOW + "crackeo" + Style.RESET_ALL + " finalizado.") 
    print("=============================================") 
    if palabra_encontrada: 
        print(f"|   La contraseÃ±a es: {Fore.GREEN}{palabra_encontrada}") 
    else: 
        print("|   No se encontrÃ³ la contraseÃ±a en el " + Fore.YELLOW + "diccionario" + Style.RESET_ALL + ".") 
    print("=============================================") 

if __name__ == "__main__": 
    main()