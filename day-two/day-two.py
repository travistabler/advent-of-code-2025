# %%
# libraries
from pathlib import Path

import pandas as pd

# %%
# read input
script_dir = Path(__file__).parent
input_file = script_dir / "input" / "day-two-input.csv"

input = ['1-100','101-200', '200-10000']
input_df = pd.read_csv(input_file, header=None)
input_list = input_df.squeeze().tolist()
input_list

# %%
total = 0
for item in input_list:
    #print(item)
    id_range = item.split("-")
    for id in range(int(id_range[0]), int(id_range[1])):
        if len(str(id)) % 2 == 0:
            first, second = str(id)[:len(str(id))//2 + len(str(id))%2], str(id)[len(str(id))//2 + len(str(id))%2:]
            #print(first, second)
            if first == second:
                total += int(first + second)
print(total)


# %%
# part two
total = 0
for item in input_list:
    #print(item)
    id_range = item.split("-")
    for id in range(int(id_range[0]), int(id_range[1])):
        for repeat_len in range(1, len(str(id)) // 2 + 1):
            if len(str(id)) % repeat_len == 0:
                pattern = str(id)[:repeat_len]
                if pattern * (len(str(id)) // repeat_len) == str(id):
                    total += id
                    break
print(total) # yeah, don't put this inside the loops
