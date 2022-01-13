import subprocess

nome_aluno = "fulano"
valor_aluno = str(47)


f = open("automacao.tex", "w")
nome = "\\newcommand{\\nomealuno}{" + nome_aluno + "}\n"
valor = "\\newcommand{\\valorquestao}{" + valor_aluno + "}"
f.write(nome)
f.write(valor)
f.close()


subprocess.run(["pdflatex", "main.tex"])