re = []
for i in range(4):
  nome = input("Qual seu nome ?")
  idade = input("Qual sua idade?")
  print("para avaliar o atendimento aperte: 1.exelente.   2. bom.   3. ruim.")
  pasta = int(input("Como foi seu atendimento?"))
  re.append(pasta)
q1 = re.count(3)
q2 = re.count(2)
q3 = re.count(1)
print(f"O número de exelentes foi {q1}, de bom foi {q2} e de ruim foi {q3}.")
