import csv

# makes math far easier
import numpy as np

# using dicts seems easier at first but we'd have to eventually convert
# to a list for easy elementwise division or use an ugly loop
funcs = []
main = []
new = []

with open("perf.csv", "r") as f:
    csv_reader = csv.reader(f)
    # skip header row
    next(csv_reader)
    
    # csv is sorted by name so we can assume even rows are main and odd are new
    for indx, (func, median) in enumerate(csv_reader):
        func = func.split("::")[-1]
        funcs.append(func)
        # indx is even
        if not (indx % 2):
            main.append(float(median))
        else:
            new.append(float(median))
    
    main = np.array(main)
    new = np.array(new)
    
    relative_perfs = new / main
    # more stats will be included when needed
    print(f"The new branch is {round(relative_perfs.mean(), 4)}x faster than the main branch!")
