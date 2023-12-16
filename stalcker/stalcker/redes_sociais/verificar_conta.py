# redes_sociais/verificar_conta.py
import requests

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

def verifica_conta_plataforma(username, plataforma, resultados):
    url = f'https://{plataforma}.com/{username}/'
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()

        if resposta.status_code == 200:
            resultado = (f'{GREEN}[!]- {RESET}A conta {GREEN}@{username} {RESET}existe no {GREEN}{plataforma}{RESET}: {BLUE}{url}')
            print(f'[!]- {resultado}')
            resultados.append(resultado)
        else:
            resultado = (f'A conta @{username} não existe no {plataforma}.')
            print(f'[!]- {resultado}')
            resultados.append(resultado)
    except requests.exceptions.RequestException as e:
        resultado = (f'{RED}[!]- {RESET}A conta {RED}@{username} {plataforma}')
        print(f'[!]- {resultado}')
        resultados.append(resultado)
