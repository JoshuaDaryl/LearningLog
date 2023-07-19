def arithmetic_arranger(problems, solve=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    line1 = []
    line2 = []
    dashes = []
    solutions = []

    for problem in problems:
        num1, operator, num2 = problem.split()

        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."

        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(num1), len(num2)) + 2

        line1.append(num1.rjust(width))
        line2.append(operator + num2.rjust(width - 1))
        dashes.append('-' * width)

        if solve:
            if operator == '+':
                result = str(int(num1) + int(num2))
            else:
                result = str(int(num1) - int(num2))
            solutions.append(result.rjust(width))

    arranged_problems = []
    arranged_problems.append("    ".join(line1))
    arranged_problems.append("    ".join(line2))
    arranged_problems.append("    ".join(dashes))

    if solve:
        arranged_problems.append("    ".join(solutions))

    return "\n".join(arranged_problems)
