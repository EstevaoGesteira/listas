notas = [7, 8.5, 6, 9, 5.5]

print(len(notas), sum(notas), max(notas), min(notas))

# len() Verifica quantos objetos temos dentro da lista.
# sum() Soma os objetos dentro da lista.
# max() Mostra o objeto de maior valor da lista.
# min() Mostra o objeto de menor valor da lista.

for nota in notas:
    if nota >= 6:
        print(nota, "Aprovado")