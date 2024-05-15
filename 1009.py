nome = input('')
salario = float(input())
total_vendas = float(input())
bonus = total_vendas*0.15
salario_final = salario+bonus
print('TOTAL = R$ {:.2f}'.format(salario_final))