# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(738, 601)
        self.comboBox = QtWidgets.QComboBox(Widget)
        self.comboBox.setGeometry(QtCore.QRect(30, 80, 171, 26))
        self.comboBox.setObjectName("comboBox")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(Widget)
        self.commandLinkButton.setGeometry(QtCore.QRect(220, 30, 91, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.listWidget = QtWidgets.QListWidget(Widget)
        self.listWidget.setGeometry(QtCore.QRect(340, 30, 256, 192))
        self.listWidget.setObjectName("listWidget")
        self.Delete = QtWidgets.QCommandLinkButton(Widget)
        self.Delete.setGeometry(QtCore.QRect(220, 70, 91, 41))
        self.Delete.setObjectName("Delete")
        self.Ausgabe = QtWidgets.QCommandLinkButton(Widget)
        self.Ausgabe.setGeometry(QtCore.QRect(220, 110, 91, 41))
        self.Ausgabe.setObjectName("Ausgabe")
        self.tableView = QtWidgets.QTableView(Widget)
        self.tableView.setGeometry(QtCore.QRect(10, 260, 711, 291))
        self.tableView.setObjectName("tableView")
        self.CSV_Exportbutton = QtWidgets.QPushButton(Widget)
        self.CSV_Exportbutton.setGeometry(QtCore.QRect(10, 560, 93, 29))
        self.CSV_Exportbutton.setObjectName("CSV_Exportbutton")
        self.TXT_Exportbutton = QtWidgets.QPushButton(Widget)
        self.TXT_Exportbutton.setGeometry(QtCore.QRect(120, 560, 93, 29))
        self.TXT_Exportbutton.setObjectName("TXT_Exportbutton")
        self.Upload_NCDATAButton = QtWidgets.QPushButton(Widget)
        self.Upload_NCDATAButton.setGeometry(QtCore.QRect(30, 50, 171, 29))
        self.Upload_NCDATAButton.setObjectName("Upload_NCDATAButton")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.commandLinkButton.setText(_translate("Widget", "Set Attr"))
        self.Delete.setText(_translate("Widget", "Delete"))
        self.Ausgabe.setText(_translate("Widget", "Ausgabe"))
        self.CSV_Exportbutton.setText(_translate("Widget", "CSV Export"))
        self.TXT_Exportbutton.setText(_translate("Widget", "TXT Export"))
        self.Upload_NCDATAButton.setText(_translate("Widget", "Upload NetCDF Data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())
