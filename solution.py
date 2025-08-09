import pandas as pd
import re

# Function to add new_column to the df based on the expression in role variable
def add_virtual_column(df: pd.DataFrame, role: str, new_column: str):
    role = get_column_names_and_operation_type(role)
    
    if check_if_any_column_name_is_incorrect(df, role, new_column):
        return pd.DataFrame()
        
    if role[1] == "+":
        return perform_addition(df, role[0], role[2], new_column)
        
    elif role[1] == "*":
        return perform_multiplication(df, role[0], role[2], new_column)
    
    elif role[1] == "-":
        return perform_substraction(df, role[0], role[2], new_column)
    
    return pd.DataFrame()


# Function to check if column names in the df, role and new_column have only letters and underscores
def check_if_any_column_name_is_incorrect(df, role, new_column):
    if len(role) != 3: return True # This will happen if column name in role contains -, + or *
    if not contains_only_letters_and_underscores(role[0]): return True # This will happen when first column name has some incorrect characters
    if not contains_only_letters_and_underscores(role[2]): return True # This will happen when second column name has some incorrect characters
    if not check_if_column_names_in_df_are_correct(df): return True # This will happen when some column name in df has some incorrect characters
    if not check_if_role_column_names_exist_in_df(role, df): return True # This will happen when role tries to use some column that doesn't exist in df
    if not contains_only_letters_and_underscores(new_column): return True # This will happen when new column name has some incorrect characters
    
    return False
    
    
# Function to check if column names specified in roles are present in df
def check_if_role_column_names_exist_in_df(roles: list[str], df: pd.DataFrame):
    return set([roles[0], roles[2]]).issubset(df.columns)
        
    
# Function to check if every column name in the df has only letters and underscores
def check_if_column_names_in_df_are_correct(df):
    for series_name, series in df.items():
        if not contains_only_letters_and_underscores(series_name):
            return False
        
    return True

# Function to perform addition of df columns
def perform_addition(df: pd.DataFrame, first_column: str, second_column: str, new_column:str):
    df[new_column] = df[first_column] + df[second_column]
    return df
    
    
# Function to perform multiplication of df columns
def perform_multiplication(df: pd.DataFrame, first_column: str, second_column: str, new_column:str):
    df[new_column] = df[first_column] * df[second_column]
    return df


# Function to perform substraction of df columns
def perform_substraction(df: pd.DataFrame, first_column: str, second_column: str, new_column:str):
    df[new_column] = df[first_column] - df[second_column]
    return df


# Function to check if word contains only letters and underscores
def contains_only_letters_and_underscores(word: str): 
    return bool(re.fullmatch("[A-Za-z_]+", word))


# Function to retrieve the column names and operation type from the role variable
def get_column_names_and_operation_type(role: str):
    column_names_and_operation_type = re.split(r'([+\*\-])', role) # Split the role string into a list on +, - or *, and include the operation sign
    column_names_and_operation_type = [x.replace(" ", "") for x in column_names_and_operation_type] # Remove all spaces from the strings
            
    return column_names_and_operation_type

