vendas = []
fiados = []
despesas = []

while True:
    print('\n1 - Adicionar vendas')
    print('2 - Adicionar fiados')
    print('3- Adicionar despesas')
    print('4 - Mostrar relatório')
    print('5 - Sair')
    opcao = input('Digite o número da opção:')

    if opcao == '1':
        valor = float(input('\nDigite o valor das vendas:'))
        vendas.append(float(valor))
        print(f'Vendas {len(vendas)} adicionadas: R${valor:.2f}')

    elif opcao == '2':
        rvalor = float(input('\nDigite o valor à receber:'))
        fiados.append(float(rvalor))
        print(f'Fiados {len(fiados)} adicionados: R${rvalor:.2f}')

    elif opcao == '3':
        custo = float(input('\nDigite os custos das despesas:'))
        despesas.append(float(custo))
        print(f'Despesas {len(despesas)} adicionadas: R${custo:.2f}')

    elif opcao == '4':
        print('\n----RELATÓRIO----')
        print('\nAqui está o seu relatório de hoje:')
        
        total_vendas = sum(vendas)
        total_fiados = sum(fiados)
        total_custos = sum(despesas)
        faturamento = total_vendas + total_fiados
        lucro = total_vendas - total_custos
        fechamento = total_vendas - total_custos

        print('\nVocê teve um total de:')
        print(f'R${faturamento:.2f} em vendas;')
        print(f'R${total_custos:.2f} em despesas;')
        print(f'R${lucro:.2f} em lucro líquido.')
        print()
        print('-' * 60)
        print('\nDados detalhados:')
        print(f'Faturamento: R${faturamento:.2f};')
        print(f'Vendas (pagas): R${total_vendas:.2f}')
        print(f'Fiados: R${total_fiados:.2f}')
        print(f'Despesas: R${total_custos:.2f}')
        print(f'Lucro: R${lucro:.2f}')
        print('\nVale ressaltar que os lançamentos futuros (fiados) não entram na conta do lucro, pois não teve entrada de caixa.')
        print()
        print('-' * 60)
        print('\n----FECHAMENTO----')
        print()
        print(f'Seu fechamento do dia é de: R${fechamento:.2f}')

    elif opcao == '5':
        print('\nSaindo...')
        break

    else:
        print('Digite uma opção válida!')