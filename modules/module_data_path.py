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
        
def import_csv(path,filename):
    """
    Imports a CSV file from the data directory

    :param path: the path to the data directory
    :param filename: the name of the CSV file
    :return: the CSV file
    """
    
    file = pd.read_csv(os.path.join(path, filename), encoding='ISO-8859-1')

    return file
