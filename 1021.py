valor = float(input()) 
valor_centavos = int(valor * 100)  

if 0 <= valor_centavos <= 100000000:
    print('NOTAS:')
    notas = [10000, 5000, 2000, 1000, 500, 200]  
    for nota in notas:
        qtd_notas = valor_centavos // nota
        valor_centavos %= nota
        print('{} nota(s) de R$ {:.2f}'.format(qtd_notas, nota / 100))

    print('MOEDAS:')
    moedas = [100, 50, 25, 10, 5, 1]
    for moeda in moedas:
        qtd_moedas = valor_centavos // moeda
        valor_centavos %= moeda
        print('{} moeda(s) de R$ {:.2f}'.format(qtd_moedas, moeda / 100))
