import pandas as pd
import os

def createDataSet():
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, '../../data/electronics.json')

    try:
        df = pd.read_json(file_path)
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return None
