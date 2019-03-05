
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from pysnmp.hlapi import *
import time
from time import sleep
import rrdtool
from datetime import datetime, timedelta
import threading

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(777, 421)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 771, 411))
        self.tabWidget.setObjectName("tabWidget")
        self.Tab1 = QtWidgets.QWidget()
        self.Tab1.setObjectName("Tab1")
        self.label = QtWidgets.QLabel(self.Tab1)
        self.label.setGeometry(QtCore.QRect(10, 10, 151, 31))
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.Tab1)
        self.tableWidget.setGeometry(QtCore.QRect(30, 60, 461, 181))
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 2))
        self.tableWidget.setSizeIncrement(QtCore.QSize(2, 2))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(133)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(77)
        self.tableWidget.verticalHeader().setDefaultSectionSize(49)
        self.tableWidget.verticalHeader().setMinimumSectionSize(46)
        self.tabWidget.addTab(self.Tab1, "")
        self.Tab2 = QtWidgets.QWidget()
        self.Tab2.setObjectName("Tab2")
        self.label_2 = QtWidgets.QLabel(self.Tab2)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 141, 31))
        self.label_2.setObjectName("label_2")
        self.hostNameLabel = QtWidgets.QLineEdit(self.Tab2)
        self.hostNameLabel.setGeometry(QtCore.QRect(120, 40, 181, 32))
        self.hostNameLabel.setObjectName("hostNameLabel")
        self.PuertoLabel = QtWidgets.QLineEdit(self.Tab2)
        self.PuertoLabel.setGeometry(QtCore.QRect(120, 80, 181, 32))
        self.PuertoLabel.setObjectName("PuertoLabel")
        self.VersSnmpLabel = QtWidgets.QLineEdit(self.Tab2)
        self.VersSnmpLabel.setGeometry(QtCore.QRect(120, 120, 181, 32))
        self.VersSnmpLabel.setObjectName("VersSnmpLabel")
        self.ComunidadLabel = QtWidgets.QLineEdit(self.Tab2)
        self.ComunidadLabel.setGeometry(QtCore.QRect(120, 160, 181, 32))
        self.ComunidadLabel.setObjectName("ComunidadLabel")
        self.BotonAgregar = QtWidgets.QPushButton(self.Tab2)
        self.BotonAgregar.setGeometry(QtCore.QRect(210, 220, 88, 34))
        self.BotonAgregar.setObjectName("BotonAgregar")
        self.label_3 = QtWidgets.QLabel(self.Tab2)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 71, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.Tab2)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 58, 18))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.Tab2)
        self.label_5.setGeometry(QtCore.QRect(10, 130, 91, 18))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.Tab2)
        self.label_6.setGeometry(QtCore.QRect(10, 170, 91, 18))
        self.label_6.setObjectName("label_6")
        self.tabWidget.addTab(self.Tab2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(10, 20, 141, 31))
        self.label_7.setObjectName("label_7")
        self.EliminarIpLabel = QtWidgets.QLineEdit(self.tab)
        self.EliminarIpLabel.setGeometry(QtCore.QRect(120, 50, 181, 32))
        self.EliminarIpLabel.setObjectName("EliminarIpLabel")
        self.BotonEliminar = QtWidgets.QPushButton(self.tab)
        self.BotonEliminar.setGeometry(QtCore.QRect(210, 110, 88, 34))
        self.BotonEliminar.setObjectName("BotonEliminar")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(10, 60, 71, 20))
        self.label_8.setObjectName("label_8")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(30, 20, 151, 18))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(30, 50, 151, 18))
        self.label_10.setObjectName("label_10")
        self.textEdit = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit.setGeometry(QtCore.QRect(30, 120, 351, 231))
        self.textEdit.setObjectName("textEdit")
        self.graphicsView = QtWidgets.QGraphicsView(self.tab_2)
        self.graphicsView.setGeometry(QtCore.QRect(390, 120, 361, 231))
        self.graphicsView.setObjectName("graphicsView")
        self.frame = QtWidgets.QFrame(self.tab_2)
        self.frame.setGeometry(QtCore.QRect(390, 30, 120, 80))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.tab_2)
        self.widget.setGeometry(QtCore.QRect(530, 30, 120, 80))
        self.widget.setObjectName("widget")
        self.comboBoxSo = QtWidgets.QComboBox(self.tab_2)
        self.comboBoxSo.setGeometry(QtCore.QRect(30, 70, 281, 32))
        self.comboBoxSo.setObjectName("comboBoxSo")
        self.comboBoxSo.addItem("")
        self.comboBoxSo.addItem("")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setGeometry(QtCore.QRect(20, 20, 151, 18))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setGeometry(QtCore.QRect(20, 50, 151, 18))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setGeometry(QtCore.QRect(390, 50, 151, 18))
        self.label_13.setObjectName("label_13")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab_3)
        self.plainTextEdit.setGeometry(QtCore.QRect(390, 80, 311, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 130, 341, 231))
        self.textEdit_2.setObjectName("textEdit_2")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.tab_3)
        self.graphicsView_2.setGeometry(QtCore.QRect(390, 130, 361, 231))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.comboBox = QtWidgets.QComboBox(self.tab_3)
        self.comboBox.setGeometry(QtCore.QRect(20, 80, 281, 32))
        self.comboBox.setObjectName("comboBox")
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Monitoreo de Agentes"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "Agente"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "Agente"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "Agente"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Estado"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Estado Interfaz"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Numero Interfaces"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab1), _translate("Dialog", "Inicio"))
        self.label_2.setText(_translate("Dialog", "Agregar Agente"))
        self.BotonAgregar.setText(_translate("Dialog", "Agregar"))
        self.label_3.setText(_translate("Dialog", "Hostname"))
        self.label_4.setText(_translate("Dialog", "Puerto"))
        self.label_5.setText(_translate("Dialog", "Version SNMP"))
        self.label_6.setText(_translate("Dialog", "Comunidad"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab2), _translate("Dialog", "Agregar"))
        self.label_7.setText(_translate("Dialog", "Eliminar Agente"))
        self.BotonEliminar.setText(_translate("Dialog", "Eliminar"))
        self.label_8.setText(_translate("Dialog", "IP"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Eliminar"))
        self.label_9.setText(_translate("Dialog", "Estado del Dispositivo"))
        self.label_10.setText(_translate("Dialog", "Selecciona el Agente"))
        self.comboBoxSo.setItemText(0, _translate("Dialog", "Linux 1"))
        self.comboBoxSo.setItemText(1, _translate("Dialog", "Windows"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Estado"))
        self.label_11.setText(_translate("Dialog", "Estado del Dispositivo"))
        self.label_12.setText(_translate("Dialog", "Selecciona el Agente"))
        self.label_13.setText(_translate("Dialog", "Escribe La MIB"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "MIBS"))


class Hora:
    @staticmethod
    def getTimeUTC():
        return int(time.time())

    @staticmethod
    def changeToDate(UTC):
        return datetime.datetime.fromtimestamp(UTC).strftime('%Y-%m-%d %H:%M:%S')


class RRDtool():
    def __init__(self, nombreDB):
        self.nombre = nombreDB
        self.nombreDB = str(nombreDB + ".rrd")
        self.colorGrap = "#FF0000"
        self.tipoDB = "COUNTER"

    def crearBD(self):
        self.timeFirstData = Hora.getTimeUTC()
        rrdtool.create(self.nombreDB,
                       "--start", "now",
                       str("DS:" + self.nombre + ':' + self.tipoDB + ':600:U:U'),
                       "RRA:AVERAGE:0.5:1:24",
                       "RRA:AVERAGE:0.5:6:10")

    def setColor(self, color):
        self.colorGrap = color

    def getColor(self):
        return self.colorGrap

    def insertarDB(self, data):
        self.timeLastData = Hora.getTimeUTC()
        formatData = str(str(self.timeLastData) + ":" + str(data))
        print("formato de la inserccion " + formatData)
        rrdtool.update(self.nombreDB, "N:32")

    def crearImagen(self):
        rrdtool.graph(str(self.nombre + '.png'),
                      "--start", str(rrdtool.first(self.nombreDB)),
                      "--end", str(rrdtool.last(self.nombreDB)),
                      str("DEF:grafica=" + self.nombreDB + ':' + self.nombre + ':AVERAGE'),
                      str("LINE1:grafica" + self.getColor())
                      )

    def getDatosDB(self):
        return rrdtool.fetch(self.nombreDB, 'AVERAGE',
                             "--start", str(rrdtool.first(self.nombreDB)),
                             "--end", str(rrdtool.last(self.nombreDB))
                             )

    def volcarDatos(self, formato):
        ''' dump Vuelca el contenido de una RRD en formato ASCII'''
        rrdtool.dump(self.nombreDB, str(self.nombre + "." + formato))


class Maquina:
    def __init__(self, n, ip, p, c, listOID):
        self.nick = n
        self.ip = ip
        self.puerto = p
        self.listOID = listOID
        self.community = c
        self.errorIndication = Null
        self.errorStatus = Null
        self.errorIndex = Null
        self.varBinds = Null
        self.ObjectTypeMIB = []

    def __makeQuery(self):
        for OID in self.listOID:
            self.ObjectTypeMIB.append(ObjectType(ObjectIdentity(OID)))

    def setIP(self, ip):
        self.ip = ip

    def setPuerto(self, p):
        self.puerto = p

    def setListaOID(self, lista):
        self.listOID = lista

    def __estaEnLista(self, MIB):
        if MIB in self.listOID:
            return False
        else:
            return True

    def agregarMIB(self, MIB):
        if not estaEnLista(MIB):
            self.listOID.add(MIB)

    def setCommunity(self, c):
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
        self.errorIndication, self.errorStatus, self.errorIndex, self.varBinds = next(
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
        print("Nick:" + self.getNick() + "\nIP:" + self.getIP() + "\nPuerto conexion: " + str(
            self.getPuerto()) + "\nCommunity: " + self.getCommunity())


class Monitorear(Maquina, threading.Thread):
    def __init__(self, n, ip, p, c, listOID):
        threading.Thread.__init__(self)
        Maquina.__init__(self, n, ip, p, c, listOID)
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





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
    listaOID = ['1.3.6.1.2.1.1.1.0', '1.3.6.1.2.1.1.6.0']  ## agregar las IODS
    puerto = 161
    community = 'SNMPcom'
    Linux1 = Monitorear('Linux 1', '192.168.1.66', puerto, community, listaOID)
    # Linux2 = Maquina('Linux 2','195.100.100.20',puerto,community,listaOID)
    Windows = Maquina('Windos XP', '192.168.1.68', puerto, community, listaOID)
    W = Monitorear('Windos XP', '192.168.1.68', puerto, community, listaOID)
    Windows

    # W.start()
    # W.join()
    # Linux1.start()
    # Linux1.join()
    base = RRDtool('estaEsMiBase')
    base.crearBD()
    base.insertarDB(12373)
    print(base.getDatosDB())