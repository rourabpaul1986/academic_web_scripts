# ERP Attendance Upload from txt file
The erp.py script can upload the attendance of students for all dates mentioned in date_loader.txt to the ERP system with a single click. This program requires the selenium and webdriver_manager packages. To install selenium, you need to write:
```
pip3 selenium
pip3 webdriver_manager
```
The program is tested with <b>python 3.9.6</b>, <b>selenium 4.25.0</b> & <b>webdriver_manager 4.0.2</b>
This repository has two files: (1) date_loader.txt and (2)erp.py
## Steps
The erp.py required 4 command line argumenrs


### 1. Write date_loader.txt
You need made a date_loader.txt. which must have 3 columns in each rows. The 1st column stores the date, 2nd column stores the student attendance status (P/A) and finaly the 3rd column should be the serial number of the students
```
15/10/2024; P; 1, 3, 5, 7
18/10/2024; A; 2, 4, 6, 7
17/10/2024; P; 1, 3, 5, 7, 22
```
In this above example, the students of serial number 1, 3, 5, 7 were present on date: 15/10/2024.<br>
Similarly, the students of serial number 2, 4, 6, 7 were absent on 18/10/2024.

### 2. run erp.py script
```
 python3 erp.py -u username -p password -sm semester -sb subject
```
For an example username: 123456789, password=password, semester='ODD SEM 2024' - ITER and subject='CSE3156/Digital Forensics Workshop'
```
 python3 erp.py -u 123456789 -p password -sm 'ODD SEM 2024 - ITER' -sb 'CSE3156/Digital Forensics Workshop'
```
If you want to run the chorme in headless mode you need to write
```
 python3 erp.py -u 123456789 -p password -sm 'ODD SEM 2024 - ITER' -sb 'CSE3156/Digital Forensics Workshop' -hl headless
```



