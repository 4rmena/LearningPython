def missionReport(*stations):
    totalFaults = list.copy(stations[0])
    totalFaults.extend(stations[1],)
    totalFaults.extend(stations[2])

    uniqueCodes = set().union(*stations)

    commonCodes = set.intersection(set(stations[0]), set(stations[1]), set(stations[2]))

    mostFreqCode = {}
    bestCount = 0

    for count in totalFaults:
        mostFreqCode[count] = mostFreqCode.get(count, 0) + 1
    for code in totalFaults:
        currentCount = totalFaults.count(code)
        if currentCount > bestCount:
            bestCount = currentCount
            mostFreqCode = code

            
    return len(totalFaults), uniqueCodes, commonCodes, mostFreqCode, stationSum()

#    stationSum = [tuple(stations[0]), tuple(stations[1]), tuple(stations[2])]
"""
    def stationSum():
        stationIndex = 0
        index = len(stations)

        while index < stationIndex:
            stationIndex += 1

        return stationIndex
"""
#    for stationIndex, faultCount, worstCode in stations:
#        pass

#        stationSum = stationIndex, faultCount, worstCode

stationA = [204, 204, 501, 302, 501]
stationB = [204, 610, 501, 204]
stationC = [302, 204, 501, 204, 610, 610]

totalFaults, uniqueCodes, commonCodes, mostFreqCode, stationSum = missionReport( stationA, stationB, stationC)

print(totalFaults)
print(uniqueCodes)
print(commonCodes)
print(mostFreqCode)
print(stationSum)