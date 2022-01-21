import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
    QPushButton
)
from ex3_ui import Ui_MainWindow


# -------------------------------------interface obj----------------------------------------#
class MainWindow(QMainWindow, Ui_MainWindow):

    # ----------------------------------init function-------------------------------------- #
    #  Call:    Call at the creation of the object                                          #
    #  Action:  create the window and connect the button to the action, place               #
    #           the interface in an unconfigurated state by disabling some button           #
    # ------------------------------------------------------------------------------------- #    
    def __init__(self,...,..., *args, obj=None, **kwargs):
        #-------initialise the superclass------#
        super(MainWindow, self).__init__(*args, **kwargs)                                   # intialise the class interface
        self.setupUi(self)                                                                  # setup the interface  


        #-----------connect the event----------#
        ...                                                                                 # connect the checkboxt to a local function
        ...                                                                                 # connect the send button to the parameter
        ...                                                                                 # connect the read button to the parameter         
        #-------------disable/enable-----------#
                                                    


    # ----------------------------------event function------------------------------------- #
    #  Call:    Each time the edition check box change value, called localy only            #
    #  Action:  Swap what is enable/disable on the interface                                #
    # ------------------------------------------------------------------------------------- #
    def editManage(self):
        ...



    # ----------------------------------parameter function--------------------------------- #
    #  Action: return the value of the checkbox                                             #
    # ------------------------------------------------------------------------------------- #
    def editEnable(self):
        ...
# ------------------------------------------------------------------------------------------#    

    

        
        
        
   