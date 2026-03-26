conttelefonica=0
contpresencial=0
contM=0
contF=0
encuestastotales=0
mayorHijo=0

encuesta=str(input("Tipo de encuesta(telefonica o presencial): ")).upper()
while encuesta!="FIN":
    encuestastotales+=1
    if encuesta=="TELEFONICA":
        conttelefonica+=1
    else:
        if encuesta=="PRESENCIAL":
            contpresencial+=1
    documento=str(input("Ingrese su documento: ")).upper()
    genero=str(input("Ingrese su género: ")).upper()
    while genero!="F" and genero!="M":
        genero=str(input("Género no valido, reingrese: ")).upper()
    if genero=="M":
        contM+=1
    elif genero=="F":
        contF+=1
    hijos=int(input("Ingrese la cantidad de hijos: "))
    while hijos>=3 or hijos<0:
        hijos=int(input("REINGRESE HIJOS: "))
    if hijos == 2 :
        h1=int(input("Ingrese la edad del primer hijo: "))
        h2=int(input("Ingrese la edad del segundo hijo: "))

        if h1>h2:
            mayor=h1
        else:
            mayor=h2
#ojo con las comparaciones porque pueden estar al revés, hay que comparar el valor que saquemos por el "cont" que en mi caso es mayorHijo
        if mayor>mayorHijo: 
            mayorHijo=mayor
            documentomayor=documento
    else: 
        if hijos == 1:
            h3=int(input("Ingrese la edad del niñ@: "))

        if h3>mayorHijo:
            mayorHijo=h3
            documentomayor=documento

    if hijos==2 and genero=="M":
        promh=(h1+h2)/2
        print(f'PROMEDIO DE EDADES DE LOS NIÑOS ES {promh}')

    encuesta=str(input("Tipo de encuesta(1=telefonica y 2=presencial): ")).upper()

if contM>contF:
    print(f'El grupo masculino fue el más encuestado con un total de {contM}')
elif contM<contF:
    print(f'El grupo femenino fue el más encuestado con un total de {contF}')
else:
    print(f'Ambos grupos fueron entrevistador por igual. Masculino {contM} y Femenino {contF}')

#para sacar el porcentaje saque el total de encuestados y el total de entrevistados, en este caso presencial. 
# Dividi el total de encuestador presenciales por el total de encuestados y el resultado lo multiplique por 100
porcentajePRE=(contpresencial/encuestastotales)*100 
print(f'El porcentaje de encuestados presenciales es {porcentajePRE}')

porcentajeTELE=(conttelefonica/encuestastotales)*100
print(f'El porcentaje de encuestados telefonicos es {porcentajeTELE}')

print('El documento de la persona con el hijo de mayor edad es', documentomayor, 'y que su hijo tiene una edad de ',mayorHijo)