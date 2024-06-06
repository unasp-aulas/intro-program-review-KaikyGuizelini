valor_casa = float(input("Qual o valor da casa? "))
salario = float(input("Qual é o salário? "))
anos_pagar = int(input("Pagar em quantos anos? "))

prestacao = valor_casa / anos_pagar * 12

if salario * 0.3 > prestacao:
  print("Reprovado")
else:
  print("Aprovado")