'''
Created on 17/08/2010

@author: matheus
'''

import pygtk
pygtk.require('2.0')
import gtk.glade

#Classe que implementa a Interface Princiapl
class Gui():

    #Construtor da classe
    def __init__(self):
        
        #Nome do arquivo Glade
        self.__glade_file = "../xml/interface.glade"
        gui = gtk.glade.XML(self.__glade_file)
        self.gui = gui
        
        main_window = gui.get_widget("janela_principal")
        main_window.connect("destroy", gtk.main_quit)
        
#        self.image = gui.get_widget('image_original')
#        self.image.set_from_file('imagem.jpg')
#        self.image.show()
#        
#        self.imagem = gui.get_widget('image_saida')
#        self.imagem.set_from_file('imagemcinza.jpg')
#        self.imagem.show()

        main_window.show_all()
        self.loop()        
    
    #Metodo da GTK
    def loop(self):
        gtk.main()