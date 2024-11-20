
def has_vowels(string):
  vowels = 'aeiouAEIOU'
  for char in string:
    if char in vowels:
      return True
  return False

# Example usage
string = "Hello, World!"
if has_vowels(string):
  print("The string has vowel characters.")
else:
  print("The string does not have vowel characters.")


