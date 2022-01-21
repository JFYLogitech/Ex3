import serial

# -------------------------------------serial obj-------------------------------------------#
class cEx3Serial():


    # ----------------------------------init function-------------------------------------- #
    #  Call:    Call at the creation of the object                                          #
    #  Action:  instanciate the serial object withe parametre given                         #
    # ------------------------------------------------------------------------------------- #        
    def __init__(self):
        self.ser = serial.Serial(port='COM6',baudrate=9600,timeout=1)                       # setup the serial object
# ------------------------------------------------------------------------------------------#







