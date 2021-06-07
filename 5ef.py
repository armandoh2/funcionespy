#ejercicio 5 calculo estadistico

def calculo_estadistico(listade):
  rmedia = (listade[0] + listade[1] + listade[2] + listade[3] + listade[4])/5
  rvarianza = (((listade[0] - rmedia)**2) + ((listade[1] - rmedia)**2) + ((listade[2] - rmedia)**2) + ((listade[3] - rmedia)**2) + ((listade[4] - rmedia)**2))/5
  rdesviacion = (rvarianza**(0.5))
  diccionariode = {'media':rmedia, 'varianza':rvarianza, 'desviacion':rdesviacion}

  print (f"La media de los números ingresados es {diccionariode['media']}")
  print (f"La varianza de los números ingresados es {diccionariode['varianza']}")
  print (f"La desviación estandar de los números ingresados es {diccionariode['desviacion']}")

  return
