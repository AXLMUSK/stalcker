# redes_sociais/verificar_conta.py
import requests
from utils.cores import colorir_texto

def verifica_conta_plataforma(username, plataforma, resultados):
    url = f'https://{plataforma}.com/{username}/'
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()

        if resposta.status_code == 200:
            resultado = colorir_texto(f'A conta @{username} existe no {plataforma}: {url}', Fore.GREEN)
            print(f'[!]- {resultado}')
            resultados.append(resultado)
        else:
            resultado = colorir_texto(f'A conta @{username} não existe no {plataforma}.', Fore.RED)
            print(f'[!]- {resultado}')
            resultados.append(resultado)
    except requests.exceptions.RequestException as e:
        resultado = colorir_texto(f'Erro ao acessar {plataforma}: {e}', Fore.RED)
        print(f'[!]- {resultado}')
        resultados.append(resultado)
