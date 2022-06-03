from PyQt5 import QtCore, QtGui, QtWidgets
from employee_leave_info import employee_leave_info
from calendar_dialogue import calendar_dialogue

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(314, 373)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(20, 20, 20, 20)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.idLabel = QtWidgets.QLabel(Dialog)
        self.idLabel.setObjectName("idLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.idLabel)
        self.idLineEdit = QtWidgets.QLineEdit(Dialog)
        self.idLineEdit.setObjectName("idLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.idLineEdit)
        self.dateLabel = QtWidgets.QLabel(Dialog)
        self.dateLabel.setObjectName("dateLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.dateLabel)
        self.datebutton = QtWidgets.QToolButton(Dialog)
        self.datebutton.setObjectName("datebutton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.datebutton)
        self.starttimelabel = QtWidgets.QLabel(Dialog)
        self.starttimelabel.setObjectName("starttimelabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.starttimelabel)
        self.starttimeLineEdit = QtWidgets.QLineEdit(Dialog)
        self.starttimeLineEdit.setObjectName("starttimeLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.starttimeLineEdit)
        self.endtimeLabel = QtWidgets.QLabel(Dialog)
        self.endtimeLabel.setObjectName("endtimeLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.endtimeLabel)
        self.endtimeLineEdit = QtWidgets.QLineEdit(Dialog)
        self.endtimeLineEdit.setObjectName("endtimeLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.endtimeLineEdit)
        self.leaveperiodlabel = QtWidgets.QLabel(Dialog)
        self.leaveperiodlabel.setObjectName("leaveperiodlabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.leaveperiodlabel)
        self.LeavePeriodLineEdit = QtWidgets.QLineEdit(Dialog)
        self.LeavePeriodLineEdit.setObjectName("LeavePeriodLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.LeavePeriodLineEdit)
        self.excuseLabel = QtWidgets.QLabel(Dialog)
        self.excuseLabel.setObjectName("excuseLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.excuseLabel)
        self.excuseLineEdit = QtWidgets.QLineEdit(Dialog)
        self.excuseLineEdit.setObjectName("excuseLineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.excuseLineEdit)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(92, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(92, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.idLabel.setText(_translate("Dialog", "ID"))
        self.dateLabel.setText(_translate("Dialog", "Date"))
        self.datebutton.setText(_translate("Dialog", "..."))
        self.starttimelabel.setText(_translate("Dialog", "Start Time"))
        self.endtimeLabel.setText(_translate("Dialog", "End Time"))
        self.leaveperiodlabel.setText(_translate("Dialog", "Leave Period"))
        self.excuseLabel.setText(_translate("Dialog", "Excuse"))
        self.pushButton.setText(_translate("Dialog", "Save"))


class EmployeeLeaveDialog(QtWidgets.QDialog):

    def __init__(self):
        super(EmployeeLeaveDialog,self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.employee_leave_info = None

        self.ui.pushButton.clicked.connect(self.save_button_clicked)
        self.ui.datebutton.clicked.connect(self.calendar_button_clicked)

    def save_button_clicked(self):
        self.employee_leave_info = employee_leave_info(
            self.ui.idLineEdit.text(),
            self.date,
            self.ui.starttimeLineEdit.text(),
            self.ui.endtimeLineEdit.text(),
            self.ui.LeavePeriodLineEdit.text(),
            self.ui.excuseLineEdit.text()
        )
        print(self.employee_leave_info.date)
        self.accept()

    def calendar_button_clicked(self):
        self.calendar_dialogue = calendar_dialogue()
        result = self.calendar_dialogue.exec()

        if result == QtWidgets.QDialog.Accepted:
            self.date = self.calendar_dialogue.date





