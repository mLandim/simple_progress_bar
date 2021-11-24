from simple_progress_bar import print_progressbar

for x in range(10000):
    print_progressbar(value=(x+1), max_value=10000, char='$')