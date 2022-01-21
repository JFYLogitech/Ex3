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
        self.window = MainWindow()                                                          # create the window object
        self.window.show()                                                                  # make the windows visible
        
# ------------------------------------------------------------------------------------------#




# -------------------------------------------main-------------------------------------------#
def Main():
    mainProj = mainProject() # Instanciate de application as an object
    mainProj.app.exec()      # loop the application
# ------------------------------------------------------------------------------------------#

    

if __name__ == "__main__":
    Main()