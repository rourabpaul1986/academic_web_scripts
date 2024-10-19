# ERP Attendance Upload 
This script can upload attenance of students of all dates in ERP system in a single click.
This repository has two files: (1) date_loader.txt and (2)erp.py
## Steps
The erp.py required 4 command line argumenrs

### 1. open
```sudo nano /etc/apt/sources.list
 python3 erp.py -u username -p password -sm semester -sb subject
```
For an example username: 123456789, password=password, semester='ODD SEM 2024' - ITER and subject='CSE3156/Digital Forensics Workshop'
```sudo nano /etc/apt/sources.list
 python3 erp.py -u 123456789 -p password -sm 'ODD SEM 2024 - ITER' -sb 'CSE3156/Digital Forensics Workshop'
```
### 2. add
deb http://deb.debian.org/debian/ bullseye main



