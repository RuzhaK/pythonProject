import re

phone = input()
pattern = r'(\+359 2 \d{3} \d{4}|\+359-2-\d{3}-\d{4})'
matches: list = re.findall(pattern,phone)
print(', '.join(matches))
