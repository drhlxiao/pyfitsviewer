# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1327, 828)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter_3 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.splitter = QtWidgets.QSplitter(self.splitter_3)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.fileGroup = QtWidgets.QGroupBox(self.splitter)
        self.fileGroup.setObjectName("fileGroup")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.fileGroup)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.url = QtWidgets.QLineEdit(self.fileGroup)
        self.url.setText("")
        self.url.setObjectName("url")
        self.horizontalLayout.addWidget(self.url)
        self.browseDirectoryButton = QtWidgets.QToolButton(self.fileGroup)
        self.browseDirectoryButton.setObjectName("browseDirectoryButton")
        self.horizontalLayout.addWidget(self.browseDirectoryButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.filterFiles = QtWidgets.QLineEdit(self.fileGroup)
        self.filterFiles.setObjectName("filterFiles")
        self.horizontalLayout_4.addWidget(self.filterFiles)
        self.clearFileFilter = QtWidgets.QPushButton(self.fileGroup)
        self.clearFileFilter.setObjectName("clearFileFilter")
        self.horizontalLayout_4.addWidget(self.clearFileFilter)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.files = QtWidgets.QListView(self.fileGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.files.sizePolicy().hasHeightForWidth())
        self.files.setSizePolicy(sizePolicy)
        self.files.setObjectName("files")
        self.verticalLayout.addWidget(self.files)
        self.sectionsGroup = QtWidgets.QGroupBox(self.splitter)
        self.sectionsGroup.setObjectName("sectionsGroup")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.sectionsGroup)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.filterSections = QtWidgets.QLineEdit(self.sectionsGroup)
        self.filterSections.setObjectName("filterSections")
        self.horizontalLayout_5.addWidget(self.filterSections)
        self.clearSectionsFilter = QtWidgets.QPushButton(self.sectionsGroup)
        self.clearSectionsFilter.setObjectName("clearSectionsFilter")
        self.horizontalLayout_5.addWidget(self.clearSectionsFilter)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.sections = QtWidgets.QTableView(self.sectionsGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sections.sizePolicy().hasHeightForWidth())
        self.sections.setSizePolicy(sizePolicy)
        self.sections.setObjectName("sections")
        self.verticalLayout_4.addWidget(self.sections)
        self.dataGroup = QtWidgets.QGroupBox(self.splitter_3)
        self.dataGroup.setObjectName("dataGroup")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.dataGroup)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.splitter_2 = QtWidgets.QSplitter(self.dataGroup)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.filterHeader = QtWidgets.QLineEdit(self.layoutWidget)
        self.filterHeader.setMaximumSize(QtCore.QSize(200, 16777215))
        self.filterHeader.setObjectName("filterHeader")
        self.horizontalLayout_3.addWidget(self.filterHeader)
        self.clearHeaderFilter = QtWidgets.QPushButton(self.layoutWidget)
        self.clearHeaderFilter.setObjectName("clearHeaderFilter")
        self.horizontalLayout_3.addWidget(self.clearHeaderFilter)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.header = QtWidgets.QTableView(self.layoutWidget)
        self.header.setObjectName("header")
        self.verticalLayout_5.addWidget(self.header)
        self.layoutWidget_2 = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.filterData = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.filterData.setMaximumSize(QtCore.QSize(200, 16777215))
        self.filterData.setObjectName("filterData")
        self.horizontalLayout_2.addWidget(self.filterData)
        self.clearDataFilter = QtWidgets.QPushButton(self.layoutWidget_2)
        self.clearDataFilter.setObjectName("clearDataFilter")
        self.horizontalLayout_2.addWidget(self.clearDataFilter)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.contents = QtWidgets.QTableView(self.layoutWidget_2)
        self.contents.setObjectName("contents")
        self.verticalLayout_2.addWidget(self.contents)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.plotButton = QtWidgets.QToolButton(self.layoutWidget_2)
        self.plotButton.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.plotButton.setObjectName("plotButton")
        self.horizontalLayout_6.addWidget(self.plotButton)
        self.indicesCheckbox = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.indicesCheckbox.setCheckable(True)
        self.indicesCheckbox.setObjectName("indicesCheckbox")
        self.horizontalLayout_6.addWidget(self.indicesCheckbox)
        self.arrayIndices = QtWidgets.QSpinBox(self.layoutWidget_2)
        self.arrayIndices.setEnabled(False)
        self.arrayIndices.setObjectName("arrayIndices")
        self.horizontalLayout_6.addWidget(self.arrayIndices)
        self.allColumnCheckBox = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.allColumnCheckBox.setObjectName("allColumnCheckBox")
        self.horizontalLayout_6.addWidget(self.allColumnCheckBox)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.verticalLayout_6.addWidget(self.splitter_2)
        self.verticalLayout_3.addWidget(self.splitter_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1327, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuHelp_2 = QtWidgets.QMenu(self.menubar)
        self.menuHelp_2.setObjectName("menuHelp_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionReset = QtWidgets.QAction(MainWindow)
        self.actionReset.setObjectName("actionReset")
        self.actionOpen_2 = QtWidgets.QAction(MainWindow)
        self.actionOpen_2.setObjectName("actionOpen_2")
        self.actionData_request = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("SP_FileDialogContentsView")
        self.actionData_request.setIcon(icon)
        self.actionData_request.setObjectName("actionData_request")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionCreatePyTemplate = QtWidgets.QAction(MainWindow)
        self.actionCreatePyTemplate.setObjectName("actionCreatePyTemplate")
        self.menuFile.addAction(self.actionOpen_2)
        self.menuFile.addAction(self.actionReset)
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionCreatePyTemplate)
        self.menuHelp_2.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuHelp_2.menuAction())

        self.retranslateUi(MainWindow)
        self.actionQuit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.fileGroup.setTitle(_translate("MainWindow", "Select file"))
        self.browseDirectoryButton.setText(_translate("MainWindow", "..."))
        self.filterFiles.setPlaceholderText(_translate("MainWindow", "Filter"))
        self.clearFileFilter.setText(_translate("MainWindow", "Clear"))
        self.sectionsGroup.setTitle(_translate("MainWindow", "Sections in file"))
        self.filterSections.setPlaceholderText(_translate("MainWindow", "Filter (regular expression)"))
        self.clearSectionsFilter.setText(_translate("MainWindow", "Clear"))
        self.dataGroup.setTitle(_translate("MainWindow", "Section contents"))
        self.label.setText(_translate("MainWindow", "Header"))
        self.filterHeader.setPlaceholderText(_translate("MainWindow", "Filter (regular expression)"))
        self.clearHeaderFilter.setText(_translate("MainWindow", "Clear"))
        self.label_2.setText(_translate("MainWindow", "Data"))
        self.filterData.setPlaceholderText(_translate("MainWindow", "Filter (only text columns)"))
        self.clearDataFilter.setText(_translate("MainWindow", "Clear"))
        self.label_3.setText(_translate("MainWindow", "Plot data:"))
        self.plotButton.setText(_translate("MainWindow", "Plot selected"))
        self.indicesCheckbox.setToolTip(_translate("MainWindow", "<html><head/><body><p>Enable to use only one index when the selected data field contains an array.</p><p>Disable to leave array untouched before passing it to the plotter.</p></body></html>"))
        self.indicesCheckbox.setText(_translate("MainWindow", "Select only array index:"))
        self.arrayIndices.setPrefix(_translate("MainWindow", "Ch: "))
        self.allColumnCheckBox.setText(_translate("MainWindow", "Select all indices"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Tools"))
        self.menuHelp_2.setTitle(_translate("MainWindow", "Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionReset.setText(_translate("MainWindow", "Reset inputs and filters"))
        self.actionReset.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionOpen_2.setText(_translate("MainWindow", "&Open"))
        self.actionData_request.setText(_translate("MainWindow", "STIX Data Query"))
        self.actionAbout.setText(_translate("MainWindow", "&About"))
        self.actionCreatePyTemplate.setText(_translate("MainWindow", "&Create python template"))
