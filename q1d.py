# Define probability tables 

# P(BT = Single | BS = 166, TD = Day/Evening) (from problem description)
p_bt_single_given_166_day = 0  
p_bt_single_given_166_evening = 1/5

# Calculate the probability
p_bt_double_given_166_day = 1 - p_bt_single_given_166_day
p_bt_double_given_166_evening = 1 - p_bt_single_given_166_evening

print("Probability of a double-deck bus given service 166 (daytime):", p_bt_double_given_166_day)
print("Probability of a double-deck bus given service 166 (evening):", p_bt_double_given_166_evening)

p_td_day = 12/18
p_td_evening = 6/18

p_bt_double_given_166 = (
    (1 - p_bt_single_given_166_day) * p_td_day +
    (1 - p_bt_single_given_166_evening) * p_td_evening
)

print("Probability of a double-deck bus given service 166 (unknown time):", p_bt_double_given_166)