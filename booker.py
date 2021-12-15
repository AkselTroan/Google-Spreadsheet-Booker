import requests, csv, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from os import system, name
from tqdm import tqdm

lab = True  # Choose between Live Sheet or Test/Lab Sheet
pre_reserve = False
get_reqs = 0

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def clear():

    # For Windows
    if name == 'nt':
        _ = system('cls')

    # For MacOS and Linux
    else:
        _ = system('clear')


def update_screen():
    global get_reqs, pre_reserve
    get_reqs += 1
    clear()
    print(bcolors.OKGREEN + f'''  ____              _             
 | __ )  ___   ___ | | _____ _ __ 
 |  _ \ / _ \ / _ \| |/ / _ \ '__|
 | |_) | (_) | (_) |   <  __/ |   
 |____/ \___/ \___/|_|\_\___|_|                                                         
 ''' + bcolors.ENDC + bcolors.OKBLUE + '''
 Automatic insert data to google spreadsheet

 Written by Aksel Troan               
                                                     
                                                  
                                                      ''' + bcolors.ENDC)
    print(bcolors.OKCYAN + f" Get requests: {get_reqs}" + bcolors.ENDC)
    if pre_reserve is True:
        print("\n")
        print(bcolors.OKGREEN + " Found a Table with your name in the reservation. Continue scanning if they remove it..." + bcolors.ENDC)
    else:
        print("\n")
        print(bcolors.FAIL+ " Could not fint a current table with your name. Continue scanning if they a table opens..." + bcolors.ENDC)
    print(bcolors.OKGREEN)
    for i in tqdm(range(300), ncols= 100):  # This represents 5 minute. So 5 minutes between each get request
	    time.sleep(1)

def reserve_table_17():
    global lab

    driver = webdriver.Chrome('./chromedriver.exe')
    
    if lab is True:
        driver.get('https://docs.google.com/spreadsheets/d/1f1Jy4l_zmWgMDeBCpVzofehPCb6hAI1fGgGYW1JiD_4/edit#gid=0')
    else:
        driver.get('LIVE SHEET')
    
    driver.implicitly_wait(10)
    
    # Insert our wanted cell on the sheet, to check if there is a team and contact person
    driver.find_element_by_xpath('//*[(@id = "t-name-box")]').clear()  # Removes the current cell
    driver.find_element_by_xpath('//*[(@id = "t-name-box")]').send_keys(
        'C11' + Keys.ENTER)  # Inserts our wanted cell
    l = driver.find_element_by_xpath(
        '//*[contains(concat( " ", @class, " " ), concat( " ", "cell-input", " " ))]')  # Checks the value of the cell
    if l.text is "":  # If the cell is empty. If it is empty = Unoccupied table, starting to reserve the table
        driver.implicitly_wait(10)
        l.send_keys("Quiz-TeamName" + Keys.ENTER) # Spits in the team name on the table
        driver.find_element_by_xpath('//*[(@id = "t-name-box")]').clear()
        driver.find_element_by_xpath('//*[(@id = "t-name-box")]').send_keys(
            'D11' + Keys.ENTER)  # Shifts one cell to the right
        b = driver.find_element_by_xpath(
            '//*[contains(concat( " ", @class, " " ), concat( " ", "cell-input", " " ))]')  # Checks the value of the cell
        if b.text == "":
            driver.implicitly_wait(10)
            b.send_keys("Aksel Troan" + Keys.ENTER)  # Enters myself as a contact person.
    else:
        print("Occupied Table by " + l.text)
        print("Checking table 18...")
    
def reserve_table_18():

    driver = webdriver.Chrome('./chromedriver.exe')
    
    if lab is True:
        driver.get('https://docs.google.com/spreadsheets/d/1f1Jy4l_zmWgMDeBCpVzofehPCb6hAI1fGgGYW1JiD_4/edit#gid=0')
    else:
        driver.get('LIVE SHEET')
    
    driver.implicitly_wait(10)

    # Insert our wanted cell on the sheet, to check if there is a team and contact person
    driver.find_element_by_xpath('//*[(@id = "t-name-box")]').clear()  # Removes the current cell
    driver.find_element_by_xpath('//*[(@id = "t-name-box")]').send_keys(
        'C10' + Keys.ENTER)  # Inserts our wanted cell
    l = driver.find_element_by_xpath(
        '//*[contains(concat( " ", @class, " " ), concat( " ", "cell-input", " " ))]')  # Checks the value of the cell
    if l.text is "":  # If the cell is empty. If it is empty = Unoccupied table, starting to reserve the table
        driver.implicitly_wait(10)
        l.send_keys("Quiz-TeamName" + Keys.ENTER) # Spits in the team name on the table
        driver.find_element_by_xpath('//*[(@id = "t-name-box")]').clear()
        driver.find_element_by_xpath('//*[(@id = "t-name-box")]').send_keys(
            'D10' + Keys.ENTER)  # Shifts one cell to the right
        b = driver.find_element_by_xpath(
            '//*[contains(concat( " ", @class, " " ), concat( " ", "cell-input", " " ))]')  # Checks the value of the cell
        if b.text == "":
            driver.implicitly_wait(10)
            b.send_keys("Aksel Troan" + Keys.ENTER)  # Enters myself as a contact person.
    else:
        print("Occupied Table by " + l.text)
        print("Checking table 16...")

def reserve_table_16():

    driver = webdriver.Chrome('./chromedriver.exe')

    if lab is True:
        driver.get('https://docs.google.com/spreadsheets/d/1f1Jy4l_zmWgMDeBCpVzofehPCb6hAI1fGgGYW1JiD_4/edit#gid=0')
    else:
        driver.get('LIVE SHEET')
    
    driver.implicitly_wait(10)

    # Insert our wanted cell on the sheet, to check if there is a team and contact person
    driver.find_element_by_xpath('//*[(@id = "t-name-box")]').clear()  # Removes the current cell
    driver.find_element_by_xpath('//*[(@id = "t-name-box")]').send_keys(
        'C12' + Keys.ENTER)  # Inserts our wanted cell
    l = driver.find_element_by_xpath(
        '//*[contains(concat( " ", @class, " " ), concat( " ", "cell-input", " " ))]')  # Checks the value of the cell
    if l.text is "":  # If the cell is empty. If it is empty = Unoccupied table, starting to reserve the table
        driver.implicitly_wait(10)
        l.send_keys("Quiz-TeamName" + Keys.ENTER) # Spits in the team name on the table
        driver.find_element_by_xpath('//*[(@id = "t-name-box")]').clear()
        driver.find_element_by_xpath('//*[(@id = "t-name-box")]').send_keys(
            'D12' + Keys.ENTER)  # Shifts one cell to the right
        b = driver.find_element_by_xpath(
            '//*[contains(concat( " ", @class, " " ), concat( " ", "cell-input", " " ))]')  # Checks the value of the cell
        if b.text == "":
            driver.implicitly_wait(10)
            b.send_keys("Aksel Troan" + Keys.ENTER)  # Enters myself as a contact person.
    else:
        print("Occupied Table by " + l.text)
        print("Checking table 16...")



def main():
    global pre_reserve
    # Test sheet: https://docs.google.com/spreadsheets/d/1f1Jy4l_zmWgMDeBCpVzofehPCb6hAI1fGgGYW1JiD_4/edit#gid=0
    # Live sheet: LIVE SHEET

    # https://stackoverflow.com/questions/33713084/download-link-for-google-spreadsheets-csv-export-with-multiple-sheets
    # https://docs.google.com/spreadsheets/d/{key}/gviz/tq?tqx=out:csv&sheet={sheet_name}
    
    clear()
    print(bcolors.OKGREEN + '''  ____              _             
 | __ )  ___   ___ | | _____ _ __ 
 |  _ \ / _ \ / _ \| |/ / _ \ '__|
 | |_) | (_) | (_) |   <  __/ |   
 |____/ \___/ \___/|_|\_\___|_|                                                         
 ''' + bcolors.ENDC + bcolors.OKBLUE + '''
 Automatic insert data to google spreadsheet

 Written by Aksel Troan
               
                                                     
                                                      ''' + bcolors.ENDC)

    if lab is True:
        CSV_URL = 'https://docs.google.com/spreadsheets/d/1f1Jy4l_zmWgMDeBCpVzofehPCb6hAI1fGgGYW1JiD_4/gviz/tq?tqx=out:csv&range=B4:D24&sheet=test'
    else:
        CSV_URL = 'LIVE SHEET'

    booked_table = False
    first_table = False
    second_table = False
    third_table = False
    new_quiz = False
    pre_reserve = False
    while new_quiz is False:
        total_occ_table = 0    
        with requests.Session() as s:  # Fecthes spread sheet
            download = s.get(CSV_URL)

            decoded_content = download.content.decode('utf-8')

            cr = csv.reader(decoded_content.splitlines(), delimiter=',')
            my_list = list(cr)
            print("Tables at " + bcolors.HEADER + "Storsalen:" + bcolors.ENDC)
            print("Table Number: Team-name - Contact person" + "\n")
            # Priority list: 1: {table 17} 2: {table 18} 3: {table 16} 
            
            for row in my_list:
                if row[1] == "Quiz-TeamName" or row[2] == "Aksel Troan":  # If the host has not removed our table
                    pre_reserve = True
                
                if row[0] == "17" and row[1] == "" and row[2] == "":
                    print("Table 17 is open!")
                    first_table = True
                    new_quiz = True

                if row[0] == "18" and row[1] == "" and row[2] == "":
                    print("Table 18 is open!")
                    second_table = True
                    new_quiz = True

                if row[0] == "16" and row[1] == "" and row[2] == "":
                    print("Table 16 is open!")
                    third_table = True
                    new_quiz = True

                if row[1] == "" and row[2] == "":
                    print(bcolors.OKGREEN + "Table: " + bcolors.ENDC + bcolors.OKCYAN + row[0] + " is empty!" + bcolors.ENDC)
                
                else:
                    print(bcolors.FAIL + 'Table ' + row[0] + ': ' + row[1] + ' - ' + row[2] + bcolors.ENDC)
                    total_occ_table += 1


        if first_table is True and booked_table is False and pre_reserve is False:
            print("Reserving table 17...")
            reserve_table_17()
            booked_table = True
            print("\n" + bcolors.OKGREEN + "Successfully reserved table 17!")

        elif second_table is True and booked_table is False and pre_reserve is False:
            print("Reserving table 18...")
            reserve_table_18()
            booked_table = True
            print("\n" + bcolors.OKGREEN + "Successfully reserved table 18!")
            
            
        elif third_table is True and booked_table is False and pre_reserve is False:
            print("Reserving table 16...")
            reserve_table_16()
            booked_table = True
            print("\n" + bcolors.OKGREEN + "Successfully reserved table 16!")

        
        elif booked_table is False and not total_occ_table >= 20 and pre_reserve is False:
            print("Favorite tables is already booked. Scanning sheets and reserving first table")
            
            driver = webdriver.Chrome('./chromedriver.exe')
            if lab is True:
                driver.get('https://docs.google.com/spreadsheets/d/1f1Jy4l_zmWgMDeBCpVzofehPCb6hAI1fGgGYW1JiD_4/edit#gid=0')
            else:
                driver.get('LIVE SHEET')
            driver.implicitly_wait(10)

            table = 4
            reserved_tables = 0
            for i in range(21):
                # Insert our wanted cell on the sheet, to check if there is a team and contact person
                driver.find_element_by_xpath('//*[(@id = "t-name-box")]').clear()  # Removes the current cell
                driver.find_element_by_xpath('//*[(@id = "t-name-box")]').send_keys(
                    f'C{table}' + Keys.ENTER)  # Inserts our wanted cell
                l = driver.find_element_by_xpath(
                    '//*[contains(concat( " ", @class, " " ), concat( " ", "cell-input", " " ))]')  # Checks the value of the cell
                if l.text is "":  # If the cell is empty. If it is empty = Unoccupied table, starting to reserve the table
                    print("Found Empty Table! The cell is: " + 'C' + str(table))
                    if reserved_tables < 1 and booked_table is False:
                        l.send_keys("Quiz-TeamName" + Keys.ENTER) # Spits in the team name on the table
                        driver.find_element_by_xpath('//*[(@id = "t-name-box")]').clear()
                        driver.find_element_by_xpath('//*[(@id = "t-name-box")]').send_keys(
                            f'D{table}' + Keys.ENTER)  # Shifts one cell to the right
                        b = driver.find_element_by_xpath(
                            '//*[contains(concat( " ", @class, " " ), concat( " ", "cell-input", " " ))]')  # Checks the value of the cell
                        if b.text == "":
                            b.send_keys("Aksel Troan" + Keys.ENTER)  # Enters myself as a contact person.
                        reserved_tables += 1  # Tracker for how many tables we should reserve
                else:
                    print("Occupied Table by " + l.text + "! Can not reserve table: " + 'C' + str(table))
                table += 1
        if total_occ_table >= 20 or pre_reserve is True:
            update_screen()
        

if __name__ == "__main__":
    main()
