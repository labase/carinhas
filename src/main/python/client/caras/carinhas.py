#! /usr/bin/env python
# -*- coding: UTF8 -*-
# Este arquivo é parte do programa Carinhas
# Copyright 2013-2014 Carlo Oliveira <carlo@nce.ufrj.br>,
# `Labase <http://labase.selfip.org/>`__; `GPL <http://is.gd/3Udt>`__.
#
# Carinhas é um software livre; você pode redistribuí-lo e/ou
# modificá-lo dentro dos termos da Licença Pública Geral GNU como
# publicada pela Fundação do Software Livre (FSF); na versão 2 da
# Licença.
#
# Este programa é distribuído na esperança de que possa ser  útil,
# mas SEM NENHUMA GARANTIA; sem uma garantia implícita de ADEQUAÇÃO
#  a qualquer MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a
# Licença Pública Geral GNU para maiores detalhes.
#
# Você deve ter recebido uma cópia da Licença Pública Geral GNU
# junto com este programa, se não, escreva para a Fundação do Software
# Livre(FSF) Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

"""
############################################################
Jogo das Carinhas - Principal
############################################################

Classe que define uma carinha e inicia o jogo com as carinhas embaralhadas.

"""
#from .tabuleiro import Tabuleiro
from random import random
URLS = [
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/c_a5.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/c_v1.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/c_a3.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/c_a2.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/c_v8.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/c_v7.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/c_v5.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/c_v6.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/c_v4.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/c_a7.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/c_v3.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/c_v2.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/c_a6.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/c_a8.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/c_a4.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/c_a1.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/e_v8.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/e_v7.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/e_v6.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/e_v5.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/e_v4.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/e_v3.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/e_v2.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/e_v1.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/e_a8.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/e_a7.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/e_a6.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/e_a3.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/e_a2.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/e_a1.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/e_a5.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/e_a4.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/g_a5.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/g_a4.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/g_a3.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/g_a2.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/g_a1.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/g_v8.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/g_v7.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/g_v6.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/g_v5.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/g_v4.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/g_v1.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/g_v3.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/g_v2.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/g_a8.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/g_a7.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/g_a6.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/blue_laco_brinco.png?disp=inline&size=G',
    'https://activufrj.nce.ufrj.br/studio/GamesInteligentesII/red_laco_brinco.png?disp=inline&size=G'     
]


class Carinhas:
    """Base do jogo com tabuleiro e carinhas."""
    def __init__(self, gui):
        """Constroi os objetos iniciais. """
        self.s = self.gui = self.tabuleiro = None
        self.urls = URLS
        self.d = 'https://activufrj.nce.ufrj.br/studio/Jogo_Carinhas/tabuleiro.png?disp=inline&size=G' 

    def numeros(self, quantidade, bonecos):
        lista = []
        for a, qnti in enumerate(quantidade):
            for b in range(qnti):
                lista.append(bonecos[a])
        return lista

    def shufle(self, lista):
        listainterna = lista[:]
        lista_saida = []
 
        while listainterna:
            indice_selecionado = int(random() * (len(listainterna)))
            elemento_selecionado = listainterna.pop(indice_selecionado)
            lista_saida.append(elemento_selecionado)
            lista = lista_saida[:]
        #print(lista_saida)
        return lista_saida
           
    def build_base(self, gui, svg):
        """Constroi as partes do Jogo. """
        p = gui['banner']
        self.s = svg.svg(width=800, height=500)
        p <= self.s
        self.gui = gui
        #self.build_tabuleiro(gui)
        self.build_carinhas(svg)
        
    def build_tabuleiro(self, gui, lista):
        """Constroi o tabuleiro onde as pecas sao jogadas."""
        self.tabuleiro = []  # Tabuleiro(gui)
        c = 0
        for i in range(12):
            interna = []
            for a in range(16):
                if (i < 2) or (i > 9):            
                    interna.append(gui.image(href=lista[c], x=a*50, y=i*50, width=50, height=50))  
                    self.s <= interna[a]
                    c += 1
                elif (i == 2) and (a == 0):
                    interna.append(gui.image(href=lista[c], x=a*50, y=i*50, width=50, height=50))  
                    self.s <= interna[a]
                    c += 1
                elif (i == 2) and (a == 1):
                    interna.append(gui.image(href=lista[c], x=a*50, y=i*50, width=50, height=50))  
                    self.s <= interna[a]
                    c += 1
                elif (a == 14) and (i == 2):
                    interna.append(gui.image(href=lista[c], x=a*50, y=i*50, width=50, height=50))  
                    self.s <= interna[a]
                    c += 1
                else:
                    interna.append(gui.image(href=self.d, x=a*50, y=i*50, width=50, height=50))  
                    self.s <= interna[a]
            self.tabuleiro.append(interna)
            
    def build_carinhas(self, gui):
        """Posiciona as carinhas onde as pecas se iniciam."""
        qnt = [3, 4, 4, 5, 5, 5, 4, 5, 5, 5, 5, 4, 2, 2, 4, 5]  # 67

        carinhas_ordenadas = self.numeros(qnt, self.urls)
        carinhas_embaralhadas = self.shufle(carinhas_ordenadas)
        self.build_tabuleiro(gui, carinhas_embaralhadas)

 
def main(doc, svg):
    print('Carinhas 0.1.0')
    carinhas = Carinhas(doc)
    carinhas.build_base(doc, svg)
