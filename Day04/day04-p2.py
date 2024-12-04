xmas_blob = []

def check_mas(line, pos):
    if  xmas_blob[line][pos] == "A" and \
            line >= 1 and \
            pos >= 1 and \
            pos < len(xmas_blob[line]) -1 and \
            line < len(xmas_blob) -1:

        up_mas = xmas_blob[line-1][pos-1] + xmas_blob[line][pos] + xmas_blob[line+1][pos+1]
        down_mas = xmas_blob[line+1][pos-1] + xmas_blob[line][pos] + xmas_blob[line-1][pos+1]

        if (up_mas == "MAS" or up_mas == "SAM") and (down_mas == "MAS" or down_mas == "SAM"):
            return 1
    return 0


with open("Day04/xmas") as xmas_file:
    xmas_blob = xmas_file.readlines()

counter=0
for line in range(0, len(xmas_blob)):
    for pos in range(0, len(xmas_blob[line])):
        counter += check_mas(line, pos)

print("Counted MAS %d times (2000)" % (counter))
