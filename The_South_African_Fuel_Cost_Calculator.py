user_kilometers = float(input("Enter the distance in kilometers: "))
petrol_price_per_liter = float(input("Enter the petrol price per liter: "))
#Calculate the fuel cost based on distance and petrol price

liters_needed = user_kilometers / 10
fuel_cost = liters_needed * petrol_price_per_liter
print(f"The estimated fuel cost is: R{round(fuel_cost, 2)}")