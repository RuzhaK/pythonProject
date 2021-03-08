data=input()
key_materials= dict(fragments=0, motes=0,shards=0)
junk={}
var=True
legendary_item=""

while var==True:
    line = data.split()
    for i in range(0,len(line),2):

        quantity=int(line[i])
        key=line[i+1].lower()
        if key=="fragments" or key=="motes" or key=="shards":

            key_materials[key]+=quantity
            if key_materials[key]>=250:
                if key=="shards":
                    legendary_item="Shadowmourne"
                elif key=="fragments":
                    legendary_item = "Valanyr"
                elif key=="motes":
                    legendary_item = "Dragonwrath"

                else:
                    continue
                key_materials[key] -= 250
                var = False
                break
        else:
            if key not in junk:
                junk[key]=0
            junk[key]+=quantity

    data = input()
print(f"{legendary_item} obtained!")
sorted_key_materials=dict(sorted(key_materials.items(),key=lambda h:(-h[1],h[0])))
for key,value in sorted_key_materials.items():
    print(f"{key}: {value}")
sorted_junk=dict(sorted(junk.items(),key=lambda h:(h[0])))
for key,value in sorted_junk.items():
    print(f"{key}: {value}")

    #todo runtime error