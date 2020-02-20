"""
Daily Problem 124
Given two strings, find if there is a one-to-one mapping of characters between the two strings.
"""

def has_character_map(str1, str2):
  # Fill this in.
  c1_dict, c2_dict = {ch: 0 for ch in 'abcdefghijklmnopqrstuvwxyz'}, {ch: 0 for ch in 'abcdefghijklmnopqrstuvwxyz'}
  for ch in str1:
  	c1_dict[ch] = 1
  for ch in str2:
  	c2_dict[ch] = 1

  sum1, sum2 = 0, 0
  for ch in 'abcdefghijklmnopqrstuvwxyz':
  	sum1 += c1_dict[ch]
  	sum2 += c2_dict[ch]
  return sum1 == sum2


print(has_character_map('abc', 'def'))
# True
print(has_character_map('aac', 'def'))
# False