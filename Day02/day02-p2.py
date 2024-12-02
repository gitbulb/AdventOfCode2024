import copy
def test_diff(num1, num2):
    return 1 <= abs(num1 - num2) <= 3


def test_ascending(num1, num2, ascending):
    if ascending:
        return num2 > num1
    #  else
    return num1 > num2

def determine_ascendence(aReport):
     #  Determine general ascendence, with at most first two similar (and ignore that)
    if aReport[0] == aReport[1]:
        return  aReport[2] > aReport[0]
    # else:
    return  aReport[1] > aReport[0]


def test_report(aReport, detected_faults=0):

    if detected_faults > 1:
        return False

    # 3 similars are too many faults in any case
    if report[0] == report[1] == report[2]:
        return False

    ascending = determine_ascendence(aReport)

    for level, levelNext in zip(range(0, len(aReport)), range(1, len(aReport))):

        if test_ascending(aReport[level], aReport[levelNext], ascending) and test_diff(aReport[level], aReport[levelNext]):
            continue


        # Remove level or leveNext to create an OK report...
        reportLevel = copy.copy(aReport)
        reportLevel.pop(levelNext)
        reportLevelNext = copy.copy(aReport)
        reportLevelNext.pop(level)

        # Sorting based on the first level may be wrong assumption. Try removing the first level
        reportLevelFirst = copy.copy(aReport)
        reportLevelFirst.pop(0)

        # Try to return a True report
        if test_report(reportLevel, detected_faults+1):
            return True
        if test_report(reportLevelNext, detected_faults+1):
            return True
        return test_report(reportLevelFirst, detected_faults+1)

    return True



levelCounter = 0

reports = []
with open("Day02/reports") as reports_file:
    for report in reports_file:
        report_levels = []
        for level in report.split():
            report_levels.append(int(level))
        reports.append(report_levels)


for report in reports:
    ascending = None


    # print(report, end=" ")
    if test_report(report):
        levelCounter += 1
    #     print("GOOD")
    # else:
    #     print("BAD")
print("Safe reports is initially 371, now (426): %d" % (levelCounter))
