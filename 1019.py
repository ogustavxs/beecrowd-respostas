N = int(input())
horas = N // 3600
minutos = (N-(horas*3600)) // 60
segundos = ((N-(horas*3600))-minutos*60)
print("{}:{}:{}".format(horas, minutos, segundos))