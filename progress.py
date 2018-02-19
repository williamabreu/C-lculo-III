arq = open('readme.md')
lista = []

for line in arq:
	if line[0] == '>':
		lista.extend(line[1:-1].split(', '))

arq.close()

pronto = sum([1 for i in lista if '__' in i])
total = len(lista)

print('{} done'.format(pronto))
print('{} missing'.format(total-pronto))
print('Progress: {:.2f}%'.format(100*pronto/total))
