
from src._shared.errors.bad_request import BadRequestError
from web.sdk.mrplato.input_validation import load_list_of_problems

def validate_list(list):
    array = []
    r, l_msgs, array_validator, author = load_list_of_problems(list.get_file())
    if not r :
        raise BadRequestError(l_msgs)
    
    for element in array_validator:
        l_premisses, conclusion = extract_premisses_and_conclusion0(element)
        premissas_concatenadas = ' , '.join(l_premisses)
        line = f"{premissas_concatenadas} ⊢ {conclusion}"
        array.append(line)
    
    return array
    

def extract_premisses_and_conclusion0(selected_problem):
    arg = ''.join(selected_problem)
    l_arg = arg.split('|=')
    l_premisses = l_arg[0].split('&')
    conclusion = l_arg[1]

    return l_premisses, conclusion