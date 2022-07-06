#proyecto terminado
import sys
import datetime

salidas = ["PANTALLA", "CSV"]
tiposv = ["EMITIDO", "DEPOSITADO"]
estadosv = ["PENDIENTE", "APROBADO", "RECHAZADO"]
permit_ran = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", ":"]
month31 = ["01", "03", "05", "07", "08", "10", "12"]
month30 = ["04", "06", "09", "11"]

def salir(m):
    print(m)
    exit() 

def rangobien(r):
    for i in r:
        if i not in permit_ran:
            return False
        else:
            pass

def bisiesto(a):
    if a % 4 == 0:
        if a % 100 == 0:
            if a % 400 == 0:
                return True
            else:
                return False    
        else:
            return True
    else:
        return False

def isrango(a):
    #revisa que no haya mas de los puntos de division de la string del rango permitidos y que no haya caracteres no permitidos
    if (a.count(":") == 1) and (a.count("-") == 4) and (rangobien(a) != False):
        #procesa la string del rango de fecha para almacenar los dias meses y años en una lista con dos listas dentro, una de los 3 valores de la primera fecha y otra con los 3 valores de la segunda
        rangevals = [a.split(":")[0].split("-"), a.split(":")[1].split("-")]
        #revisa que la cantidad de caracteres por parte sea la adecuada
        if (len(rangevals[0][0]) == 2) and (len(rangevals[0][1]) == 2) and (len(rangevals[0][2]) == 4) and (len(rangevals[1][0]) == 2) and (len(rangevals[1][1]) == 2) and (len(rangevals[1][2]) == 4):
            #comprueba si el mes de la primera fecha tiene 31 dias
            if rangevals[0][1] in month31:
                #comprueba que la cantidad de dias proporcionada sea adecuada para un mes de 31 dias
                if (not int(rangevals[0][0]) > 31) and (int(rangevals[0][0]) != 0):
                    #comprueba si el mes de la segunda fecha tiene 31 dias
                    if rangevals[1][1] in month31:
                        #comprueba que la cantidad de dias proporcionada sea adecuada para un mes de 31 dias
                        if (not int(rangevals[1][0]) > 31) and (int(rangevals[1][0]) != 0):
                            return True
                        else:
                            return False
                    #comprueba si el mes de la segunda fecha tiene 30 dias
                    elif rangevals[1][1] in month30:
                        #comprueba que la cantidad de dias proporcionada sea adecuada para un mes de 30 dias
                        if (not int(rangevals[1][0]) > 30) and (int(rangevals[1][0]) != 0):
                            return True
                        else:
                            return False
                    #comprueba si el mes de la segunda fecha tiene 28 dias        
                    elif rangevals[1][1] == "02":
                        if bisiesto(int(rangevals[1][2])):
                                #comprueba que la cantidad de dias proporcionada sea adecuada para un mes de 28 dias
                                if (not int(rangevals[1][0]) > 29) and (int(rangevals[1][0]) != 0):
                                    return True
                                else:
                                    return False
                        else:
                            #comprueba que la cantidad de dias proporcionada sea adecuada para un mes de 28 dias
                            if (not int(rangevals[1][0]) > 28) and (int(rangevals[1][0]) != 0):
                                return True
                            else:
                                return False
                    else:
                        return False
                else:
                    return False
            #comprueba si el mes de la primera fecha tiene 30 dias
            elif rangevals[0][1] in month30:
                #comprueba que la cantidad de dias proporcionada sea adecuada para un mes de 30 dias
                if (not int(rangevals[0][0]) > 30) and (int(rangevals[0][0]) != 0):
                    #comprueba si el mes de la segunda fecha tiene 31 dias
                    if rangevals[1][1] in month31:
                        #comprueba que la cantidad de dias proporcionada sea adecuada para un mes de 31 dias
                        if (not int(rangevals[1][0]) > 31) and (int(rangevals[1][0]) != 0):
                            return True
                        else:
                            return False
                    #comprueba si el mes de la segunda fecha tiene 30 dias        
                    elif rangevals[1][1] in month30:
                        #comprueba que la cantidad de dias proporcionada sea adecuada para un mes de 30 dias
                        if (not int(rangevals[1][0]) > 30) and (int(rangevals[1][0]) != 0):
                            return True
                        else:
                            return False
                    #comprueba si el mes de la segunda fecha tiene 28 dias
                    elif rangevals[1][1] == "02":
                        if bisiesto(int(rangevals[1][2])):
                                #comprueba que la cantidad de dias proporcionada sea adecuada para un mes de 28 dias
                                if (not int(rangevals[1][0]) > 29) and (int(rangevals[1][0]) != 0):
                                    return True
                                else:
                                    return False
                        else:
                            #comprueba que la cantidad de dias proporcionada sea adecuada para un mes de 28 dias
                            if (not int(rangevals[1][0]) > 28) and (int(rangevals[1][0]) != 0):
                                return True
                            else:
                                return False
                    else:
                        return False
                else:
                    return False
            #comprueba si el mes de la primera fecha tiene 28 dias
            elif rangevals[0][1] == "02":
                if bisiesto(int(rangevals[0][2])):
                    #comprueba que la cantidad de dias proporcionada sea adecuada para un mes de 28 dias
                    if (not int(rangevals[0][0]) > 29) and (int(rangevals[0][0]) != 0):
                        #comprueba si el mes de la segunda fecha tiene 31 dias
                        if rangevals[1][1] in month31:
                            #comprueba que la cantidad de dias proporcionada sea adecuada para un mes de 31 dias
                            if (not int(rangevals[1][0]) > 31) and (int(rangevals[1][0]) != 0):
                                return True
                            else:
                                return False
                        #comprueba si el mes de la segunda fecha tiene 30 dias
                        elif rangevals[1][1] in month30:
                            #comprueba que la cantidad de dias proporcionada sea adecuada para un mes de 30 dias
                            if (not int(rangevals[1][0]) > 30) and (int(rangevals[1][0]) != 0):
                                return True
                            else:
                                return False
                        #comprueba si el mes de la segunda fecha tiene 28 dias
                        elif rangevals[1][1] == "02":
                            if bisiesto(int(rangevals[1][2])):
                                #comprueba que la cantidad de dias proporcionada sea adecuada para un mes de 28 dias
                                if (not int(rangevals[1][0]) > 29) and (int(rangevals[1][0]) != 0):
                                    return True
                                else:
                                    return False
                            else:
                                #comprueba que la cantidad de dias proporcionada sea adecuada para un mes de 28 dias
                                if (not int(rangevals[1][0]) > 28) and (int(rangevals[1][0]) != 0):
                                    return True
                                else:
                                    return False
                        else:
                            return False
                    else:
                        return False
                else:
                    #comprueba que la cantidad de dias proporcionada sea adecuada para un mes de 28 dias
                    if (not int(rangevals[0][0]) > 28) and (int(rangevals[0][0]) != 0):
                        #comprueba si el mes de la segunda fecha tiene 31 dias
                        if rangevals[1][1] in month31:
                            #comprueba que la cantidad de dias proporcionada sea adecuada para un mes de 31 dias
                            if (not int(rangevals[1][0]) > 31) and (int(rangevals[1][0]) != 0):
                                return True
                            else:
                                return False
                        #comprueba si el mes de la segunda fecha tiene 30 dias
                        elif rangevals[1][1] in month30:
                            #comprueba que la cantidad de dias proporcionada sea adecuada para un mes de 30 dias
                            if (not int(rangevals[1][0]) > 30) and (int(rangevals[1][0]) != 0):
                                return True
                            else:
                                return False
                        #comprueba si el mes de la segunda fecha tiene 28 dias
                        elif rangevals[1][1] == "02":
                            if bisiesto(int(rangevals[1][2])):
                                #comprueba que la cantidad de dias proporcionada sea adecuada para un mes de 28 dias
                                if (not int(rangevals[1][0]) > 29) and (int(rangevals[1][0]) != 0):
                                    return True
                                else:
                                    return False
                            else:
                                #comprueba que la cantidad de dias proporcionada sea adecuada para un mes de 28 dias
                                if (not int(rangevals[1][0]) > 28) and (int(rangevals[1][0]) != 0):
                                    return True
                                else:
                                    return False
                        else:
                            return False
                    else:
                        return False
            else:
                return False
        else: return False
    else:
        return False

if len(sys.argv) < 5 or len(sys.argv) > 7:
    salir("Cantidad de parámetros inadecuada")

if (len(sys.argv) == 7):
    csv = sys.argv[1]
    dni = sys.argv[2]
    salida = sys.argv[3]
    tipo = sys.argv[4]
    estado = sys.argv[5]
    rango = sys.argv[6]
elif (len(sys.argv) == 6) and sys.argv[5] in estadosv:
    csv = sys.argv[1]
    dni = sys.argv[2]
    salida = sys.argv[3]
    tipo = sys.argv[4]
    estado = sys.argv[5]
    rango = None
elif (len(sys.argv) == 6) and isrango(sys.argv[5]):
    csv = sys.argv[1]
    dni = sys.argv[2]
    salida = sys.argv[3]
    tipo = sys.argv[4]
    estado = None
    rango = sys.argv[5] 
elif (len(sys.argv) == 6) and (sys.argv[5] not in estadosv) and (not isrango(sys.argv[5])):
    salir("Estado o rango inadecuado")
else:
    csv = sys.argv[1]
    dni = sys.argv[2]
    salida = sys.argv[3]
    tipo = sys.argv[4]
    estado = None
    rango = None

try:
    csv.split(".")
except: ValueError: salir("Archivo inadecuado")

if len(csv.split(".")) != 2:
    salir("Archivo inadecuado")

if csv.split(".")[1] != "csv":
    salir("El archivo no es un CSV")

try:
    int(dni)
except: ValueError: salir("DNI inadecuado")

if salida not in salidas:
    salir("Formato de salida inadecuado")

if tipo not in tiposv:
    salir("Tipo de cheque inadecuado")

if estado and estado not in estadosv:
    salir("Estado del cheque inadecuado")

if rango and (not isrango(rango)):
    salir("Rango de fecha inadecuado")

csvfile = open(f"./{csv}")
cheques = []
bancos = []
sucursales = []
origenes = []
destinos = []
valores = []
fechaso = []
fechasp = []
dnis = []
estados = []
tipos = []

for linea in csvfile:
    linedatalist = linea.replace("\n", "").split(",")
    cheques.append(linedatalist[0])
    bancos.append(linedatalist[1])
    sucursales.append(linedatalist[2])
    origenes.append(linedatalist[3])
    destinos.append(linedatalist[4])
    valores.append(linedatalist[5])
    fechaso.append(linedatalist[6])
    fechasp.append(linedatalist[7])
    dnis.append(linedatalist[8])
    estados.append(linedatalist[9])
    tipos.append(linedatalist[10])

if rango:
    rangedates = rango.split(":")
    datefrom = datetime.datetime.strptime(rangedates[0], "%d-%m-%Y")#.strftime('%d-%m-%Y')
    dateto = datetime.datetime.strptime(rangedates[1], "%d-%m-%Y")#.strftime('%d-%m-%Y')

def rep(index):
    cheqrevisados = [] #lista a la que se le agregan los numeros de cheques no repetidos
    cta = origenes[index[0]] #lista a la que se le agregan los numeros de cuentas repetidas
    cheqrep = False
    ctadist = False
    for i in index:
        if cheques[i] not in cheqrevisados:
            cheqrevisados.append(cheques[i])
        else:
            cheqrep = True
    for i in index:
        if origenes[i] != cta:
            ctadist = True   
    if cheqrep and ctadist:
        salir("Error del sistema: este DNI tiene más de un número de cuenta asociado y sus números de cheque se repiten al menos una vez")
    elif cheqrep and not ctadist:
        salir("Error del sistema: para este DNI, los números de cheque se repiten al menos una vez")
    elif ctadist and not cheqrep:
        salir("Error del sistema: este DNI tiene más de un número de cuenta asociado")
        
    

def makeindex(state=None, rang=None):
    indicesdni = [i for i, x in enumerate(dnis) if x == dni]
    typeindex = [i for i, x in enumerate(tipos) if x == tipo]
    resultindex = [i for i in typeindex if i in indicesdni] 
    if resultindex == []:
        salir("Este DNI no tiene ningún cheque de este tipo asociado")
    if state:
        stateindex = [i for i, x in enumerate(estados) if x == state]
        resultindex = [i for i in resultindex if i in stateindex]
        if resultindex == []:
            salir(f"Este DNI no tiene ningún cheque de este tipo asociado que se encuentre {estado}")
    if rang:
        if tipo == "EMITIDO":
            fechaso.pop(0)
            rangindex = [i+1 for i, x in enumerate(fechaso) if datefrom <= datetime.datetime.fromtimestamp(int(x)) <= dateto]
            resultindex = [i for i in resultindex if i in rangindex]
            if resultindex == []:
                salir("Este DNI no tiene ningún cheque de este tipo asociado que se encuentre en este rango de fecha")
        elif tipo == "DEPOSITADO":
            fechasp.pop(0)
            rangindex = [i+1 for i, x in enumerate(fechasp) if datefrom <= datetime.datetime.fromtimestamp(int(x)) <= dateto]
            resultindex = [i for i in resultindex if i in rangindex]
            if resultindex == []:
                salir("Este DNI no tiene ningún cheque de este tipo asociado que se encuentre en este rango de fecha")
    return resultindex

def dispscreen(state=None, rang=None):
    checkn = 0
    resultindex = makeindex(state, rang)
    dnindex = [i for i, x in enumerate(dnis) if x == dni]
    rep(dnindex)
    for i in resultindex:
        checkn = checkn + 1
        print(f'Cheque {checkn}:\nFecha de emisión: {datetime.datetime.fromtimestamp(int(fechaso[i-1])).strftime("%d-%m-%Y")}\nFecha de pago/cobro: {datetime.datetime.fromtimestamp(int(fechasp[i-1])).strftime("%d-%m-%Y")}\nValor del cheque: {valores[i]}\nNúmero de cuenta: {origenes[i]}')
        print("")

def expcsv(state=None, rang=None):  
    checkn = 0
    resultindex = makeindex(state, rang)
    dnindex = [i for i, x in enumerate(dnis) if x == dni]
    rep(dnindex)
    arc = open(f".\\csv_exportados\\DNI_{dnis[resultindex[0]]} TIMESTAMP_{int(datetime.datetime.now().timestamp())}.csv", 'w')
    arc.writelines(f"Cheque,Fecha de emision,Fecha de pago/cobro,Valor del cheque,Numero de cuenta\n")
    for i in resultindex:
        checkn = checkn + 1
        arc.writelines(f"{checkn},{datetime.datetime.fromtimestamp(int(fechaso[i-1])).strftime('%d-%m-%Y')},{datetime.datetime.fromtimestamp(int(fechasp[i-1])).strftime('%d-%m-%Y')},{valores[i]},{origenes[i]}\n")
    arc.close()

if dni in dnis:
    if salida == "PANTALLA":
        if estado and rango:
            dispscreen(state=estado, rang=rango)
        elif estado and not rango:
            dispscreen(state=estado)
        elif rango and not estado:
            dispscreen(rang=rango)
        else:
            dispscreen()
    elif salida == "CSV":
        if estado and rango:
            expcsv(state=estado, rang=rango)
        elif estado and not rango:
            expcsv(state=estado)
        elif rango and not estado:
            expcsv(rang=rango)
        else:
            expcsv()
        print("archivo creado")
else:
    salir("No existe ningún cheque asociado a este DNI")

csvfile.close()