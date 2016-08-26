def processHouseEntryRecords(entries):
    criminalRecords = {}
    unknows = {
        'IN': 0,
        'OUT': 0
    }
    anotherEntranceInCrimeHouse = False
    guranteedInside = 0;
    atLeastOneEntered = False

    for action,id in entries:
        if (id == '0'):
            if (action == 'E'):
                if (unknows['OUT'] > 0):
                    unknows['OUT'] -= 1
                else:
                    unknows['IN'] += 1
                guranteedInside += 1
            elif (action == 'L'):
                if (unknows['IN'] > 0):
                    unknows['IN'] -= 1
                else:
                    unknows['OUT'] += 1
                if (guranteedInside > 0):
                    guranteedInside -= 1
            continue

        if (id not in criminalRecords):
            criminalRecords[id] = ''

        if (action == 'E'):
            guranteedInside += 1

            if (not atLeastOneEntered):
                atLeastOneEntered = True

            if (criminalRecords[id] != 'outside' and unknows['OUT'] > 0):
                criminalRecords[id] = 'inside'
                unknows['OUT'] -= 1
            elif (criminalRecords[id] != 'inside'):
                criminalRecords[id] = 'inside'
            elif (criminalRecords[id] == 'inside' and unknows['OUT'] == 0):
                # if he was known to be inside and he is again entering, but 
                # no masked person has left the house, then there must be a second
                # entrance/exit in the house
                anotherEntranceInCrimeHouse = True
        elif (action == 'L'):
            if (guranteedInside > 0):
                guranteedInside -= 1

            if (criminalRecords[id] != 'inside' and unknows['IN'] > 0):
                # if the criminal was not recoreded as "inside" (i.e. criminal is "outside"
                # or its a new entry) but some masked criminals entered the house, then
                # mark him as "outside" but also subtract 1 from unknown entries, since he
                # may have entered with mask.
                criminalRecords[id] = 'outside'
                unknows['IN'] -= 1
            elif (criminalRecords[id] != 'outside'):
                criminalRecords[id] = 'outside'
            elif (criminalRecords[id] == 'outside' and unknows['IN'] == 0):
                # if he was known to be outside and he is again leaning, but 
                # no masked person has entered the house, then there must be a second
                # entrance to the house
                anotherEntranceInCrimeHouse = True

    insideCount = unknows['IN']
    for key,val in criminalRecords.items():
        if val == 'inside':
            insideCount += 1
    
    if (unknows['OUT'] > 0):
        insideCount = max(0, insideCount - unknows['OUT'])
    
    #print(entries)
    print(unknows)
    print(criminalRecords)
    #print('Guranteed Inside', guranteedInside)
    print('CRIME TIME' if anotherEntranceInCrimeHouse else insideCount)

def run(testcase):
    print(testcase)
    totalExpectedEntries, entries = testcase.split('; ')
    entries = [tuple(record.split()) for record in entries.split('|')]

    if (len(entries) != int(totalExpectedEntries)):
        raise AssertionError('entries count mismatch')

    processHouseEntryRecords(entries)

run('15; E 0|L 0|E 0|L 1756|E 0|E 0|E 0|L 0|L 0|E 0|L 0|L 0|L 0|E 591|E 0')  # should return 1
run('15; L 0|L 0|E 0|L 671|E 0|E 0|E 1480|E 0|L 1878|L 0|L 1316|E 0|E 0|E 0|E 0')

run('3; E 5|L 0|E 5')                       # 1
run('2; L 1|L 1')                           # CRIME TIME
run('4; L 1|E 0|E 0|L 1')                   # 1
run('7; L 2|E 0|E 1|E 2|E 0|E 3|L 4')       # 4
run('13; L 4|L 1|L 2|E 0|L 1|E 0|L 2|E 0|L 2|E 0|E 0|L 1|L 4')  #0