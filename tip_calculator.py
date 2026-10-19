bill = float(input("whats the bill total today"))
tip_percent = float(input("what percent tip"))
tip_amount = bill * (tip_percent / 100)
print(tip_amount)
total = bill + tip_amount
print(total)
