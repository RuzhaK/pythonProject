import operator
import re
from collections import OrderedDict

participants = input().split(", ")
text = input()
results = {}
while text != "end of race":
    name = ""
    res = 0
    pattern_name = r"[A-Za-z]+"
    matches_name = re.findall(pattern_name, text)
    for match_name in matches_name:
        name += match_name
    if name in participants:
        pattern_number = r"\d"
        matches_number = re.findall(pattern_number, text)
        for match_number in matches_number:
            res += int(match_number)
        if name not in results:
            results[name] = res
        else:
            results[name] += res



    text = input()
results_sorted = sorted(results.items(), key=lambda x: x[1], reverse=True)
print(f"1st place: {results_sorted[0][0]}\n2nd place: {results_sorted[1][0]}\n3rd place: {results_sorted[2][0]}")

