# Your code below:
print('''--------- WE open new pizza joint.
Let's keep track of what have there. 
WE need have list of toppings  and list of their prices:''')
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anhcovies', 'mushrooms']
print('toppings:', toppings)

prices = [2, 6, 1, 3, 2, 7, 2]
print('prices:', prices)

print('--------- Let\'s figure out the number of occurrences of 2 in the prices list ----------')
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)


print('--------- Let\'s find out all kinds of pizza ----------')
num_pizza = len(toppings)

print(f'We sell {num_pizza} different kinds of pizza!')

print('--------- Creating a Two-dimensional list: kind of pizza and its associated price ----------')
pizza_and_prices = [
  [2, 'pepperoni'],
  [6, 'pineapple'],
  [1, 'cheese'],
  [3, 'sausage'],
  [2, 'olives'],
  [7, 'anhcovies'],
  [2, 'mushrooms']
]
print(pizza_and_prices)

pizza_and_prices.sort()
print('--------- Sorted pizza_and_prices list ----------')
print(pizza_and_prices)


print('--------- Let\'s find out cheapest and priciest kinds 0f pizza ----------')
cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]

print('cheapest:', cheapest_pizza)
print('priciest:', priciest_pizza)

print('''--------- 
Suppose, there is no longer "anchovies" pizza in menu.
Let's remove it from list:''')
pizza_and_prices.pop()
print(pizza_and_prices)

print('and add new one:')
pizza_and_prices.insert(-2, [2.5, 'peppers'])
# or other way:
# 1) pizza_and_prices.append();
# 2) pizza_and_prices.sort()
print(pizza_and_prices)

print('''-------- Let\'s slice the 'pizza_and_prices' list and store the 3 lowest cost pizzas in a list called three_cheapest.----------''')
three_cheapest = pizza_and_prices[:4]
print('Three cheapets pizzas are:', three_cheapest)

print('--------- Mice are very pleased !----------')
