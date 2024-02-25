# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dell.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_DeleteUser(object):
    def setupUi(self, DeleteUser):
        DeleteUser.setObjectName("DeleteUser")
        DeleteUser.resize(400, 250)
        DeleteUser.setMinimumSize(QtCore.QSize(400, 250))
        DeleteUser.setMaximumSize(QtCore.QSize(400, 250))
        DeleteUser.setStyleSheet("QWidget{\n"
"    background-color:   rgb(0, 0, 0);\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(DeleteUser)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top = QtWidgets.QFrame(DeleteUser)
        self.top.setStyleSheet("QFrame{\n"
"    background-color:  rgb(56, 58, 86);\n"
"    border: 0px;\n"
"}")
        self.top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top.setObjectName("top")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.top)
        self.horizontalLayout.setContentsMargins(-1, 2, -1, 2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_4 = QtWidgets.QFrame(self.top)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.id = QtWidgets.QLabel(self.frame_4)
        self.id.setStyleSheet("QLabel{\n"
"color: rgb(28,191,255);\n"
"}")
        self.id.setAlignment(QtCore.Qt.AlignCenter)
        self.id.setObjectName("id")
        self.verticalLayout_2.addWidget(self.id)
        self.horizontalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.top)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.line_id = QtWidgets.QLineEdit(self.frame_5)
        self.line_id.setStyleSheet("QLineEdit:hover {\n"
"    border:  1px ridge rgb(85, 170, 0);\n"
"}\n"
"QLineEdit {\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.line_id.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.line_id.setMaxLength(10)
        self.line_id.setPlaceholderText("")
        self.line_id.setClearButtonEnabled(True)
        self.line_id.setObjectName("line_id")
        self.verticalLayout_3.addWidget(self.line_id)
        self.horizontalLayout.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.top)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.push_search = QtWidgets.QPushButton(self.frame_6)
        self.push_search.clicked.connect(self.search_btn)
        self.push_search.setStyleSheet("QPushButton{\n"
"color: rgb(28,191,255);\n"
"}\n"
"QPushButton:hover {\n"
"    border:  1px ridge rgb(170, 255, 0);\n"
"    color: rgb(0, 255, 0);\n"
"}\n"
"")
        self.push_search.setObjectName("push_search")
        self.verticalLayout_4.addWidget(self.push_search)
        self.horizontalLayout.addWidget(self.frame_6)
        self.verticalLayout.addWidget(self.top)
        self.middle = QtWidgets.QFrame(DeleteUser)
        self.middle.setStyleSheet("QFrame{\n"
"    background-color:  rgb(56, 58, 86);\n"
"    border: 0px;\n"
"}")
        self.middle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.middle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.middle.setObjectName("middle")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.middle)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_7 = QtWidgets.QFrame(self.middle)
        self.frame_7.setStyleSheet("")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.out_name = QtWidgets.QLabel(self.frame_7)
        self.out_name.setStyleSheet("QLabel{\n"
"color: rgb(28,191,255);\n"
"}")
        self.out_name.setAlignment(QtCore.Qt.AlignCenter)
        self.out_name.setObjectName("out_name")
        self.verticalLayout_5.addWidget(self.out_name)
        self.out_view = QtWidgets.QLabel(self.frame_7)
        self.out_view.setStyleSheet("QLabel{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(81, 84, 125);\n"
"}")
        self.out_view.setAlignment(QtCore.Qt.AlignCenter)
        self.out_view.setObjectName("out_view")
        self.verticalLayout_5.addWidget(self.out_view, 0, QtCore.Qt.AlignVCenter)
        self.horizontalLayout_2.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.middle)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_8)
        self.tableWidget.setStyleSheet("QTableWidget{\n"
"color: rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 0);\n"
"}")
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.horizontalLayout_4.addWidget(self.tableWidget)
        self.horizontalLayout_2.addWidget(self.frame_8)
        self.verticalLayout.addWidget(self.middle)
        self.bottom = QtWidgets.QFrame(DeleteUser)
        self.bottom.setStyleSheet("QFrame{\n"
"    background-color:  rgb(56, 58, 86);\n"
"    border: 0px;\n"
"}")
        self.bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom.setObjectName("bottom")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.bottom)
        self.horizontalLayout_5.setContentsMargins(-1, 2, -1, 2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.push_exit = QtWidgets.QPushButton(self.bottom)
        self.push_exit.setStyleSheet("QPushButton{\n"
"color: rgb(28,191,255);\n"
"}\n"
"QPushButton:hover {\n"
"    border:  1px ridge rgb(170, 255, 0);\n"
"    color: rgb(0, 255, 0);\n"
"}\n"
"")
        self.push_exit.setObjectName("push_exit")
        self.horizontalLayout_5.addWidget(self.push_exit)
        self.pushButton = QtWidgets.QPushButton(self.bottom)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    color: rgb(28,191,255);\n"
"}\n"
"QPushButton:hover {\n"
"    border:  1px ridge rgb(176, 165, 101);\n"
"    color: rgb(176, 165, 101);\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        self.push_delete = QtWidgets.QPushButton(self.bottom)
        self.push_delete.clicked.connect(self.delete_id)
        self.push_delete.setStyleSheet("QPushButton{\n"
"color: rgb(28,191,255);\n"
"}\n"
"QPushButton:hover {\n"
"    border:  1px ridge rgb(170, 255, 0);\n"
"    color: rgb(255, 0, 0);\n"
"}\n"
"")
        self.push_delete.setObjectName("push_delete")
        self.horizontalLayout_5.addWidget(self.push_delete)
        self.verticalLayout.addWidget(self.bottom)

        self.retranslateUi(DeleteUser)
        self.push_exit.clicked.connect(DeleteUser.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(DeleteUser)

    def retranslateUi(self, DeleteUser):
        _translate = QtCore.QCoreApplication.translate
        DeleteUser.setWindowTitle(_translate("DeleteUser", "Delete user"))
        self.id.setText(_translate("DeleteUser", "ID"))
        self.push_search.setText(_translate("DeleteUser", "Search"))
        self.out_name.setText(_translate("DeleteUser", "Output Info :"))
        self.out_view.setText(_translate("DeleteUser", "..."))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("DeleteUser", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("DeleteUser", "NAME"))
        self.push_exit.setText(_translate("DeleteUser", "Exit"))
        self.pushButton.setText(_translate("DeleteUser", "Back"))
        self.push_delete.setText(_translate("DeleteUser", "Delete"))

    
    def search_btn(self):
        data_path = "BD/"
        self.out_view.setText("Searching...")
        self.line_id.clear()
        i=0
        for path, subdirname, filenames in os.walk(data_path):
            for f_id in filenames:
                file_name = os.path.basename(path)          # Denumirea Folderului
                if f_id.lower().endswith(('.wav')):
                    self.tableWidget.setRowCount(99)
                    for ids in f_id:
                        self.tableWidget.setColumnCount(2)
                        self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(f_id.replace('.wav','')))
                        self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(file_name))
                    i = i+1
                
        
        

    def delete_id(self):
        valoare = self.line_id.text()
        gmm_path = "models/"
        data_path = "BD/" 

        for fname in os.listdir(gmm_path):
            if fname == str(valoare)+".gmm":
                os.remove(gmm_path+str(valoare)+".gmm")
            else:
                self.out_view.setText("Empty")
                    
        for path, subdirname, filenames in os.walk(data_path):
            for f_id in filenames:
                if (str(valoare+".wav") == f_id):
                    os.remove(path+"/"+str(valoare)+".wav")
                    self.out_view.setText(valoare+" Deleted")
                    self.line_id.clear()
                else:
                    self.out_view.setText("Empty")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DeleteUser = QtWidgets.QWidget()
    ui = Ui_DeleteUser()
    ui.setupUi(DeleteUser)
    DeleteUser.show()
    sys.exit(app.exec_())
