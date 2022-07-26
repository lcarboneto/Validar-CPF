cpf = input('digite o cpf, somente os numeros:')

numero = cpf[0:9]
digito = cpf[9:]
p = 10
st = 0

pm = cpf[0:3]
sm = cpf[3:6]
tm = cpf[6:9]

for n in numero:
    a = int(n)
    st = st + a*p
    p -= 1

r1 = st % 11
prd = 11 - r1

if prd >=10:
    pd = 0
else:
    pd = prd

numero2 = numero+str(pd)

p = 11
st = 0

for n in numero2:
    a = int(n)
    st = st + a*p
    p -= 1

r2 = st % 11
srd = 11 - r2

if srd >=10:
    sd = 0
else:
    sd = srd

df = int(pd)*10 + int(sd)

if df == int(digito):
    print(f'O CPF {pm}.{sm}.{tm}-{digito} é válido')
else:
    print(f'O CPF {pm}.{sm}.{tm}-{digito} NÃO É VÁLIDO')
