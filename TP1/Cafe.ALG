Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Elberth Moraes
// Descri��o   : Escreva um algoritmo, em forma de fluxograma b�sico,
// para a tarefa Preparar uma X�cara de Caf� Utilizando uma M�quina de Caf�
// Expresso que Utiliza C�psulas de Caf�.
// Autor(a)    : Lucas PAgliarini
// Data atual  : 06/03/2022
Var
xicara :caracter


Inicio
procedimento fazerCafe()
 inicio
  escreval ("Pegar a xicara")
  escreval ("botar a xicara na maquina")
  escreval ("pegar a capsula")
  escreval ("inserir a capsula na maquina")
  escreval ("pressionar o botao de ligar")
  escreval ("esperar a agua esquentar")
  escreval ("esperar a maquina encher a xicara")

  xicara <- "cheia"
fimprocedimento
  xicara <- "vazia"
escreval (" A xicara esta " ,xicara)
fazerCafe()
escreval (" A xicara esta " ,xicara)



Fimalgoritmo