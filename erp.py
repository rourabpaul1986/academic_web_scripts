from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
from selenium.common.exceptions import TimeoutException
import time
import os
from datetime import datetime
import webdriver_manager
import selenium
import sys
import argparse
import threading

def find_oldest_and_latest_dates(date_strings):
    """
    Find the oldest and latest dates from a list of date strings.

    Args:
        date_strings (list): A list of date strings in 'dd/mm/yyyy' format.

    Returns:
        tuple: A tuple containing the oldest date and the latest date as strings.
    """
    # Define the date format
    date_format = "%d/%m/%Y"
    
    # Convert the date strings into datetime objects
    dates = [datetime.strptime(date_str, date_format) for date_str in date_strings]
    
    # Find the oldest and latest dates
    oldest_date = min(dates)
    latest_date = max(dates)
    
    # Convert the datetime objects back to strings for display
    oldest_date_str = oldest_date.strftime(date_format)
    latest_date_str = latest_date.strftime(date_format)
    
    return oldest_date_str, latest_date_str

def click_button():
    try:
        button.click()
        #print("Button clicked successfully!")
    except Exception as e:
        print(f"Error to load ERP: {e}")
       
def read_nth_column(file_path, n, separator): 
    column_data = []
    with open(file_path, 'r') as file:
        for line in file:
            # Remove leading/trailing whitespace and split the line into columns
            columns = line.strip().split(separator)
            if len(columns) > n:  # Check if the nth column exists
                column_data.append(columns[n])
    return column_data
print("#######################This Program is Tested With Below Version :#######################")
print(f"\t python version of this device : {sys.version}")
print(f"\t selenium version of this device: {selenium.__version__}")
print(f"\t webdriver_manager version of this device :  {webdriver_manager.__version__}")
print("\t The program is tested with python: 3.9.6, selenium: 4.25.0 &webdriver_manager: 4.0.2")
print("#########################################################################################")


parser = argparse.ArgumentParser(description="A simple argument parser example.")
    
# Add arguments
parser.add_argument('-u', '--username', type=str, help='Your ERP username', required=True)
parser.add_argument('-p', '--password', type=str, help='Your ERP Password', required=True)
parser.add_argument('-sm', '--semester', type=str, help='Enter Semester ', required=True)
parser.add_argument('-sb', '--subject', type=str, help='Enter Subject', required=True)
parser.add_argument('-hl', "--headless", type=str, default='', help="to run chrome in headless mode")

parser.add_argument('--verbose', action='store_true', help='Enable verbose mode')

# Parse the arguments
args = parser.parse_args()

# Access the arguments
#print(f"Hello, {args.username}!")
#print(f"You are {args.password} years old.")
 
username=args.username
password= args.password  
semester=args.semester
subject=args.subject
print(f"\t Hi {username}, you have chosen Semester: {semester} \n\t Subjects : {subject} for ERP Attendance Script")
print("#########################################################################################")   
if args.verbose:
 print("Verbose mode is enabled.")
##############################################################



file_name = "date_loader.txt"
dates = read_nth_column(file_name, 0, ";")
times = read_nth_column(file_name, 1, ";")
modes = read_nth_column(file_name, 2, ";")
sl = read_nth_column(file_name, 3, ";")

min_date, max_date = find_oldest_and_latest_dates(dates)
#min_date = min(dates)
#max_date = max(dates)

f=min_date 
t=max_date 
print(f"\t Starting Date: {f} & Last Date : {t} is entered in date_loader.txt")
#print(sl)

chrome_options = Options()
chrome_options.add_argument("--headless")  # Enable headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920x1080") 
# Optionally, you can use ChromeDriverManager for automatic management of the driver
if(args.headless=="headless"): 
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
else:
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# If using a downloaded chromedriver
# driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

driver.get('http://10.0.2.45:8082/CLXOAuthServer/')

driver.maximize_window()
# Perform actions...
username_input = driver.find_element(By.ID, "j_username")
username_input.send_keys(username)
password_field = driver.find_element(By.NAME, 'j_password')
password_field.send_keys(password)

try:
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'buttonui') and normalize-space(text())='Login']"))
    )
    ##################################################
    # Create a thread to handle the button click
    click_thread = threading.Thread(target=click_button)
    click_thread.start()
    print("\t ERP Loading Started..")
    # Print loading messages while waiting for the button click to complete
    loading_percent = 0
    while click_thread.is_alive():
     dot="#"
     #print(f"Loading... {loading_percent}%")
     print(f"{dot}", end='', flush=True) 
     time.sleep(1.2)  # Adjust the sleep time to control how often the message is printed
     loading_percent += 1
     #dot=f"{dot}|"
     if loading_percent > 100:
        loading_percent = 0

    # Join the thread to ensure it finishes before moving on
    click_thread.join()
    print(f"\t successfully logged in with {username} credentials")
    ####################################################
except Exception as e:
    print(f"Error: {e}")

# Keep the browser open for a while to see the result (for demonstration)
# Locate the element by its id and click it
webkiosk_li = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "Webkiosk (Staff)"))
)
webkiosk_li.click()


# Wait until the link is clickable
link = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='widgetgroup']/div/a/div/div[2]"))
)
link.click()
print("\t Web Kiosk Opened")
# Wait until the dropdown is visible and click to open the options
dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'institute_chosen'))
)
dropdown.click()

# Wait until the specific option with data-option-array-index="1" is visible and click on it
option = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "li[data-option-array-index='1']"))
)
option.click()

# Locate the "SUBMIT" link and click it
submit_button = driver.find_element(By.XPATH, "//a[contains(@class, 'btn') and text()='SUBMIT']")
submit_button.click()

academic_info = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Academic Info']"))
)
academic_info.click()

# Wait until the anchor element containing "Student Attendance Entry" is clickable, then click it
attendance_entry_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Student Attendance Entry')]"))
)
attendance_entry_link.click()

# Wait until the <span> element containing "Select Semester" is clickable, then click it
select_semester_span = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Select Semester']"))
)
select_semester_span.click()


# Wait until the list item containing "ODD SEM 2024 - ITER" is clickable, then click it
semester_option = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, f"//li[@data-option-array-index='1' and text()='{semester}']"))
    
    #EC.element_to_be_clickable((By.CSS_SELECTOR, "li[data-option-array-index='1']"))
)
semester_option.click()

# Wait until the <span> element containing "Select" is clickable, then click it
select_span = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Select']"))
)
select_span.click()


# Wait until the list item containing "ODD SEM 2024 - ITER" is clickable, then click it
subject_option = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, f"//li[@data-option-array-index='1' and text()='{subject}']"))
)
subject_option.click()



###################################################

date_from = driver.find_element(By.NAME, "datefrom")  # Adjust the selector as needed
date_from.clear()  # Clear any existing text
date_from.send_keys(f)  # Insert your desired text

date_to = driver.find_element(By.NAME, "dateto")  # Adjust the selector as needed
date_to.clear()  # Clear any existing text
date_to.send_keys(t)  # Insert your desired textprint(f"{absent_radio_button_id} is clicked")


load_button = driver.find_element(By.CSS_SELECTOR, "a.btn.btn-success.btn-md")
load_button.click()  # Click the Load button

print(f"Date range: {f} to {t} is loaded in ERP")

time.sleep(10)


###################################################

for i in range(0, len(dates)):
    target_date = dates[i]
    target_time = times[i]
    print(f"\t target time:{target_time} target date:{target_date}")
    mode = modes[i]
    #xpath_expression = f"//tr[td/a[contains(text(), '{target_date}')] and td[contains(text(), '{target_time}')]]"
    # XPath to find the row where the <a> contains the date and the <td> contains the time
    # XPath to locate the input field
    #input_xpath = "//input[@type='search' and contains(@class, 'form-control input-sm')]"

    
    # Wait for the input field to be present
    #input_xpath = "//input[@type='search' and contains(@class, 'form-control input-sm')]"
    input_xpath ="//*[@id='datatable_filter']/label/input"
    try:
        # Wait for the input field to be present
        search_input = WebDriverWait(driver, 10).until(
         EC.presence_of_element_located((By.XPATH, input_xpath))
        )
    
        # Clear the input field if needed, and type the desired text
        search_input.clear()
        search_input.send_keys(target_time)
        print(f"\t {target_time} entered in filter successfully.")

    except Exception as e:
        print(f"Error: {str(e)}")
    #time.sleep(10)
    xpath_expression=f"//a[contains(text(), '{target_date}')]"
 
    ################## Date Clicking #####################################
    try:
        # Attempt to find the date link
        date_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, xpath_expression))
        )
        
        # Scroll to the element to make sure it is visible in the viewport
        driver.execute_script("arguments[0].scrollIntoView(true);", date_link)
        
        # Click the element using JavaScript if normal click fails
        driver.execute_script("arguments[0].click();", date_link)
        
        print(f"\tClass on: {target_date}, Time: {target_time} link opened")

    except TimeoutException as e:
        # Handle the case where the target date link is not found
        print(f"Error: Target date '{target_date}' not found within the time limit.")
        print(f"Exception message: {str(e)}")
        sys.exit(1)
    except Exception as e:
        # Handle any other exceptions
        print(f"An error occurred: {str(e)}")
        sys.exit(1)
    #######################################################
    #print(f"full sl: {sl[i]}")    
    if(mode=="P" or mode==" P" ):
     s="absent"
     s_inv="present"
    else:
     s="present"
     s_inv="absent"
    status_radio_button = WebDriverWait(driver, 50).until(
         EC.element_to_be_clickable((By.ID, f"all{s}"))
    )
    time.sleep(1)
    status_radio_button.click()
    driver.execute_script("arguments[0].click();", status_radio_button)
    print(f"\t All {s} of target date: {target_date} and time : {target_time} link is clicked")
    ###################################################################
    sl_list = sl[i].split(",") ##split by comma
    for j in range(len(sl_list)):
     #print(f"sl list {sl_list[j]}")
     #students=sl_list[j]
     students= sl_list[j].replace(" ", "")
     student=int(students)-1 # Calibration of given Serial Number with ERP Serial Number
     ###################################################################
     absent_radio_button_id = f"status{s_inv}{student}"  
     #print(absent_radio_button_id)
     absent_radio_button = WebDriverWait(driver, 50).until(
     EC.element_to_be_clickable((By.ID, absent_radio_button_id))
     )
     time.sleep(1)
     #print(f"{absent_radio_button_id} is not clicked")   
     #absent_radio_button.click()     
     #print(f"{absent_radio_button_id} is clicked")   
     driver.execute_script("arguments[0].click();", absent_radio_button)
     print(f"\t Class Attendance on Date: {target_date} & Time: {target_time}  is updated for Student Sl. No. {student-1}")
     ####################################################################     
    save_attendance_button = WebDriverWait(driver, 50).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Save Attendance')]"))
    )
    save_attendance_button.click()
    print(f"\n\t \033[31m Class Attendance on Date: {target_date} & Time: {target_time}  is Saved Successfully\033[0m")
    time.sleep(10)
######################################################

time.sleep(10)
print(f"\n \033[31m{username} your student attendance of date range {dates} uploaded successfully in ERP\033[0m")
driver.quit()
