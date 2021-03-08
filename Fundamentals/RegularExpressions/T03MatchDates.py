import re
dates=input()
pattern=r'(\d{2})([/\.-])([A-Z][a-z]{2})\2(\d{4})'
for match in re.findall(pattern,dates):
    day,separator,month,year=match
    print(f"Day: {day}, Month: {month}, Year: {year}")



