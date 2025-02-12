"""

app que premite add alunos
    calcular a media de cada aluno
    listar alunos
    Mostrar melhor e pior nota
    registar notas de alunos
    deve ser possivel saber que professor deu a nota


escola
    lista Alunos
    Lista de professores

    listar_alunos()
    melhor_nota(UFCD)
    pior_nota(UFCD)

    registar notas de alunos(aluno, professor, nota)


nota
    nota
    UFCD
    professor

registar Alunos
    nome
    email
    turma
    lista de notas
    calc_media()

registar professores
    nome
    email

"""


from Escola import Escola
from modelos import Aluno, Professor

escola = Escola('Escola Secundária de Vila Nova de Gaia')

def menu():
    while True:
        print("\nEscolha uma opção:")
        print("1 - Adicionar Aluno")
        print("2 - Adicionar Professor")
        print("3 - Lançar Nota")
        print("4 - Listar Alunos")
        print("5 - Listar Professores")
        print("6 - Melhor Nota")
        print("7 - Pior Nota")
        print("8 - Melhor Média")
        print("9 - Pior Média")
        print("10 - Sair")
        
        opcao = input("Opção: ")
        
        if opcao == "1":
            nome_aluno = input("Digite o nome do aluno: ")
            email_aluno = input("Digite o email do aluno: ")
            turma_aluno = input("Digite a turma do aluno: ")
            aluno = Aluno(nome=nome_aluno, email=email_aluno, turma=turma_aluno, notas=[])
            escola.add_aluno(aluno)
            print(f"Aluno {nome_aluno} adicionado.")
        
        elif opcao == "2":
            nome_professor = input("Digite o nome do professor: ")
            email_professor = input("Digite o email do professor: ")
            professor = Professor(nome=nome_professor, email=email_professor)
            escola.add_professor(professor)
            print(f"Professor {nome_professor} adicionado.")
        
        elif opcao == "3":
            nome_aluno = input("Digite o nome do aluno: ")
            aluno = next((a for a in escola.lista_alunos if a.nome == nome_aluno), None)
            if aluno:
                nome_professor = input("Digite o nome do professor: ")
                professor = next((p for p in escola.lista_professores if p.nome == nome_professor), None)
                if professor:
                    ufcd = input("Digite a UFCD: ")
                    try:
                        nota = float(input("Digite a nota: "))
                        escola.lancarNota(nota, ufcd, aluno, professor)
                        print(f"Nota de {nota} lançada para {aluno.nome}.")
                    except ValueError:
                        print("Nota inválida!")
                else:
                    print("Professor não encontrado.")
            else:
                print("Aluno não encontrado.")
        
        elif opcao == "4":
            alunos = escola.listarAlunos()
            if alunos:
                print("Lista de Alunos:")
                for aluno in alunos:
                    print(f"{aluno.nome} - {aluno.turma} - {aluno.email}")
            else:
                print("Nenhum aluno cadastrado.")
        
        elif opcao == "5":
            professores = escola.listarProfessores()
            if professores:
                print("Lista de Professores:")
                for professor in professores:
                    print(f"{professor.nome} - {professor.email}")
            else:
                print("Nenhum professor cadastrado.")
        
        elif opcao == "6":
            melhor_nota = escola.melhorNota()
            if melhor_nota:
                print(f"A melhor nota é {melhor_nota.nota} de {melhor_nota.aluno.nome} em {melhor_nota.ufcd}.")
            else:
                print("Nenhuma nota registrada.")
        
        elif opcao == "7":
            pior_nota = escola.piorNota()
            if pior_nota:
                print(f"A pior nota é {pior_nota.nota} de {pior_nota.aluno.nome} em {pior_nota.ufcd}.")
            else:
                print("Nenhuma nota registrada.")
        
        elif opcao == "8":
            melhor_media = escola.melhorMedia()
            if melhor_media:
                print(f"A melhor média é de {melhor_media[0]} com média {melhor_media[1]:.2f}.")
            else:
                print("Nenhum aluno registrado.")
        
        elif opcao == "9":
            pior_media = escola.piorMedia()
            if pior_media:
                print(f"A pior média é de {pior_media[0]} com média {pior_media[1]:.2f}.")
            else:
                print("Nenhum aluno registrado.")
        
        elif opcao == "10":
            print("Saindo...")
            break
        
        else:
            print("Opção inválida!")

# Iniciar o menu
if __name__ == "__main__":
    menu()


