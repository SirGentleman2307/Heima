from Ui.Ui_Sys import System_UI
from Logic.Log_Sys import System_LOG
from Data.Data_Sys import System_DATA

if __name__ == "__main__":

    Ui = System_UI()
    Logic = System_LOG()
    Data = System_DATA()
    Ui.start_up()
