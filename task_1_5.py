profit = float(input("Please, enter the company's revenue: "))
costs = float(input("Please, enter the firm's costs: "))
if profit > costs:
    print(f"The company is operating at a profit. Return on revenue amounted to: {profit / costs:.2f}")
    workers = int(input("Please, enter the number of company employees: "))
    print(f"Profit per employee was: {profit / workers:.2f}")
elif profit == costs:
    print("The firm's profit is zero")
else:
    print("The company is operating at a loss.")