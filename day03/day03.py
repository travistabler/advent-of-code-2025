# %%
# libraries
from pathlib import Path

import pandas as pd

# %%
# read input
script_dir = Path(__file__).parent
input_file = script_dir / "input" / "day03-input.csv"

input_df = pd.read_csv(input_file, header=None)
input_list = input_df.squeeze().tolist()
input_list

# %%
# test_input = ['1111111156', '1111111121', '1111111123'] # test and debug

# %%
# part one
total_joltage = 0

for bank in input_list:
    batteries_indexed = []
    for idx, battery in enumerate(bank):
        batteries_indexed.append((idx, int(battery)))
    batteries_indexed.sort(key=lambda x: x[1], reverse=True)
    print(batteries_indexed)

    if batteries_indexed[0][0] == len(batteries_indexed) - 1:
        largest = batteries_indexed[1]
        second_largest = max(
            (b for b in batteries_indexed if b[0] > batteries_indexed[1][0]),
            key=lambda x: x[1],
        )
        bank_joltage = str(largest[1]) + str(second_largest[1])
        print(str(largest[1]) + str(second_largest[1]))
    else:
        largest = batteries_indexed[0]
        second_largest = max(
            (b for b in batteries_indexed if b[0] > batteries_indexed[0][0]),
            key=lambda x: x[1],
        )
        bank_joltage = str(largest[1]) + str(second_largest[1])
        print(str(largest[1]) + str(second_largest[1]))
    total_joltage += int(bank_joltage)

print(total_joltage)


# %%
# part two
total_joltage = 0
battery_chain = 12

for bank in input_list:
    batteries_indexed = []
    for idx, battery in enumerate(bank):
        batteries_indexed.append((idx, int(battery)))
    batteries_indexed.sort(key=lambda x: x[1], reverse=True)

    selected = []

    for battery_num in range(battery_chain):
        batteries_needed = battery_chain - battery_num
        last_idx = selected[-1][0] if selected else -1

        # only pick batteries that could still make a full 12 after
        valid = [
            b
            for b in batteries_indexed
            if b[0] > last_idx and b[0] <= len(bank) - batteries_needed
        ]

        selected.append(valid[0])  # "switch" the battery on

    bank_joltage = ""
    for b in selected:
        bank_joltage += str(b[1])
    # print(bank_joltage)
    total_joltage += int(bank_joltage)

print(total_joltage)
