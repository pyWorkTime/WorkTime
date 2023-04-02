import yaml
from yaml.loader import SafeLoader
from pathlib import Path
import sys
import os
import pandas as pd
import pyarrow.parquet as pq

#  from this project
from ui import menu


def main():
    """read in the user supplied yaml data then call the ui object"""

    try:
        yaml_file_path = f"{sys.argv[1]}"
        parquet_file_path = f"{sys.argv[1]}.parquet"
    except:
        yaml_file_path = "default.yml"
        parquet_file_path = "default.parquet"

    yaml_path = Path(__file__).with_name(yaml_file_path)
    parquet_path = Path(__file__).with_name(parquet_file_path)
    with yaml_path.open("r") as f:
        data = yaml.load(f, Loader=SafeLoader)

    if os.path.exists(parquet_path):

        #  open the Parquet file using PyArrow,  testing for validity
        try:
            pq.ParquetFile(parquet_path)
            print("The Parquet file is valid")
        except Exception as e:
            print("The Parquet file is not valid: ", e)

    else:
        #  create a DataFrame with header row only
        df_header = pd.DataFrame(columns=['project_id', 'project_name', 'start_time', 'stop_time', 'total_time', 'remark'])

        #  pyarrow does not support writing to parquet file without index, so we can just drop it from the data frame initially
        df_header.reset_index(drop=True)

        #  write the header row to the parquet file using DataFrame.to_parquet()
        df_header.to_parquet(parquet_path, engine='pyarrow', partition_cols=None)

        print('Parquet file created!', parquet_path)

    ui = menu(data, parquet_path)


if __name__ == "__main__":
    main()