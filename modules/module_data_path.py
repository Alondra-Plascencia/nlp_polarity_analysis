# ====================================
# Libraries
# ====================================

from pathlib import Path
import os
import pandas as pd


def df_data_path() -> Path:
    """
    Returns the location of the data frames, allowing for script executions in subfolders without worrying about the
    relative location of the data

    :return: the path to the data frames
    """
    cwd = Path("..")
    for folder in (cwd, cwd / "..", cwd / ".." / ".."):
        data_folder = folder / "data"
        if data_folder.exists() and data_folder.is_dir():
            print("Data (main) directory found in ", data_folder)
            return data_folder
        else:
            raise Exception("Data not found")
        
def plot_data_path() -> Path:
    """
    Returns the location of the plot directory, allowing for script executions in subfolders without worrying about the
    relative location of the data

    :return: the path to the plot directory
    """
    cwd = Path("..")
    for folder in (cwd, cwd / "..", cwd / ".." / ".."):
        data_folder = folder / "plots"
        if data_folder.exists() and data_folder.is_dir():
            print("Plot directory found in ", data_folder)
            return data_folder
        else:
            raise Exception("Plots directory not found")
        

def catalog_data_path() -> Path:
    """
    Returns the location of the catalog, allowing for script executions in subfolders without worrying about the
    relative location of the catalog directory

    :return: the path to the catalog folder
    """
    cwd = Path("..")
    for folder in (cwd, cwd / "..", cwd / ".." / ".."):
        data_folder = folder / "catalog"
        if data_folder.exists() and data_folder.is_dir():
            print("Catalog directory found in ", data_folder)
            return data_folder
        else:
            raise Exception("Catalog directory not found")

def import_csv(path,filename):
    """
    Imports a CSV file from the data directory

    :param path: the path to the data directory
    :param filename: the name of the CSV file
    :return: the CSV file
    """
    
    file = pd.read_csv(os.path.join(path, filename), encoding='UTF-8')

    return file

def save_dataframe_to_csv(df, folder_path, file_name):
    """
    Saves a pandas DataFrame as a CSV file in the specified folder with the given file name.

    Parameters:
    - df: pandas DataFrame to save
    - folder_path: str or Path, path to the destination folder
    - file_name: str, name of the CSV file (with or without '.csv')
    """

    # Ensure the file_name ends with .csv
    if not file_name.endswith('.csv'):
        file_name += '.csv'

    # Create the folder if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)

    # Build full path
    full_path = os.path.join(folder_path, file_name)

    # Save the DataFrame
    df.to_csv(full_path, index=False)

    print(f"DataFrame saved successfully at: {full_path}")