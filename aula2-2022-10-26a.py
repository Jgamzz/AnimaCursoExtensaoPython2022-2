# comando input(): quero permitir que
# o usuário digite algo...
nome = input("Digite seu nome: ")
#pede a idade para o usuário "Qual sua idade?"
idade = int(input("\nDigite sua idade: "))

#comando de saída..exibir na tela
print(f"\nBoa noite, seu nome é {nome}")
#exiba "Sua idade é ..."
print("\nSua idade é {}".format(idade))

#e se eu quisesse mostrar o DOBRO da idade informada?
dobro = idade * 2
print("\nO dobro da idade informada é {}".format(dobro))

#Estrutura condicional - o famoso "SE" (if)
#Se a pessoa for maior de idade, mostre           "Você é maior de idade, ótimo! Já pode beber ou dirigir"
if idade >= 18:
  print("\nVocê é maior de idade, ótimo! Já pode beber ou dirigir")
else:
  print("\nInfelizmente você ainda é menor de idade. Que pena, você não pode beber ou dirigir")

# E se eu quissesem perguntar o gênero (M = masculino e F= Feminino)                                         
#Mostre (... e voce também precisa/precisou prestar o serviço militar obrigatório)
genero= input("\nInforme o gênero M=Masculino, F=Feminino, O=Outros") 
if idade >=18 and genero =="M":
  print("\n\n... e você também precisa/precisou prestar o serviço militar obrigatório")
  



print("Vai ser executada de qualquer jeito")  