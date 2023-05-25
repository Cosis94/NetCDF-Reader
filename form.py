from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout,  QTableView, QFileDialog
from PyQt5.QtCore import QAbstractTableModel, Qt, QDir
import netCDF4 as nc
import pandas as pd 
import numpy as np 




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
        Widget.resize(738, 601)
        self.Attr_Liste =[]
        self.comboBox = QtWidgets.QComboBox(Widget)
        self.comboBox.setGeometry(QtCore.QRect(30, 80, 171, 26))
        self.comboBox.setObjectName("comboBox")

                
        self.commandLinkButton = QtWidgets.QCommandLinkButton(Widget)
        self.commandLinkButton.setGeometry(QtCore.QRect(220, 30, 120, 41))
        self.commandLinkButton.setObjectName("Set Attr")
        self.commandLinkButton.clicked.connect(self.set_one)

        self.listWidget = QtWidgets.QListWidget(Widget)
        self.listWidget.setGeometry(QtCore.QRect(390, 30, 256, 192))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.itemDoubleClicked.connect(self.delete_set_one)


        self.Delete = QtWidgets.QCommandLinkButton(Widget)
        self.Delete.setGeometry(QtCore.QRect(220, 70, 120, 41))
        self.Delete.setObjectName("Delete")
        self.Delete.clicked.connect(self.delete_set_one)

        self.Ausgabe = QtWidgets.QCommandLinkButton(Widget)
        self.Ausgabe.setGeometry(QtCore.QRect(220, 110, 120, 41))
        self.Ausgabe.setObjectName("Delete")
        self.Ausgabe.clicked.connect(self.DataFrame_ex)

        self.tableView = QtWidgets.QTableView(Widget)
        self.tableView.setGeometry(QtCore.QRect(10, 260, 711, 291))
        self.tableView.setObjectName("tableView")

        self.CSV_Exportbutton = QtWidgets.QPushButton(Widget)
        self.CSV_Exportbutton.setGeometry(QtCore.QRect(10, 560, 93, 29))
        self.CSV_Exportbutton.setObjectName("CSV_Exportbutton")
        self.CSV_Exportbutton.clicked.connect(self.export_csv)

        self.TXT_Exportbutton = QtWidgets.QPushButton(Widget)
        self.TXT_Exportbutton.setGeometry(QtCore.QRect(120, 560, 93, 29))
        self.TXT_Exportbutton.setObjectName("TXT_Exportbutton")
        self.TXT_Exportbutton.clicked.connect(self.export_txt)

        self.Upload_NCDATAButton = QtWidgets.QPushButton(Widget)
        self.Upload_NCDATAButton.setGeometry(QtCore.QRect(30, 50, 171, 29))
        self.Upload_NCDATAButton.setObjectName("Upload_NCDATAButton")
        self.Upload_NCDATAButton.clicked.connect(self.get_text_file)

        self.label = QtWidgets.QLabel(Widget)
        self.label.setGeometry(QtCore.QRect(30, 120, 141, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Widget)
        self.label_2.setGeometry(QtCore.QRect(30, 140, 91, 20))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)


    def get_text_file(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Dirs)

        if dialog.exec_():
            file_name = dialog.selectedFiles()

        if file_name[0].endswith('.nc'):
                self.new_File = file_name[0]
                fn = self.new_File
                self.ds = nc.Dataset(fn)
                Liste = []

                for x in self.ds.variables.values():
                    Liste.append(x.name)
                self.comboBox.addItems(Liste)
        else:
            pass

    def delete_set_one(self):
        self.temp_par = self.listWidget.currentItem().text()
        self.Attr_Liste.remove(self.temp_par)     
        self.listWidget.clear()
        self.listWidget.addItems(self.Attr_Liste)


    def DataFrame_ex(self):
        init_dict = {}
        for x in self.Attr_Liste:
            self.Liste_temp = self.ds[x][:]
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
        for k in self.ds[self.set_one_par].shape:
            self.label_2.setText(self.set_one_par+" :" +str(k))


    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.commandLinkButton.setText(_translate("Widget", "Set Attr"))
        self.Delete.setText(_translate("Widget", "Delete"))
        self.Ausgabe.setText(_translate("Widget", "Ausgabe"))
        self.CSV_Exportbutton.setText(_translate("Widget", "CSV Export"))
        self.TXT_Exportbutton.setText(_translate("Widget", "TXT Export"))
        self.Upload_NCDATAButton.setText(_translate("Widget", "Upload NetCDF Data"))
        self.label.setText(_translate("Widget", "Current Dimension:"))
        self.label_2.setText(_translate("Widget", "Dimension"))

    def export_csv(self):
        path = self.new_File[:-3]+".csv"
        self.df.to_csv(path)

    def export_txt(self):
        path = self.new_File[:-3]+".txt"
        self.df.to_csv(path, header=None, index=None, sep=' ', mode='a')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())