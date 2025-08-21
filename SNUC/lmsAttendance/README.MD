# 📘 LMS Attendance Export Automation Tool
This Python script automates the workflow for [SNU Chennai LMS](https://lms.snuchennai.edu.in). It downloads the student attendance from the LMS and generates a formatted PDF output. This PDF can be directly pasted into the Class Record (Log Book). The current version of the tool does not include registration numbers, as they are not available in the LMS. Student names are listed in alphabetical order based on their first names."


1. ✅ Logs in to the LMS using Selenium
2. 📥 Downloads the attendance sheet
3. ✂️ Cleans and processes the downloaded Excel file
4. 🧹 Removes unwanted patterns (e.g. `(2/2)`, `?`, `All students`)
5. 🧬 Merges name columns
6. 📤 Exports selected columns to a clean, print-friendly PDF for CLASS RECORD (log_book.pdf)

---

## 🚀 Features

- Automatic login and navigation using Selenium
- Auto-installs required Python packages
- Merges first and last names from two columns
- Removes unnecessary text patterns
- Selects and formats specific columns
- Outputs a **PDF** with fixed column widths (As per Class Record):
  - First column: `46.66mm`
  - All other columns: `5.83mm`

---

## 🛠️ Requirements

- Python 3.6+
- Google Chrome (latest)
- ChromeDriver (auto-managed by `webdriver-manager`)

---

## 📦 Auto-installed Python Libraries

These are automatically installed at runtime if not present:


---

## 🧾 Usage

```bash
python lmsAttandacne.py -u <username> -c "<Course Name>" -s <starting class no.> -l <number_of_lectures>
```
If you write
```bash
python lmsAttandacne.py -u <username> -c "<Course Name>" -s 1 -l 20
```
This means it will download the attendance from 1st class to 20.
if you write
```bash
python lmsAttandacne.py -u <username> -c "<Course Name>" -s 3 -l 20
```
This means it will download the attendance from 3rd class to 23.
## Author
Dr. Rourab Paul
Department of Computer Science and Engineering
Shiv Nadar University Chennai

## Contact
If you are facing any dificulties please contact at rourabpaul@gmail.com


## Tested
The program is tested in all kind of linux OS

