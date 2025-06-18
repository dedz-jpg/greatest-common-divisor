# Greatest Common Divisor (GCD) Calculator

Este projeto tem como objetivo calcular o **Máximo Divisor Comum (GCD)** entre dois números inteiros, utilizando Python.

---

## O que é GCD (Máximo Divisor Comum)?

O GCD de dois números é o maior número que divide os dois ao mesmo tempo.

### Exemplos:

- GCD(8, 12) → 4
- GCD(8, 24) → 8
- GCD(9, 11) → 1
- GCD(6, 4) → 2

---

## Lógica utilizada:

O algoritmo faz o seguinte:

1. Lê os dois números (A e B) informados pelo usuário.
2. Define o menor valor entre A e B (já que o GCD nunca pode ser maior que o menor dos dois números).
3. Cria um laço que vai de 1 até o menor número.
4. Em cada passo, verifica se o número atual (`i`) é divisor de **ambos**.
5. Se for, atualiza o valor de `gcd`.
6. No final, exibe o GCD encontrado.

---

## Exemplo de execução:

### Exemplo 1:

**Entrada:**
A = 8
B = 12

**Saída:**
O Máximo Divisor Comum (GCD) entre 8 e 12 é: 4

### Exemplo 2:

**Entrada:**
A = 6
B = 4


**Saída:**
O Máximo Divisor Comum (GCD) entre 6 e 4 é: 2

---

## Motivação:

Este projeto foi feito como parte dos meus estudos de **Lógica de Programação**, dentro do curso **Coding Essentials – Logic Building for Beginners (Udemy)**.  
Meu foco foi treinar **estruturas de repetição**, **condicionais** e **operações matemáticas** em Python.

---

## Tecnologias usadas:

- Python 3.x

---

## Sobre mim:

Sou André Ricardo, estudante em transição de carreira para a área de Tecnologia da Informação.  
Atualmente focado em aprender **lógica de programação**, **Python** e áreas como **Inteligência Artificial** e **Hardware**.
