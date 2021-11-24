# Simple Progress Bar

This module will print a progress bar for console apps.
It should be used inside a for loop.


## Installation

pip install simple-progress-bar

## Usage

```python

# import function from module
from simple_progress_bar import print_progressbar

def test_function():
    
    df_test = pd.read_excel('test_file_read.xls')
    df_test_size = len(df_dles.index)

    # iterate through anything
    for index, row in df_test.iterrows():
        index_fix = index + 1
        result = 'Test' 
        df_test.loc[index, 'result'] = result

        # Printing the progress bar
        print_progressbar(index_fix, df_test_size, blank='-', description=f"Testing: Line {index}")

    df_test.to_excel('test_file_write.xls')


```
