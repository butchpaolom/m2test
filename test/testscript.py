import xlrd
import os
import requests
import threading
import json

files = os.listdir()

url = 'http://localhost:8080/api/people/'

while True:
    print("Test\n1. Create (Creates data based on the test values in the excel file)\n2. Retrieve (Show records)\n3. Update (Update the first_name of a selected record to `abcde`)\n4. Delete (Deletes a selected/all record(s))")
    opt = input()
    os.system('cls')

    def r_post(url, data):
        r = requests.post(url, json=data)

    def r_put(url, id, data):
        r = requests.put(url+str(id)+'/', json=data)


    def r_list(url):
        r = requests.get(url)
        print("id - first_name - last_name - middle_name - gender - age")
        ids = []
        for each in r.json():   
            print(f'{each["id"]} - {each["first_name"]} - {each["last_name"]} - {each["middle_name"]} - {each["gender"]} - {each["age"]}')
            ids.append(each["id"])
        return ids

    def r_delete(url, id):
        r = requests.delete(url+str(id))

    if opt == '1':
        for each in files:
            if each == 'testdata.xlsx':
                loc = (each)
                wb = xlrd.open_workbook(loc) 
                sheet = wb.sheet_by_index(0)
                for row in range(1,sheet.nrows):
                    data = {
                        "first_name": sheet.cell_value(row, 0),
                        "last_name": sheet.cell_value(row, 1),
                        "middle_name": sheet.cell_value(row, 2),
                        "gender": sheet.cell_value(row, 3),
                        "age": sheet.cell_value(row, 4)
                    }
                    threading.Thread(target=r_post, args=(url, data)).start()
    if opt == '2':
        r_list(url)
    if opt == '3':
        r_list(url)
        id = input("ID of the instance you want to update:\n")
        data = {
                "first_name": 'abcde',
            }
        r_put(url, id, data)
        os.system('cls')
        r_list(url)
    if opt == '4':
        id = input("Please select ID or input 'all' if you wish to delete all records: \n")
        if id == 'all':
            for each in r_list(url):
                threading.Thread(target=r_delete, args=(url, each)).start()
                os.system('cls')
        else:
            r_delete(url, id)