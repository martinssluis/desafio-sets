funcionarios = ["Ana", "Marcos", "Alice", "Pedro", "Sophia", "Bruno", "Melissa"]
turno_dia = ["Ana", "Marcos", "Alice", "Melissa"]
turno_noite = ["Pedro", "Sophia", "Bruno"]
tem_carro = ["Marcos", "Alice", "Bruno","Melissa"]

lista1 = set(tem_carro).intersection(turno_noite)

lista2 = set(tem_carro).intersection(turno_dia)

lista3 = set(funcionarios).difference(tem_carro)