Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Elberth Moraes
// Descrição   : Escreva um algoritmo, em forma de fluxograma básico,
// para a tarefa Preparar uma Xícara de Café Utilizando uma Máquina de Café
// Expresso que Utiliza Cápsulas de Café.
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