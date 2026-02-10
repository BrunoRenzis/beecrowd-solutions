line1 = input().split()

code1 = int(line1[0])
qtd1 = int(line1[1])
priceU1 = float(line1[2])

line2 = input().split()

code2 = int(line2[0])
qtd2 = int(line2[1])
priceU2 = float(line2[2])

ValorAPagar = (qtd1 * priceU1) + (qtd2 * priceU2)

print("VALOR A PAGAR: R$ %.2f"% ValorAPagar)