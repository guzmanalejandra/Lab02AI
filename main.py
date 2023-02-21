
from bayesiannetwork import *

def main():

  # Crear Network
  net = Network('EjemploMain')

  # Crear nodo 'Fuel'
  Fu = Node('Fu')

  # Asignando nombre y numero a los resultados
  Fu.addOutcome('yes')
  Fu.addOutcome('no')

  # Crear nodo 'Bujias limpias'
  SP = Node('SP')

  # Asignando nombre y numero a los resultados
  SP.addOutcomes(['yes','no'])

  # Crear nodo 'Medidor de combustible'
  FM = Node('FM')

  # Asignando nombre y numero a los resultados
  FM.addOutcomes(['full','half','empty'])

  # Crear nodo 'Start'
  St = Node('St')

  # Asignando nombre y numero a los resultados
  St.addOutcomes(['yes','no'])

  # Add arc 
  arc_Fu_FM = Arc(Fu,FM)


  arc_Fu_St = Arc(Fu,St)

  arc_SP_St = Arc(SP,St)




  # Distribucion condificonal para el nodo 
  Fu.setProbabilities([0.98,0.02])

  # Distribucion condificonal para el nodo 
  SP.setProbabilities([0.96,0.04])

  # Distribucion condificonal para el nodo 
  FM.setProbabilities([0.39, 0.60, 0.01, 0.001, 0.001, 0.998])

  # Distribucion condificonal para el nodo
  St.setProbabilities([0.99, 0.01, 0.01, 0.99, 0.0, 1.0, 0.0, 1.0])


  # Cambiando nodos y atributos visuales
  Fu.setNodePosition(100,10)

  SP.setNodePosition(300,10)

  FM.setNodePosition(0,150)
  FM.setInteriorColor('cc99ff')

  St.setNodePosition(200,150)
  St.setInteriorColor('ff0000')

  # Agregar nodos a la network
  net.addNodes([Fu,SP,FM,St])

  # Crear documento
  net.writeFile('Ejemplo.xdsl')

  # Evidencia
  net.setEvidence('FM',2)
  net.setEvidence('St',2)

  # Calcula las creencias
  net.computeBeliefs()

  # Imprime los resultados de cada nodo
  print('Fu', Fu.getBeliefs())
  print('SP', SP.getBeliefs())
  print('St', St.getBeliefs())
  print('FM', FM.getBeliefs())


if __name__ == '__main__':
  main()
