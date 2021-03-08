data=input()
# submissions={}
results={}

while data!="exam finished":
    line=data.split("-")
    username=line[0]
    language=line[1]


    if language!="banned":
        if username not in results:
            results[username] = {"subkey": []}
        results[username] = username
        if language not in results[username]['subkey']:
            results[username]['subkey'] = language
        points=line[3]
    # else:
    # todo

    data = input()