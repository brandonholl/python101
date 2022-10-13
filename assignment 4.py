# Convert this while loop to a for loop
x = 21
while x > 4 and x < 121:
    print(x)
    if x == 56:
        break
    x = x + 3

for x in range (21, 121, 3):
    print (x)
    if x == 56:
        break
   

# Convert this for loop to a while loop
for i in range(-100, 150, 25):
    if i == 50:
        continue
    print(i)

i = -100
while i < 150:
    if i == 50:
        i = i + 25
        continue
    print(i)
    i = i + 25


# 9, 10, 18, 30
#9
# 51 * 21 = 1071
# 50 * 20 = 1000
# add both
# 2071 asterisks

# #10
# 100*100*100 =
# 1 million asterisks

# #18
# No

#30
x = 5
while x > 0:
    y = int(input())
    if y != 25:
        x-=1
        print('x=', x)