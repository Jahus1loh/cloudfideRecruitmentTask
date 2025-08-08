# cloudfideRecruitmentTask
# 📌 Recruitment Task

## 📍 Task Description

Implement the function `add_virtual_column` which:
- Takes a `pandas.DataFrame`, a formula (`role`), and a name for a new column.
- Performs basic operations (**addition `+`**, **subtraction `-`**, **multiplication `*`**) using existing DataFrame columns.
- Returns a new DataFrame with the calculated column.
- Returns an **empty DataFrame** if:
  - Column names are invalid (must contain only letters and underscores `_`).
  - The formula contains unsupported characters.
  - The formula references columns not in the DataFrame.

---

## 📦 Function Signature

```python
import pandas

def add_virtual_column(df: pandas.DataFrame, role: str, new_column: str) -> pandas.DataFrame:
    return pandas.DataFrame([])
