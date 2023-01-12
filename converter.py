from PIL import Image    # Importa a biblioteca Pillow e o módulo para a conversão.
import os        # Importa a função que permite o run do script.

list_images = os.listdir("images")       # Variável para armazenar as imagens.

for arquivo in list_images:        # Função para selecionar da primeira imagem até a última.
    imagem = Image.open(f"images/{arquivo}")     # Função para abrir cada imagem da pasta.

    imagem.save(f'svg/{arquivo.replace("png", "webp")}')      # Função para dar um replace junto com o save da imagem refatorada.
   