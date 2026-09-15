def missionReport(*stations):
    totalFaults = list.copy(stations[0])
    totalFaults.extend(stations[1],)
    totalFaults.extend(stations[2])

    uniqueCodes = set().union(*stations)

    commonCodes = set.intersection(set(stations[0]), set(stations[1]), set(stations[2]))

    return len(totalFaults), uniqueCodes, commonCodes

stationA = [204, 204, 501, 302, 501]
stationB = [204, 610, 501, 204]
stationC = [302, 204, 501, 204, 610, 610]

totalFaults, uniqueCodes, commonCodes = missionReport( stationA, stationB, stationC)

print(totalFaults)
print(uniqueCodes)
print(commonCodes)