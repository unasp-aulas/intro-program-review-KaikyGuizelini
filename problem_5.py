def main(distancia):
  passagem = 0

  if distancia <= 200:
    passagem = distancia * 0.5
  elif distancia <= 400:
    passagem = distancia * 0.45
  else: 
    passagem = distancia * 0.35
  
  return passagem