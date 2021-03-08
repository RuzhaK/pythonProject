substrings=input().split(", ")
words=input().split(", ")

result=[subst for subst in substrings for word in words if subst in word]

# for word in words:
#     for subst in substrings:
#         if subst in word and subst not in result:
#             result.append(subst)
print(sorted(set(result), key=result.index))