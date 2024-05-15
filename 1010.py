entrada = input().split(' ')
entrada2 = input().split(' ')
valor1 = int(entrada[1]) * float(entrada[2])
valor2 = int(entrada2[1]) * float(entrada2[2])
total = valor1 + valor2
print('VALOR A PAGAR: R$ {:.2f}'.format(total))