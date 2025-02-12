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
        return [aluno.nome for aluno in self.alunos]
    
    def listarProfessores(self):
        return [professor.nome for professor in self.professores]
    
    def add_aluno(self, aluno):
        self.alunos.append(aluno)
    
    def add_professor(self, professor):
        self.professores.append(professor)
    
    def melhorNota(self, ufcd=None, aluno=None):
        notas = []
        for a in self.alunos:
            if aluno and a != aluno:
                continue
            for u, nota in a.notas.items():
                if ufcd and u != ufcd:
                    continue
                notas.append(nota)
        return max(notas) if notas else None
    
    def piorNota(self, ufcd=None, aluno=None):
        notas = []
        for a in self.alunos:
            if aluno and a != aluno:
                continue
            for u, nota in a.notas.items():
                if ufcd and u != ufcd:
                    continue
                notas.append(nota)
        return min(notas) if notas else None
    
    def piorMedia(self, ufcd=None, aluno=None, aprovado=True):
        medias = []
        for a in self.alunos:
            if aluno and a != aluno:
                continue
            media = sum(a.notas.values()) / len(a.notas) if a.notas else 0
            if aprovado and media < 10:
                continue
            if not aprovado and media >= 10:
                continue
            medias.append((a.nome, media))
        return min(medias, key=lambda x: x[1]) if medias else None
    
    def melhorMedia(self, ufcd=None, aluno=None):
        medias = []
        for a in self.alunos:
            if aluno and a != aluno:
                continue
            media = sum(a.notas.values()) / len(a.notas) if a.notas else 0
            medias.append((a.nome, media))
        return max(medias, key=lambda x: x[1]) if medias else None



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