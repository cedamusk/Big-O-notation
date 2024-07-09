expense=[2200, 2350, 2600, 2130, 2190]
print("In February, I spent ",expense[1]-expense[0],"more than in January")

print('The total expense for the first quarter is', expense[0]+expense[1]+expense[2])

print("Did I spent 2000 in any month:", 2000 in expense)

expense.append(1980)
print(expense)
print("Spent token in June is:",expense[5])
expense[3]=expense[3]-200
print(expense)



heroes=['spider man', 'thor', 'hulk','iron man', 'captain america']

print(len(heroes))
heroes.remove('hulk')
heroes.insert(2,'black panther')
print(heroes)
heroes[1:3]=['doctor strange']
print(heroes)

heroes.sort()
print(heroes)


max=int(input("Enter number here:"))
odd_numbers=[]

for i in range (1, max):
    if i%2==1:
        odd_numbers.append(i)

print('Odd numbers:', odd_numbers)