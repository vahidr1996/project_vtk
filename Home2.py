import sys
import vtk
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import vtk
from PyQt5 import QtCore
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import*
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from PyQt5.QtWidgets import QDialog, QApplication
import math
from PyQt5 import QtCore, QtGui, QtWidgets
from vedo import *
import numpy as np
import implant_points  

class timer():
    def repeat(self,obj,event):
      iren = obj
      iren.GetRenderWindow().Render()
class timer_S():
    def repeat(self,obj,event):
      iren_S = obj
      iren_S.GetRenderWindow().Render()
   

class Ui_MainWindow(QMainWindow):
    def setupUi(self,MainWindow):
        #print(MainWindow)
        print(self) 
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 700) 

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/download.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    ################################################################# 
        MainWindow.setWindowIcon(icon)
    
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setItalic(False)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
     #######################################################
       
       
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 1401, 671))
        self.tabWidget.setStyleSheet(""" QTabBar::tab {
        padding:10px;
        margin:0;
        background: black;
        color:white;
        width:210%;
       
        
        
                             }
                             
        QTabBar::tab:selected{
        background:white;
        color:black;
        
        } 
        QTabBar::tab:hover{
        background:grey;
        }

        
        """)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setDocumentMode(True)
        #self.listtab=[self.tabWidget]
        
        
    ################################################### 
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.tab_1.setStyleSheet("background-color:  #91989c;")
        

     #####################################################
        self.frame_left = QtWidgets.QFrame(self.tab_1)
        self.frame_left.setGeometry(QtCore.QRect(-1, 9, 841, 621))
        self.frame_left.setStyleSheet("background-color: black;")
        self.frame_left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left.setObjectName("frame_left")
        self.frame_2 = QtWidgets.QFrame(self.tab_1)
        self.frame_2.setGeometry(QtCore.QRect(859, 9, 521, 201))
        self.frame_2.setStyleSheet("background-color: black;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.tab_1)
        self.frame_3.setGeometry(QtCore.QRect(859, 220, 521, 201))
        self.frame_3.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_4 = QtWidgets.QFrame(self.tab_1)
        self.frame_4.setGeometry(QtCore.QRect(859, 430, 521, 201))
        self.frame_4.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.tabWidget.addTab(self.tab_1, "")
     #################################################################################################
        
        
        
          
       
        self.tab_2 = QtWidgets.QWidget()
        
        self.tab_2.setObjectName("tab_2")
        self.tab_2.setStyleSheet("background-color: black;")  
        self.tabWidget.addTab(self.tab_2, "") 
        
        

       
        
     ##########################################################
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        
        self.tabWidget.currentChanged.connect(self.change_tab)  

        #if self.tabWidget.currentIndex()==0:
       
              
        self.frame_rom = QtWidgets.QFrame( self.centralwidget)
        self.frame_rom.setGeometry(QtCore.QRect(10, 39, 1400, 671))
        self.frame_rom.setStyleSheet("background-color: black;")
        self.frame_rom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_rom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_rom.setObjectName("frame_5")
        self.frame_rom.hide()
        self.vtkWidget_R = QVTKRenderWindowInteractor(self.frame_rom)
        self.vl = QVBoxLayout() 
        self.vl.addWidget(self.vtkWidget_R)
        self.frame_rom.setLayout(self.vl)
#########################################################################################
        #animation
        self.label_ar1 = QtWidgets.QLabel(self.frame_rom)
        self.label_ar1.setGeometry(QtCore.QRect(665, 60, 51, 61))
        self.label_ar1.setText("")
        self.label_ar1.setPixmap(QtGui.QPixmap("icon/arrow.png"))
        self.label_ar1.setScaledContents(True)
        self.label_ar1.hide()

        self.frame_tx1 = QtWidgets.QFrame( self.frame_rom)
        self.frame_tx1.setGeometry(QtCore.QRect(570,120, 240,60))
        self.frame_tx1.setStyleSheet("background-color: orange;"
        "border-radius: 10px;")
        self.frame_tx1.hide()
        

        self.label_tx1 = QtWidgets.QLabel(self.frame_tx1)
        self.label_tx1.setGeometry(QtCore.QRect(30, 0,180, 60))
        self.label_tx1.setText("1-Select the point key")
        self.label_tx1.setStyleSheet("color: white;"
        "font: 18px ;")
        
        self.frame_tx2 = QtWidgets.QFrame( self.frame_rom)
        self.frame_tx2.setGeometry(QtCore.QRect(450,120, 500,60))
        self.frame_tx2.setStyleSheet("background-color: orange;"
        "border-radius: 10px;")
        self.frame_tx2.hide()
        

        self.label_tx2 = QtWidgets.QLabel(self.frame_tx2)
        self.label_tx2.setGeometry(QtCore.QRect(20, 0,480, 60))
        self.label_tx2.setText("2-Point the surface of the pelvis to design the shelf implant ")
        self.label_tx2.setStyleSheet("color: white;"
        "font: 18px ;")


        self.label_ar2 = QtWidgets.QLabel(self.frame_rom)
        self.label_ar2.setGeometry(QtCore.QRect(712, 60, 51, 61))
        self.label_ar2.setText("")
        self.label_ar2.setPixmap(QtGui.QPixmap("icon/arrow.png"))
        self.label_ar2.setScaledContents(True)
        self.label_ar2.hide()

        self.frame_tx3 = QtWidgets.QFrame( self.frame_rom)
        self.frame_tx3.setGeometry(QtCore.QRect(630,130, 240,60))
        self.frame_tx3.setStyleSheet("background-color: orange;"
        "border-radius: 10px;")
        self.frame_tx3.hide()
        

        self.label_tx3 = QtWidgets.QLabel(self.frame_tx3)
        self.label_tx3.setGeometry(QtCore.QRect(30, 0,180, 60))
        self.label_tx3.setText("3-Select the spline key")
        self.label_tx3.setStyleSheet("color: white;"
        "font: 18px ;")


        self.label_ar3 = QtWidgets.QLabel(self.frame_rom)
        self.label_ar3.setGeometry(QtCore.QRect(760, 60, 51, 61))
        self.label_ar3.setText("")
        self.label_ar3.setPixmap(QtGui.QPixmap("icon/arrow.png"))
        self.label_ar3.setScaledContents(True)
        self.label_ar3.hide()

        self.frame_tx4 = QtWidgets.QFrame( self.frame_rom)
        self.frame_tx4.setGeometry(QtCore.QRect(670,130, 240,60))
        self.frame_tx4.setStyleSheet("background-color: orange;"
        "border-radius: 10px;")
        self.frame_tx4.hide()
        

        self.label_tx3 = QtWidgets.QLabel(self.frame_tx4)
        self.label_tx3.setGeometry(QtCore.QRect(30, 0,195, 60))
        self.label_tx3.setText("4-Select the extrude key")
        self.label_tx3.setStyleSheet("color: white;"
        "font: 18px ;")

        # font = QtGui.QFont()
        # font.setFamily("Tahoma")
        # font.setPointSize(12)
        
        
        # self.frame_s = QtWidgets.QFrame(self.tab_3)
        # self.frame_s.setGeometry(QtCore.QRect(-1, 9, 1347, 627))
        # self.frame_s.setStyleSheet("background-color: rgb(0, 0, 0);")
        # self.frame_s.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_s.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_s.setObjectName("frame_s")
        # self.vtkWidget_S = QVTKRenderWindowInteractor(self.frame_s)
        # self.vl = QVBoxLayout() 
        # self.vl.addWidget(self.vtkWidget_R)
        # self.frame_s.setLayout(self.vl)
     
       
        
       
       
        #if self.tabWidget.currentIndex()==0:
     
       
      
     ##############################################################3   

        self.frame_6 = QtWidgets.QFrame(self.frame_rom)
        self.frame_6.setGeometry(QtCore.QRect(300, 0,800, 60))
        #self.frame_6.setStyleSheet("background-color: blue;")

        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.frame_6.hide()

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame_6)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 700,45))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
       #کلید زوم اوت
        self.pushButton_zoomout = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_zoomout.setEnabled(True)
        self.pushButton_zoomout.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_zoomout.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_zoomout.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton_zoomout.setAutoFillBackground(False)
        self.pushButton_zoomout.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icon/zoom out-512 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_zoomout.setIcon(icon4)
        self.pushButton_zoomout.setStyleSheet("background-color: #91989c;\n"
         "border-radius:20px;\n"
         "padding:5px")
        self.pushButton_zoomout.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_zoomout.setObjectName("pushButton_zoomout")
        self.horizontalLayout.addWidget(self.pushButton_zoomout)
        #self.pushButton_zoomout.clicked.connect(self.file_zoomout)
 
        #کلید زوم این
        self.pushButton_zoomin = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_zoomin.setText("")
        self.pushButton_zoomin.setStyleSheet("background-color: #91989c;\n"
         "border-radius:20px;\n"
         "padding:5px")
        #self.pushButton_zoomin.setStyleSheet("border-style:solid; ")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icon/zoom-in-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_zoomin.setIcon(icon5)
        self.pushButton_zoomin.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_zoomin.setObjectName("pushButton_zoomin")
        self.horizontalLayout.addWidget(self.pushButton_zoomin)
        #self.pushButton_zoomin.clicked.connect(self.file_zoomin)

        #کلید نمای چپ
        self.pushButton_left = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_left.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icon/__view_3d_prespective_tool_modeling_cube_left-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_left.setIcon(icon6)
        self.pushButton_left.setStyleSheet("background-color: #91989c;\n"
         "border-radius:20px;\n"
         "padding:5px")
        self.pushButton_left.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_left.setObjectName("pushButton_left")
        #self.pushButton_left.clicked.connect(self.Left)
        self.horizontalLayout.addWidget(self.pushButton_left)

        #کلید نمای راست
        self.pushButton_right = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_right.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icon/__view_3d_prespective_tool_modeling_cube_right-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_right.setIcon(icon7)
        self.pushButton_right.setStyleSheet("background-color: #91989c;\n"
         "border-radius:20px;\n"
         "padding:5px")
        self.pushButton_right.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_right.setObjectName("pushButton_right")
        #self.pushButton_right.clicked.connect(self.Right)
        self.horizontalLayout.addWidget(self.pushButton_right)

        #کلید نمای بالا
        self.pushButton_top = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_top.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icon/__view_3d_prespective_tool_modeling_cube_top-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_top.setIcon(icon8)
        self.pushButton_top.setStyleSheet("background-color: #91989c;\n"
         "border-radius:20px;\n"
         "padding:5px")
        self.pushButton_top.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_top.setObjectName("pushButton_top")
        #self.pushButton_top.clicked.connect(self.Up)
        self.horizontalLayout.addWidget(self.pushButton_top)

        #کلید نمای جلو
        self.pushButton_front = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_front.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icon/__view_3d_prespective_tool_modeling_cube_front-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_front.setIcon(icon9)
        self.pushButton_front.setStyleSheet("background-color: #91989c;\n"
         "border-radius:20px;\n"
         "padding:5px")
        self.pushButton_front.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_front.setAutoDefault(True)
        self.pushButton_front.setObjectName("pushButton")
        #self.pushButton_front.clicked.connect(self.Front)
        self.horizontalLayout.addWidget(self.pushButton_front)

        #کلید چرخش
        self.pushButton_rotate = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_rotate.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("icon/Rotate-Right-Direction-Reload-Repeat-Rotation-Arrow-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_rotate.setIcon(icon12)
        self.pushButton_rotate.setStyleSheet("background-color: #91989c;\n"
         "border-radius:20px;\n"
         "padding:5px")
        self.pushButton_rotate.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_rotate.setObjectName("pushButton_12")
        #self.pushButton_rotate.clicked.connect(self.file_rot)  
        self.horizontalLayout.addWidget(self.pushButton_rotate)

        self.frame_7 = QtWidgets.QFrame(self.centralwidget)
        self.frame_7.setGeometry(QtCore.QRect(10, 40, 91, 211))
        #self.frame_7.setStyleSheet("background-color: #ff9626;")
        self.frame_7.setObjectName("frame_7")
        self.frame_7.hide()

        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame_7)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 71, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        #کلید باز کردن فایل
        self.pushButton_open = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_open.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/62917-open-file-folder-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_open.setIcon(icon1)
        self.pushButton_open.setStyleSheet("background-color: #91989c;\n"
         "border-radius:20px;\n"
         "padding:5px")
        self.pushButton_open.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_open.setFlat(False)
        self.pushButton_open.setObjectName("pushButton_open")
        self.verticalLayout.addWidget(self.pushButton_open)
        #self.pushButton_open.clicked.connect(self.file_open)

        #کلید ذخیره فایل
        self.pushButton_save = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_save.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/save-icon-9.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_save.setIcon(icon2)
        self.pushButton_save.setStyleSheet("background-color: #91989c;\n"
         "border-radius:20px;\n"
         "padding:5px")
        self.pushButton_save.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_save.setObjectName("pushButton_save")
        self.verticalLayout.addWidget(self.pushButton_save)

       #کلید خروج برنامه
        self.pushButton_exit = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_exit.setText("")
        self.pushButton_exit.setStyleSheet("background-color: #91989c;\n"
         "border-radius:20px;\n"
         "padding:5px")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icon/Actions-window-close-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_exit.setIcon(icon3)
        self.pushButton_exit.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.verticalLayout.addWidget(self.pushButton_exit)
#########################################################################
       #کلید نقطه
        self.pushButton_point = QtWidgets.QPushButton(self.horizontalLayoutWidget)
       # self.pushButton_point.setGeometry(QtCore.QRect(320, 180, 75, 141))
        self.pushButton_point.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_point.setCheckable(True)
        self.pushButton_point.setText("")
        self.pushButton_point.setStyleSheet("background-color: #91989c;\n"
         "border-radius:20px;\n"
         "padding:5px;\n"
         )
        icon_p= QtGui.QIcon()
        icon_p.addPixmap(QtGui.QPixmap("icon/dot-png-images-free-download-167838.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_point.setIcon(icon_p)
        self.pushButton_point.setIconSize(QtCore.QSize(40, 40))
        self.horizontalLayout.addWidget(self.pushButton_point)
###########################################################################
       #کلید اسپیلاین
        self.pushButton_spline = QtWidgets.QPushButton(self.horizontalLayoutWidget)
       # self.pushButton_point.setGeometry(QtCore.QRect(320, 180, 75, 141))
        self.pushButton_spline.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_spline.setCheckable(True)
        self.pushButton_spline.setText("")
        self.pushButton_spline.setStyleSheet("background-color: #91989c;\n"
         "border-radius:20px;\n"
         "padding:5px;\n"
         )
        icon_spline= QtGui.QIcon()
        icon_spline.addPixmap(QtGui.QPixmap("icon/spline.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_spline.setIcon(icon_spline)
        self.pushButton_spline.setIconSize(QtCore.QSize(40, 40))
        self.horizontalLayout.addWidget( self.pushButton_spline)  
        #کلید خط
       # self.pushButton_line = QtWidgets.QPushButton(self.horizontalLayoutWidget)
       # self.pushButton_point.setGeometry(QtCore.QRect(320, 180, 75, 141))
      #  self.pushButton_line.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
      #  self.pushButton_line.setCheckable(True)
      #  self.pushButton_line.setText("")
      #  self.pushButton_line.setStyleSheet("background-color: #91989c;\n"
      #   "border-radius:20px;\n"
      #   "padding:5px;\n"
      #   )
      #  icon_l= QtGui.QIcon()
      #  icon_l.addPixmap(QtGui.QPixmap("icon/line.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
      #  self.pushButton_line.setIcon(icon_l)
      #  self.pushButton_line.setIconSize(QtCore.QSize(40, 40))
      #  self.horizontalLayout.addWidget( self.pushButton_line)        
################################################################################

        #کلید اکسترود
        self.pushButton_extrude = QtWidgets.QPushButton(self.horizontalLayoutWidget)
       # self.pushButton_point.setGeometry(QtCore.QRect(320, 180, 75, 141))
        self.pushButton_extrude.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_extrude.setCheckable(True)
        self.pushButton_extrude.setText("")
        self.pushButton_extrude.setStyleSheet("background-color: #91989c;\n"
         "border-radius:20px;\n"
         "padding:5px;\n"
         )
        icon_ext= QtGui.QIcon()
        icon_ext.addPixmap(QtGui.QPixmap("icon/extrude.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_extrude.setIcon(icon_ext)
        self.pushButton_extrude.setIconSize(QtCore.QSize(40, 40))
        self.horizontalLayout.addWidget( self.pushButton_extrude)  
###################################################################################
        #کلید خط کش
        self.pushButton_ruler = QtWidgets.QPushButton(self.horizontalLayoutWidget)
       # self.pushButton_point.setGeometry(QtCore.QRect(320, 180, 75, 141))
        self.pushButton_ruler.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_ruler.setCheckable(True)
        self.pushButton_ruler.setText("")
        self.pushButton_ruler.setStyleSheet("background-color: #91989c;\n"
         "border-radius:20px;\n"
         "padding:5px;\n"
         )
        icon_ruler= QtGui.QIcon()
        icon_ruler.addPixmap(QtGui.QPixmap("icon/ruler.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_ruler.setIcon(icon_ruler)
        self.pushButton_ruler.setIconSize(QtCore.QSize(40, 40))
        self.horizontalLayout.addWidget( self.pushButton_ruler)  
        ######################################################################

        #کلید زاویه
        self.pushButton_angle = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_angle.setGeometry(QtCore.QRect(320, 180, 75, 141))
        self.pushButton_angle.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_angle.setCheckable(True)
        self.pushButton_angle.setText("")
        self.pushButton_angle.setStyleSheet("background-color: #91989c;\n"
         "border-radius:20px;\n"
         "padding:5px;\n"
         )
        icon_ang= QtGui.QIcon()
        icon_ang.addPixmap(QtGui.QPixmap("icon/angle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_angle.setIcon(icon_ang)
        self.pushButton_angle.setIconSize(QtCore.QSize(40, 40))
        self.horizontalLayout.addWidget( self.pushButton_angle)  



       
        ##########################################################
        #کلید برش
        self.pushButton_cut = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_cut.setGeometry(QtCore.QRect(320, 180, 75, 141))
        self.pushButton_cut.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_cut.setCheckable(True)
        self.pushButton_cut.setText("")
        self.pushButton_cut.setStyleSheet("background-color: #91989c;\n"
         "border-radius:20px;\n"
         "padding:5px;\n"
         )
        icon_cut= QtGui.QIcon()
        icon_cut.addPixmap(QtGui.QPixmap("icon/cut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_cut.setIcon(icon_cut)
        self.pushButton_cut.setIconSize(QtCore.QSize(40, 40))
        self.horizontalLayout.addWidget( self.pushButton_cut)  





        ##########################################################
             #کلید ani
        self.pushButton_ani = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_ani.setGeometry(QtCore.QRect(320, 180, 75, 141))
        self.pushButton_ani.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_ani.setCheckable(True)
        self.pushButton_ani.setText("")
        self.pushButton_ani.setStyleSheet("background-color: #91989c;\n"
         "border-radius:20px;\n"
         "padding:5px;\n"
         )
        icon_ani= QtGui.QIcon()
        icon_ani.addPixmap(QtGui.QPixmap("icon/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_ani.setIcon(icon_ani)
        self.pushButton_ani.setIconSize(QtCore.QSize(40, 40))
        self.horizontalLayout.addWidget( self.pushButton_ani)  
        self.pushButton_ani.clicked.connect(self.file_ani) 

        
        ########################################################################
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tabWidget.addTab(self.tab_6, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1400, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)
        #self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bio_Mechanic"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Home"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "ROM"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "FAI"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "THR"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Shelf Implant"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Guid"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
    def change_tab(self):
        print(self.tabWidget.currentIndex())
        if self.tabWidget.currentIndex()==0:
           self.tabWidget.setGeometry(QtCore.QRect(10, 0, 1401, 671))
           self.frame_rom.hide()
           self.frame_6.hide()
           self.frame_7.hide()
           

        if self.tabWidget.currentIndex()>=1:
           self.tabWidget.setGeometry(QtCore.QRect(10, 0, 1401, 40))
           self.frame_rom.show()

        if self.tabWidget.currentIndex()==1:
           self.frame_6.show()
           self.frame_7.show()
           
        

        if self.tabWidget.currentIndex()>1:
           self.frame_6.hide() 
           self.frame_7.hide()
    def file_ani(self):
            
            self.label_ar1.show()
            self.frame_tx1.show()
            self.timer = QTimer()
            self.timer.timeout.connect(self.lab1_hide)
            self.timer.start(5*1000)

    def lab1_hide(self):
            self.label_ar1.hide()
            self.frame_tx1.hide()
            self.frame_tx2.show()
            self.timer.timeout.connect(self.lab2_hide)
            self.timer.start(8*1000)
    def lab2_hide(self):
            self.frame_tx2.hide()
            self.label_ar2.show()
            self.frame_tx3.show()
            self.timer.timeout.connect(self.lab3_hide)
            self.timer.start(8*1000)
    def lab3_hide(self):
            self.label_ar2.hide()
            self.frame_tx3.hide()
            self.label_ar3.show()
            self.frame_tx4.show()
            self.timer.timeout.connect(self.lab4_hide)
            self.timer.start(5*1000)
    def lab4_hide(self):
            self.label_ar3.hide()
            self.frame_tx4.hide()        

    # d ef fun(self):
    #    #print(setupUi(self))
    #    #self.s.tabWidget
           
    #    #global tabWidget
    #    if self.tabWidget.currentIndex()==0:
    #        print("ok")
    #        self.frame_S = QtWidgets.QFrame(self.tab_3)
    #        self.frame_S.setGeometry(QtCore.QRect(-1, 9, 1347, 627))
    #        self.frame_S.setStyleSheet("background-color: blue;")
    #        self.frame_S.setFrameShape(QtWidgets.QFrame.StyledPanel)
    #        self.frame_S.setFrameShadow(QtWidgets.QFrame.Raised)
    #        self.frame_S.setObjectName("frame_R")
    #        self.vtkWidget_R = QVTKRenderWindowInteractor(self.frame_S)
    #        self.vl = QVBoxLayout() 
    #        self.vl.addWidget(self.vtkWidget_R)
    #        self.frame_S.setLayout(self.vl)   
    #    if self.tabWidget.currentIndex()==0: 
    #       self.frame_5 = QtWidgets.QFrame(self.tab_2)
    #       self.frame_5.setGeometry(QtCore.QRect(-1, 9, 1347, 627))
    #       self.frame_5.setStyleSheet("background-color: rgb(0, 0, 0);")
    #       self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
    #       self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
    #       self.frame_5.setObjectName("frame_5")
    #       self.vtkWidget_R = QVTKRenderWindowInteractor(self.frame_5)
    #       self.vl = QVBoxLayout() 
    #       self.vl.addWidget(self.vtkWidget_R)
    #       self.frame_5.setLayout(self.vl)
                   
#class Pick_position(vtk.vtkInteractorStyleTrackballCamera):
#    
#    def __init__(self):
#        self.AddObserver("MiddleButtonPressEvent", self.middleButtonPressEvent)
#        self.p=[]
        
       

#    def middleButtonPressEvent(self, obj, event):
        #print(obj)
        #print(event)
        
#        self.clickPos = self.GetInteractor().GetEventPosition()
        #print( self.clickPos)

#        self.picker = vtk.vtkPicker()
#        self.picker.Pick(913, 433, 0, self.GetDefaultRenderer())
#        self.OnMiddleButtonUp
#        self.p1 = self.picker.GetPickPosition()
#        self.p.append(self.p1)
#        print(self.p)
        #self.a=AppWindow()
        #self.a.Front(self.p)
  
        
    
    
    
        
        
class AppWindow(QMainWindow,implant_points.points_spline):
    def __init__(self,parent=None):
        QMainWindow.__init__(self,parent)
        #self.q=QMainWindow()
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self)
        #self.ui.fun()
        #self.ui= Ui_MainWindow()
        #self.ui.setupUi(self)
        #print(self.ui1)
      
     ######################################################################  
        #print(self.sender() is self.ui.tab_2)
        self.style=vtk.vtkInteractorStyleTrackballCamera()

        self.style1=vtk.vtkInteractorStyleTrackballCamera()
        self.style1.AddObserver("LeftButtonPressEvent", self.leftButtonPressEvent_point)

        self.style2=vtk.vtkInteractorStyleTrackballCamera()
        self.style2.AddObserver("LeftButtonPressEvent", self.leftButtonPressEvent_line)

        self.style_hole=vtk.vtkInteractorStyleTrackballCamera()
        self.style_hole.AddObserver("LeftButtonPressEvent", self.leftButtonPressEvent_hole)


     ######################################################################## 

        self.count=-1
        self.count_l=0
        self.count_p=1
        self.count_point=0
        self.count_point1=len(self.list_points_spline)
        self.count_line=1
        self.count_h=1
        self.count_ruler=0
        self.count_angle=0
        self.list1=[]
        self.list2=[]
        self.reader=[]
        self.mapper=[]
        self.actor=[]
        self.readerdi=[]
        self.img=[]
        self.p=[]
        self.listp0=[]
        self.listpoint=[]
        self.listcount_p=[]
        self.listpoint_insert=[]
        self.list_count_spline=[]
        #print(self.list_points_spline.
        for i in range(1,len(self.list_points_spline)+1):
                
                self.list_count_spline.append(i)
            
                #print(i)
            
                 #print(i)
        # obj=0
        # while len(self.list_points_spline)>=136:
           
                
        #         self.list_points_spline.remove( self.list_points_spline[obj+1]) 
        #         obj=obj+1
              
        # #print(self.list_points_spline)   
        # obj=0 
        # while len(self.list_points_spline)>=70:
        #         print(obj)
                
        #         self.list_points_spline.remove( self.list_points_spline[obj+1]) 
        #         obj=obj+1
        # obj=0        
        # while len(self.list_points_spline)>=37:
        #         print(obj)
                
        #         self.list_points_spline.remove( self.list_points_spline[obj+1]) 
        #         obj=obj+1      
        # obj=0        
        # while len(self.list_points_spline)>=20:
        #         print(obj)
                
        #         self.list_points_spline.remove( self.list_points_spline[obj+1]) 
        #         obj=obj+1              
        # #print(self.list_points_spline)      
        # for i in range(1,len(self.list_points_spline)+1):
             
        #          self.list_count_spline.append(i)
        #          print(i)
    
       
################################ #########################################################
         #self.ren1=vtk.vtkRenderer()
        
    
        self.ren=vtk.vtkRenderer()
        self.colors=vtk.vtkNamedColors()
        self.ren.SetBackground(self.colors.GetColor3d("black"))
        #self.ren1.SetBackground(self.colors.GetColor3d("black"))
     
        self.ui.vtkWidget_R.GetRenderWindow().AddRenderer(self.ren)
        #self.ui.vtkWidget_S.GetRenderWindow().AddRenderer(self.ren)
        self.iren=self.ui.vtkWidget_R.GetRenderWindow().GetInteractor()
        self.iren.GetRenderWindow().Render()
        #self.iren=self.ui.vtkWidget_S.GetRenderWindow().GetInteractor()
        self.iren.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())
        
        self.tran=vtk.vtkTransform()
        self.tran.Translate(0,0,0)
        self.axes1=vtk.vtkAxesActor()
        self.axes1.SetTotalLength(70,70,70)
        self.fonts=vtk.vtkTextProperty()
        self.fonts.SetFontSize(1)
        self.axes1.GetXAxisCaptionActor2D().SetCaptionTextProperty(self.fonts)
        self.axes1.GetYAxisCaptionActor2D().SetCaptionTextProperty(self.fonts)
        self.axes1.GetZAxisCaptionActor2D().SetCaptionTextProperty(self.fonts)
          #print(self.axes1.GetXAxisCaptionActor2D())
        self.axes1.SetUserTransform(self.tran)
        self.ren.AddActor(self.axes1)
        self.camera=vtk.vtkCamera()
        self.camera.SetPosition(0,0,-600) 
        self.ren.SetActiveCamera(self.camera)
        # self.ren_S=vtk.vtkRenderer()
        # self.ren_S.SetBackground(self.colors.GetColor3d("black"))
        # self.ui.vtkWidget_S.GetRenderWindow().AddRenderer(self.ren_S)
        # self.iren_S=self.ui.vtkWidget_S.GetRenderWindow().GetInteractor()
        # self.iren_S.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())


        # self.tran=vtk.vtkTransform()
        # self.tran.Translate(0,0,0)
        # self.axes1=vtk.vtkAxesActor()
        # self.axes1.SetTotalLength(70,70,70)
        # self.fonts=vtk.vtkTextProperty()
        # self.fonts.SetFontSize(1)
        # self.axes1.GetXAxisCaptionActor2D().SetCaptionTextProperty(self.fonts)
        # self.axes1.GetYAxisCaptionActor2D().SetCaptionTextProperty(self.fonts)
        # self.axes1.GetZAxisCaptionActor2D().SetCaptionTextProperty(self.fonts)
        #   #print(self.axes1.GetXAxisCaptionActor2D())
        # self.axes1.SetUserTransform(self.tran)
        # self.ren_S.AddActor(self.axes1)
        # self.camera=vtk.vtkCamera()
        # self.camera.SetPosition(0,0,-600) 
        # self.ren_S.SetActiveCamera(self.camera)
        
        #self.style = Pick_position()
        #self.style.SetDefaultRenderer(self.ren)
        #self.iren.SetInteractorStyle(self.style)
        
        
        ###################################################
        self.cb=timer()
        self.iren.AddObserver('TimerEvent', self.cb.repeat)
        self.timerId =self.iren.CreateRepeatingTimer(1)

        # self.cb=timer()
        # self.iren_S.AddObserver('TimerEvent', self.cb.repeat)
        # self.timerId =self.iren_S.CreateRepeatingTimer(1)
        #####################################################
        #self.cb_S=timer_S()
        #self.iren_S.AddObserver('TimerEvent', self.cb_S.repeat)
        #self.timerId =self.iren_S.CreateRepeatingTimer(1)

        #self.tran=vtk.vtkTransform()
        #self.tran.Translate(0,0,0)
        #self.axes1=vtk.vtkAxesActor()
        #self.axes1.SetTotalLength(70,70,70)
        #self.fonts=vtk.vtkTextProperty()
        #self.fonts.SetFontSize(1)
        #self.axes1.GetXAxisCaptionActor2D().SetCaptionTextProperty(self.fonts)
        #self.axes1.GetYAxisCaptionActor2D().SetCaptionTextProperty(self.fonts)
        #self.axes1.GetZAxisCaptionActor2D().SetCaptionTextProperty(self.fonts)
        #print(self.axes1.GetXAxisCaptionActor2D())
        #self.axes1.SetUserTransform(self.tran)
        #self.ren.AddActor(self.axes1)
        #self.camera=vtk.vtkCamera()
        #self.camera.SetPosition(0,0,-600) 
        #self.ren.SetActiveCamera(self.camera)


        ################################################################
        self.planeSource = vtk.vtkPlaneSource()
        self.planeSource.SetPoint1(-14.365364202056908, 12.923931255657825, 22.755638962319335)
        self.planeSource.SetPoint2(-5.493677574222656, 18.97932947910819, 38.13890416897924)
        print(self.planeSource.GetNormal())
        #self.planeSource.SetCenter(0,0,0)
        #self.planeSource.SetNormal(0, 0, -1.0)
        self.planeSource.Update()

         
        self.mapper_plane = vtk.vtkPolyDataMapper()
        self.mapper_plane.SetInputConnection(self.planeSource.GetOutputPort())
        self.actor_plane = vtk.vtkActor()
        self.actor_plane.SetMapper(self.mapper_plane)
        #########################################################################
        #self.ren.AddActor(self.actor_plane)
        #self.sphereSource =vtk.vtkSphereSource()
        #self.sphereSource.SetThetaResolution(20)
        #self.sphereSource.SetPhiResolution(11)
        #self.sphereSource.SetRadius(100) 

        #self.plane = vtk.vtkPlane()
        #self.plane.SetOrigin(0, 0, 0)
        #self.plane.SetNormal(0,0, -1)
        #self.cy=vtk.vtkCylinder()
        #self.cy.SetCenter(0,0,0)
        #self.cy.SetRadius(50)

        #self.clipper = vtk.vtkClipPolyData()
        #self.clipper.SetInputConnection(self.sphereSource.GetOutputPort())
        #self.clipper.SetClipFunction(self.cy)
        #self.clipper.SetValue(0)
        #self.clipper.Update()

        #self.clipMapper = vtk.vtkPolyDataMapper()
        #self.clipMapper.SetInputConnection(self.sphereSource.GetOutputPort())

        #self.clipActor =vtk.vtkActor()
        #self.clipActor.SetMapper(self.clipMapper)
        #self.clipActor.GetProperty().SetColor(1.0000, 0.3882, 0.2784)
        #self.clipActor.GetProperty().SetInterpolationToFlat()
        #self.ren.AddActor(self.clipActor)
          
        self.ui.pushButton_zoomout.clicked.connect(self.file_zoomout)
        self.ui.pushButton_zoomin.clicked.connect(self.file_zoomin) 
        self.ui.pushButton_left.clicked.connect(self.Left)
        self.ui.pushButton_right.clicked.connect(self.Right)
        self.ui.pushButton_top.clicked.connect(self.Up)
        self.ui.pushButton_front.clicked.connect(self.Front)
        self.ui.pushButton_open.clicked.connect(self.file_open)
        self.ui.pushButton_point.clicked.connect(self.file_point)
       # self.ui.pushButton_line.clicked.connect(self.file_line)
        self.ui.pushButton_extrude.clicked.connect(self.file_extrude)
        self.ui.pushButton_spline.clicked.connect(self.file_spline)
        self.ui.pushButton_ruler.clicked.connect(self.file_ruler)
        self.ui.pushButton_angle.clicked.connect(self.file_angle)
        self.ui.pushButton_cut.clicked.connect(self.file_cut) 
        #self.ui.tabWidget.currentChanged.connect(self.fun)  
        
         
        #self.ui.tab_2.clicked.connect(self.tab_h)
        
     #   self.ui.pushButton_hole.clicked.connect(self.file_hole)
  #  def file_hole(self):
   #      self.count_h=self.count_h+1
   #      if self.count_h % 2 ==0:
   #            self.style_hole.SetDefaultRenderer(self.ren)
   #            self.iren.SetInteractorStyle(self.style_hole)
    #     else:      
     #          self.style.SetDefaultRenderer(self.ren)
     #          self.iren.SetInteractorStyle(self.style)
   # def file_line(self):
   #      self.count_line=self.count_line+1
   #      if self.count_line % 2 ==0:
   #            self.style2.SetDefaultRenderer(self.ren)
   #            self.iren.SetInteractorStyle(self.style2)
   #      else:    
      
   # def tab_h(self):
     
       # print(self.sender() is self.ui.tab_2)
    
    #def fun(self):
        
         
          
        #   self.ren=vtk.vtkRenderer()
        # #self.ren1=vtk.vtkRenderer()
        
        #   self.colors=vtk.vtkNamedColors()
        #   self.ren.SetBackground(self.colors.GetColor3d("black"))
        # #self.ren1.SetBackground(self.colors.GetColor3d("black"))
     
        #   self.vtkWidget_R.GetRenderWindow().AddRenderer(self.ren)
        # #self.ui.vtkWidget_S.GetRenderWindow().AddRenderer(self.ren)
        #   self.iren=self.vtkWidget_R.GetRenderWindow().GetInteractor()
        # #self.iren=self.ui.vtkWidget_S.GetRenderWindow().GetInteractor()
        #   self.iren.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())
        #   #self.iren.GetRenderWindow().Render()
        #   self.tran=vtk.vtkTransform()
        #   self.tran.Translate(0,0,0)
        #   self.axes1=vtk.vtkAxesActor()
        #   self.axes1.SetTotalLength(70,70,70)
        #   self.fonts=vtk.vtkTextProperty()
        #   self.fonts.SetFontSize(1)
        #   self.axes1.GetXAxisCaptionActor2D().SetCaptionTextProperty(self.fonts)
        #   self.axes1.GetYAxisCaptionActor2D().SetCaptionTextProperty(self.fonts)
        #   self.axes1.GetZAxisCaptionActor2D().SetCaptionTextProperty(self.fonts)
        #   #print(self.axes1.GetXAxisCaptionActor2D())
        #   self.axes1.SetUserTransform(self.tran)
        #   self.ren.AddActor(self.axes1)
        #   self.camera=vtk.vtkCamera()
        #   self.camera.SetPosition(0,0,-600) 
        #   self.ren.SetActiveCamera(self.camera)
              
            
    def file_cut(self):
        self.selection_points = vtk.vtkPoints()
        for val in self.listcount_p :
          
             self.selection_points.InsertNextPoint(self.listpoint[val-1][0], self.listpoint[val-1][1],self.listpoint[val-1][2])

        self.loop =vtk.vtkSelectPolyData() 
        self.loop.SetInputConnection(self.reader[self.count].GetOutputPort())
        self.loop.SetLoop( self.selection_points)
        self.loop.GenerateSelectionScalarsOn()
        self.loop.SetSelectionModeToSmallestRegion()

        self.clipper = vtk.vtkClipPolyData()
        self.clipper.SetInputConnection(self.loop.GetOutputPort())
         
        #self.clipper.SetValue ()
        self.clipper.Update()

        print( self.clipper.GetValue ())


        self.clipMapper = vtk.vtkDataSetMapper()
        self.clipMapper.SetInputData(self.clipper.GetOutput())

        self.clipActor =vtk.vtkActor()
        self.clipActor.SetMapper(self.clipMapper)
        self.ren.AddActor(self.clipActor)
        self.ren.RemoveActor(self.actor[self.count])
    def file_angle(self):
        self.handle =vtk.vtkPointHandleRepresentation3D()
        self.rep_a =vtk.vtkAngleRepresentation3D()
        self.rep_a.SetHandleRepresentation( self.handle)

        self.widget =vtk.vtkAngleWidget()
        self.widget.SetInteractor( self.iren)
        self.widget.SetRepresentation(self.rep_a)
        self.widget.On() 
        self.count_angle=self.count_angle+1
        
               
        if self.count_ruler % 2==0:
            self.widget.Off()
                 
        else:
            self.widget.On()
         
    def file_ruler(self):
        
        self.handle = vtk.vtkPointHandleRepresentation3D()
        self.rep_r =vtk.vtkDistanceRepresentation3D()
        self.rep_r.SetHandleRepresentation(self.handle )

        self.distanceWidget = vtk.vtkDistanceWidget()
        self.distanceWidget.SetInteractor(self.iren)
        self.distanceWidget.SetRepresentation( self.rep_r )
        self.distanceWidget.SetWidgetStateToManipulate()
        

#print(distanceWidget.GetDistanceRepresentation ())
        self.distanceWidget.ProcessEventsOn()  

        self.count_ruler=self.count_ruler+1
               
        if self.count_ruler % 2==0:
            self.distanceWidget.Off()
                 
        else:
            self.distanceWidget.On()
    def file_spline(self):
        #print(self.list_points_spline)
        #print( self.list_count_spline)
       
        

       self.points_counter = vtk.vtkPoints()
       self.lines_counter = vtk.vtkCellArray()
       self.points_counter.SetNumberOfPoints(len(self.list_points_spline))
       self.lines_counter.InsertNextCell(len(self.list_points_spline)+1)
       self.lines_counter.InsertCellPoint(0)
       self.lines_counter.InsertCellPoint(0)
       for val in  self.list_count_spline :
              
             
             self.points_counter.SetPoint(val-1,self.list_points_spline[val-1][0],self.list_points_spline[val-1][1],self.list_points_spline[val-1][2])
             
             self.lines_counter.InsertCellPoint(val)


# vtkCellArray is a supporting object that explicitly represents cell connectivity.
# The cell array structure is a raw integer list of the form:
# (n,id1,id2,...,idn, n,id1,id2,...,idn, ...) where n is the number of points in
# the cell, and id is a zero-offset index into an associated point list.
      
     

       self.polygon = vtk.vtkPolyData()
       self.polygon.SetPoints(self.points_counter)
       self.polygon.SetLines(self.lines_counter)

       self.contourWidget = vtk.vtkContourWidget()
       self.contourWidget.SetInteractor(self.iren) 
       self.contourRep =self.contourWidget.GetRepresentation()
       self.contourRep.GetLinesProperty().SetColor(1, 0.2, 0)
       self.contourRep.GetLinesProperty().SetLineWidth(3)
       #print(self.contourRep.GetNthNode (2))
       
       
       self.contourWidget.SetRepresentation(self.contourRep) 
       #self.contourWidget.DeleteActiveNode ()
       self.contourWidget.On()
       self.contourWidget.Initialize(self.polygon)   
       
    #    self.loop =vtk.vtkSelectPolyData() 
    #    self.loop.SetInputConnection(self.reader[self.count].GetOutputPort())
       self.cp=self.contourWidget.GetContourRepresentation ().GetContourRepresentationAsPolyData ()
    #    self.loop.SetLoop(self.cp.GetPoints())
    #    self.loop.GenerateSelectionScalarsOn()
    #    self.loop.SetSelectionModeToLargestRegion ()
    #    #self.loop.SetSelectionModeToSmallestRegion()
    #    #print(loop.GetInsideOut ())
    #    #loop.SetSelectionModeToClosestPointRegion ()
    #    #loop.InsideOutOn ()
    #    #loop.GetSelectionEdges ()
    # #    self.mapper_l = vtk.vtkPolyDataMapper()
    # #    self.mapper_l.SetInputConnection(self.loop.GetOutputPort())
    # #    self.actor_l = vtk.vtkActor()
    # #    self.actor_l.SetMapper(self.mapper_l)

    # #    self.ren.AddActor(self.actor_l)
    #    clipper = vtk.vtkClipPolyData()
    #    clipper.SetInputConnection(self.loop.GetOutputPort())
    #    clipper.Update()


    #    clipMapper = vtk.vtkDataSetMapper()
    #    clipMapper.SetInputData(clipper.GetOutput())

    #    clipActor =vtk.vtkActor()
    #    clipActor.SetMapper(clipMapper)
       #self.ren.AddActor(clipActor)
       #self.ren.RemoveActor(self.actor[self.count])
       extrude = vtk.vtkLinearExtrusionFilter()
       extrude.SetInputData(self.cp)
       extrude.SetScaleFactor (10)
       extrude.SetVector(-6.8,-1.126,2.3)

    #    #extrude.SetExtrusionTypeToPointExtrusion()

       extrude.Update()
       mapper1 =vtk.vtkPolyDataMapper()
       mapper1.SetInputConnection(extrude.GetOutputPort())
       
       model = vtk.vtkActor()
       model.SetMapper(mapper1)
       color=vtk.vtkNamedColors() 
       model.GetProperty().SetColor(color.GetColor3d("red"))
       #model.GetProperty().EdgeVisibilityOn()
       #self.ren.AddActor(model)

       fillHolesFilter = vtk.vtkFillHolesFilter()
       fillHolesFilter.SetInputConnection(extrude.GetOutputPort())
       fillHolesFilter.SetHoleSize( 10000 )  
       fillHolesFilter.Update()
#        ruledSurfaceFilter =vtk.vtkRuledSurfaceFilter()

#        ruledSurfaceFilter.SetInputData(self.polygon)
# #endif
#        ruledSurfaceFilter.SetResolution(21, 21)
#        ruledSurfaceFilter.SetRuledModeToResample()

       

       mapper_h = vtk.vtkPolyDataMapper()
       mapper_h.SetInputConnection(fillHolesFilter.GetOutputPort())
       actor_h = vtk.vtkActor()
       actor_h.SetMapper(mapper_h)
       #self.ren.AddActor(actor_h)
    #    self.contourWidget1 = vtk.vtkContourWidget()
    #    self.contourWidget1.SetInteractor(self.iren) 
    #    self.contourRep1 = vtk.vtkOrientedGlyphContourRepresentation()
    #    self.contourRep1.GetLinesProperty().SetColor(1, 0.2, 0)
    #    self.contourRep1.GetLinesProperty().SetLineWidth(3.0)
    #    self.contourWidget1.SetRepresentation(self.contourRep1) 
      # self.contourWidget1.On()    
        #self.splinewidget = vtk.vtkSplineWidget()
        #self.splinewidget.SetInteractor(self.iren)
        #self.splinewidget.InitializeHandles (self.points_spline)
        #self.splinewidget.SetHandleSize (0.0003)
       
        #self.para= self.splinewidget.GetParametricSpline()
        #self.splinewidget.SetClosed(True)
        #self.splinewidget.On() 
        
        
    def file_smoo(self):
        print("rgrtrtr")
        self.smoothFilter = vtk.vtkSmoothPolyDataFilter() 
        self.smoothFilter.SetInputConnection( self.contourFilter.GetOutputPort())
        self.smoothFilter.SetNumberOfIterations(15)
        self.smoothFilter.SetRelaxationFactor(0.5)
        self.smoothFilter.FeatureEdgeSmoothingOff()
        self.smoothFilter.BoundarySmoothingOn()
        self.smoothFilter.Update()


        self.normalGenerator =vtk.vtkPolyDataNormals()
        self.normalGenerator.SetInputConnection(self.smoothFilter.GetOutputPort())
        self.normalGenerator.ComputePointNormalsOn()
        self.normalGenerator.ComputeCellNormalsOn()
        self.normalGenerator.Update()  

        self.mapper_smoo = vtk.vtkPolyDataMapper()
        self.mapper_smoo.SetInputConnection(self.normalGenerator.GetOutputPort())
 
        self.actor_smoo = vtk.vtkActor()
        self.actor_smoo.SetMapper(self.mapper_smoo)
 
        self.ren.AddActor(self.actor_smoo) 
        self.ren.RemoveActor(self.actor_f)
    def file_fillet(self):
        global obj_ex
        self.extrudedata = self.obj_ex.GetOutput()

        self.implicitModeller = vtk.vtkImplicitModeller()
        self.implicitModeller.SetSampleDimensions(30,30,30)
        self.implicitModeller.SetInputData(self.extrudedata)
        self.implicitModeller.AdjustBoundsOn()
        self.implicitModeller.SetAdjustDistance(0.1)
        self.implicitModeller.SetMaximumDistance(0.1)

        self.contourFilter = vtk.vtkContourFilter()
        self.contourFilter.SetInputConnection(self.implicitModeller.GetOutputPort())
        self.contourFilter.SetValue(0,10)


        self.mapper_f = vtk.vtkPolyDataMapper()
        self.mapper_f.SetInputConnection(self.contourFilter.GetOutputPort())
 
        self.actor_f = vtk.vtkActor()
        self.actor_f.SetMapper(self.mapper_f)

        self.ren.AddActor(self.actor_f)
        self.ren.RemoveActor(self.model)


    def file_point(self):
                 #self.sphere = vtk.vtkSphereSource()
                 #self.sphere.SetRadius(20)
                 #self.sphere.Update()
                 #self.mapper_s = vtk.vtkPolyDataMapper()
                 #self.mapper_s.SetInputConnection(self.sphere.GetOutputPort())
                 #self.actor_s = vtk.vtkActor()
                 #self.actor_s.SetMapper(self.mapper_s)
                 #self.ren.AddActor(self.actor_s)
                 
                 
                 self.count_p=self.count_p+1
                 #print(self.count_p)
                 if self.count_p % 2==0:
    
                   self.style1.SetDefaultRenderer(self.ren)
                   self.iren.SetInteractorStyle(self.style1)
                 else:
                     self.style.SetDefaultRenderer(self.ren)
                     self.iren.SetInteractorStyle(self.style)
    def leftButtonPressEvent_hole(self, obj, event):
        self.clickPos = self.style_hole.GetInteractor().GetEventPosition()
       

        self.picker = vtk.vtkWorldPointPicker()
        self.picker.Pick(self.clickPos[0], self.clickPos[1], 0, self.style_hole.GetDefaultRenderer())
        self.style_hole.OnLeftButtonUp 
        self.p2=self.picker.GetPickPosition()
        print(self.p2)

        #self.sphereSource =vtk.vtkSphereSource()
        #self.sphereSource.SetThetaResolution(20)
        #self.sphereSource.SetPhiResolution(11)
        #self.sphereSource.SetRadius(100) 

        self.plane = vtk.vtkPlane()
        self.plane.SetOrigin(self.p2[0],self.p2[1],self.p2[2])
        self.plane.SetNormal(0,0, -1)
        self.cy=vtk.vtkCylinder()
        self.cy.SetCenter(self.p2[0],self.p2[1],self.p2[2])
        self.cy.SetRadius(10)

        self.clipper = vtk.vtkClipPolyData()
        self.clipper.SetInputConnection(self.extrude.GetOutputPort())
        self.clipper.SetClipFunction(self.cy)
        self.clipper.SetValue(0)
        #self.clipper.GenerateClippedOutputOn()
        #self.clipper.InsideOutOn()
        self.clipper.Update()

        self.clipMapper = vtk.vtkDataSetMapper()
        self.clipMapper.SetInputData(self.clipper.GetOutput())

        self.clipActor =vtk.vtkActor()
        self.clipActor.SetMapper(self.clipMapper)
        self.clipActor.GetProperty().SetColor(1.0000, 0.3882, 0.2784)
        self.clipActor.GetProperty().SetInterpolationToFlat()
        self.ren.AddActor(self.clipActor)
         


    def leftButtonPressEvent_line(self, obj, event):
        self.clickPos = self.style2.GetInteractor().GetEventPosition()
       

        self.picker = vtk.vtkPicker()
        self.picker.Pick(self.clickPos[0], self.clickPos[1], 0, self.style2.GetDefaultRenderer())
        self.style2.OnLeftButtonUp
        #print(self.picker.GetActor().GetBounds())
        self.dot1=self.picker.GetActor()
        #print(self.dot)
        #print(self.picker.GetActor().GetProperty().GetPointSize())
        
        
        if  self.dot1 :
            
               print("point")
               self.p0=[self.picker.GetActor().GetOrigin()[0]+100,self.picker.GetActor().GetOrigin()[1] +100,100]
               self.listp0.append(self.p0)
               print(self.listp0)
               self.count_l=self.count_l+1
               print(self.count_l)
          
         #print(self.p0)
               #if self.count_l % 2 ==0:
          
         
               #self.p1=[self.picker.GetActor().GetBounds()[0],self.picker.GetActor().GetBounds()[2] ,self.picker.GetActor().GetBounds()[4]]
           #self.listp0.append(self.p1)
               self.lineSource = vtk.vtkLineSource()
    
               self.lineSource.SetPoint1(self.listp0[0])
           #self.listp0.append(self.p0)
           #print(self.listp0)
           #print(self.p1)
               if self.count_l % 2 ==0:
                self.lineSource.SetPoint2(self.listp0[1])
                del self.listp0[0]
                del self.listp0[0]
           #del self.listp0[0]
                print(self.listp0)
                self.lineSource.Update()


                self.mapper = vtk.vtkPolyDataMapper()
                self.mapper.SetInputConnection(self.lineSource.GetOutputPort())
                self.actor = vtk.vtkActor()
    
                self.actor.SetMapper(self.mapper)
                self.actor.GetProperty().SetLineWidth(1)
                self.ren.AddActor(self.actor)

            #if  self.actor.GetProperty().GetLineWidth()==1:
                #print("line")

    def leftButtonPressEvent_point(self, obj, event):
         if  self.count_point==0:
           self.points_counter1 = vtk.vtkPoints()
           self.lines_counter1 = vtk.vtkCellArray()
           self.points_counter1.SetNumberOfPoints(len(self.list_points_spline))
           self.lines_counter1.InsertNextCell(len(self.list_points_spline)+1)
           self.lines_counter1.InsertCellPoint(0)
           self.lines_counter1.InsertCellPoint(0)
           for val in  self.list_count_spline :
              
             
             self.points_counter1.SetPoint(val-1,self.list_points_spline[val-1][0],self.list_points_spline[val-1][1],self.list_points_spline[val-1][2])
             
             self.lines_counter1.InsertCellPoint(val)


           self.polygon1 = vtk.vtkPolyData()
           self.polygon1.SetPoints(self.points_counter1)
           self.polygon1.SetLines(self.lines_counter1)

           self.mapper3 = vtk.vtkPolyDataMapper()    
           self.mapper3.SetInputData(self.polygon1)
        
           self.actor_3 = vtk.vtkActor()    
           self.actor_3.SetMapper(self.mapper3)
           
           self.ren.AddActor(self.actor_3)
         
         self.count_point=self.count_point+1
         self.listcount_p.append(self.count_point)
         self.count_point1=self.count_point1+1
         
         #print(self.count_point1)
        
         self.list_count_spline.append(self.count_point1) 
         self.list_count_spline.sort()
         #print(self.list_count_spline)   
         
         self.clickPos = self.style1.GetInteractor().GetEventPosition()
       

         self.picker = vtk.vtkWorldPointPicker()
         self.picker.Pick(self.clickPos[0],self.clickPos[1] , 0, self.style1.GetDefaultRenderer())
         self.style1.OnLeftButtonUp
         self.p1 = self.picker.GetPickPosition()
         #print(self.p1)

         self.points = vtk.vtkPoints()
               
         self.p = [self.p1[0], self.p1[1], self.p1[2]]
         
         self.listpoint.append(self.p)
         #print(self.p)
         self.list_points_spline.append(self.p)
         
         #print(self.listpoint_insert)
         #print(self.listpoint)
         #self.point1=vtk.vtkPoints()
         #self.point1.InsertNextPoint(0,0,0) 
         #self.point1.InsertNextPoint(10,10,10)  
         #print(self.point1)     
    
         self.vertices = vtk.vtkCellArray()
         self.points.InsertNextPoint(self.p)
         
         
         self.id = self.points.InsertNextPoint(self.p)
             
         self.vertices.InsertNextCell(1)
              
         self.vertices.InsertCellPoint(self.id)
         #print(self.id)
            
         self.point = vtk.vtkPolyData()


         self.point.SetPoints(self.points)
         self.point.SetVerts(self.vertices)
         

         #print(self.point)

         self.mapper2 = vtk.vtkPolyDataMapper()
             
    
         self.mapper2.SetInputData(self.point)
        

         self.actor_p = vtk.vtkActor()
              
         self.actor_p.SetMapper(self.mapper2)
           
         self.actor_p.GetProperty().SetPointSize(5)
         #self.actor.SetPosition(self.p1[0], self.p1[1], self.p1[2])
         #self.actor_p.SetOrigin(self.p1[0], self.p1[1], self.p1[2])
         

         self.ren.AddActor(self.actor_p)
    def boxCallback(self,obj, event):
          print("ohhh")
          #global extrude 
          
          t = vtk.vtkTransform()
          obj.GetTransform(t)
          #print(t)
          #self.extrude.SetVector(t)
          obj.GetProp3D().SetUserTransform(t ) 
          #print(type(obj))
          #print(self.boxCallback(event="InteractionEvent",obj=vtkmodules.vtkInteractionWidgets.vtkBoxWidget()))  
          
    def file_extrude(self):
       

        extrude = vtk.vtkLinearExtrusionFilter()
        extrude.SetInputData(self.polygon1)
        extrude.SetScaleFactor (10)
        #extrude.SetVector(-6.8,-1.126,2.3)
        extrude.SetExtrusionTypeToNormalExtrusion
       
        extrude.Update()
        print(extrude)

        centerFilter = vtk.vtkCenterOfMass()
        centerFilter.SetInputData(extrude.GetOutput())
        centerFilter.SetUseScalarsAsWeights(False)
        centerFilter.Update()
        center = centerFilter.GetCenter()
        # ribbonFilter =vtk.vtkRibbonFilter()
        # ribbonFilter.SetInputData(self.polygon1)
        # ribbonFilter.SetWidth(4)

        mapper1 =vtk.vtkPolyDataMapper()
        mapper1.SetInputConnection(extrude.GetOutputPort())
       
        model = vtk.vtkActor()
        model.SetMapper(mapper1)
        
        
        color=vtk.vtkNamedColors() 
        model.GetProperty().SetColor(color.GetColor3d("red"))
        
       
        #model.GetProperty().EdgeVisibilityOn()
        
        self.ren.AddActor(model)

        normals = vtk.vtkPolyDataNormals()
        normals.SetInputConnection(extrude.GetOutputPort())
        #normals.ComputePointNormalsOff()
        #normals.ComputeCellNormalsOn()
        normals.SplittingOn()
        #normals.FlipNormalsOn()
        #normals.ConsistencyOn()
        #normals.AutoOrientNormalsOn()
        normals.Update()
        print(normals)

        extrude2 = vtk.vtkLinearExtrusionFilter()
        extrude2.SetInputData(normals.GetOutput())
        extrude2.SetScaleFactor (-10)
           
        extrude2.SetExtrusionTypeToNormalExtrusion()
       # -97.52576336555634, 19.948874029688792, 41.72288466522438
        extrude2.Update()
       

        mapper2 =vtk.vtkPolyDataMapper()
        mapper2.SetInputConnection(extrude2.GetOutputPort())
       
        model2 = vtk.vtkActor()
        model2.SetMapper(mapper2)
        
        
        color=vtk.vtkNamedColors() 
        model2.GetProperty().SetColor(color.GetColor3d("red"))
        
        #self.ren.AddActor(model2)

        translation =vtk.vtkTransform()
        translation.Translate(3*-6.8,3*-1.126,3*2.3)
        
         
        transformFilter = vtk.vtkTransformPolyDataFilter() 
        #transformFilter.SetInputConnection(reader->GetOutputPort())
        transformFilter.SetInputData(self.cp) 
        transformFilter.SetTransform(translation) 
        transformFilter.Update() 
       
       
        #print(center)

        mapper_t =vtk.vtkPolyDataMapper()
        mapper_t.SetInputConnection(transformFilter.GetOutputPort()) 

        mainActor = vtk.vtkActor()
        mainActor.SetMapper(mapper_t)

        #self.ren.AddActor(mainActor)

        # num_point_trans=self.cp.GetNumberOfPoints()
        # print(num_point_trans)
        # list_point_x=[self.list_points_spline[0][0]]
        # list_point_y=[self.list_points_spline[0][1]]
        # list_point_z=[self.list_points_spline[0][2]]
        # for i in range(1,len(self.list_points_spline)):
        #     list_point_x.append(self.list_points_spline[i][0])
        #     list_point_y.append(self.list_points_spline[i][1])
        #     list_point_z.append(self.list_points_spline[i][2])
    
      
        # x_point=sum(list_point_x)/len(self.list_points_spline)
        # y_point=sum(list_point_y)/len(self.list_points_spline)
        # z_point=sum(list_point_z)/len(self.list_points_spline)
            
           
        
        polygonSource =vtk.vtkRegularPolygonSource()
        polygonSource.GeneratePolygonOff()
        polygonSource.SetNumberOfSides(50)
        polygonSource.SetRadius(10)
        polygonSource.SetCenter(center[0],center[1]+6,center[2]+10)
        polygonSource.SetNormal (-6.8,-1.126,2.3)
        polygonSource.Update()
        
        translation1 =vtk.vtkTransform()
       
        translation1.Translate(3*-6.8,3*-1.126,3*2.3)
        #translation1.Scale(0.1,0.1,0.1)
        
         
        transformFilter1 = vtk.vtkTransformPolyDataFilter() 
        #transformFilter.SetInputConnection(reader->GetOutputPort())
        transformFilter1.SetInputData(polygonSource.GetOutput()) 
        transformFilter1.SetTransform(translation1)
        transformFilter1.Update() 
        poly_trans1=transformFilter1.GetOutput()
        mapper_t1 =vtk.vtkPolyDataMapper()
        mapper_t1.SetInputConnection(transformFilter1.GetOutputPort()) 

        mainActor1 = vtk.vtkActor()
        mainActor1.SetMapper(mapper_t1)

        #self.ren.AddActor(mainActor1)

        num_point2=poly_trans1.GetNumberOfPoints()
        num_point1=transformFilter.GetOutput().GetNumberOfPoints ()
        poly_transform=transformFilter.GetOutput()
        # #print(transformFilter.GetOutput().GetPoint(888))
       
        # if num_point%2==1:
        #    num_point=num_point-1
        # else:
        #     num_point=num_point 
        # print(num_point/2)  
        points_tra1 = vtk.vtkPoints()
        #points_tra2 = vtk.vtkPoints()

        lines_tra1= vtk.vtkLine()
        lines_tra2= vtk.vtkLine()  

        lines_tra1.GetPointIds().SetNumberOfIds(num_point1)
        lines_tra2.GetPointIds().SetNumberOfIds(num_point2)
        
        for num in range(num_point1):

            points_tra1.InsertPoint(num,poly_transform.GetPoint(num)[0],poly_transform.GetPoint(num)[1],poly_transform.GetPoint(num)[2] )
        
        for num in range(num_point2):
    
            points_tra1.InsertPoint(num,poly_trans1.GetPoint(num)[0],poly_trans1.GetPoint(num)[1],poly_trans1.GetPoint(num)[2] )


        for num in range(num_point1):

            lines_tra1.GetPointIds().SetId(num,num)
            
        # i=0    
        for num in range(num_point2):
    
            lines_tra2.GetPointIds().SetId(num,num)
        #      i+=1
              
        lines_cell_tra =vtk.vtkCellArray() 
        lines_cell_tra.InsertNextCell(lines_tra1) 
        lines_cell_tra.InsertNextCell(lines_tra2) 
             
        self.polygon_tra = vtk.vtkPolyData()
        self.polygon_tra.SetPoints(points_tra1)
      
        self.polygon_tra.SetLines(lines_cell_tra)

        ruledSurfaceFilter =vtk.vtkRuledSurfaceFilter()
        ruledSurfaceFilter.SetInputData(self.polygon_tra)
        ruledSurfaceFilter.SetResolution(50, 50)
        ruledSurfaceFilter.SetRuledModeToResample()
        
        #ruledSurfaceFilter.SetOffset(10)

        
        ruledSurfaceFilter.Update()
        
        mapper_s =vtk.vtkPolyDataMapper()
        mapper_s.SetInputConnection(ruledSurfaceFilter.GetOutputPort()) 

        mainActor_s = vtk.vtkActor()
        mainActor_s.SetMapper(mapper_s)
        mainActor_s.GetProperty().SetColor(color.GetColor3d("red"))
#######################################################################################################
        # app = vtk.vtkAppendPolyData()
        # app.AddInputData(self.reader[self.count].GetOutput())
        # app.AddInputData(extrude.GetOutput())
        # app.Update()
        # cleaner = vtk.vtkCleanPolyData()
        # cleaner.SetInputData(app.GetOutput())
        # cleaner.Update()

        #result = cleaner.GetOutput()
        #print(self.listpoint)
        #selectionPoints =vtk.vtkPoints()
        #for sel in range(len(self.list_points_spline)):

        #     selectionPoints.InsertPoint( sel,self.list_points_spline[sel][0], self.list_points_spline[sel][1], self.list_points_spline[sel][2] )
        self.loop =vtk.vtkSelectPolyData() 
        self.loop.SetInputConnection(extrude.GetOutputPort())
     
        self.loop.SetLoop(extrude.GetOutput().GetPoints())
        self.loop.GenerateSelectionScalarsOn()
        self.loop.SetSelectionModeToLargestRegion ()
        #self.loop.SetSelectionModeToSmallestRegion()
       #print(loop.GetInsideOut ())
       #loop.SetSelectionModeToClosestPointRegion ()
       #loop.InsideOutOn ()
       #loop.GetSelectionEdges ()
        self.mapper_l = vtk.vtkPolyDataMapper()
        self.mapper_l.SetInputConnection(self.loop.GetOutputPort())
        self.actor_l = vtk.vtkActor()
        self.actor_l.SetMapper(self.mapper_l)

        #self.ren.AddActor(self.actor_l)
      
        # clipper = vtk.vtkClipPolyData()
        # clipper.SetInputConnection(self.loop.GetOutputPort())
        # clipper.Update()


        # clipMapper = vtk.vtkDataSetMapper()
        # clipMapper.SetInputData(clipper.GetOutput())

        # clipActor =vtk.vtkActor()
        # clipActor.SetMapper(clipMapper)
        #self.ren.RemoveActor(self.actor[self.count])
        #self.ren.AddActor(clipActor)
       
        extrude1 = vtk.vtkLinearExtrusionFilter()
        extrude1.SetInputConnection(self.loop.GetOutputPort())
        extrude1.SetScaleFactor (0.3)
        
       # extrude1.SetExtrusionTypeToNormalExtrusion ()
       #extrude.SetVector(-6.8,-1.126,2.3)

        extrude1.SetExtrusionTypeToPointExtrusion()
        
       
        extrude1.Update()
        mapper1 =vtk.vtkPolyDataMapper()
        mapper1.SetInputConnection(extrude1.GetOutputPort())
       
        model1 = vtk.vtkActor()
        model1.SetMapper(mapper1)
        color=vtk.vtkNamedColors() 
        #model1.GetProperty().SetColor(color.GetColor3d("blue"))
        
       #model.GetProperty().EdgeVisibilityOn()
        self.ren.AddActor(model1)
      
     #######################################################################################
        self.loop1 =vtk.vtkSelectPolyData() 
        self.loop1.SetInputConnection(self.reader[self.count].GetOutputPort())
        self.loop1.SetLoop(self.cp.GetPoints())
        self.loop1.GenerateSelectionScalarsOn()
        self.loop1.SetSelectionModeToLargestRegion ()
        self.loop1.Update()

        self.loop1Mapper = vtk.vtkPolyDataMapper()
        self.loop1Mapper.SetInputConnection(self.loop1.GetOutputPort())
        
        self.loop1Actor =vtk.vtkActor()
        self.loop1Actor.SetMapper(self.loop1Mapper)
        self.color=vtk.vtkNamedColors() 
        self.loop1Actor.GetProperty().SetColor(self.color.GetColor3d("green"))
        print(self.loop1Actor.GetProperty())
        
        self.ren.AddActor(self.loop1Actor)

        clipper1 = vtk.vtkClipPolyData()
        clipper1.SetInputConnection(self.loop1.GetOutputPort())
        clipper1.Update()


        clipMapper = vtk.vtkDataSetMapper()
        clipMapper.SetInputData(clipper1.GetOutput())

        clipActor =vtk.vtkLODActor()
        clipActor.SetMapper(clipMapper)
        self.color=vtk.vtkNamedColors() 
        clipActor.GetProperty().SetColor(self.color.GetColor3d("green"))
        
        # self.ren.RemoveActor(self.actor[self.count])
        # self.ren.AddActor(clipActor)
       
        extrude3 = vtk.vtkLinearExtrusionFilter()
        extrude3.SetInputConnection(clipper1.GetOutputPort())
        extrude3.SetScaleFactor (0.3)
        
       # extrude1.SetExtrusionTypeToNormalExtrusion ()
       #extrude.SetVector(-6.8,-1.126,2.3)

        extrude3.SetExtrusionTypeToPointExtrusion()
        
       
        extrude3.Update()
        mapper3 =vtk.vtkPolyDataMapper()
        mapper3.SetInputConnection(extrude3.GetOutputPort())
       
        model3 = vtk.vtkActor()
        model3.SetMapper(mapper3)
        #self.color=vtk.vtkNamedColors() 
        #model3.GetProperty().SetColor(2,2,2)
       
       #model.GetProperty().EdgeVisibilityOn()
        #self.ren.RemoveActor(self.actor[self.count])
        #self.ren.AddActor(model3)

     ###################################################################  

       
        #self.points1 = vtk.vtkPoints()
#         self.function=vtk.vtkParametricFunctionSource()
#         self.function.SetParametricFunction(self.para)
#         #self.function.SetUResolution(10*points.GetNumberOfPoints()) 
#         self.function.Update()
#         #for val in self.listcount_p :
          
#          # self.points1.InsertNextPoint(self.listpoint[val-1][0], self.listpoint[val-1][1],self.listpoint[val-1][2])
#         #self.points1.InsertNextPoint(self.listpoint[1][0], self.listpoint[1][1],self.listpoint[1][2])
#         #self.points1.InsertNextPoint(self.listpoint[2][0], self.listpoint[2][1],self.listpoint[2][2])
#         #self.points1.InsertNextPoint(self.listpoint[3][0], self.listpoint[3][1],self.listpoint[3][2])
# #points.InsertPoint(4, 1.5, 0.0, 0.0)
# #points.InsertPoint(5, 1.4268, 0.0, 0.1768)
# #points.InsertPoint(6, 1.25, 0.0, 0.25)
# #points.InsertPoint(7, 1.0732, 0.0, 0.1768)
#         #self.polygon =vtk.vtkPolygon()
#         #self.polygon.GetPointIds().SetNumberOfIds(self.count_point)
#         #for val in self.listcount_p :
#          # self.polygon.GetPointIds().SetId(val-1, val-1)
          
         
#           #self.count_point=self.count_point-1
#         #self.polygon.GetPointIds().SetId(1, 1)
#         #self.polygon.GetPointIds().SetId(2, 2)
#         #self.polygon.GetPointIds().SetId(3, 3)

#         #self.cell=vtk.vtkCellArray()
#         #self.cell.InsertNextCell(self.polygon)
# #d.InsertCellPoint(0)
# #d.InsertCellPoint(1)
# #d.InsertCellPoint(2)
# #d.InsertCellPoint(3)
# #d.InsertCellPoint(4)
# #d.InsertCellPoint(5)
# #d.InsertCellPoint(6)
# #d.InsertCellPoint(7) 
#         #self.profile = vtk.vtkPolyData()
#         #self.profile.SetPoints(self.points1)
#         #self.profile.SetPolys(self.cell)

#         self.extrude = vtk.vtkLinearExtrusionFilter()
#         self.extrude.SetInputData(self.function.GetOutput())
# #extrude.SetExtrusionType()
#         #self.extrude.SetScaleFactor(1)
#         #self.extrude.SetExtrusionTypeToNormalExtrusion()
#         #self.extrude.SetVector(-6.8,-1.126,2.3)
#         #self.extrude.SetVector(-20.4,-3.4,6.9)
#         self.pts=np.array(self.list_points_spline)
#         self.plane = fitPlane(self.pts)

#         self.extrude.SetVector(15*self.plane.normal[0],15*self.plane.normal[1],15*self.plane.normal[2])
#         print(self.plane.normal)
# #print(extrude.GetExtrusionType())
#         self.extrude.Update()
#extrude.SetResolution(360)
#extrude.SetTranslation(6)
#extrude.SetDeltaRadius(1.0)
#extrude.SetAngle(2160.0)
#normals = vtk.vtkPolyDataNormals()
#normals.SetInputData(extrude.GetOutput())
#normals.SetFeatureAngle(30)
        #self.tria =vtk.vtkTriangleFilter()
        #self.tria.SetInputConnection(self.extrude.GetOutputPort())
        #self.tria.Update()
       # self.algo=vtk.vtkPolyDataNormals()
       # self.algo.SetInputData(self.extrude.GetOutput())
       # self.algo.Update()

        #self.norm =vtk.vtkPolyDataNormals()
        #self.norm.SetInputData(self.tria.GetOutput())
        #self.smoo=vtk.vtkSmoothPolyDataFilter()
        #self.smoo.SetInputConnection(self.extrude.GetOutputPort())
        #self.smoo.SetNumberOfIterations(30)
        #self.smoo.SetRelaxationFactor(0.01)
        #self.smoo.FeatureEdgeSmoothingOff()
        #self.smoo.BoundarySmoothingOn()
        #self.smoo.FeatureEdgeSmoothingOn()
        #self.smoo.SetEdgeAngle(80) 
        #self.smoo.SetFeatureAngle(80)
       # self.smoo.Update()
        #self.edge=vtk.vtkFeatureEdges()
        #self.edge.SetInputConnection(self.extrude.GetOutputPort())
        #self.edge.SetEdgeAngle(60)
        #print(self.edge)
        #self.edge.SetFeatureAngle (60)
        #self.edge.BoundaryEdgesOn()
        #self.edge.ManifoldEdgesOff()
        #self.edge.NonManifoldEdgesOff()
        #self.edge.FeatureEdgesOff()
        #self.edge.Update()
        #self.smoo.FeatureEdgeSmoothingOn()
        #self.smoo.SetNumberOfIterations (50)
        #print(self.smoo)
        #self.stripped = vtk.vtkStripper()
        #self.stripped.SetInputData(self.edge.GetOutput())
        #self.stripped.Update()

        #self.tube = vtk.vtkTubeFilter()
        #self.tube.SetInputData(self.stripped.GetOutput())
        #self.tube.SetRadius(1)
        #self.tube.SetNumberOfSides(10)
        #self.tube.Update()
        #self.mapper_tube =vtk.vtkPolyDataMapper()
        #self.mapper_tube.SetInputConnection(self.tube.GetOutputPort())
       # print(self.mapper1)
        #self.model_tube = vtk.vtkActor()
        #self.model_tube.SetMapper(self.mapper_tube)
        #self.color=vtk.vtkNamedColors() 
        #self.model_tube.GetProperty().SetColor(self.color.GetColor3d("red"))
        #self.model_tube.GetProperty().EdgeVisibilityOn()
        #print(self.model.GetOrientation())
        #self.ren.AddActor(self.model_tube)


    #     self.mapper1 =vtk.vtkPolyDataMapper()
    #     self.mapper1.SetInputConnection(self.extrude.GetOutputPort())
    #    # print(self.mapper1)
    #     self.model = vtk.vtkActor()
    #     self.model.SetMapper(self.mapper1)
    #     self.color=vtk.vtkNamedColors() 
    #     self.model.GetProperty().SetColor(self.color.GetColor3d("red"))
    #     self.model.GetProperty().EdgeVisibilityOn()
    #     #print(self.model.GetOrientation())
 
    #     self.ren.AddActor(self.model)
    #     self.fillHolesFilter = vtk.vtkFillHolesFilter()
    #     self.fillHolesFilter.SetInputConnection(self.extrude.GetOutputPort())
    #     self.fillHolesFilter.SetHoleSize( 10000 )  
    #     self.fillHolesFilter.Update()


    #     self.mapper_f = vtk.vtkPolyDataMapper()
    #     self.mapper_f.SetInputConnection(self.function.GetOutputPort())
    #     self.actor_f = vtk.vtkActor()
    #     self.actor_f.SetMapper(self.mapper_f)
    #     self.ren.AddActor(self.actor_f)

    #     self.mapper_h = vtk.vtkPolyDataMapper()
    #     self.mapper_h.SetInputConnection(self.fillHolesFilter.GetOutputPort())
    #     self.actor_h = vtk.vtkActor()
    #     self.actor_h.SetMapper(self.mapper_h)
    #     self.ren.AddActor(self.actor_h)
        #self.ren.AddActor(self.model)
        #self.boxWidget = vtk.vtkBoxWidget()
        #self.boxWidget.SetInteractor(self.iren)
        #self.boxWidget.SetProp3D(self.model)
        #self.boxWidget.SetPlaceFactor( 1 ) # Make the box 1.25x larger than the actor
        #self.boxWidget.PlaceWidget()
        #self.boxWidget.On()
        #self.boxWidget.AddObserver("InteractionEvent", self.boxCallback)
        #print(self.boxWidget)

       

     



        #self.fill=vtk.vtkFillHolesFilter()
        #self.fill.SetInputData(self.extrude())
        #self.fill.SetHoleSize(1000)
        #self.fill.Update()
        
        #self.plt = Plotter()
        

        #self.plt += self.plane
        #self.plt += Points(self.pts)

        #self.plt += Arrow(self.plane.center, self.plane.center+self.plane.normal/5)

        #self.plt.show()


          
    def Front(self):
        
         if self.sender() is self.ui.pushButton_front:
               self.cb=timer()
               self.iren.AddObserver('TimerEvent', self.cb.repeat)
               self.timerId =self.iren.CreateRepeatingTimer(1)
               self.camera=vtk.vtkCamera()
               self.camera.SetPosition(0,0,-600)  
               self.ren.SetActiveCamera(self.camera)
              
               

    def Up(self):
        if self.sender() is self.ui.pushButton_top:
            self.cb=timer()
            self.iren.AddObserver('TimerEvent', self.cb.repeat)
            self.timerId =self.iren.CreateRepeatingTimer(1)
            self.camera=vtk.vtkCamera()
            self.camera.SetPosition(0,0,-600)
            self.camera.Elevation(87)  
            self.ren.SetActiveCamera(self.camera)
           
                
    def Right(self):
        if self.sender() is self.ui.pushButton_right:
            self.cb=timer()
            self.iren.AddObserver('TimerEvent', self.cb.repeat)
            self.timerId =self.iren.CreateRepeatingTimer(1)
            self.camera=vtk.vtkCamera()
            self.camera.SetPosition(0,0,-600)
            self.camera.Azimuth(90)  
            self.ren.SetActiveCamera(self.camera)

    def Left(self):
        if self.sender() is self.ui.pushButton_left:
            self.cb=timer()
            self.iren.AddObserver('TimerEvent', self.cb.repeat)
            self.timerId =self.iren.CreateRepeatingTimer(1)
            self.camera=vtk.vtkCamera()
            self.camera.SetPosition(0,0,-600)
            self.camera.Azimuth(-90)  
            self.ren.SetActiveCamera(self.camera)       
            
    

    def file_zoomout(self):
           
             self.camera.Zoom(.9) 
           
             self.ren.SetActiveCamera(self.camera)
             self.cb=timer()
             self.iren.AddObserver('TimerEvent', self.cb.repeat)
             self.timerId =self.iren.CreateRepeatingTimer(1)  
     
    def file_zoomin(self):
           
             self.camera.Zoom(1.1) 
             self.ren.SetActiveCamera(self.camera) 
             self.cb=timer()
             self.iren.AddObserver('TimerEvent', self.cb.repeat)
             self.timerId =self.iren.CreateRepeatingTimer(1)  
       
    def file_open(self):         
         self.fname = QFileDialog.getOpenFileName(self, caption='Open file')
         
         if self.fname[0]:
            f = open(self.fname[0],'r')
            print(self.fname[0])
            self.count=self.count+1
            #print(self.count)
            #if self.count==1:
             # self.count=int(input("enter:")) 

            self.reader.append("self.reader"+str(self.count+1))
            #self.readerdi.append("self.readerdi"+str(self.count+1))
            #print(self.reader)
            self.reader[self.count]=vtk.vtkSTLReader()    
            #self.readerdi[self.count]=vtk.vtkDICOMImageReader()

            self.reader[self.count].SetFileName(self.fname[0])  
            self.reader[self.count].Update() 
            #self.readerdi[self.count].SetFileName(self.fname[0])
            print(self.fname[0])
            
            #self.img.append("self.img"+str(self.count+1))
            #self.img[self.count]=vtk.vtkImageViewer2()
            #self.img[self.count].SetInputConnection(self.readerdi[self.count].GetOutputPort())
            #self.iren1=vtk.vtkRenderWindowInteractor()
            #self.img[self.count].SetupInteractor(self.iren1)
            #self.img[self.count].Render()
            #self.img[self.count].GetRenderer().ResetCamera()
            #self.img[self.count].Render()
            #self.iren1.Start()
            self.list2.append(self.reader[self.count].GetFileName())
            print(self.list2)
           
            self.mapper.append("self.mapper"+str(self.count+1))
            self.mapper[self.count]=  vtk.vtkPolyDataMapper()  
            
            self.mapper[self.count].SetInputConnection(self.reader[self.count].GetOutputPort())
            self.actor.append("self.actor"+str(self.count+1))
            self.actor[self.count] = vtk.vtkActor()
            self.actor[self.count].SetMapper(self.mapper[self.count])
            #self.actor[self.count].SetPosition(89.93,-5.37,-5.92)
    
            self.color=vtk.vtkNamedColors() 
            self.actor[self.count].GetProperty().SetColor(self.color.GetColor3d("orange"))
            
              
            self.camera=vtk.vtkCamera()
            self.camera.SetPosition(0,0,-600)
         
            self.ren.AddActor(self.actor[self.count])  
            self.list1.append(self.actor[self.count])
           
           

            #self.plane=vtk.vtkPlane()
            #self.plane.SetOrigin(0,0,-75)
            #self.plane.SetNormal(0.75,0,1)
           

            #self.planes=vtk.vtkPlaneCollection()
            #self.planes.AddItem(self.plane)
        
            #self.clip=vtk.vtkClipClosedSurface()
            #self.clip.SetClippingPlanes(self.planes)
            #self.clip.SetInputConnection(self.reader[0].GetOutputPort())
    
            #self.cutMapper=vtk.vtkPolyDataMapper()
            #self.cutMapper.SetInputConnection(self.clip.GetOutputPort())

            #self.cutactor=vtk.vtkActor()
            #self.cutactor.SetMapper(self.cutMapper)
            #self.cutactor.SetPosition(89.93,-5.37,-5.92)
            #self.cutactor.GetProperty().SetColor(self.color.GetColor3d("orange"))
            #self.cutactor.VisibilityOff()
          

            #self.centerfile=vtk.vtkCenterOfMass()
            #self.centerfile.SetInputConnection(self.clip.GetOutputPort())
            #self.centerfile.Update()
            
            #self.assemble=vtk.vtkAssembly()
            #self.assemble.AddPart(self.actor[self.count])
            #self.assemble.AddPart(self.cutactor)
            #self.ren.AddActor(self.assemble) 
             
if __name__ == "__main__":  
   app = QtWidgets.QApplication(sys.argv)
   
   w=AppWindow()

   w.show()

   w.iren.Initialize()
   #MainWindow = QtWidgets.QMainWindow()
   #ui = Ui_MainWindow()
   #ui.setupUi(MainWindow)
   #MainWindow.show()
   sys.exit(app.exec_())