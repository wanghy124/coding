x_rate = 0.65
total_dollars = 200
fee = 2
total_pounds = (total_dollars - fee) * x_rate
total_dollars = (total_pounds - 100) / x_rate + fee
print(total_dollars)
