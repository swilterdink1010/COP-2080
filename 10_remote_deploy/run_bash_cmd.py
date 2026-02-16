from os import system
def run_bash_cmd(some_choice):
    print('\n', '-' * 80, '\n')
    # print('You entered #', some_choice)
    match some_choice:
        case 1:
            print('The available memory is ')
            system('free -tmh')
        case 2:
            print('The current network connections include: ')
            system('netstat -an | grep -i Estab | cut -d \':\' -f 2,3 | gawk'\
                    '{print $2}\' | grep [0-9] | uniq')
        case 3:
            print('Available file space is: ')
            system('df -h | grep \"Filesystem\|root\"')
    
    print('\n', '-' * 80, '\n')
    return