# Mail ID Matcher

This project provides a Python script to match mail IDs from a CSV file against an Excel file (with multiple sheets).  
If a match is found, the script copies the corresponding value from the **35th column** of the Excel sheet.  

---

## 📂 Input Files

- **File A (CSV)**  
  - Contains mail IDs in the **5th column**.  
  - First **9 rows are skipped** (data starts from row 10).  

- **File B (Excel, `.xlsx`)**  
  - May contain multiple sheets.  
  - Each sheet has mail IDs in the **5th column**.  
  - Value to be copied is in the **35th column**.

---

## ⚙️ How it Works

1. Read `file_a.csv` and extract mail IDs from the 5th column (row 10 onwards).  
2. For each mail ID:
   - Search through all sheets of `file_b.xlsx`.  
   - If a match is found in the 5th column, copy the value from the 35th column.  
   - Record the sheet name where the match was found.  
3. If no match is found, record `None`.  
4. Save the results to a new Excel file `output_results.xlsx`.

---

## 📊 Output Format

The output Excel file contains:

| Mail ID         | Sheet Found | Matched Value (Col 35) |
|-----------------|-------------|-------------------------|
| test@example.com | Sheet1      | SomeValue              |
| foo@bar.com     | None        | None                   |

---

## 🚀 Usage

### 1. Install dependencies
```bash
pip install pandas openpyxl
