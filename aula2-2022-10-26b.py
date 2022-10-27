#Pede o nome do aluno e sua nota ( de 0 a 10) e, se ele tirou nota 10, mostra "{nome}Você é bichão, mesmo..."
nome = input("Informe seu nome: ")
nota = float(input("Digite sua nota: "))

if (nota == 10):
  print("{}, você é bichão, mesmo...".format(nome))
elif (nota >= 6 and nota < 10):
  print("{}, bom trabalho".format(nome))
else: # é sempre automaticamente o que as duas condiçoes não tratamento
  print("Animal,não tirou 10 KKKK")
