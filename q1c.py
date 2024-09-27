# Define probability tables (from your Bayesian Network)

# P(BS) (same as before)
p_bs = {
    "131": 5/10,
    "166": 3/10,
    "146": 2/10,
}

# P(BT = Single | BS, TD = Day)
p_bt_single_given_bs_day = {
    "131": 9/10,
    "166": 0,  # No single deck during day
    "146": 1/2,  # Alternates
}

# P(BC = SMT | BS) (same as before)
p_bc_smt_given_bs = {
    "131": 3/5,
    "166": 2/5,
    "146": 0,  # No SMT on 146
}

# Calculate the probability
numerator = 0
denominator = 0
for bs in p_bs.keys():
    numerator += (
        p_bc_smt_given_bs[bs] 
        * p_bt_single_given_bs_day[bs] 
        * p_bs[bs]
    )
    denominator += (
        p_bt_single_given_bs_day[bs] 
        * p_bs[bs]
    )

probability = numerator / denominator

print("Probability of an SMT bus given single-deck and daytime:", probability)
