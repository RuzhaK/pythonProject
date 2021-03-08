# обръщаме инпута в интеджъри
pirate_ship=[int(x) for x in input().split(">")]
minimum_health=0.20
count=len([x for x in pirate_ship if x<minimum_health])
# To stop code execution in Python you first need to import the sys object. After this you can then call the exit() method to stop the program running. It is the most reliable, cross-platform way of stopping code execution. Here is a simple example.
#
# import sys
# sys.exit()