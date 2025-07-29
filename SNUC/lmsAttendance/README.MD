# 📘 LMS Attendance Export Automation Tool

This Python script automates the following workflow for [SNU Chennai LMS](https://lms.snuchennai.edu.in):
The pdf out put you can paste directly on Class Record (Log Book)

1. ✅ Logs in to the LMS using Selenium
2. 📥 Downloads the attendance sheet
3. ✂️ Cleans and processes the downloaded Excel file
4. 🧹 Removes unwanted patterns (e.g. `(2/2)`, `?`, `All students`)
5. 🧬 Merges name columns
6. 📤 Exports selected columns to a clean, print-friendly PDF

---

## 🚀 Features

- Automatic login and navigation using Selenium
- Auto-installs required Python packages
- Merges names from two columns
- Removes unnecessary text patterns
- Selects and formats specific columns
- Outputs a **PDF** with fixed column widths:
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
python script.py -u <username> -p <password> -c "<Course Name>" -l <number_of_lectures>
```
## Author
Dr. Rourab Paul
Department of Computer Science and Engineering
Shiv Nadar University Chennai

