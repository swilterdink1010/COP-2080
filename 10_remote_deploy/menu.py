## An adjustable menu displayed in the terminal.
#
class Menu:
    ## Constructs a menu with no options by default.
    #
    def __init__(self):
        self._options = []
        
        
    def _printMenu(self):
        i = 1
        for option in self._options:
            print(i, " " + option)
            i += 1
    ## Adds an option to the menu.
    #
    def addOption(self, option):
        self._options.append(option)
    ##  Displays the menu, prompts user, and specifically 
    #   returns an index [1, n+1] from the list of menu options
    #        
    def getInput(self)->int:
        input_ = 0
        while True:
            self._printMenu()
            input_ = int(input("Enter a menu option: "))
            if input_ <= len(self._options) and input_ > 0:
                return input_
            print(f"Please enter a valid selection from the menu [1 - {len(self._options)}]")