# %%
# libraries
from pathlib import Path

import pandas as pd

# %%
# read input
script_dir = Path(__file__).parent
input_file = script_dir / "input" / "day04-input.csv"

input_df = pd.read_csv(input_file, header=None)
input_list = input_df.squeeze().tolist()
input_list


# %%
# part one
floor = input_list

total_count = 0

for row_id, row in enumerate(floor):
    for col_id, tile in enumerate(row):

        if tile != "@":  # the last piece I had to put in for this joint to work.
            continue

        adjacent_count = 0

        for left_right in [-1, 0, 1]:
            for down_up in [-1, 0, 1]:
                if left_right == 0 and down_up == 0:  # don't need to consider itself
                    continue

                adjacent_row = row_id + down_up
                adjacent_col = col_id + left_right

                if 0 <= adjacent_row < len(floor) and 0 <= adjacent_col < len(row):
                    if floor[adjacent_row][adjacent_col] == "@":
                        adjacent_count += 1

        if adjacent_count < 4:  # less than 4 rolls around it - count it
            total_count += 1


print(f"\nTotal tiles with 4+ neighbors: {total_count}")


# %%
# part two
floor = [list(row) for row in input_list]  # this took me way too long to figure out

total_count = 0

while True:
    open_rolls = []

    for row_id, row in enumerate(floor):
        for col_id, tile in enumerate(row):
            if tile != "@":
                continue

            adjacent_count = 0

            for left_right in [-1, 0, 1]:
                for down_up in [-1, 0, 1]:
                    if (
                        left_right == 0 and down_up == 0
                    ):  # don't need to consider itself
                        continue

                    adjacent_row = row_id + down_up
                    adjacent_col = col_id + left_right

                    if 0 <= adjacent_row < len(floor) and 0 <= adjacent_col < len(row):
                        if floor[adjacent_row][adjacent_col] == "@":
                            adjacent_count += 1

            if adjacent_count < 4:  # less than 4 rolls around it - count it
                open_rolls.append((row_id, col_id))

    if not open_rolls:
        break

    for row_id, col_id in open_rolls:
        floor[row_id][col_id] = "."  # replaced picked rolls with .

    removed = len(open_rolls)
    total_count += removed
    print(total_count)

print(total_count)
