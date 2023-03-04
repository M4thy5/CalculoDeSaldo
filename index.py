

nome = str(input("Qual o seu nome completo ou o nome e sobrenome? ")).strip()
nome = nome.title()
if 'M'[0] in nome:
  print("Seja muito bem vindo(a)! {} {}, vamos fazer os cálculos.".format(nome.split()[0], nome.split()[1]))
elif 'G'[0] in nome: 
  print("Seja muito bem vindo(a)! {} {}, vamos fazer os cálculos.".format(nome.split()[0], nome.split()[1]))
else:
  print("Bem-vindo(a)!")
saldo = float(input("Saldo no banco: "))
prejuizo = int(input("Quantos itens/prejuízos você tem para pagar? "))

if prejuizo == 1:
  pv1 = float(input("Valor do 1° iten/prejuízo: "))
  pvt = pv1
  pvtr = saldo - pvt
  print("Seu prejuízo será de R${}".format(pvt))
  print("Seu saldo é de R${} e ficará R${}".format(saldo, pvtr))
  if pvtr <= 0:
    print("Seu saldo está negativo (R${})".format(pvtr))
  else:
    print("Seu saldo está positivo (R${}).".format(pvtr))
if prejuizo == 2:
  pv1 = float(input("Valor do 1° iten/prejuízo: "))
  pv2 = float(input("Valor do 2° iten/prejuízo: "))
  pvt = pv1 + pv2
  pvtr = saldo - pvt
  print("Seu prejuízo será de R${}".format(pvt))
  print("Seu saldo é de R${} e ficará R${}".format(saldo, pvtr))
  if pvtr <= 0:
    print("Seu saldo está negativo (R${})".format(pvtr))
  else:
    print("Seu saldo está positivo (R${}).".format(pvtr))
if prejuizo == 3: 
  pv1 = float(input("Valor do 1° iten/prejuízo: "))
  pv2 = float(input("Valor do 2° iten/prejuízo: "))
  pv3 = float(input("Valor do 3° iten/prejuízo: "))
  pvt = pv1 + pv2 + pv3
  pvtr = saldo - pvt
  print("Seu prejuízo será de R${}".format(pvt))
  print("Seu saldo é de R${} e ficará R${}".format(saldo, pvtr))
  if pvtr <= 0:
    print("Seu saldo está negativo (R${})".format(pvtr))
  else:
    print("Seu saldo está positivo ({}).".format(pvtr))
if prejuizo == 4: 
  pv1 = float(input("Valor do 1° iten/prejuízo: "))
  pv2 = float(input("Valor do 2° iten/prejuízo: "))
  pv3 = float(input("Valor do 3° iten/prejuízo: "))
  pv4 = float(input("Valor do 4° iten/prejuízo: "))
  pvt = pv1 + pv2 + pv3 + pv4
  pvtr = saldo - pvt
  print("Seu prejuízo será de R${}".format(pvt))
  print("Seu saldo é de R${} e ficará R${}".format(saldo, pvtr))
  if pvtr <= 0:
    print("Seu saldo está negativo (R${}).".format(pvtr))
  else:
    print("Seu saldo está positivo (R${}).".format(pvtr))
if prejuizo == 5: 
  pv1 = float(input("Valor do 1° iten/prejuízo: "))
  pv2 = float(input("Valor do 2° iten/prejuízo: "))
  pv3 = float(input("Valor do 3° iten/prejuízo: "))
  pv4 = float(input("Valor do 4° iten/prejuízo: "))
  pv5 = float(input("Valor do 5° iten/prejuízo: "))
  pvt = pv1 + pv2 + pv3 + pv4 + pv5
  pvtr = saldo - pvt
  print("Seu prejuízo será de R${}".format(pvt))
  print("Seu saldo é de R${} e ficará R${}".format(saldo, pvtr))
  if pvtr <= 0:
    print("Seu saldo está negativo (R${}).".format(pvtr))
  else:
    print("Seu saldo está positivo (R${}).".format(pvtr))
if prejuizo == 6: 
  pv1 = float(input("Valor do 1° iten/prejuízo: "))
  pv2 = float(input("Valor do 2° iten/prejuízo: "))
  pv3 = float(input("Valor do 3° iten/prejuízo: "))
  pv4 = float(input("Valor do 4° iten/prejuízo: "))
  pv5 = float(input("Valor do 5° iten/prejuízo: "))
  pv6 = float(input("Valor do 6° iten/prejuízo: "))
  pvt = pv1 + pv2 + pv3 + pv4 + pv5 + pv6
  pvtr = saldo - pvt
  print("Seu prejuízo será de R${}".format(pvt))
  print("Seu saldo é de R${} e ficará R${}".format(saldo,pvtr))
  if pvtr <= 0:
    print("Seu saldo está negativo (R${}).".format(pvtr))
  else:
    print("Seu saldo está postivo (R${}).".format(pvtr))
if prejuizo == 7: 
  pv1 = float(input("Valor do 1° iten/prejuízo: "))
  pv2 = float(input("Valor do 2° iten/prejuízo: "))
  pv3 = float(input("Valor do 3° iten/prejuízo: "))
  pv4 = float(input("Valor do 4° iten/prejuízo: "))
  pv5 = float(input("Valor do 5° iten/prejuízo: "))
  pv6 = float(input("Valor do 6° iten/prejuízo: "))
  pv7 = float(input("Valor do 7° iten/prejuízo: "))
  pvt = pv1 + pv2 + pv3 + pv4 + pv5 + pv6 + pv7
  pvtr = saldo - pvt
  print("Seu prejuízo será de R${}".format(pvt))
  print("Seu saldo é de R${} e ficará R${}".format(saldo, pvtr))
  if  pvtr <= 0:
    print("Seu saldo está negativo (R${}).".format(pvtr))
  else:
    print("Seu saldo está positivo (R${}).".format(pvtr))
if prejuizo == 8: 
  pv1 = float(input("Valor do 1° iten/prejuízo: "))
  pv2 = float(input("Valor do 2° iten/prejuízo: "))
  pv3 = float(input("Valor do 3° iten/prejuízo: "))
  pv4 = float(input("Valor do 4° iten/prejuízo: "))
  pv5 = float(input("Valor do 5° iten/prejuízo: "))
  pv6 = float(input("Valor do 6° iten/prejuízo: "))
  pv7 = float(input("Valor do 7° iten/prejuízo: "))
  pv8 = float(input("Valor do 8° iten/prejuízo: "))
  pvt = pv1 + pv2 + pv3 + pv4 + pv5 + pv6 + pv7 + pv8
  pvtr = saldo - pvt
  print("Seu prejuízo será de R${}".format(pvt))
  print("Seu saldo é de R${} e ficará R${}".format(saldo, pvtr))
  if pvtr <= 0:
    print("Seu saldo está negativo (R${}).".format(pvtr))
  else:
    print("Seu saldo está positivo (R${}).".format(pvtr))
if prejuizo == 9: 
  pv1 = float(input("Valor do 1° iten/prejuízo: "))
  pv2 = float(input("Valor do 2° iten/prejuízo: "))
  pv3 = float(input("Valor do 3° iten/prejuízo: "))
  pv4 = float(input("Valor do 4° iten/prejuízo: "))
  pv5 = float(input("Valor do 5° iten/prejuízo: "))
  pv6 = float(input("Valor do 6° iten/prejuízo: "))
  pv7 = float(input("Valor do 7° iten/prejuízo: "))
  pv8 = float(input("Valor do 8° iten/prejuízo: "))
  pv9 = float(input("Valor do 9° iten/prejuízo: "))
  pvt = pv1 + pv2 + pv3 + pv4 + pv5 + pv6 + pv7 + pv8 + pv9
  pvtr = saldo - pvt
  print("Seu prejuízo será de R${}".format(pvt))
  print("Seu saldo é de R${} e ficará R${}".format(saldo, pvtr))
  if pvtr <= 0:
    print("Seu saldo está negativo (R${}).".format(pvtr))
  else:
    print("Seu saldo está positivo (R${}).".format(pvtr))
if prejuizo == 10: 
  pv1 = float(input("Valor do 1° iten/prejuízo: "))
  pv2 = float(input("Valor do 2° iten/prejuízo: "))
  pv3 = float(input("Valor do 3° iten/prejuízo: "))
  pv4 = float(input("Valor do 4° iten/prejuízo: "))
  pv5 = float(input("Valor do 5° iten/prejuízo: "))
  pv6 = float(input("Valor do 6° iten/prejuízo: "))
  pv7 = float(input("Valor do 7° iten/prejuízo: "))
  pv8 = float(input("Valor do 8° iten/prejuízo: "))
  pv9 = float(input("Valor do 9° iten/prejuízo: "))
  pv10 = float(input("Valor do 10° iten/prejuízo: "))
  pvt = pv1 + pv2 + pv3 + pv4 + pv5 + pv6 + pv7 + pv8 + pv9 + pv10
  pvtr = saldo - pvt
  print("Seu prejuízo será de R${}".format(pvt))
  print("Seu saldo é de R${} e ficará R${}".format(saldo, pvtr))
  if pvtr <= 0:
    print("Seu saldo está negativo (R${}).".format(pvtr))
  else:
    print("Seu saldo está positivo (R${}).".format(pvtr))
