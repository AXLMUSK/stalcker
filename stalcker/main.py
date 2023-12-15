# main.py
from utils.cores import colorir_texto
from redes_sociais.verificar_conta import verifica_conta_plataforma
from redes_sociais.salvar_resultados import salvar_resultados
from colorama import Fore
import os

def buscar_redes_sociais():
    os.system('clear')
    username = input(f"{colorir_texto('Digite o nome de usuário: ', Fore.RED)}")

    plataformas = [
        'instagram', 'twitter', 'youtube', 'github', 'facebook',
        'br.linkedin', 'xvideos', 'tiktok', 'snapchat', 'reddit',
        'br.pinterest', 'flickr', 'pt.quora', 'mewe', 'vimeo', 'tumblr',
        'soundcloud', 'slack', 'medium', 'hackerrank', 'pinterest', 'whatsapp',
        'vine', 'skype', 'dribbble', 'behance', 'angel', 'goodreads', 'viber',
        'quizzes', 'mix', 'yelp', 'github', 'dailymotion', 'weheartit', 'ello',
        'lastfm', 'badoo', 'couchsurfing', 'aboutme', 'slideshare', 'bandsintown'
    ]

    resultados = []

    for plataforma in plataformas:
        verifica_conta_plataforma(username, plataforma, resultados)

    salvar_resultados(resultados)

if __name__ == "__main__":
    buscar_redes_sociais()
