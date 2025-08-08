# cloudfideRecruitmentTask

## Task Description

You have a panda DataFrame with existing data and want to create a new DataFrame that includes the original data along with an additional column calculated based on specific operations. To achieve this, implement the add_virtual_column_function.

---

## Inputs
 - df: Any pandas DataFrame.
 - role: A mathematical expression defining how to compute the values for the virtual column. For example, first_column - second_column.
 - new_column: The name of the new virtual column to be added.

---

## Examples

```python
print(fruits_sales)
# Output:
#    name  quantity  price
# 0  banana    10     10
# 1  apple      3      1

sales_total = add_virtual_column(fruits_sales, "quantity * price", "price_total")
print(sales_total)
# Output:
#    name  quantity  price  price_total
# 0  banana   10       10        100
# 1  apple     3        1          3
```

## Function Signature

```python
import pandas

def add_virtual_column(df: pandas.DataFrame, role: str, new_column: str) -> pandas.DataFrame:
    return pandas.DataFrame([])

```

---

## Validations

 - Column labels must consist only of letters and underscores (_).
 - The function must support basic operations: addition (+), subtraction (-), and multiplication (*).
 - If the role or any column label is incorrect, the function should return an empty DataFrame.

---


