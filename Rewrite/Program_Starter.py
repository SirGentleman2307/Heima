from Data.data_class import Data
from UI.tui_rewrite import Tui
from Logic_.Logic import Main_logic

if __name__ == "__main__":

    data_api = Data()
    Ui_api = Tui()
    logic_api = Main_logic()

    Ui_api.start_up()