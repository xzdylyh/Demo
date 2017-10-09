# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\test.ui'
#
# Created: Sat May 27 13:46:51 2017
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import excel
import log
from Bll import loadTest
import time
import os
import gl

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("AM"))
        MainWindow.resize(800, 640)

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        #table control
        self.tableView = QtGui.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(10, 50, 780, 270))
        self.tableView.setSortingEnabled(False)
        self.tableView.setObjectName(_fromUtf8("tableView"))

        #文本浏览
        self.textBrowser =  QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 350, 780, 270))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))

        #com link button
        self.comBtn = QtGui.QCommandLinkButton(self.centralwidget)
        self.comBtn.setGeometry(QtCore.QRect(550,320,75,23))
        self.comBtn.setObjectName(_fromUtf8("comBtn"))
        self.comBtn.resize(210,30)
        self.comBtn.setText(_fromUtf8("测试报告 Reportxml.xml"))


        self.lable = QtGui.QLabel(self.centralwidget)
        self.lable.setGeometry(QtCore.QRect(10, 325, 75, 23))
        self.lable.setObjectName(_fromUtf8("lable"))

        #运行按钮
        self.runBtn = QtGui.QPushButton(self.centralwidget)
        self.runBtn.setGeometry(QtCore.QRect(190, 20, 75, 23))
        self.runBtn.setObjectName(_fromUtf8("runBtn"))

        #全选按钮
        self.SelectBtn = QtGui.QPushButton(self.centralwidget)
        self.SelectBtn.setGeometry(QtCore.QRect(10, 20, 75, 23))
        self.SelectBtn.setObjectName(_fromUtf8("SelectBtn"))

        #取消全选
        self.unSelectBtn = QtGui.QPushButton(self.centralwidget)
        self.unSelectBtn.setGeometry(QtCore.QRect(100, 20, 75, 23))
        self.unSelectBtn.setObjectName(_fromUtf8("unSelectBtn"))


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 5))
        self.menubar.setObjectName(_fromUtf8("menubar"))

        '''
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action_3 = QtGui.QAction(MainWindow)
        self.action_3.setObjectName(_fromUtf8("action_3"))
        self.menu.addAction(self.action_3)
        self.menu.addSeparator()
        self.menubar.addAction(self.menu.menuAction())
        '''
        self.retranslateUi(MainWindow)
        self.SelectBtn.connect(self.SelectBtn,QtCore.SIGNAL(_fromUtf8("clicked()")),self.allSelect)
        self.unSelectBtn.connect(self.unSelectBtn,QtCore.SIGNAL(_fromUtf8("clicked()")),self.unAllSelect)
        self.runBtn.connect(self.runBtn,QtCore.SIGNAL(_fromUtf8("clicked()")),self.runSelect)
        self.comBtn.connect(self.comBtn,QtCore.SIGNAL(_fromUtf8('clicked()')),self.startFile)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("AM", "AM", None))
        self.SelectBtn.setText(_translate("AM", "全 选", None))
        self.unSelectBtn.setText(_translate("AM", "取消全选", None))
        self.runBtn.setText(_translate("AM", "运 行", None))
        self.lable.setText(_translate("AM","Reponse信息:",None))
        self.comBtn.setVisible(False)

        '''
        self.menu.setTitle(_translate("MainWindow", "文件", None))
        self.action_3.setText(_translate("MainWindow", "加载测试用例", None))
        '''
        self.tableView_set() #初始化表格内容

    def startFile(self):
        os.startfile(gl.reporterPath+"\\reportxml.xml")

    def allSelect(self):
        colNameList = self.getColName()
        allData = self.getAllRowData()
        for i in range(0,len(colNameList)):
            for row in range(len(allData)):
                self.model.setData(self.model.index(row,0,QModelIndex()),QVariant(True)) #复选框,选中状态

    def unAllSelect(self):
        colNameList = self.getColName()
        allData = self.getAllRowData()
        for i in range(0,len(colNameList)):
            for row in range(len(allData)):
                self.model.setData(self.model.index(row,0,QModelIndex()),QVariant(False)) #复选框,选中状态


    def runSelect(self):
        #pass
        reload(sys)
        sys.setdefaultencoding('utf-8')
        resultArr = loadTest.cRun().go() #执行测试
        #print resultArr
        self.textBrowser.append("**************************************Start**********************************")
        self.textBrowser.append("*Execute Time:"+ gl.curTime)
        self.textBrowser.append("*Execute by:yhleng")
        self.textBrowser.append("*****************************************************************************")

        for i in range(0,len(resultArr)):

            self.textBrowser.append("--------------------------Step:"+str(i+1)+"__Reponse Information-------------------------")
            for j in resultArr[i]:
                dictTmp = resultArr[i][j]
                #print dictTmp
                self.textBrowser.append(j + ":" +str(dictTmp).decode('utf-8'))
            self.textBrowser.append("------------------------------------------------------------------------------")
        self.textBrowser.append("***************************************END************************************")
        self.comBtn.setVisible(True) #显示测试报告控件

    def tableView_set(self):
        self.model = QtGui.QStandardItemModel()
        colNameList = self.getColName()
        allData = self.getAllRowData()
        print allData
        #设置行,列
        self.model.setRowCount(len(allData))
        self.model.setColumnCount(len(colNameList))
        self.model.setHorizontalHeaderLabels(colNameList) #表头
        #绑定数据
        for i in range(0,len(colNameList)):
            for row in range(len(allData)):
                self.model.setData(self.model.index(row,0,QModelIndex()),QVariant(True)) #复选框,选中状态
                self.model.setData(self.model.index(row,i,QModelIndex()),QVariant(allData[row][colNameList[i]]))
                #设置字符颜色
                self.model.item(row,i).setForeground(QtGui.QBrush(QtGui.QColor(0, 0, 255)))
                #设置字符位置
                self.model.item(row,i).setTextAlignment(QtCore.Qt.AlignCenter)

        self.tableView.setModel(self.model) #加载表格
        self.tableView.setItemDelegateForColumn(0,CheckBoxDelegate(self.tableView))
        #table.setItemDelegateForColumn(2, CheckBoxDelegate(table))

    def getColName(self):
        try:
            testCasePath = loadTest.cRun().getTestCasePath()
            colNameList = excel.Excel(testCasePath).getRowData(5) #列名所在行
        except Exception,ex:
            log.out().debug(ex.message)
        return colNameList

    def getAllRowData(self):
        try:
            testCasePath = loadTest.cRun().getTestCasePath()
            allData = excel.Excel(testCasePath).getExcelDataByName(5)
        except Exception,ex:
            log.out().debug(ex.message)
        return  allData



class CheckBoxDelegate(QItemDelegate):

  def __init__(self, parent=None):
    QItemDelegate.__init__(self, parent)
    self.chkboxSize = 19 #?!

  def createEditor(self, parent, option, index):
    chkbox = QCheckBox(parent)
    chkbox.setText('')
    chkbox.setTristate(False) #只用两个状态
    left = option.rect.x() + (option.rect.width() - self.chkboxSize) / 2
    top  = option.rect.y() + (option.rect.height() - self.chkboxSize) / 2
    chkbox.setGeometry(left, top, self.chkboxSize, self.chkboxSize)
    return chkbox

  def paint(self, painter, option, index):
    value = index.data().toBool()
    opt = QStyleOptionButton()
    opt.state |= QStyle.State_Enabled | (QStyle.State_On if value else QStyle.State_Off)
    opt.text = ''
    left = option.rect.x() + (option.rect.width() - self.chkboxSize) / 2
    top  = option.rect.y() + (option.rect.height() - self.chkboxSize) / 2
    opt.rect = QRect(left, top, self.chkboxSize, self.chkboxSize)
    QApplication.style().drawControl(QStyle.CE_CheckBox, opt, painter)

  def updateEditorGeometry(self, editor, option, index):
    pass


def execApp():
    app = QtGui.QApplication(sys.argv)
    form = QtGui.QMainWindow()
    ui =Ui_MainWindow()
    ui.setupUi(form)
    ui.retranslateUi(form)
    form.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    form = QtGui.QMainWindow()
    ui =Ui_MainWindow()
    ui.setupUi(form)
    ui.retranslateUi(form)
    form.show()
    sys.exit(app.exec_())
