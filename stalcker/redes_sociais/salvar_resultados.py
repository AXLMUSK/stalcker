# redes_sociais/salvar_resultados.py
def salvar_resultados(resultados):
    with open('resultados_redes_sociais.txt', 'w') as arquivo:
        for resultado in resultados:
            arquivo.write(resultado + '\n')
