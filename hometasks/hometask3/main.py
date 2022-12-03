from typing import Final
import re

import json
from sly import Lexer

#

s_expression = open('names.sxpr', 'r')
lines_expression = s_expression.readlines()
s_expression.close()

EQUAL: Final = '::='
COMMENT: Final = '//'
NONE_OBJ: Final = 'p1@#i1dIJ#345sl@c#346p&eq'
TYPES: Final = \
    {
        'PROGRAM_NAME' : 'program',
        # По хорошему сюда вставить сразу указатели на методы
        # я этого не сделал и это была глобальная ошибка, теперь придётся писать 100500 вложенных ифов
        'TYPES_DATA' : ['string', 'int'],
        'TYPES_OPERATION' : ['math', 'logic']
    }

PROGRAM = \
    {
        'program' : "",
        'string' : {},
        'int' : {}
    }


for index, line in enumerate(lines_expression):
    full_line = lines_expression[index].replace('\n', '')
    line = line.split(COMMENT)[0].replace('\n', '').replace(' ', '').replace('\t', '')
    if not line: continue
    slice_args_re = re.findall(r'^(<([^<>]+)>(::=)<([^<>]+)>)$', line)
    slice_args = [varn for cort in slice_args_re for varn in cort]

    if index == 0 and len(slice_args) == 4 and slice_args[1] == TYPES['PROGRAM_NAME']:
        print(f"Program: {slice_args[3]}")
        PROGRAM['program'] = slice_args[3]
        continue
    elif index == 0:
        exit(f'error in: "{full_line}"\nuncorrent program name in line: {index + 1}')

    if slice_args and slice_args[1] in TYPES['TYPES_DATA']:
        PROGRAM[slice_args[1]][slice_args[3]] = NONE_OBJ
        continue
    elif slice_args and slice_args[1].count('::') == 1 and slice_args[1].split('::')[0] in TYPES['TYPES_DATA']:
        var_type = slice_args[1].split('::')[0]
        var_name = slice_args[1].split('::')[1]
        if PROGRAM[var_type].get(var_name) is None:
            exit(f'error in: "{full_line}"\nvar does not exist in line: {index + 1}')
        res = slice_args[3]
        try:
            if var_type == 'int': res = int(res)
            PROGRAM[var_type][var_name] = res
        except ValueError:
            exit(f'error in: "{full_line}"\npassing values is not supported in line: {index + 1}')
        continue
    elif slice_args and slice_args[1].count('::') == 1 and slice_args[1].split('::')[0] in TYPES['TYPES_OPERATION']:
        var_type = 'int'
        var_name = slice_args[1].split('::')[1]
        if PROGRAM[var_type].get(var_name) is None:
            exit(f'error in: "{full_line}"\nvar does not exist in line: {index + 1}')
        try:
            res = int(eval(slice_args[3]))
            PROGRAM[var_type][var_name] = res
        except ZeroDivisionError:
            exit(f'error in: "{full_line}"\ndivision by zero in line: {index + 1}')
        continue
    else:
        exit(f'error in: "{full_line}"\nuncorrent program logic in line: {index + 1}')


print(json.dumps(PROGRAM, sort_keys=False, indent=4))
print(f"{PROGRAM['program']} is finished")
