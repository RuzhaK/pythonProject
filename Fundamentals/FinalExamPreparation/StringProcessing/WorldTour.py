stops=input()
line=input()


def index_is_valid(index, stops):
    if 0<=index<len(stops):
        return True


def string_in_string(substring, stops):
    if substring in stops:
        return True


while line !="Travel":
    command, index, token=line.split(":")
    if command=="Add Stop":
        index=int(index)
        if index_is_valid(index,stops):
            first_part=stops[:index]
            second_part=stops[index:]
            stops=first_part+token+second_part
            print(stops)

    elif command=="Remove Stop":
        start_index=int(index)
        end_index=int(token)
        if index_is_valid(start_index,stops) and index_is_valid(end_index,stops):
            stops=stops[:start_index]+stops[end_index+1:]
        print(stops)
    elif command=="Switch":
        string_to_check=stops
        while string_in_string(index,string_to_check):
            start_index = str.find(stops,index)

            stops=stops.replace(index,token)
            string_to_check=string_to_check[start_index+1:]



        print(stops)
    line = input()


print(f"Ready for world tour! Planned stops: {stops}")