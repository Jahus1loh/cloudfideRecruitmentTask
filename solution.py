import pandas as pd
import re

def add_virtual_column(df: pd.DataFrame, role: str, new_column: str):
    if not contains_only_letters_and_underscores(new_column):
        return pd.DataFrame()
    
    role = get_column_names_and_operation_type(role)
    
    for series_name, series in df.items():
        if not contains_only_letters_and_underscores(series_name):
            return pd.DataFrame()
    
    if  len(role) != 3 or not (
        contains_only_letters_and_underscores(role[0]) and 
        contains_only_letters_and_underscores(role[2]) and 
        check_if_role_column_names_exist_in_df(role, df)):
        return pd.DataFrame()
        
    if role[1] == "+":
        return perform_addition(df, role[0], role[2], new_column)
        
    elif role[1] == "*":
        return perform_multiplication(df, role[0], role[2], new_column)
    
    elif role[1] == "-":
        return perform_substraction(df, role[0], role[2], new_column)
    
    return pd.DataFrame()
    
def check_if_role_column_names_exist_in_df(roles: list[str], df: pd.DataFrame):
    try:
        df[roles[0]]
        df[roles[2]]
        return True
    except Exception as e:
        print("There isn't column with this name in the dataframe")
        return False
    

def perform_addition(df: pd.DataFrame, first_column: str, second_column: str, new_column:str):
    df[new_column] = df[first_column] + df[second_column]
    return df
    
def perform_multiplication(df: pd.DataFrame, first_column: str, second_column: str, new_column:str):
    df[new_column] = df[first_column] * df[second_column]
    return df

def perform_substraction(df: pd.DataFrame, first_column: str, second_column: str, new_column:str):
    df[new_column] = df[first_column] - df[second_column]
    return df

# Helper function to check if word contains only letters and underscores
def contains_only_letters_and_underscores(word: str): 
    return bool(re.fullmatch("[a-zA-z_]+", word))


# Helper function to retrieve the column names and operation type from the role variable
def get_column_names_and_operation_type(role: str):
    column_names_and_operation_type = re.split(r'([+\*\-])', role)
    column_names_and_operation_type = [x.replace(" ", "") for x in column_names_and_operation_type]
    
    #column_names_and_operation_type[1] = deterimne_operation_type(column_names_and_operation_type[1])
        
    return column_names_and_operation_type
        
    
df = pd.DataFrame([[1, 1]] * 2, columns = ["label_one", "label_two"])

print(add_virtual_column(df, "label_one + label_two", "label_three"))
