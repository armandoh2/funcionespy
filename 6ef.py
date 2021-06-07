# ejercicio 6 

def calculo_mcd(numero1,numero2):
	mcd = 1
	if numero1 % numero2 == 0:
		return numero2
	for k in range(int(numero2/2), 0, -1):
		if numero1 % k == 0 and numero2 % k == 0:
			mcd = k
			break
	return mcd


def calculo_mcm(numero1,numero2):

  if numero1 > numero2:
  	mayor = numero1
  else:
  	mayor = numero2
  while (mayor % numero1 != 0) or (mayor % numero2 != 0):
  		mayor += 1
  return mayor
