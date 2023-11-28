import sys
import os
import shutil
from datetime import datetime

# List of paths to backup
chromedata_paths = [
    'C:/Users/<username>/AppData/Roaming/Mozilla/Firefox/Profiles/<profilename>/storage/default/moz-extension+++<extension-number>^userContextId=<contextId>', #<contextId> is located in the filepath. Only two files in that filepath will contain your extension number
    'C:/Users/<username>/AppData/Roaming/Mozilla/Firefox/Profiles/7dwg01ao.default-release/storage/default/moz-extension+++<extension-number>' #insert <username> and <extension-number> from filepath. Can find extension number by right-clicking onetab icon > `OneTab` > `Display OneTab`
]

local_path = './Backups/'  # this is your backups folder path

def backup():
    now = datetime.now()  # current date and time
    date_time = now.strftime('%m-%d-%Y_%H-%M-%S')
    
    # Create a backup folder with the current datetime
    backup_path = os.path.join(local_path, date_time)
    os.makedirs(backup_path, exist_ok=True)
    print(f'Backup folder created at {backup_path}')

    # Iterate over the folders to back up
    for path in chromedata_paths:
        # Determine the name of the folder to create in the backup directory
        folder_name = os.path.basename(path)
        dest = os.path.join(backup_path, folder_name)
        os.makedirs(dest, exist_ok=True)
        print(f'Created directory {dest}')

        # Copy the contents of the source directory to the backup directory
        for item in os.listdir(path):
            s = os.path.join(path, item)
            d = os.path.join(dest, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, dirs_exist_ok=True)
                print(f'Copied directory {s} to {d}')
            else:
                shutil.copy2(s, d)
                print(f'Copied file {s} to {d}')

    print('Backup complete')

def main():
    args = sys.argv[1:]

    if len(args) == 0:
        fn = input('Backup or restore? ').lower()
        if fn == 'backup':
            backup()
        else:
            print('Restore function not implemented for directories.')
    elif args[0] == '--backup':
        backup()
    else:
        print('Invalid command. Usage: --backup')

if __name__ == '__main__':
    main()
