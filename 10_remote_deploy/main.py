import run_bash_cmd
from menu import Menu

def main():
    mainMenu = Menu()
    mainMenu.addOption("Check available memory")
    mainMenu.addOption("View network connections")
    mainMenu.addOption("Display free ram and swap")
    mainMenu.addOption("Quit")
    
    while choice != 4:
        choice = mainMenu.getInput()
        match choice:
            case 1, 2, 3:
                run_bash_cmd(choice)
            case 4:
                pass