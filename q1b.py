# Define the frequency ratios for the bus services 131, 166, and 146
frequency_ratio = [5, 3, 2]

# Calculate the total frequency
total_frequency = sum(frequency_ratio)

# Define the probabilities for each bus service based on the frequency ratio
prob_131 = frequency_ratio[0] / total_frequency
prob_166 = frequency_ratio[1] / total_frequency
prob_146 = frequency_ratio[2] / total_frequency

# Define the probabilities for single deck buses during the evening
prob_single_deck_131_evening = 1  # always single deck during evening
prob_single_deck_166_evening = 1 / 5  # single deck in 1 out of 5 trips during evening
prob_single_deck_146_evening = 1 / 2  # alternates between single and double deck

# Define the operator probabilities for each bus service
# For bus service 131
prob_SGS_131 = 2 / 5
prob_SMT_131 = 3 / 5

# For bus service 166
prob_SMT_166 = 0.4
prob_remaining_166 = 0.6
prob_SGS_166 = prob_remaining_166 / 3
prob_TT_166 = prob_remaining_166 / 3
prob_CB_166 = prob_remaining_166 / 3

# For bus service 146
# TT only uses single deck and CB only uses double deck
prob_TT_146 = 0.5
prob_CB_146 = 0.5

# Calculate the probability of getting a single deck SMT bus for each service
prob_single_deck_SMT_131 = prob_single_deck_131_evening * prob_SMT_131
prob_single_deck_SMT_166 = prob_single_deck_166_evening * prob_SMT_166
prob_single_deck_SMT_146 = 0  # SMT does not operate bus service 146

# Calculate the combined probability of a single deck SMT bus across all services
prob_single_deck_SMT = (
    prob_131 * prob_single_deck_SMT_131 +
    prob_166 * prob_single_deck_SMT_166 +
    prob_146 * prob_single_deck_SMT_146
)

print(prob_single_deck_SMT)
