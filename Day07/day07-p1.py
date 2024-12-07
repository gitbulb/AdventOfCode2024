import itertools



def calculate(test_numbers, operators):

    product = test_numbers[0]
    for i in range(len(operators)):
        match operators[i]:
            case "ADD":
                product += test_numbers[i+1]
            case "MUL":
                product *= test_numbers[i+1]
    return product


def test_equation(test_value, test_numbers):

    number_of_operators = len(test_numbers) -1

    operators_list = list(itertools.product(["ADD", "MUL"], repeat=number_of_operators))

    for operators in operators_list:
        if calculate(test_numbers, operators) == test_value:
            return True

    return False



test_values = []
numbers = []
# for equation in open("Day07/Calibrations_example"):
for equation in open("Day07/Calibrations"):
    test_values.append(int(equation.split(":")[0]))

    numbers.append( [ int(num) for num in equation.split(":")[1].split()] )

summage = 0
for equation_index in range(len(test_values)):
    if test_equation(test_values[equation_index], numbers[equation_index]):
        summage += test_values[equation_index]

print(f"Summage of correct equations (8401132154762/3749): {summage}")
