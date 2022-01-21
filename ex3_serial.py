import serial

# -------------------------------------serial obj-------------------------------------------#
class cEx3Serial():


    # ----------------------------------init function-------------------------------------- #
    #  Call:    Call at the creation of the object                                          #
    #  Action:  instanciate the serial object withe parametre given                         #
    # ------------------------------------------------------------------------------------- #        
    def __init__(self,...,...):
        self.ser = serial.Serial(port=...,baudrate=...,timeout=1)                       # setup the serial object


    # ----------------------------------parameter function--------------------------------- #
    #  Action: read the data from the serial and return them as a string                    #
    # ------------------------------------------------------------------------------------- #
    def read(self):
        ...                                                                                 # get data from serial
        return ...                                                                          # return a str

    # ----------------------------------parameter function--------------------------------- #
    #  Action: send the data on the serial                                                  #
    # ------------------------------------------------------------------------------------- #
    def send(self,data):
        ...                 

    # ----------------------------------parameter function--------------------------------- #
    #  Action: close the serial port                                                        #
    # ------------------------------------------------------------------------------------- #
    ...

# ------------------------------------------------------------------------------------------#







