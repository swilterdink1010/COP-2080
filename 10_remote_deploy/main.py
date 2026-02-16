from run_bash_cmd import run_bash_cmd as rbc
from menu import Menu

def main():
    mainMenu = Menu()
    mainMenu.addOption("Check available memory")
    mainMenu.addOption("View network connections")
    mainMenu.addOption("Display free ram and swap")
    mainMenu.addOption("Quit")
    
    choice = 0
    while choice != 4:
        choice = mainMenu.getInput()
        rbc(choice)
            
if __name__ == "__main__":
    main()