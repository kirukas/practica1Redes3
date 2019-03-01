
from pysnmp.hlapi import *
import time
from time import sleep
import rrdtool
from datetime import datetime, timedelta
import threading

class Hora:
    @staticmethod
    def getTimeUTC():
        return int( time.time())
    @staticmethod
    def changeToDate(UTC):
        return datetime.datetime.fromtimestamp(UTC).strftime('%Y-%m-%d %H:%M:%S')
class RRDtool():
    def __init__(self,nombreDB):
        self.nombre = nombreDB
        self.nombreDB =str(nombreDB+".rrd")
        self.colorGrap = "#FF0000"
        self.tipoDB = "COUNTER"
        
    def crearBD(self):
        self.timeFirstData = Hora.getTimeUTC()
        rrdtool.create(self.nombreDB,
                       "--start","now",
                       str("DS:"+self.nombre+':'+self.tipoDB+':600:U:U'),
                       "RRA:AVERAGE:0.5:1:24",
                       "RRA:AVERAGE:0.5:6:10")
    def setColor(self,color):
        self.colorGrap = color
    def getColor(self):
        return self.colorGrap
    def insertarDB(self,data):
        self.timeLastData = Hora.getTimeUTC() 
        formatData = str(str(self.timeLastData)+":"+str(data))
        print("formato de la inserccion "+formatData)
        rrdtool.update(self.nombreDB,"N:32")
    def crearImagen(self):
        rrdtool.graph(str(self.nombre+'.png'),
                      "--start",str(rrdtool.first(self.nombreDB)),
                      "--end",str(rrdtool.last(self.nombreDB)),
                       str("DEF:grafica="+self.nombreDB+':'+self.nombre+':AVERAGE'),
                       str("LINE1:grafica"+self.getColor())
        )
    def getDatosDB(self):
        return rrdtool.fetch(self.nombreDB,'AVERAGE',
                             "--start",str(rrdtool.first(self.nombreDB)),
                             "--end",str(rrdtool.last(self.nombreDB))
        )
    def volcarDatos(self,formato):
        ''' dump Vuelca el contenido de una RRD en formato ASCII'''
        rrdtool.dump(self.nombreDB,str(self.nombre+"."+formato)) 
class Maquina:
    def __init__(self,n,ip,p,c,listOID):
        self.nick = n
        self.ip = ip
        self.puerto = p
        self.listOID = listOID
        self.community = c
        self.errorIndication = Null
        self.errorStatus  = Null
        self.errorIndex = Null
        self.varBinds= Null
        self.ObjectTypeMIB = []
    def __makeQuery(self):
        for OID in self.listOID:
            self.ObjectTypeMIB.append(ObjectType(ObjectIdentity(OID)))
    def setIP(self,ip):
        self.ip = ip
    def setPuerto(self,p):
        self.puerto = p
    def setListaOID(self,lista):
        self.listOID = lista
    def __estaEnLista(self,MIB):
        if MIB in self.listOID:
            return False
        else:
            return True
    def agregarMIB(self,MIB):
       if not estaEnLista(MIB):
           self.listOID.add(MIB)
    def setCommunity(self,c):
        self.community = c
    def setNick(self, n):
        self.nick = n
    def getIP(self):
        return self.ip
    def getPuerto(self):
        return self.puerto
    def getListaIOD(self):
        return self.listOID
    def getNick(self):
        return self.nick
    def getCommunity(self):
        return self.community
## AQUI ESTA LA MAGIA!!!######
    def enviarPeticion(self):
        print('Enviando Peticion!!')
        self.__makeQuery();
        self.errorIndication,self.errorStatus, self.errorIndex, self.varBinds = next(
            getCmd(SnmpEngine(),
                   CommunityData(self.getCommunity(), mpModel=0),
                   UdpTransportTarget((self.getIP(), self.getPuerto())),
                   ContextData(),
                   *self.ObjectTypeMIB
            )
        )
    def getMIBS(self):
        if self.errorIndication:
            print(self.errorIndication)
        elif self.errorStatus:
            print('%s at %s' % (self.errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        else:
            for varBind in self.varBinds:
                print(' = '.join([x.prettyPrint() for x in varBind]))
 ##### toString##################################
    def getInfotMIBS(self):
         self.enviarPeticion()
         self.getMIBS()
    def infoMachine(self):
        print ("Nick:"+self.getNick()+"\nIP:"+self.getIP()+"\nPuerto conexion: "+str(self.getPuerto()) + "\nCommunity: "+self.getCommunity())
class Monitorear(Maquina,threading.Thread):
    def __init__(self,n,ip,p,c,listOID):
        threading.Thread.__init__(self)
        Maquina.__init__(self,n,ip,p,c,listOID)
        self.tiempoActulizacion = 10
        self.estadoMonitor = True
    def getEstadoMonitor(self):
        return self.estadoMonitor
    def estaMonitoreando(self):
        return self.getEstadoMonitor()
    def setTiempoActualizacion(self, tiempo):
        self.tiempoActulizacion = tiempo
    def getTiempoActualizacion(self):
        return self.tiempoActulizacion
    def setEstadoMonitor(self, estado):
        self.estadoMonitor = estado
    def run(self):
        print("Este es  el hilo!")
        while self.getEstadoMonitor():   
            self.getInfotMIBS()
            sleep(self.getTiempoActualizacion())
    def stop(self):
        if self.estaMonitoreando():
            self.setEstadoMonitor(False)
   
if __name__=="__main__":
    listaOID=['1.3.6.1.2.1.1.1.0','1.3.6.1.2.1.1.6.0']## agregar las IODS
    puerto = 161
    community = 'SNMPcom'
    Linux1 = Monitorear('Linux 1','192.168.1.66',puerto,community,listaOID)
    #Linux2 = Maquina('Linux 2','195.100.100.20',puerto,community,listaOID)
    Windows = Maquina('Windos XP','192.168.1.68',puerto,community,listaOID)
    W = Monitorear('Windos XP','192.168.1.68',puerto,community,listaOID)
   # W.start()
   # W.join()
    #Linux1.start()
    #Linux1.join()
    base = RRDtool('estaEsMiBase')
    #base.crearBD()
    base.insertarDB(12373)
    print(base.getDatosDB())
