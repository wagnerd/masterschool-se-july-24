a = [1,2,3]

for number in a:
    print(number)
    if number == 4:
        break
else:
    print("Complete list done!")
    raise ValueError("No number 4!!")

print("I run always")

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")