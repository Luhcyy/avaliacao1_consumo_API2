import os
import platform

def clearScreen():
    """
    Limpa a tela do terminal.
    """
    # Detecta o sistema operacional
    system = platform.system()
    
    if system == 'Windows':
        os.system('cls')  # Comando para Windows
    else:
        os.system('clear')  # Comando para Unix (Linux, macOS)
