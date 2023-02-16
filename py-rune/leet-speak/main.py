import random

# Get the input
phrase = input("What's the phrase? ")

# Upper the input
phrase = phrase.upper()

# Convert to leet-speak
lookup = {
    'A': ['4', '/\\', '@'],
    'B': ['I3'],
    'C': ['['],
    'D': ['|)'],
    'E': ['3'],
    'F': ['|='],
    'G': ['6'],
    'H': ['#'],
    'I': ['1', '|'],
    'J': [',_|'],
    'K': ['|<'],
    'L': ['1', '2', '|_'],
    'M': ['^^', '/\\/\\'],
    'N': ['/\\/', '|\\|'],
    'O': ['0', '()'],
    'P': ['|*', '|>'],
    'Q': ['0_', '9', '(_,)'],
    'R': ['I2', '/2'],
    'S': ['5', 'ehs'],
    'T': ['7', '+', '-|-'],
    'U': ['|_|', '(_)'],
    'V': ['\\/', '|/'],
    'W': ['vv'],
    'X': ['><'],
    'Y': ['j', '`/'],
    'Z': ['7_', '2'],
}
leet = ''
for char in phrase:
    leet += random.choice(lookup.get(char, char))

# Print them out
print(f'leet: {leet}')
import random

# Get the input
phrase = input("What's the phrase? ")

# Upper the input
phrase = phrase.upper()

# Convert to leet-speak
lookup = {
    'A': ['4', '/\\', '@'],
    'B': ['I3'],
    'C': ['['],
    'D': ['|)'],
    'E': ['3'],
    'F': ['|='],
    'G': ['6'],
    'H': ['#'],
    'I': ['1', '|'],
    'J': [',_|'],
    'K': ['|<'],
    'L': ['1', '2', '|_'],
    'M': ['^^', '/\\/\\'],
    'N': ['/\\/', '|\\|'],
    'O': ['0', '()'],
    'P': ['|*', '|>'],
    'Q': ['0_', '9', '(_,)'],
    'R': ['I2', '/2'],
    'S': ['5', 'ehs'],
    'T': ['7', '+', '-|-'],
    'U': ['|_|', '(_)'],
    'V': ['\\/', '|/'],
    'W': ['vv'],
    'X': ['><'],
    'Y': ['j', '`/'],
    'Z': ['7_', '2'],
}
leet = ''
for char in phrase:
    leet += random.choice(lookup.get(char, char))

# Print them out
print(f'leet: {leet}')
