import pandas as pd

def match_and_copy(file_a, file_b, output_file):
    # Read CSV (File A)
    df_a = pd.read_csv(file_a)

    # Mail column (5th col = index 4)
    col_mail = 4
    col_target = 34  # 35th col (index 34)

    # Take mail IDs starting from row 10 (skip first 9)
    mails_a = df_a.iloc[9:, col_mail]

    results = []

    # Load all sheets from File B
    xls = pd.ExcelFile(file_b)
    
    for mail in mails_a:
        if pd.isna(mail):  # stop if blank
            break

        found = False
        for sheet in xls.sheet_names:
            df_b = pd.read_excel(file_b, sheet_name=sheet)

            # Make sure sheet has enough columns
            if df_b.shape[1] <= col_target:
                continue

            # Search mail in 5th column
            match = df_b[df_b.iloc[:, col_mail] == mail]

            if not match.empty:
                value = match.iloc[0, col_target]
                results.append((mail, sheet, value))
                print(f"Found match in '{sheet}': {mail} -> {value}")
                found = True
                break  # stop searching once found in a sheet

        if not found:
            results.append((mail, None, None))
            print(f"No match found for: {mail}")

    # Save results into Excel
    result_df = pd.DataFrame(results, columns=["Mail ID", "Sheet Found", "Matched Value (Col 35)"])
    result_df.to_excel(output_file, index=False)
    print(f"\n✅ Results saved in {output_file}")

# Example usage
match_and_copy("file_a.csv", "file_b.xlsx", "output_results.xlsx")
