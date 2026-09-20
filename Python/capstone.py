def missionReport(*stations):
    totalFaults = []
    for station in stations:
        totalFaults.extend(station)

#    totalFaults = list.copy(stations[0])
#    totalFaults.extend(stations[1])
#    totalFaults.extend(stations[2])

    uniqueCodes = set().union(*stations)

    commonCodes = set.intersection(set(stations[0]), set(stations[1]), set(stations[2]))

    mostFreqCode = {}
    bestCount = 0

    stationSummaries = []

    mostFreqCode = {}

    for value in totalFaults:
        mostFreqCode[value] = mostFreqCode.get(value, 0) + 1

    mostFreqCode = max(mostFreqCode, key=mostFreqCode.get)

#    for count in totalFaults:
#        mostFreqCode[count] = mostFreqCode.get(count, 0) + 1
#    for code in totalFaults:
#        currentCount = totalFaults.count(code)
#        if currentCount > bestCount:
#            bestCount = currentCount
#            mostFreqCode = code

    for index, station in enumerate(stations):
        worstCode = 0
        worstCodeCount = {}
        bestWorstCount = 0

        stationIndex = index

        faultCount = (len(station))

        for count in station:
            worstCodeCount[count] = worstCodeCount.get(count, 0) + 1
        for code in station:
            currentWorst = worstCodeCount[code]
            if currentWorst > bestWorstCount:
                bestWorstCount = currentWorst
                worstCode = code
            stationSum = (stationIndex, faultCount, worstCode)
        stationSummaries.append(stationSum)


    return len(totalFaults), uniqueCodes, commonCodes, mostFreqCode, stationSummaries


stationA = [204, 204, 501, 302, 501]
stationB = [204, 610, 501, 204]
stationC = [302, 204, 501, 204, 610, 610]

totalFaults, uniqueCodes, commonCodes, mostFreqCode, stationSummaries = missionReport(stationA, stationB, stationC)

print(f"Total number of faults across all stations: {totalFaults}")
print(f"Set of every distict code seen across all stations: {uniqueCodes}")
print(f"Set of codes that appeared in every single stations: {commonCodes}")
print(f"Most frequent code that is seen in every station: {mostFreqCode}")
print(f"Station summary report:{stationSummaries}")