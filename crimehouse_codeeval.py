# https://www.codeeval.com/open_challenges/195/


def processHouseEntryRecords(entries):
	criminalRecords = {}
	unknows = {
		'IN': 0,
		'OUT': 0
	}
	anotherEntranceInCrimeHouse = False

	for action,id in entries:
		if (id == '0'):
			if (action == 'E'):
				unknows['IN'] += 1
			elif (action == 'L'):
				unknows['OUT'] += 1
			continue

		if (id not in criminalRecords):
			criminalRecords[id] = ''

		if (action == 'E'):
			if (criminalRecords[id] == '' and unknows['OUT'] > 0):
				criminalRecords[id] = 'inside'
				unknows['OUT'] -= 1
			elif (criminalRecords[id] == 'outside' or criminalRecords[id] == ''):
				criminalRecords[id] = 'inside'
			elif (criminalRecords[id] == 'inside' and unknows['OUT'] > 0):
				unknows['OUT'] -= 1
			elif (criminalRecords[id] == 'inside' and unknows['OUT'] == 0):
				anotherEntranceInCrimeHouse = True
		elif (action == 'L'):
			if (criminalRecords[id] == '' and unknows['IN'] > 0):
				criminalRecords[id] = 'outside'
				unknows['IN'] -= 1
			elif (criminalRecords[id] == 'inside' or criminalRecords[id] == ''):
				criminalRecords[id] = 'outside'
			elif (criminalRecords[id] == 'outside' and unknows['IN'] > 0):
				unknows['IN'] -= 1
			elif (criminalRecords[id] == 'outside' and unknows['IN'] == 0):
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
	print('CRIME TIME' if anotherEntranceInCrimeHouse else insideCount)

def run(testcase):
	print(testcase)
	totalExpectedEntries, entries = testcase.split('; ')
	entries = [tuple(record.split()) for record in entries.split('|')]

	if (len(entries) != int(totalExpectedEntries)):
		raise AssertionError('{} entries expected. Found {}'.format(totalExpectedEntries, len(entries)))

	processHouseEntryRecords(entries)


run('3; E 5|L 0|E 5')						# 1
run('2; L 1|L 1')							# CRIME TIME
run('4; L 1|E 0|E 0|L 1')					# 1
run('7; L 2|E 0|E 1|E 2|E 0|E 3|L 4')		# 4
run('13; L 4|L 1|L 2|E 0|L 1|E 0|L 2|E 0|L 2|E 0|E 0|L 1|L 4')	#0