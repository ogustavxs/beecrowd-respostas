valor = int(input())
if 0 < valor < 1000000:
    print(valor)
    nota100 = valor // 100
    print('{} nota(s) de R$ 100,00'.format(nota100))
    nota50 = (valor-(nota100*100)) // 50
    print('{} nota(s) de R$ 50,00'.format(nota50))
    nota20 = ((valor-(nota100*100))-nota50*50) // 20
    print('{} nota(s) de R$ 20,00'.format(nota20))
    nota10 = (((valor-(nota100*100))-nota50*50)-nota20*20) // 10
    print('{} nota(s) de R$ 10,00'.format(nota10))
    nota5 = ((((valor-(nota100*100))-nota50*50)-nota20*20)-nota10*10) // 5
    print('{} nota(s) de R$ 5,00'.format(nota5))
    nota2 = (((((valor-(nota100*100))-nota50*50)-nota20*20)-nota10*10)-nota5*5) // 2
    print('{} nota(s) de R$ 2,00'.format(nota2))
    nota1 = ((((((valor-(nota100*100))-nota50*50)-nota20*20)-nota10*10)-nota5*5)-nota2*2) // 1
    print('{} nota(s) de R$ 1,00'.format(nota1))