'''
Created on 17/08/2010

@author: matheus
'''
from ImageManager import ImageManager
from Interface import Gui

if __name__ == '__main__':
#    Gui()
    
    imageManager = ImageManager()
    
    file_path_origem = "imagemOrigem.jpg"
    file_path_cinza = "modificada_escala_cinza.png"
    file_path_binaria = "modificada_limiarizao_global_simples.png"
    file_path_binaria1 = "imagem1.PNG"
    file_path_binaria2 = "imagem2.PNG"
    limiar_t = 125
    
#    imageManager.escala_cinza(file_path_origem)
#    imageManager.histograma_escala_cinza(file_path_cinza)
#    imageManager.histograma_rgb(file_path_origem)
#    imageManager.limiarizacao_global_simples(file_path_binaria, limiar_t)
#    imageManager.limiarizacao_diversas_variaveis(file_path_origem, limiar_t)
#    imageManager.operacao_aritmetica_adicao(file_path_origem, file_path_origem)
#    imageManager.operacao_aritmetica_subtracao(file_path_origem, file_path_origem)
#    imageManager.operacao_aritmetica_multiplicacao(file_path_origem, file_path_origem)
    imageManager.operacao_logica_and(file_path_binaria1, file_path_binaria2)
    imageManager.operacao_logica_or(file_path_binaria1, file_path_binaria2)
    imageManager.operacao_logica_xor(file_path_binaria1, file_path_binaria2)