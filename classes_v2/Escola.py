#######################################
# Codigo feito por: Gonçalo Feliciano #
#     Fork feito por: ShovCkOk        #
#            Data: 02/2025            #
#######################################


"""
from dataclasses import dataclass
from modelos import *

class Escola:

    def __init__(self,
                 nome: str,
                 lista_alunos: list[Aluno] = [],
                 lista_professores: list[Professor] = []
                 ):
        self.__nome = nome
        self.lista_alunos = lista_alunos
        self.lista_professores = lista_professores
        self.__melhorNota = None
        self.__piorNota = None

    def __update_melhorNota(self, nota:Nota, aluno:Aluno):
        if self.__melhorNota is None:
            self.__melhorNota = (aluno, nota)
            return

        if self.__melhorNota[1].nota < nota.nota:
            self.__melhorNota = (aluno, nota)


    def __update_piorNota(self, nota: Nota, aluno: Aluno):
        if self.__melhorNota is None:
            self.__melhorNota = (aluno, nota)
            return

        if self.__melhorNota[1].nota < nota.nota:
            self.__melhorNota = (aluno, nota)



    def __updateTops(self, nota:Nota, aluno:Aluno):
        self.__update_melhorNota(nota, aluno)
        self.__update_piorNota(nota, aluno)



    def listarAlunos(self):
        pass

    def listarProfessores(self):
        pass

    def add_aluno(self, aluno:Aluno):
        pass

    def add_professor(self, professor:Professor):
        pass

    def melhorNota(self, ufcd:str = None, aluno:Aluno = None):
        pass

    def piorNota(self, ufcd:str = None, aluno:Aluno = None):
        pass



    def piorMedia(self, ufcd: str = None, aluno: Aluno = None, aprovado:bool = True):
    
        ###################################################
        #    Lista os alunos com pior media               #
        #                                                 #
        #   :param aporvado:                              #
        #       - True para listar os alunos aprovados,   #
        #       - False para listar os alunos reprovados, #
        #                                                 #
        #   um Aluno aprovado e um aluno com media >= 10  #
        ###################################################
        pass

    def melhorMedia(self, ufcd: str = None, aluno: Aluno = None):
        pass


    def __int__(self):

        return len(self.lista_alunos)
        #return self.lista_alunos.__len__()



    def lancarNota(self,
                   nota:float,
                   ufcd:str ,
                   aluno:Aluno,
                   professor:Professor
                   ):
        nota = Nota(ufcd, nota, professor)
        aluno.add_notas(nota)

        # a nota e sempre bem add

        self.__updateTops(nota, aluno)



e = Escola("Escola 1")

e.listarAlunos()
"""

from modelos import Aluno, Professor, Nota

class Escola:

    def __init__(self, nome: str, lista_alunos=None, lista_professores=None):
        self.__nome = nome
        self.lista_alunos = lista_alunos if lista_alunos else []
        self.lista_professores = lista_professores if lista_professores else []
        self.__melhorNota = None
        self.__piorNota = None

    def __update_melhorNota(self, nota:Nota, aluno:Aluno):
        if self.__melhorNota is None or self.__melhorNota[1].nota < nota.nota:
            self.__melhorNota = (aluno, nota)

    def __update_piorNota(self, nota: Nota, aluno: Aluno):
        if self.__piorNota is None or self.__piorNota[1].nota > nota.nota:
            self.__piorNota = (aluno, nota)

    def __updateTops(self, nota:Nota, aluno:Aluno):
        self.__update_melhorNota(nota, aluno)
        self.__update_piorNota(nota, aluno)

    def listarAlunos(self):
        return self.lista_alunos

    def listarProfessores(self):
        return self.lista_professores
    
    def add_aluno(self, aluno: Aluno):
        self.lista_alunos.append(aluno)

    def add_professor(self, professor: Professor):
        self.lista_professores.append(professor)
    
    def melhorNota(self, ufcd=None, aluno=None):
        notas = []
        for a in self.lista_alunos:
            if aluno and a != aluno:
                continue
            for nota in a.notas:
                if ufcd and nota.ufcd != ufcd:
                    continue
                notas.append(nota)
        return max(notas, key=lambda x: x.nota) if notas else None
    
    def piorNota(self, ufcd=None, aluno=None):
        notas = []
        for a in self.lista_alunos:
            if aluno and a != aluno:
                continue
            for nota in a.notas:
                if ufcd and nota.ufcd != ufcd:
                    continue
                notas.append(nota)
        return min(notas, key=lambda x: x.nota) if notas else None

    def piorMedia(self, ufcd=None, aluno=None, aprovado=True):
        medias = []
        for a in self.lista_alunos:
            if aluno and a != aluno:
                continue
            media = a.calcularMedia()
            if aprovado and media < 10:
                medias.append((a.nome, media))
            if not aprovado and media >= 10:
                medias.append((a.nome, media))
        return min(medias, key=lambda x: x[1]) if medias else None
    
    def melhorMedia(self, ufcd=None, aluno=None):
        medias = []
        for a in self.lista_alunos:
            if aluno and a != aluno:
                continue
            media = a.calcularMedia()
            medias.append((a.nome, media))
        return max(medias, key=lambda x: x[1]) if medias else None

    def lancarNota(self, nota:float, ufcd:str , aluno: Aluno, professor: Professor):
        nota_obj = Nota(ufcd, nota, professor)
        aluno.add_notas(nota_obj)
        self.__updateTops(nota_obj, aluno)

    def __int__(self):
        return len(self.lista_alunos)