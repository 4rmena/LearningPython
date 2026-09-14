def missionReport(*stations):
    pass

stationA = [204, 204, 501, 302, 501]
stationB = [204, 610, 501, 204]
stationC = [302, 204, 501, 204, 610, 610]

uniqueCodes = missionReport(stationA, stationB, stationC)

totalfaults = stationA.copy()
totalfaults.extend(stationB)
totalfaults.extend(stationC)

print(totalfaults)