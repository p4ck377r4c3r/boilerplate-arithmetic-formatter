def arithmetic_arranger(problems, display_answers=False):
    operands = []
    row_1 = ''
    row_2 = ''
    equal_line = ''
    equal_line_count = ''
    answers = ''
    
    if len(problems)>5:
        return 'Error: Too many problems.'
    
    for problem in problems:
        if '*' or '/' in problem:
            return 'Error: Operator must be ''+'' or ''-''.'
        else:
            operands.append(problem.split(' '))
            
    for i in range((len(operands))):
        if not operands[i][0].isdigit() or not operands[i][2].isdigit():
            return 'Error: Numbers must only contain digits.'
        elif len(operands[i][0]) > 4 or len(operands[i][2] > 4:
            return 'Error: Numbers cannot be more than four digits.'
    
    i = 0
    for operand in operands:
        if len(str(operand[0])) < len(str(operand[2])):
            row_1 += ' ' + ' ' * (len(str(operand[2])) - len(str(operand[0]))) + str(operand[0])
            row_2 += operand[1] + ' ' + str(operand[2])
        else:
            row_1 += ' ' str(operand[0])
            row_2 += operand[1] + ' ' + ' ' * (len(str(operand[0])) - len(str(operand[2]))) + str(operand[2])

        equal_line += '-' * (max(len(str(operand[0])), len(str(operand[2]))) + 2)
        equal_line_count.append(max(len(str(operand[0])), len(str(operand[2]))) + 2)
        if i == len(operand) -1:
            row_1 += '\n'
            row_2 += '\n'
        else:
            row_1 += '    '
            row_2 += '    '
            equal_line += '    '
            i += 1
    
    arranged_problems = row_1 + row_2 + equal_line
    return arranged_problems
                                            
