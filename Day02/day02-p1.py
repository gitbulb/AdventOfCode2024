
def allCreasing(aReport: list, increase: bool) -> bool:

    for level, levelNext in zip(aReport, aReport[1:]):
        if (int(levelNext) > int(level)) == increase and level != levelNext:
            continue
        return False

    return True

def safeDifference(aReport: list):
    # print("x")
    for level, levelNext in zip(aReport, aReport[1:]):
        if  1 <= abs(level - levelNext) <= 3:
            continue
        return False
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
    if safeDifference(report):
        if allCreasing(report, (report[1] > report[0])):
            levelCounter += 1

print("Safe reports: %d" % (levelCounter))
