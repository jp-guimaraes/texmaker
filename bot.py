import subprocess


def criar_arquivo_auxiliar(nome,valor):
    f = open("automacao.tex", "w")
    nome = "\\newcommand{\\nomealuno}{" + nome_aluno + "}\n"
    valor = "\\newcommand{\\valorquestao}{" + valor_aluno + "}"
    f.write(nome)
    f.write(valor)
    f.close()


def gerar_pdf(nome_arquivo):
    aux = nome_arquivo = ".pdf"
    subprocess.run(["pdflatex", "main.tex"])
    subprocess.run(["mv", "main.pdf", aux])


lista_de_alunos = ["fulano", "cicrano", "beltrano"]
lista_de_valores = ["13", "47", "22"] 


cont = 0
N = len(lista_de_alunos)

print(N)
while (cont < N):
    nome_aluno = lista_de_alunos[cont]
    valor_aluno = str(lista_de_valores[cont])    
    criar_arquivo_auxiliar(nome_aluno,valor_aluno)  
    gerar_pdf(nome_aluno)
    cont = cont +1





