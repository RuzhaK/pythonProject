import collections

data = input()
dwarfs = {}
dwarf_name_hat_color_count=collections.defaultdict(int)
while data != "Once upon a time":
    dwarf_name, hat_color, physics = data.split(" <:> ")
    key = (dwarf_name, hat_color)
    dwarf_name_hat_color_count[key]+=1
    physics = int(physics)

    dwarfs[key] = physics
    if key in dwarfs:
        if dwarfs[key] < physics:
            dwarfs[key] = physics
    else:
        dwarfs[key] = physics

    data = input()
for key, value in sorted(dwarfs.items(),key=lambda item:(-item[1],dwarf_name_hat_color_count[item[0]])):
    dwarf_name, hat_color = key
    physics = value

    print(f"({hat_color}) {dwarf_name} <-> {physics}")

#todo ne minava na 100%
