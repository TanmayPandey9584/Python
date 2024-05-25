s=input("enter numeral")
char = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
total = 0
prev_value = 0
print(s)
for i in range(len(s) - 1, -1, -1):
    curr_value = char[s[i]]
    print("curr_val=",curr_value)
    print("prev_val=",prev_value)
    if curr_value < prev_value:
        total -= curr_value
        print("total in if:",total)
    else:
        total += curr_value
        print("total in else:",total)
        prev_value = curr_value

print(total)

#MCMXCIV

'''
def roman_to_int(roman_num):
  """
  Converts a Roman numeral string to an integer.

  Args:
      roman_num: The Roman numeral string to convert.

  Returns:
      The integer equivalent of the Roman numeral string.

  Raises:
      ValueError: If the Roman numeral string is invalid.
  """

  roman_dict = {
      'I': 1,
      'V': 5,
      'X': 10,
      'L': 50,
      'C': 100,
      'D': 500,
      'M': 1000,
  }

  int_val = 0
  prev = 0  # Initialize prev to 0

  for char in roman_num:
    if char not in roman_dict:
      raise ValueError("Invalid Roman numeral character: {}".format(char))

    val = roman_dict[char]

    # Handle subtractive notation correctly:
    if val > prev:
      int_val -= prev  # Subtract the previous value
      prev = 0        # Reset prev to 0 after subtraction

    else:
      int_val += val
      prev = val  # Update prev only if not subtracted

  return int_val


# Convert MCMXCIV to integer
roman_num = "MCMXCIV"
int_val = roman_to_int(roman_num)

print(f"{roman_num} is equivalent to {int_val}")


'''