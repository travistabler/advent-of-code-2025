# %%
# libraries
from pathlib import Path

import pandas as pd

# %%
# read input
script_dir = Path(__file__).parent
input_file = script_dir / "input" / "day-one-input.csv"

# input_list = ['R51', 'L51', 'R50', 'L50']
input_df = pd.read_csv(input_file, header=None)
input_list = input_df.squeeze().tolist()
input_list

# %%
# define the dial
dial_start = 50
count = 0
other_count = 0

for x in input_list:

    if x.startswith("L"):
        l_value = x.strip("L")
        print(x)
        # print(l_value)
        # print(int(l_value))
        # bonus question
        for i in range(1, int(l_value) + 1):
            if (dial_start - i) % 100 == 0:
                other_count += 1
        dial_start = (dial_start - int(l_value)) % 100
        print(dial_start)
    elif x.startswith("R"):
        r_value = x.strip("R")
        print(x)
        # print(r_value)
        # print(int(r_value))
        # bonus questions
        for i in range(1, int(r_value) + 1):
            if (dial_start + i) % 100 == 0:
                other_count += 1
        dial_start = (dial_start + int(r_value)) % 100
        print(dial_start)
    else:
        print(False)

    if dial_start == 0:
        count += 1

    print(f"stopped on zero: {count}")
    print(f"passed or landed on zero: {other_count}")
