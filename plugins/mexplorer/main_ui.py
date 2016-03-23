# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(766, 479)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/mexplorer.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(_fromUtf8("QWidget {\n"
"background-color: #2c3e50;\n"
"color: #bdc3c7;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"     border: 1px outset;\n"
"     border-color: #0F2D40;\n"
"     width: 10px;\n"
"     margin: 22px 0 22px 0;\n"
" }\n"
" QScrollBar::handle:vertical {\n"
"     background: #95a5a6;\n"
"     min-height: 20px;\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: 1px outset;\n"
"     border-color: #0F2D40;\n"
"     background: #95a5a6;\n"
"     height: 16px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:vertical {\n"
"     border: 1px outset;\n"
"     border-color: #0F2D40;\n"
"     background: #95a5a6;\n"
"     height: 16px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     width: 3px;\n"
"     height: 3px;\n"
"     background: white;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar:horizontal {\n"
"border: 1px outset;\n"
"     border-color: #0F2D40;\n"
"     height: 10px;\n"
"     margin: 0px 40px 0 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #95a5a6;\n"
"    min-width: 20px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    border: 1px outset;\n"
"    border-color: #0F2D40;\n"
"    background: #95a5a6;\n"
"    width: 16px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: 1px outset;\n"
"    border-color: #0F2D40;\n"
"    background: #95a5a6;\n"
"    width: 16px;\n"
"    subcontrol-position: top right;\n"
"    subcontrol-origin: margin;\n"
"    position: absolute;\n"
"    right: 20px;\n"
"}\n"
"\n"
"QScrollBar:left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"    width: 3px;\n"
"    height: 3px;\n"
"    background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}"))
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.explorerDrivesDrop = QtGui.QComboBox(Form)
        self.explorerDrivesDrop.setMinimumSize(QtCore.QSize(50, 0))
        self.explorerDrivesDrop.setMaximumSize(QtCore.QSize(50, 32))
        self.explorerDrivesDrop.setBaseSize(QtCore.QSize(0, 0))
        self.explorerDrivesDrop.setStyleSheet(_fromUtf8("border: 1px ridge;\n"
"border-color: #2c3e50;\n"
"height: 15px;\n"
"font-size: 12px;\n"
"background-color: #34495e;"))
        self.explorerDrivesDrop.setObjectName(_fromUtf8("explorerDrivesDrop"))
        self.horizontalLayout_2.addWidget(self.explorerDrivesDrop)
        self.line_4 = QtGui.QFrame(Form)
        self.line_4.setStyleSheet(_fromUtf8(""))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.horizontalLayout_2.addWidget(self.line_4)
        self.refreshButton = QtGui.QPushButton(Form)
        self.refreshButton.setMinimumSize(QtCore.QSize(28, 28))
        self.refreshButton.setMaximumSize(QtCore.QSize(28, 28))
        self.refreshButton.setStyleSheet(_fromUtf8("QPushButton#refreshButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            border-right: none;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#refreshButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.refreshButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refreshButton.setIcon(icon1)
        self.refreshButton.setIconSize(QtCore.QSize(18, 18))
        self.refreshButton.setObjectName(_fromUtf8("refreshButton"))
        self.horizontalLayout_2.addWidget(self.refreshButton)
        self.upButton = QtGui.QPushButton(Form)
        self.upButton.setMinimumSize(QtCore.QSize(28, 28))
        self.upButton.setMaximumSize(QtCore.QSize(28, 28))
        self.upButton.setStyleSheet(_fromUtf8("QPushButton#upButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            border-left: none;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#upButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.upButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/up.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.upButton.setIcon(icon2)
        self.upButton.setIconSize(QtCore.QSize(18, 18))
        self.upButton.setObjectName(_fromUtf8("upButton"))
        self.horizontalLayout_2.addWidget(self.upButton)
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_2.addWidget(self.line)
        self.downloadButton = QtGui.QPushButton(Form)
        self.downloadButton.setMinimumSize(QtCore.QSize(28, 28))
        self.downloadButton.setMaximumSize(QtCore.QSize(28, 28))
        self.downloadButton.setStyleSheet(_fromUtf8("QPushButton#downloadButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            border-right: none;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#downloadButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.downloadButton.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/update.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.downloadButton.setIcon(icon3)
        self.downloadButton.setIconSize(QtCore.QSize(18, 18))
        self.downloadButton.setObjectName(_fromUtf8("downloadButton"))
        self.horizontalLayout_2.addWidget(self.downloadButton)
        self.uploadButton = QtGui.QPushButton(Form)
        self.uploadButton.setMinimumSize(QtCore.QSize(28, 28))
        self.uploadButton.setMaximumSize(QtCore.QSize(28, 28))
        self.uploadButton.setStyleSheet(_fromUtf8("QPushButton#uploadButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            border-left: none;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#uploadButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.uploadButton.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/upload.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uploadButton.setIcon(icon4)
        self.uploadButton.setIconSize(QtCore.QSize(18, 18))
        self.uploadButton.setObjectName(_fromUtf8("uploadButton"))
        self.horizontalLayout_2.addWidget(self.uploadButton)
        self.line_2 = QtGui.QFrame(Form)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout_2.addWidget(self.line_2)
        self.executeButton = QtGui.QPushButton(Form)
        self.executeButton.setMinimumSize(QtCore.QSize(28, 28))
        self.executeButton.setMaximumSize(QtCore.QSize(28, 28))
        self.executeButton.setStyleSheet(_fromUtf8("QPushButton#executeButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            border-right: none;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#executeButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.executeButton.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/execute.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.executeButton.setIcon(icon5)
        self.executeButton.setIconSize(QtCore.QSize(18, 18))
        self.executeButton.setObjectName(_fromUtf8("executeButton"))
        self.horizontalLayout_2.addWidget(self.executeButton)
        self.openFolderButton = QtGui.QPushButton(Form)
        self.openFolderButton.setMinimumSize(QtCore.QSize(28, 28))
        self.openFolderButton.setMaximumSize(QtCore.QSize(28, 28))
        self.openFolderButton.setStyleSheet(_fromUtf8("QPushButton#openFolderButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            border-right: none;\n"
"            border-left: none;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#openFolderButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.openFolderButton.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.openFolderButton.setIcon(icon6)
        self.openFolderButton.setIconSize(QtCore.QSize(18, 18))
        self.openFolderButton.setObjectName(_fromUtf8("openFolderButton"))
        self.horizontalLayout_2.addWidget(self.openFolderButton)
        self.renameButton = QtGui.QPushButton(Form)
        self.renameButton.setMinimumSize(QtCore.QSize(28, 28))
        self.renameButton.setMaximumSize(QtCore.QSize(28, 28))
        self.renameButton.setStyleSheet(_fromUtf8("QPushButton#renameButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            border-right: none;\n"
"            border-left: none;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#renameButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.renameButton.setText(_fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/rename.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.renameButton.setIcon(icon7)
        self.renameButton.setIconSize(QtCore.QSize(18, 18))
        self.renameButton.setObjectName(_fromUtf8("renameButton"))
        self.horizontalLayout_2.addWidget(self.renameButton)
        self.deleteButton = QtGui.QPushButton(Form)
        self.deleteButton.setMinimumSize(QtCore.QSize(28, 28))
        self.deleteButton.setMaximumSize(QtCore.QSize(28, 28))
        self.deleteButton.setStyleSheet(_fromUtf8("QPushButton#deleteButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            border-left: none;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#deleteButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.deleteButton.setText(_fromUtf8(""))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/remove.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteButton.setIcon(icon8)
        self.deleteButton.setIconSize(QtCore.QSize(18, 18))
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.horizontalLayout_2.addWidget(self.deleteButton)
        self.line_3 = QtGui.QFrame(Form)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.horizontalLayout_2.addWidget(self.line_3)
        self.hideButton = QtGui.QPushButton(Form)
        self.hideButton.setMinimumSize(QtCore.QSize(28, 28))
        self.hideButton.setMaximumSize(QtCore.QSize(28, 28))
        self.hideButton.setStyleSheet(_fromUtf8("QPushButton#hideButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            border-right: none;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#hideButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.hideButton.setText(_fromUtf8(""))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/hidden.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.hideButton.setIcon(icon9)
        self.hideButton.setIconSize(QtCore.QSize(18, 18))
        self.hideButton.setObjectName(_fromUtf8("hideButton"))
        self.horizontalLayout_2.addWidget(self.hideButton)
        self.unhideButton = QtGui.QPushButton(Form)
        self.unhideButton.setMinimumSize(QtCore.QSize(28, 28))
        self.unhideButton.setMaximumSize(QtCore.QSize(28, 28))
        self.unhideButton.setStyleSheet(_fromUtf8("QPushButton#unhideButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            border-left: none;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#unhideButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.unhideButton.setText(_fromUtf8(""))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/unhide.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.unhideButton.setIcon(icon10)
        self.unhideButton.setIconSize(QtCore.QSize(18, 18))
        self.unhideButton.setObjectName(_fromUtf8("unhideButton"))
        self.horizontalLayout_2.addWidget(self.unhideButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.explorerPathEntry = QtGui.QLineEdit(Form)
        self.explorerPathEntry.setMinimumSize(QtCore.QSize(0, 28))
        self.explorerPathEntry.setStyleSheet(_fromUtf8("border: 1px ridge;\n"
"border-color: #2c3e50;\n"
"height: 15px;\n"
"font-size: 12px;\n"
"background-color: #34495e;"))
        self.explorerPathEntry.setText(_fromUtf8(""))
        self.explorerPathEntry.setObjectName(_fromUtf8("explorerPathEntry"))
        self.verticalLayout.addWidget(self.explorerPathEntry)
        self.explorerTable = QtGui.QTableWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.explorerTable.sizePolicy().hasHeightForWidth())
        self.explorerTable.setSizePolicy(sizePolicy)
        self.explorerTable.setFocusPolicy(QtCore.Qt.NoFocus)
        self.explorerTable.setAcceptDrops(True)
        self.explorerTable.setStyleSheet(_fromUtf8("QHeaderView::section {\n"
"    background-color: #34495e;\n"
"    padding: 2px;\n"
"    color: #bdc3c7;\n"
"    font: 75 8pt \"MS Shell Dlg 2\";\n"
"    border: 1px ridge;\n"
"    border-right: none;\n"
"    border-color: #2c3e50;\n"
"}\n"
"\n"
"QTableWidget#explorerTable {\n"
"    background-position: center;\n"
"    border: 1px ridge;\n"
"    padding: 5px;\n"
"    color: #ecf0f1;\n"
"    border-color: #2c3e50;\n"
"    font: 8pt \"MS Shell Dlg 2\";\n"
"    background-color: #34495e;\n"
"}\n"
"\n"
"QTableWidget#explorerTable:item:selected {\n"
"background-color: #2c3e50;\n"
"color: #f1c40f;\n"
"}"))
        self.explorerTable.setFrameShape(QtGui.QFrame.StyledPanel)
        self.explorerTable.setFrameShadow(QtGui.QFrame.Plain)
        self.explorerTable.setLineWidth(1)
        self.explorerTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.explorerTable.setProperty("showDropIndicator", False)
        self.explorerTable.setDragDropOverwriteMode(False)
        self.explorerTable.setAlternatingRowColors(False)
        self.explorerTable.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.explorerTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.explorerTable.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.explorerTable.setShowGrid(False)
        self.explorerTable.setGridStyle(QtCore.Qt.DotLine)
        self.explorerTable.setWordWrap(False)
        self.explorerTable.setCornerButtonEnabled(True)
        self.explorerTable.setObjectName(_fromUtf8("explorerTable"))
        self.explorerTable.setColumnCount(4)
        self.explorerTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.explorerTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.explorerTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.explorerTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.explorerTable.setHorizontalHeaderItem(3, item)
        self.explorerTable.horizontalHeader().setVisible(True)
        self.explorerTable.horizontalHeader().setCascadingSectionResizes(True)
        self.explorerTable.horizontalHeader().setDefaultSectionSize(50)
        self.explorerTable.horizontalHeader().setHighlightSections(True)
        self.explorerTable.horizontalHeader().setSortIndicatorShown(False)
        self.explorerTable.horizontalHeader().setStretchLastSection(True)
        self.explorerTable.verticalHeader().setVisible(False)
        self.explorerTable.verticalHeader().setCascadingSectionResizes(False)
        self.verticalLayout.addWidget(self.explorerTable)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.fileLabel = QtGui.QLabel(Form)
        self.fileLabel.setMaximumSize(QtCore.QSize(16777215, 15))
        self.fileLabel.setStyleSheet(_fromUtf8("color: #ecf0f1;"))
        self.fileLabel.setObjectName(_fromUtf8("fileLabel"))
        self.horizontalLayout_5.addWidget(self.fileLabel)
        self.dirLabel = QtGui.QLabel(Form)
        self.dirLabel.setMaximumSize(QtCore.QSize(16777215, 15))
        self.dirLabel.setStyleSheet(_fromUtf8("color: #e67e22;"))
        self.dirLabel.setObjectName(_fromUtf8("dirLabel"))
        self.horizontalLayout_5.addWidget(self.dirLabel)
        self.hfileLabel = QtGui.QLabel(Form)
        self.hfileLabel.setMaximumSize(QtCore.QSize(16777215, 15))
        self.hfileLabel.setStyleSheet(_fromUtf8("color: #9b59b6;"))
        self.hfileLabel.setObjectName(_fromUtf8("hfileLabel"))
        self.horizontalLayout_5.addWidget(self.hfileLabel)
        self.hdirLabel = QtGui.QLabel(Form)
        self.hdirLabel.setMaximumSize(QtCore.QSize(16777215, 15))
        self.hdirLabel.setStyleSheet(_fromUtf8("color: #3498db;"))
        self.hdirLabel.setObjectName(_fromUtf8("hdirLabel"))
        self.horizontalLayout_5.addWidget(self.hdirLabel)
        self.selectedLabel = QtGui.QLabel(Form)
        self.selectedLabel.setStyleSheet(_fromUtf8("color: #f1c40f;"))
        self.selectedLabel.setObjectName(_fromUtf8("selectedLabel"))
        self.horizontalLayout_5.addWidget(self.selectedLabel)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.dirfilesLabel = QtGui.QLabel(Form)
        self.dirfilesLabel.setObjectName(_fromUtf8("dirfilesLabel"))
        self.horizontalLayout_5.addWidget(self.dirfilesLabel)
        self.dirfilesCountLabel = QtGui.QLabel(Form)
        self.dirfilesCountLabel.setObjectName(_fromUtf8("dirfilesCountLabel"))
        self.horizontalLayout_5.addWidget(self.dirfilesCountLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.progressBar = QtGui.QProgressBar(Form)
        self.progressBar.setStyleSheet(_fromUtf8("QProgressBar:horizontal {\n"
"border: 1px ridge;\n"
"border-color: #2c3e50;\n"
"background-color: #34495e;\n"
"padding: 1px;\n"
"text-align: top;\n"
"}\n"
"QProgressBar::chunk:horizontal {\n"
"background: #1abc9c;\n"
"margin-right: 1px;\n"
"width: 5px;\n"
"}"))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.horizontalLayout.addWidget(self.progressBar)
        self.cancelButton = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelButton.sizePolicy().hasHeightForWidth())
        self.cancelButton.setSizePolicy(sizePolicy)
        self.cancelButton.setMinimumSize(QtCore.QSize(70, 25))
        self.cancelButton.setMaximumSize(QtCore.QSize(70, 16777215))
        self.cancelButton.setStyleSheet(_fromUtf8("QPushButton#cancelButton {\n"
"            border: 1px ridge;\n"
"            border-color: #2c3e50;\n"
"            padding: 2px;\n"
"            background-color: #34495e;\n"
"            }\n"
"\n"
"QPushButton#cancelButton:pressed {\n"
"            background-color: #2c3e50;\n"
"            }"))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.explorerTable.setSortingEnabled(False)
        item = self.explorerTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Type", None))
        item = self.explorerTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Name", None))
        item = self.explorerTable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Date Modified", None))
        item = self.explorerTable.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Size", None))
        self.fileLabel.setText(_translate("Form", "File", None))
        self.dirLabel.setText(_translate("Form", "Directory", None))
        self.hfileLabel.setText(_translate("Form", "Hidden File", None))
        self.hdirLabel.setText(_translate("Form", "Hidden Directory", None))
        self.selectedLabel.setText(_translate("Form", "Selected", None))
        self.dirfilesLabel.setText(_translate("Form", "Directories / Files:", None))
        self.dirfilesCountLabel.setText(_translate("Form", "0", None))
        self.progressBar.setFormat(_translate("Form", "%p%", None))
        self.cancelButton.setText(_translate("Form", "Cancel", None))
