#
from sys import argv
import csv
import json
import uuid

csvFileSource = argv
jsonFileOutput = "nextcloud_passwords_db.json"


def rm_quotes(val):
    if val == '""':
        return ''
    else:
        return val[1:-1]


home_dir_uuid = "00000000-0000-0000-0000-000000000000"
vals = []
folders_ = []
dirs = {}

with open('keepass.csv', encoding='utf-8', newline='\n') as csvfile:
    csvReader = csv.DictReader(csvfile, delimiter=',', quotechar=' ')
    for value in csvReader:
        path = rm_quotes(value["\"Group\""]).split("/")
        for dir_name in path:
            if not dir_name in dirs:
                dirs[dir_name] = str(uuid.uuid4())
            folder_record = dirs[dir_name]
            dirs_list = list(folder_record)
            if path.index(dir_name) == 0:
                parent_folder_uuid = home_dir_uuid
            else:
                try:
                    parent_folder_uuid = dirs[path[path.index(dir_name) - 1]]
                    parent_folder_nm = dirs_list[path.index(dir_name) - 1]
                except (ValueError, IndexError):
                    parent_folder_uuid = home_dir_uuid
            folders = {
                "id": dirs[dir_name],
                "label": dir_name,
                "parent": parent_folder_uuid
            }
            if folders in folders_:
                continue
            else:
                folders_.append(folders)
        pw = rm_quotes(value["\"Password\""])
        if pw == '':
            pw = "empty"
        else:
            pw = rm_quotes(value["\"Password\""])
        passwords = {
                        "label": rm_quotes(value["\"Title\""]),
                        "username": rm_quotes(value["\"Username\""]),
                        "password": pw,
                        "notes": rm_quotes(value["\"Notes\""]),
                        "url": rm_quotes(value["\"URL\""]),
                        "customFields": [],
                        "folder": folder_record
                    },
        vals.append(passwords)

pws = [x[0] for x in vals]
fld = [x for x in folders_]

res = {
    "version": 3,
    "encrypted": False,
    "passwords": pws,
    "folders": fld
}


with open(jsonFileOutput, 'w') as jsonFile:
    jsonFile.write(json.dumps(res))
