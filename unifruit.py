fruit_basket=[]
unique_fruit=[]
for i in range(2):
  fruits=input('Enter your fruits:')
  fruit_basket.append(fruits)
for fruits in fruit_basket:
    if fruits.lower() not in unique_fruit:
      unique_fruit.append(fruits)
print(unique_fruit)