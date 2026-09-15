# UNIQUE SENSOR IDs

pass1 = ["S1", "S2", "S3", "S2", "S4"]
pass2 = ["S3", "S5", "S1"]
pass3 = ["S6", "S2", "S1", "S1"]

set1 = set(pass1)
set2 = set(pass2)
set3 = set(pass3)

sets = set.union(set1 , set2, set3)

print(set1)
print(sets)

print()

# DUPLICATE TELEMETRY DETECTION
readings = [101, 102, 102, 103, 104, 104, 104, 105]

def findDuplicates(data):
    setReadings = set(data)
    tally = {}
    Count = 1
    freq = set()

    for value in data:
        tally[value] = tally.get(value, 0) + 1
        if tally[value] > Count:
            freq.add(value)

    return freq, setReadings

freq, setReadings = findDuplicates(readings)
print(f"Values that appeared more than once: {freq}")
print(f"Values: {setReadings}")

print()

# REDUNDANT SYSTEMS CHECK
arrayA_active = {"propulsion", "comms", "life_support", "navigation"}
arrayB_active = {"comms", "navigation", "thermal", "power"}

active = set.intersection(arrayA_active, arrayB_active)
array = set.union(arrayB_active, arrayA_active)
diff = set.difference(arrayA_active, arrayB_active)
unique = set.symmetric_difference(arrayA_active, arrayB_active)

print(f"Active in both arrays: {active}")
print(f"Seen in both arrays: {array}")
print(f"Reportings : {diff}")
print(f"Unique reporting(s): {unique}")

print()

# CREW ROSTER VALIDATION
flight_ops_roster = {"Chen", "Alvarez", "Osei", "Kowalski"}
medical_roster = {"Alvarez", "Kowalski", "Reyes", "Chen"}

def roster_mismatch(setA, setB):
    rosterA = set(setA)
    rosterB = set(setB)
    finalRoster = set.union(rosterA, rosterB)
    mismatch = None

    if rosterA != rosterB:
        mismatch = set.symmetric_difference(rosterA, rosterB)
    else:
        print("Match!")

    return mismatch, finalRoster

mismatch, finalRoster = roster_mismatch(flight_ops_roster, medical_roster)

print(f"Persons missing from each roster: {mismatch}")
print(f"Approved Final Roster: {finalRoster}")

print()

# MISSION CONTROL DASHBOARD (CAPSTONE)
def alertSummary(log):
    uniqueCodeSets = set(log)

    mostFreq = {}
    count = 0

    for freq in log:
        mostFreq[freq] = mostFreq.get(freq, 0) + 1

    totalAlerts = len(log)

    return uniqueCodeSets, max(mostFreq, key=mostFreq.get), totalAlerts
alert_log = [204, 204, 501, 302, 501, 501, 204, 610]

uniqueCodeSets, mostFreq, totalAlerts = alertSummary(alert_log)

print(f"Unique Code sets: {uniqueCodeSets}")
print(f"Most frequent integer: {mostFreq}")
print(f"Total numbers of code: {totalAlerts}")