# Tendencias e Innovacion en Tecnologia Agricola (TEA)
horas= input ("horas de trabajo? ")
valorPorHora = input ("valor por hora? ")

# se utiliza la conversion de tipo a int
# sino se hace la conversion existira error porque trata de multiplicar strings
# calculando el valor total de las minutos juagadas
total = int(horas) * int(valorPorHoras)
print(total)