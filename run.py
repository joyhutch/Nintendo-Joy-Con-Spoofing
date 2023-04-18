from os import geteuid
from joyspoof.joyspoof import main

if __name__ == '__main__':
    # check if root
    if geteuid() != 0:
        raise PermissionError('Script must be run as root!')
    main()
