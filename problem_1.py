def main(cargo, salario):
  if cargo.lower() == 'junior':
    salario = salario * 1.15
  elif cargo.lower() == 'pleno':
    salario = salario * 1.26
  elif cargo.lower() == 'senior':
    salario = salario * 1.34
  else:
    salario = -1
  return salario