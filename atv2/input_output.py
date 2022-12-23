arquivo = open("palavras.txt", "w")
arquivo.write("Morango\n")
arquivo.write("Manga\n")

arquivo.close()

#with fecha automaticamente o arquivo, sem ser necessário a apliacação do comando .close()
with open("palavras.txt") as arquivo:
    for linha in arquivo:
        print(linha)