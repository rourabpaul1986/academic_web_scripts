# ERP Attendance Upload 
This script can upload attenance of students of all dates in ERP system in a single click.
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
In this above example on date: 15/10/2024, the students of serial number 1, 3, 5, 7 were present.\n
Similarly on 18/10/2024, the students of serial number 2, 4, 6, 7 were absent.

### 1. open
```
 python3 erp.py -u username -p password -sm semester -sb subject
```
For an example username: 123456789, password=password, semester='ODD SEM 2024' - ITER and subject='CSE3156/Digital Forensics Workshop'
```sudo nano /etc/apt/sources.list
 python3 erp.py -u 123456789 -p password -sm 'ODD SEM 2024 - ITER' -sb 'CSE3156/Digital Forensics Workshop'
```



