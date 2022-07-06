import sys
import datetime

salidas = ["PANTALLA", "CSV"]
tiposv = ["EMITIDO", "DEPOSITADO"]
estadosv = ["PENDIENTE", "APROBADO", "RECHAZADO"]
permit_ran = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", ":"]

def salir(m):
    print(m)
    exit() 

def rangobien(r):
    for i in r:
        if i not in permit_ran:
            return False
        else:
            pass
print(rangobien)
def isrango(a):
    if (a.count(":") == 1) and (a.count("-") == 4) and (rangobien(a) != False):
        rangevals = [a.split(":")[0].split("-"), a.split(":")[1].split("-")]
        if (len(rangevals[0][0]) == 2) and (len(rangevals[0][1]) == 2) and (len(rangevals[0][2]) == 4) and (len(rangevals[1][0]) == 2) and (len(rangevals[1][1]) == 2) and (len(rangevals[1][2]) == 4):
            return True
    else:
        return False
print(isrango)

def checkotherwrong(a, f):
    if a and (not f(a)):
        return True

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

#print(f"Archivo CSV: {csv}\nDNI: {dni}\nFormato de salida: {salida}\nTipo de cheque: {tipo}\nEstado del cheque: {estado}\nRango de fecha: {rango}")
#print("")
#print("")

csvfile = open(f"./{csv}")
cheques = []
bancos = []
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
    cheques.append(linedatalist[1])
    bancos.append(linedatalist[2])
    origenes.append(linedatalist[3])
    destinos.append(linedatalist[4])
    valores.append(linedatalist[5])
    fechaso.append(linedatalist[6])
    fechasp.append(linedatalist[7])
    dnis.append(linedatalist[8])
    estados.append(linedatalist[9])
    tipos.append(linedatalist[10])


indices = [i for i, x in enumerate(dnis) if x == dni]


def dispscreen():
    checkn = 0
    for i in indices:
        checkn = checkn + 1
        print(f'Cheque {checkn}:\nFecha de emisión: {fechaso[i]}\nFecha de pago/cobro: {fechasp[i]}\nValor del cheque: {valores[i]}\nNúmero de cuenta: {origenes[i]}')
        print("")

def expcsv():  
    checkn = 0
    fechahora = str(datetime.datetime.now()).split('.')[0].replace(":", ",")
    arc = open(f"C:\\Python\\DNI_{dnis[indices[0]]} TIMESTAMP_{fechahora}.csv", 'w')
    arc.writelines(f"Cheque,Fecha de emision,Fecha de pago/cobro,Valor del cheque,Numero de cuenta\n")
    for i in indices:
        checkn = checkn + 1
        arc.writelines(f"{checkn},{fechaso[i]},{fechasp[i]},{valores[i]},{origenes[i]}\n")
    arc.close()


if salida == "PANTALLA":
    dispscreen()
elif salida == "CSV":
    expcsv()
    print("archivo creado")
