# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_new_point.ui'
#
# Created: Tue Feb 17 13:44:56 2015
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AddNewPointDialog(object):
    def setupUi(self, AddNewPointDialog):
        AddNewPointDialog.setObjectName(_fromUtf8("AddNewPointDialog"))
        AddNewPointDialog.resize(343, 251)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddNewPointDialog.sizePolicy().hasHeightForWidth())
        AddNewPointDialog.setSizePolicy(sizePolicy)
        AddNewPointDialog.setMinimumSize(QtCore.QSize(343, 251))
        AddNewPointDialog.setMaximumSize(QtCore.QSize(343, 251))
        AddNewPointDialog.setWindowTitle(QtGui.QApplication.translate("AddNewPointDialog", "Add New Point", None, QtGui.QApplication.UnicodeUTF8))
        AddNewPointDialog.setAccessibleName(_fromUtf8(""))
        AddNewPointDialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.ResetButton = QtGui.QPushButton(AddNewPointDialog)
        self.ResetButton.setGeometry(QtCore.QRect(130, 220, 81, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ResetButton.sizePolicy().hasHeightForWidth())
        self.ResetButton.setSizePolicy(sizePolicy)
        self.ResetButton.setText(QtGui.QApplication.translate("AddNewPointDialog", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.ResetButton.setObjectName(_fromUtf8("ResetButton"))
        self.AddButton = QtGui.QPushButton(AddNewPointDialog)
        self.AddButton.setGeometry(QtCore.QRect(20, 220, 81, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddButton.sizePolicy().hasHeightForWidth())
        self.AddButton.setSizePolicy(sizePolicy)
        self.AddButton.setText(QtGui.QApplication.translate("AddNewPointDialog", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.AddButton.setObjectName(_fromUtf8("AddButton"))
        self.CloseButton = QtGui.QPushButton(AddNewPointDialog)
        self.CloseButton.setGeometry(QtCore.QRect(240, 220, 81, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CloseButton.sizePolicy().hasHeightForWidth())
        self.CloseButton.setSizePolicy(sizePolicy)
        self.CloseButton.setText(QtGui.QApplication.translate("AddNewPointDialog", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.CloseButton.setObjectName(_fromUtf8("CloseButton"))
        self.AddNewPointGroup = QtGui.QGroupBox(AddNewPointDialog)
        self.AddNewPointGroup.setGeometry(QtCore.QRect(10, 10, 321, 201))
        self.AddNewPointGroup.setTitle(QtGui.QApplication.translate("AddNewPointDialog", "Add New Point with Coordinates", None, QtGui.QApplication.UnicodeUTF8))
        self.AddNewPointGroup.setObjectName(_fromUtf8("AddNewPointGroup"))
        self.PointTypeLineEdit = QtGui.QLineEdit(self.AddNewPointGroup)
        self.PointTypeLineEdit.setGeometry(QtCore.QRect(110, 170, 201, 20))
        self.PointTypeLineEdit.setObjectName(_fromUtf8("PointTypeLineEdit"))
        self.NorthCoordLabel = QtGui.QLabel(self.AddNewPointGroup)
        self.NorthCoordLabel.setGeometry(QtCore.QRect(10, 80, 101, 16))
        self.NorthCoordLabel.setText(QtGui.QApplication.translate("AddNewPointDialog", "North", None, QtGui.QApplication.UnicodeUTF8))
        self.NorthCoordLabel.setObjectName(_fromUtf8("NorthCoordLabel"))
        self.PointCodeLabel = QtGui.QLabel(self.AddNewPointGroup)
        self.PointCodeLabel.setGeometry(QtCore.QRect(10, 140, 101, 16))
        self.PointCodeLabel.setText(QtGui.QApplication.translate("AddNewPointDialog", "Point Code", None, QtGui.QApplication.UnicodeUTF8))
        self.PointCodeLabel.setObjectName(_fromUtf8("PointCodeLabel"))
        self.PointNumberLineEdit = QtGui.QLineEdit(self.AddNewPointGroup)
        self.PointNumberLineEdit.setGeometry(QtCore.QRect(110, 20, 201, 20))
        self.PointNumberLineEdit.setObjectName(_fromUtf8("PointNumberLineEdit"))
        self.PointTypeLabel = QtGui.QLabel(self.AddNewPointGroup)
        self.PointTypeLabel.setGeometry(QtCore.QRect(10, 170, 101, 16))
        self.PointTypeLabel.setText(QtGui.QApplication.translate("AddNewPointDialog", "Point Type", None, QtGui.QApplication.UnicodeUTF8))
        self.PointTypeLabel.setObjectName(_fromUtf8("PointTypeLabel"))
        self.EastCoordLineEdit = QtGui.QLineEdit(self.AddNewPointGroup)
        self.EastCoordLineEdit.setGeometry(QtCore.QRect(190, 50, 121, 20))
        self.EastCoordLineEdit.setObjectName(_fromUtf8("EastCoordLineEdit"))
        self.ZCoordLineEdit = QtGui.QLineEdit(self.AddNewPointGroup)
        self.ZCoordLineEdit.setGeometry(QtCore.QRect(190, 110, 121, 20))
        self.ZCoordLineEdit.setObjectName(_fromUtf8("ZCoordLineEdit"))
        self.EastCoordLabel = QtGui.QLabel(self.AddNewPointGroup)
        self.EastCoordLabel.setGeometry(QtCore.QRect(10, 50, 101, 16))
        self.EastCoordLabel.setText(QtGui.QApplication.translate("AddNewPointDialog", "East", None, QtGui.QApplication.UnicodeUTF8))
        self.EastCoordLabel.setObjectName(_fromUtf8("EastCoordLabel"))
        self.PointNumberLabel = QtGui.QLabel(self.AddNewPointGroup)
        self.PointNumberLabel.setGeometry(QtCore.QRect(10, 20, 101, 16))
        self.PointNumberLabel.setText(QtGui.QApplication.translate("AddNewPointDialog", "Point ID", None, QtGui.QApplication.UnicodeUTF8))
        self.PointNumberLabel.setObjectName(_fromUtf8("PointNumberLabel"))
        self.NorthCoordLineEdit = QtGui.QLineEdit(self.AddNewPointGroup)
        self.NorthCoordLineEdit.setGeometry(QtCore.QRect(190, 80, 121, 20))
        self.NorthCoordLineEdit.setObjectName(_fromUtf8("NorthCoordLineEdit"))
        self.PointCodeLineEdit = QtGui.QLineEdit(self.AddNewPointGroup)
        self.PointCodeLineEdit.setGeometry(QtCore.QRect(110, 140, 201, 20))
        self.PointCodeLineEdit.setObjectName(_fromUtf8("PointCodeLineEdit"))
        self.ZCoordLabel = QtGui.QLabel(self.AddNewPointGroup)
        self.ZCoordLabel.setGeometry(QtCore.QRect(10, 110, 91, 16))
        self.ZCoordLabel.setText(QtGui.QApplication.translate("AddNewPointDialog", "Elevation", None, QtGui.QApplication.UnicodeUTF8))
        self.ZCoordLabel.setObjectName(_fromUtf8("ZCoordLabel"))

        self.retranslateUi(AddNewPointDialog)
        QtCore.QMetaObject.connectSlotsByName(AddNewPointDialog)
        AddNewPointDialog.setTabOrder(self.PointNumberLineEdit, self.EastCoordLineEdit)
        AddNewPointDialog.setTabOrder(self.EastCoordLineEdit, self.NorthCoordLineEdit)
        AddNewPointDialog.setTabOrder(self.NorthCoordLineEdit, self.ZCoordLineEdit)
        AddNewPointDialog.setTabOrder(self.ZCoordLineEdit, self.PointCodeLineEdit)
        AddNewPointDialog.setTabOrder(self.PointCodeLineEdit, self.PointTypeLineEdit)
        AddNewPointDialog.setTabOrder(self.PointTypeLineEdit, self.AddButton)
        AddNewPointDialog.setTabOrder(self.AddButton, self.ResetButton)
        AddNewPointDialog.setTabOrder(self.ResetButton, self.CloseButton)

    def retranslateUi(self, AddNewPointDialog):
        pass

