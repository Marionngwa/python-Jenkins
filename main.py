

asking = input("enter a word: ").strip()
num_v = 0
num_c = 0

for i in asking:
    if i in "aeiouAEIOU":  # Check for both lowercase and uppercase vowels
        num_v += 1
    elif i.isalpha():  # Check if the character is a letter
        num_c += 1

print(f'Number of vowels: {num_v}')
print(f'Number of consonants: {num_c}')
