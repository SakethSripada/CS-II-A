principal_amt = 24000
rate = 5
time = 4


def calc_interest(principal_amt, rate, time):
    if not (isinstance(principal_amt, (int, float)) and isinstance(rate, (int, float)) and isinstance(time, int)):
        print("Error. Principal amount and rate must be either float or int, and time must be type int.")
    if principal_amt < 0 or rate < 0 or time < 0 or time > 50:
        print("Error. Values must be nonnegative and time must not exceed 50 years")
    interest = principal_amt * (1 + (rate / 100) * time) - principal_amt
    return round(interest, 2)


interest = calc_interest(principal_amt, rate, time)
print(interest)
