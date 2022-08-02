from pathlib import Path
import configparser
import re

import requests

# Regex para eliminar tags html 
# https://stackoverflow.com/questions/9662346/python-code-to-remove-html-tags-from-a-string
CLEANR = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});') 

# Funcao que verificar se o arquivo existe
def verify_if_file_exist(path_file):
    path = Path(path_file)
    return path.is_file()

# Funcao que faz a leitura do arquivo
def read_ini_file(path_file):
    config = configparser.ConfigParser()
    config.read(path_file)
    return config

# Funcao que faz o request da url 
def get_html(url):
    try:
        response = requests.get(url)
        if response.ok:
            return response.text
    except:
        return 'Não foi possivel fazer a requisição'

# Funcao regex que elimina as tags html
def clean_html(raw_html):
    return re.sub(CLEANR, '', raw_html) 

# Funcao que remove multiplas quebras de linha em sequencia
def remove_multiple_line_breaks(text):
    new_text = ""
    old_word = None

    # Mantendo apenas uma quebra de linha entre cada linha
    for word in text:
        if word != "":
            new_text+= word
            old_word = None
        if old_word == None and word == "":
            new_text+= "\n"
            old_word = ""
    print(new_text)
    return new_text

# Funcao que busca por palavras que comecam com o conteudo dos parametros inicio e fim
def search_words(list_of_words,configs):
    cont_word = 0
    found_words = []
    
    # Localizando todas as palavras que comecam com conteúdo do parâmetro inicio e terminem com o conteúdo do parâmetro fim
    for word in list_of_words:
        if word.lower().startswith(configs["default"]["inicio"]) and word.lower().endswith(configs["default"]["fim"]):
            cont_word+= 1
            found_words.append(word)
    print("A quantidade de palavras encontradas foi: ",cont_word)
    print("Lista de palavras encontradas:", found_words)