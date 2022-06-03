from PyQt5 import QtCore, QtGui, QtWidgets
from Employee_Add_Info import Employee_Add_Info


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(283, 399)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setVerticalSpacing(4)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(20, 20, 20, 20)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.firstnamelabel = QtWidgets.QLabel(Dialog)
        self.firstnamelabel.setObjectName("firstnamelabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.firstnamelabel)
        self.firstnamelineedit = QtWidgets.QLineEdit(Dialog)
        self.firstnamelineedit.setObjectName("firstnamelineedit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.firstnamelineedit)
        self.lastnamelabel = QtWidgets.QLabel(Dialog)
        self.lastnamelabel.setObjectName("lastnamelabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lastnamelabel)
        self.lastnamelineedit = QtWidgets.QLineEdit(Dialog)
        self.lastnamelineedit.setObjectName("lastnamelineedit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lastnamelineedit)
        self.departmentlabel = QtWidgets.QLabel(Dialog)
        self.departmentlabel.setObjectName("departmentlabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.departmentlabel)
        self.departmentlineedit = QtWidgets.QLineEdit(Dialog)
        self.departmentlineedit.setObjectName("departmentlineedit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.departmentlineedit)
        self.positionlabel = QtWidgets.QLabel(Dialog)
        self.positionlabel.setObjectName("positionlabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.positionlabel)
        self.positionlineedit = QtWidgets.QLineEdit(Dialog)
        self.positionlineedit.setObjectName("positionlineedit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.positionlineedit)
        self.idlabel = QtWidgets.QLabel(Dialog)
        self.idlabel.setObjectName("idlabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.idlabel)
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(81, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(81, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.firstnamelabel.setText(_translate("Dialog", "First Name"))
        self.lastnamelabel.setText(_translate("Dialog", "Last Name"))
        self.departmentlabel.setText(_translate("Dialog", "Department"))
        self.positionlabel.setText(_translate("Dialog", "Position"))
        self.idlabel.setText(_translate("Dialog", "Personal ID"))
        self.pushButton.setText(_translate("Dialog", "Save"))



class EmployeeDialog(QtWidgets.QDialog):

    def __init__(self):
        super(EmployeeDialog,self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.employee_info = None

        self.ui.pushButton.clicked.connect(self.save_button_clicked)


    def save_button_clicked(self):
        self.employee_info = Employee_Add_Info(
            self.ui.lineEdit_5.text(),
            self.ui.firstnamelineedit.text(),
            self.ui.lastnamelineedit.text(),
            self.ui.departmentlineedit.text(),
            self.ui.positionlineedit.text()
            )

        self.accept()
