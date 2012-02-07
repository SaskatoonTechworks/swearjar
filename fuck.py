"""
A simple script to count the amount of Fuck in a given channel

DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE

Everyone is permitted to copy and distribute verbatim or modified
copies of this license document, and changing it is allowed as long
as the name is changed.

DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE

TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
    0. You just DO WHAT THE FUCK YOU WANT TO. 
"""

import time
import re

starttime   = time.time()   #Time of script start
jar         = {}            #Dictionary mapping Nick:Swear

def print_fucks(phenny, input):
    #Print the fuck totals for the given users

    global jar
    global starttime
    
    #Make sure that we have the proper number of elements
    if len(input.groups()) != 2:
        return

    #Split the names by spaces, and loop through the code
    print li
    for i in li:
        if i in jar:
            freq            = jar[i]/((time.time()-starttime)/(60*60))
            phenny.say("%-16s:%.3f Fucks/Hour" % (i, freq))
        else:
            phenny.say("%-16s:No Data" % (i))


def increment(phenny, input):
    #Monitors all traffic and silently updates the counters
    global jar

    if re.search("(?i)fuck", input.group()) != None:
        if input.nick in jar:
            jar[input.nick] += 1
        else:
            jar[input.nick]  = 1

#Phenny rules 
increment.rule = r'.*'
increment.priority = 'high'
increment.thread = False

print_fucks.commands = ['fuck']
print_fucks.priority = 'high'

