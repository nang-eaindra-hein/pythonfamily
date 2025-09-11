#for i (num,valid num)
def proc_list():

  numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]

  valid_numbers = []

  total = 0

  average = 0.0



  for i in numbers:

    if i >= 0 and i <= 100:

      valid_numbers.append(i)



  total = sum(valid_numbers)

  average = total / len(valid_numbers)

  print("Numbers =", numbers)

  print("Valid Numbers =", valid_numbers)

  print("Total =", total)

  print("Average =", average)



proc_list()
