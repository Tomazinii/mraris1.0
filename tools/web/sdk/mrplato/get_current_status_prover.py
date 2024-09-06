

def filter_new_lines(proof_lines):
    lines = []
    for element in proof_lines:
        if element[1] != "P":
            formate = {"content": f"{element[0]}", "methods_used_info":f"{element[1]}", "type":"default",}
            lines.append(formate)
    
    return lines


def get_current_status_prover(prover_instance, problem):

    r, msg = prover_instance.input_an_argument(problem)


    lines = []
    for element in prover_instance.argument_premisses:
        formate = {"content": f"{element[0]}", "methods_used_info":f"{element[1]}", "type":"default",}
        lines.append(formate)

    s = str(prover_instance.argument_conclusion)
    new_lines = filter_new_lines(prover_instance.proof_lines)

    output = {
        "premisses": lines, 
        "conclusion":s,
        "new_lines": new_lines,
        
    }

    return output
