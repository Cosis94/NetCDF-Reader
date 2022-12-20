from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout,  QTableView
from PyQt5.QtCore import QAbstractTableModel, Qt
import netCDF4 as nc
import pandas as pd 
import numpy as np 

fn = r'Documents/Python/Templates/AMS/Datei.nc'
ds = nc.Dataset(fn)
Liste = []

for x in ds.variables.values():
    Liste.append(x.name)


class pandasModel(QAbstractTableModel):
    import sys 
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        
        return self._data.shape[0]
        

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        if orientation == QtCore.Qt.Vertical and role == QtCore.Qt.DisplayRole:
            return self._data.index[col]
        return None

class Ui_Widget(object):


    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(738, 578)
        self.Attr_Liste =[]
        self.comboBox = QtWidgets.QComboBox(Widget)
        self.comboBox.setGeometry(QtCore.QRect(140, 60, 171, 26))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(Liste)
                
        self.commandLinkButton = QtWidgets.QCommandLinkButton(Widget)
        self.commandLinkButton.setGeometry(QtCore.QRect(340, 50, 187, 41))
        self.commandLinkButton.setObjectName("Set Attr")
        self.commandLinkButton.clicked.connect(self.set_one)

        self.listWidget = QtWidgets.QListWidget(Widget)
        self.listWidget.setGeometry(QtCore.QRect(460, 10, 256, 192))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.itemDoubleClicked.connect(self.delete_set_one)


        self.Delete = QtWidgets.QCommandLinkButton(Widget)
        self.Delete.setGeometry(QtCore.QRect(340, 90, 187, 41))
        self.Delete.setObjectName("Delete")
        self.Delete.clicked.connect(self.delete_set_one)

        self.Ausgabe = QtWidgets.QCommandLinkButton(Widget)
        self.Ausgabe.setGeometry(QtCore.QRect(340, 120, 187, 41))
        self.Ausgabe.setObjectName("Delete")
        self.Ausgabe.clicked.connect(self.DataFrame_ex)

        self.tableView = QtWidgets.QTableView(Widget)
        self.tableView.setGeometry(QtCore.QRect(10, 260, 711, 291))
        self.tableView.setObjectName("tableView")



        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def delete_set_one(self):
        self.temp_par = self.listWidget.currentItem().text()
        self.Attr_Liste.remove(self.temp_par)
        self.listWidget.clear()
        self.listWidget.addItems(self.Attr_Liste)

    def DataFrame_ex(self):
        init_dict = {}
        for x in self.Attr_Liste:
            self.Liste_temp = ds[x][:]
            init_dict[x] = self.Liste_temp
        self.df = pd.DataFrame(data=init_dict)
        self.model = pandasModel(self.df)
        Dataframe_columns = self.df.columns
        self.tableView.setModel(self.model)





    def set_one(self):
        self.listWidget.clear()
        self.set_one_par = self.comboBox.currentText()
        self.Attr_Liste.append(self.set_one_par)
        self.listWidget.addItems(self.Attr_Liste)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.commandLinkButton.setText(_translate("Widget", "Set Attr"))
        self.Delete.setText(_translate("Widget", "Delete"))
        self.Ausgabe.setText(_translate("Widget", "Ausgabe"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())
