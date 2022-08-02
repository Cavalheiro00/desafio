from modules import utils

PATH_INI = "./desafio.ini"

def main():
    if utils.verify_if_file_exist(PATH_INI):
        configs = utils.read_ini_file(PATH_INI)  # Armazenando as informacoes do arquivo de entrada
        raw_html = utils.get_html(configs["default"]["url"]) # Carregando o conteudo apontando pelo parametro url
        text = utils.clean_html(raw_html).split("\n") # Transformando a string em uma lista sem tags html    
        formatted_text = utils.remove_multiple_line_breaks(text).replace("\n"," ") # Mantem apenas uma quebra de linha entre cada linha
        list_of_words = formatted_text.split(" ")  # Transformando a string em uma lista de palavras
        utils.search_words(list_of_words,configs) # Localiza as palavras com as combinacoes desejadas
    else:
        print('Arquivo INI nao existe!')

if __name__ == '__main__':
    main()