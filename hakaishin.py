import os
import random
import string
import time
import ctypes
from subprocess import run, DEVNULL
from colorama import init, Fore, Style
from pystyle import Center

# Função para gerar uma chave aleatória para o título
def gerar_titulo(tamanho):
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

# Configuração inicial
titulo = gerar_titulo(12)
ctypes.windll.kernel32.SetConsoleTitleW(titulo)
init(autoreset=True)

# Definição de mensagens formatadas
informacao = f"{Fore.RED}  [+] > {Style.RESET_ALL}"
prompt = f"{Fore.RED}[?]{Style.RESET_ALL} - "
arte = f"""                   
$$\   $$\  $$$$$$\  $$\   $$\  $$$$$$\  $$$$$$\  $$$$$$\  $$\   $$\ $$$$$$\ $$\   $$\ 
$$ |  $$ |$$  __$$\ $$ | $$  |$$  __$$\ \_$$  _|$$  __$$\ $$ |  $$ |\_$$  _|$$$\  $$ |
$$ |  $$ |$$ /  $$ |$$ |$$  / $$ /  $$ |  $$ |  $$ /  \__|$$ |  $$ |  $$ |  $$$$\ $$ |
$$$$$$$$ |$$$$$$$$ |$$$$$  /  $$$$$$$$ |  $$ |  \$$$$$$\  $$$$$$$$ |  $$ |  $$ $$\$$ |
$$  __$$ |$$  __$$ |$$  $$<   $$  __$$ |  $$ |   \____$$\ $$  __$$ |  $$ |  $$ \$$$$ |
$$ |  $$ |$$ |  $$ |$$ |\$$\  $$ |  $$ |  $$ |  $$\   $$ |$$ |  $$ |  $$ |  $$ |\$$$ |
$$ |  $$ |$$ |  $$ |$$ | \$$\ $$ |  $$ |$$$$$$\ \$$$$$$  |$$ |  $$ |$$$$$$\ $$ | \$$ |
\__|  \__|\__|  \__|\__|  \__|\__|  \__|\______| \______/ \__|  \__|\______|\__|  \__|

"""

# Arte e mensagens formatadas
arte_vermelha = f"{Fore.RED}{Style.DIM}{arte}"
prompt_confirmacao = f"{prompt}Você tem certeza que quer continuar? (S/N): "
acoes = [
    f"{informacao}Desativando ajuste automático de TCP...",
    f"{informacao}Limpando cache do resolvedor DNS...",
    f"{informacao}Registrando registros DNS...",
    f"{informacao}Reiniciando estado do Winsock...",
    f"{informacao}Reiniciando catálogo do Winsock...",
    f"{informacao}Redefinindo configuração de IP...",
    f"{informacao}Redefinindo conexão IPv4...",
    f"{informacao}Deletando logs de configuração do IPv4...",
    f"{informacao}Redefinindo conexão IPv6...",
    f"{informacao}Deletando logs de configuração do IPv6...",
    f'{informacao}Configurando interface "Wi-Fi" para DHCP...',
    f'{informacao}Configurando interface "Ethernet" para DHCP...',
    f'{informacao}Desativando interface "Ethernet"...',
    f'{informacao}Desativando interface "Wi-Fi"...',
    f'{informacao}Ativando interface "Ethernet"...',
    f'{informacao}Ativando interface "Wi-Fi"...',
    f"{informacao}Liberando endereço IP atual...",
    f"{informacao}Renovando conexão DHCP...",
    f"{informacao}Concluído!"
]

# Comandos para reset de rede
comandos_reset = [
    "netsh int tcp set global autotuninglevel=disabled",
    "ipconfig /flushdns",
    "ipconfig /registerdns",
    "netsh winsock reset",
    "netsh winsock reset catalog",
    "netsh int ip reset",
    "netsh interface ipv4 reset",
    "netsh int ipv4 reset reset.log",
    "netsh interface ipv6 reset",
    "netsh int ipv6 reset reset.log",
    'netsh interface ipv4 set address "Wi-Fi" dhcp',
    'netsh interface ipv4 set address "Ethernet" dhcp',
    'netsh interface set interface "Ethernet" admin=disable',
    'netsh interface set interface "Ethernet" admin=enable',
    'netsh interface set interface "Wi-Fi" admin=disable',
    'netsh interface set interface "Wi-Fi" admin=enable',
    "ipconfig /release",
    "ipconfig /renew"
]

def reset_rede():
    for i, comando in enumerate(comandos_reset):
        print(acoes[i])
        run(comando, stdout=DEVNULL, stderr=DEVNULL, shell=True)
        time.sleep(0.1)

    print(f"{acoes[-1]}\nRenovação da conexão DHCP concluída com sucesso!")
    input("Pressione qualquer tecla para sair.")
    exit()

def exibir_arte():
    os.system("cls")
    print(Center.XCenter(arte_vermelha))

# Execução principal
exibir_arte()
resposta = input(prompt_confirmacao).lower()

if resposta == "s":
    reset_rede()
elif resposta == "n":
    run("start https://discord.gg/U2Qrnk84Nf", stdout=DEVNULL, stderr=DEVNULL, shell=True)
    exit()
else:
    print("Resposta inválida!")
    time.sleep(0.777)
    exit()
