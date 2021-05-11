#Script to pick random civ without replacement
#This code can be freely used and shared under the terms of the Apache 2.0 license

#Instructions:
#1) copy this text into a word editor and save as pick_random_civ.py in a directory of your choosing
#2) run with the version of your choice. This script has been tested with Python 3.7.4.
#3) the script will run and pick a random civ for you, storing civs you have already played in a file called recently_played.txt (which it creates in the script directory) and ignoring these. Once all civs have been played, it restarts with the entire pool of civs.

#Note that you can customize civ_list below to whatever you want, e.g. if you never want to play Malay then just remove "Malay" from civ_list. When you've done this, be sure to manually delete recently_played.txt from the script directory prior to running it again a first time in order to avoid unintented behavior. 
civ_list = ["Britons","Byzantines","Celts","Chinese","Franks","Goths","Japanese","Mongols","Persians","Saracens","Teutons","Turks","Vikings","Aztecs","Huns","Koreans","Mayans","Spanish","Incas","Indians","Italians","Magyars","Slavs","Berbers","Ethiopians","Malians","Portuguese","Burmese","Khmer","Malay","Vietnamese","Bulgarians","Cumans","Lithuanians","Tatars","Burgundians","Sicilians"]
recent_civ_list = []

#Check if recently_played.txt exists in directory. if not, create it.
fname = "./recently_played.txt"
import os.path
if not os.path.isfile(fname):
    open(fname, 'a').close()
with open(fname,"r") as f:
    recent_civ_list = f.read().splitlines()

pick = ""
import random
if (len(recent_civ_list) < len(civ_list)):
    candidate_civ_list = list(set(civ_list) - set(recent_civ_list))
    pick = random.choice(candidate_civ_list)
    with open(fname,"a") as f:
        f.write(pick + "\n")
else:
    candidate_civ_list = civ_list
    pick = random.choice(candidate_civ_list)
    with open(fname,"w") as f:
        f.write(pick + "\n")

#Print the next randomly chosen civ to the console
msg = "You have played %i/%i civilizations recently. The next civ you will be playing is:\n\n%s\n\nGlhf!" % (len(recent_civ_list),len(civ_list),pick)
print(msg)