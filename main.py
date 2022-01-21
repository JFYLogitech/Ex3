import sys
from ex3_serial import cEx3Serial
from ex3_mainWindow import MainWindow
from PyQt6.QtWidgets import QApplication


# -------------------------------------main project obj-------------------------------------#
class mainProject():

    # ----------------------------------init function-------------------------------------- #
    #  Call:    Call at the creation of the main object                                     #
    #  Action:  Initialise the app window and display it                                    #
    # ------------------------------------------------------------------------------------- #    
    def __init__(self):
        self.app = QApplication(sys.argv)                                                   # initialise QT
        self.window = MainWindow(self...,self...)                                                          # create the window object
        self.window.show()                                                                  # make the windows visible
        



    # ----------------------------------event function------------------------------------- #
    #  Call:    When the send button is pressed                                             #
    #  Action:  send the data from the text box to the serial                               #
    # ------------------------------------------------------------------------------------- #
    def sendData(self):        
        ...



    # ----------------------------------event function------------------------------------- #
    #  Call:    When the button read is pressed                                             #
    #  Action:  Read data from the serial and display them in the text box                  #
    # ------------------------------------------------------------------------------------- #  
    def getData(self):
        ...


# ------------------------------------------------------------------------------------------#




# -------------------------------------------main-------------------------------------------#
def Main():
    mainProj = mainProject() # Instanciate de application as an object
    mainProj.app.exec()      # loop the application
# ------------------------------------------------------------------------------------------#

    

if __name__ == "__main__":
    Main()