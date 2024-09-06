


from src._shared.errors.bad_request import BadRequestError
from web.sdk.mrplato.get_options_dto import InputGetOptionDto, OutputGetOptionDto




def options_in_rows(options):
    
    if options[0] == ["a"] or options[0] == []:
        options_rows = []
        for element in options[1]:
            z = {"content": f"{element}", "methods_used_info":"", "type":""}
            options_rows.append(z)

        return options_rows
    

    options_rows = []

    for element in options[0]:
        z = {"content": f"{element}", "methods_used_info":"", "type":""}
        options_rows.append(z)

    return options_rows



def get_option(prover_instance: any, data: InputGetOptionDto, problem: str) -> OutputGetOptionDto:


    pv = prover_instance
    type_selected = data.type_selected
    sel_rule = data.sel_rule
    selected_proof_line_indexes = data.selected_proof_line_indexes
    total_or_partial = data.total_or_partial

    r, msg = pv.input_an_argument(problem)
    rule_types = {'0': 'HYP', '1': 'INF', '2': 'EQ', '3': 'PRED_I', '4': 'PRED_E'}
    rule_type = rule_types[type_selected]

    r, msg, user_input, new_line, proof_line_updated = \
                pv.prove(rule_type, sel_rule, selected_proof_line_indexes, pv.proof_lines, (0, None, total_or_partial))   
    



    
    if not r:
        raise BadRequestError(msg)
        
    else:
        if user_input > 0:
            if rule_type == "EQ":
                labels, options = new_line
    
                print(f"r: {r}")

            elif rule_type == "PRED_E":
                labels, options = new_line

            else:  #rule_type == "PRED_I"

                labels, options = new_line

    
    if not r:
        output = OutputGetOptionDto(
        type_output = "ERROR",
        prover_instance=pv,
        message = msg,
        lines = [{"content": "", "methods_used_info":"", "type":""}],
    )
        return output

    list_options = options_in_rows(options)

    output = OutputGetOptionDto(
        lines=list_options,
        message=msg,
        prover_instance=pv,
        type_output="CREATED"
    )

    return output
    
