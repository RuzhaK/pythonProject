paintings = input().split()
line = input()


def painting_exists(painting_num, paintings):
    if painting_num in paintings:
        return True


while line != "END":
    command, *tokens = line.split()

    if command == "Change":
        painting_num = tokens[0]
        changed_num = tokens[1]
        if painting_exists(painting_num, paintings):
            # moga da mahna komprehensiona i da ostane edna podmiana - ne e tova
            paintings = [changed_num if num == painting_num else num for num in paintings]
    elif command == "Hide":
        painting_num = tokens[0]
        if painting_exists(painting_num, paintings):
            #  ako e prazen lista
            # ako ne sa integers?
            # probwam s ednokratno mahvane - ne se promeni, pak e 90/100
            paintings.remove(painting_num)

            # paintings = [num for num in paintings if num != painting_num]
    elif command == "Switch":
        painting_num = tokens[0]
        painting_two = tokens[1]

        #  ako ima po dwa? sega raboti za wsichki, da probwam da raboti samo za savpadashta broika
        if painting_exists(painting_num, paintings) and painting_exists(painting_two, paintings):
            # paintings=["a" if num==painting_num else num for num in paintings]
            # paintings=[painting_num if num==painting_two else num for num in paintings]
            # paintings=[painting_two if num=="a" else num for num in paintings]
            index_first = paintings.index(painting_num)
            index_second = paintings.index(painting_two)
            paintings[index_first], paintings[index_second] = paintings[index_second], paintings[index_first]
    elif command == "Insert":
        place = int(tokens[0])
        painting = tokens[1]
        if 0 <= (place + 1) < len(paintings):
            paintings.insert((place + 1), painting)
    elif command == "Reverse":
        paintings = paintings[::-1]

    line = input()
print(" ".join(paintings))

