

from numpy import True_


problems_limit = 5
operand_limit = 4
numIndex = 0
opIndex = 1
denoIndex = 2
tabSpace = 4


def sum(a, b):
    result = a + b
    return result


def sub(a, b):
    result = a - b
    return result


operation = []
operators = "+-"
numerator = []
denominator = []
result = []


def valid(list):

    error_msg = []
    if len(list) > problems_limit:
        error_msg.append("Error: Too many problems.")
        return error_msg, False
    else:
        for items in list:
            operations = items.split(" ")
            i = 0
            while(i < 3):
                if i % 2 == 0:
                    if operations[i].isdigit():
                        if len(operations[i]) > 4:
                            error_msg.append(
                                "Error: Numbers cannot be more than four digits.")
                        else:
                            if i == numIndex:
                                numerator.append(int(operations[i]))
                            elif i == denoIndex:
                                denominator.append(int(operations[i]))
                    else:
                        error_msg.append("Numbers must only contain digits.")
                    i += 1
                else:
                    if operations[i].isdigit() == False and operations[i] in operators:
                        operation.append(operations[i])
                    else:
                        error_msg.append("Error: Operator must be '+' or '-'.")
                    i += 1
        if error_msg == []:
            return None, True
        else:
            return error_msg, False


def arithmetic_arranger(list, bool):
    numerator_str = ""
    denominator_str = ""
    results_str = ""
    dash = ""
    Error_msg, Valid = valid(list)
    if Valid == False:
        for msg in Error_msg:
            print(msg)
    else:
        for i in range(0, len(list)):
            if operation[i] == '+':
                result.append(sum(numerator[i], denominator[i]))
            else:
                result.append(sub(numerator[i], denominator[i]))
            maxLen = 0
            if len(str(numerator[i])) > len(str(denominator[i])):
                maxLen = len(str(numerator[i]))
            else:
                maxLen = len(str(denominator[i]))
            maxLen = maxLen + 2
            numLen = len(str(numerator[i]))
            denoLen = len(str(denominator[i]))
            resLen = len(str(result[i]))
            numerator_str += " " * (maxLen - numLen) + \
                str(numerator[i]) + " " * tabSpace
            denominator_str += operation[i] + " " * (
                maxLen - (denoLen + 1)) + str(denominator[i]) + " " * tabSpace
            dash += "-" * maxLen + " " * tabSpace
            results_str += " " * (maxLen - resLen) + \
                str(result[i]) + " " * tabSpace
        if bool:
            print(numerator_str)
            print(denominator_str)
            print(dash)
            print(results_str)
        else:
            print(numerator_str)
            print(denominator_str)
            print(dash)


arithmetic_arranger(["32 + 698", "1 / 35801", "9999 * 9999"], False)
