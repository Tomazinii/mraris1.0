from web.sdk.mrplato.prover_dto import InputProverDto, OutputProverDto
from web.sdk.mrplato.resources import tools_file as tools






def prover(prover_instance, data: InputProverDto, problem: str) -> OutputProverDto:
    selected_proof_line_indexes = data.selected_proof_line_indexes
    type_selected = data.type_selected
    sel_rule = data.sel_rule
    input_formula = data.input_formula
    total_or_partial = data.total_or_partial
    selection = data.selection

    pv = prover_instance

    tls = tools.UsefullTools()

    rule_types = {'0': 'HYP', '1': 'INF', '2': 'EQ', '3': 'PRED_I', '4': 'PRED_E'}
    rule_type = rule_types[type_selected]

    r, msg = pv.input_an_argument(problem)



    r, msg, user_input, new_line, proof_line_updated = \
                pv.prove(rule_type, sel_rule, selected_proof_line_indexes, pv.proof_lines, (0, None, total_or_partial))
    


    if not r:
        raise Exception(f"ERROR: {msg}")
    else:
        if user_input > 0:
            if rule_type in ["HYP", "INF"]:
                ru, error_message, new_formula = tls.input_formula(input_formula)
                if not ru:
                    
                    raise Exception(f"ERROR: {error_message}")
                else:
                    r, msg, new_line, proof_line_updated = continue_proving_inference(total_or_partial, pv, rule_type, sel_rule,
                                                        selected_proof_line_indexes, new_formula)
            elif rule_type == "EQ":
                labels, options = new_line
                sub_form = select_option(options[0], selection=selection)
                r, msg, new_line, proof_line_updated = continue_proving_equivalence(total_or_partial, pv, rule_type, sel_rule,
                                                        selected_proof_line_indexes, sub_form)

            elif rule_type == "PRED_E":
                labels, options = new_line
                sub_formula = select_option(options[0], selection=selection)
                r, msg, new_line, proof_line_updated = \
                    continue_proving_pred_equivalence(total_or_partial, pv,
                                                        rule_type,sel_rule,selected_proof_line_indexes,
                                                        sub_formula)
                
            else:  #rule_type == "PRED_I"
                labels, options = new_line
                selected_term = select_option(options[0], selection=selection)
                r, msg, new_line, proof_line_updated = \
                    continue_proving_predicates_1(labels[1], options[1], pv, rule_type,
                                                    sel_rule,selected_proof_line_indexes,
                                                    selected_term)
                
    

    lines = []

    for element in proof_line_updated:
            formate = {"content": f"{element[0]}", "methods_used_info":f"{element[1]}", "type":"default",}
            lines.append(formate)

    if r:

        output = OutputProverDto(
            type_output = "CREATED",
            message = str(msg),
            lines = lines,
            prover_instance=pv
    )
    else:
        output = OutputProverDto(
            type_output = "ERROR",
            message = str(msg),
            lines = lines,
            prover_instance=pv
            
    )

    rf, final_msg = pv.check_for_success(new_line)

    if rf:

        output = OutputProverDto(
        type_output = "PROVED",
        message = str(final_msg),
        lines = lines,
        prover_instance=pv
    )
    return output



def continue_proving_inference(total_or_partial, pv, type_selected, rule_index, sel_lines, new_formula):

    r, msg, user_input, new_line, proof_line_updated = \
            pv.prove(type_selected, rule_index, sel_lines, pv.proof_lines,
                     (0, new_formula, total_or_partial))

    return r, msg, new_line, proof_line_updated




def select_option(options,selection):
    return options[selection]


def continue_proving_equivalence(total_or_partial, pv, type_selected, rule_index, sel_lines,sub_form):
    r, msg, user_input, new_line, proof_line_updated = \
        pv.prove(type_selected, rule_index, sel_lines, pv.proof_lines, (0, sub_form, total_or_partial))

    return r, msg, new_line, proof_line_updated


def continue_proving_pred_equivalence(total_ou_partial, pv, type_selected, rule_index,
                                      sel_lines,sub_formula):

    r, msg, user_input, new_line, proof_line_updated = \
        pv.prove(type_selected, rule_index, sel_lines, pv.proof_lines, (0, sub_formula, total_ou_partial))

    return r, msg, new_line, proof_line_updated


def continue_proving_predicates_1(label, options, pv, type_selected, rule_index, sel_lines, selected_term):
    selected_var = options[0]
    r, msg, new_line, proof_line_updated = \
        continue_proving_predicates_2(pv, type_selected, rule_index, sel_lines,
                                      selected_var, selected_term)
    return r, msg, new_line, proof_line_updated


def continue_proving_predicates_2(pv, type_selected, rule_index, sel_lines, selected_var, selected_term):

    user_resp = (selected_var, selected_term)
    r, msg, user_input, new_line, proof_line_updated = \
        pv.prove(type_selected, rule_index, sel_lines, pv.proof_lines, (0, user_resp, "total"))

    if not r:
        msg = msg + "\n\n This rule cannot be applied here!"
        return r, msg, new_line, proof_line_updated
    else:
        if user_input == 0:
            return r, msg, new_line, proof_line_updated
        elif user_input == 1:
            user_resp = (new_line[0][0], selected_var, selected_term)

            r, msg, user_input, new_line, proof_line_updated = \
                pv.prove(type_selected, rule_index, sel_lines, pv.proof_lines, (0, user_resp, "total"))
            if r:
                return r, msg, new_line, proof_line_updated
            else:
                return r, msg+ "\n\n This rule cannot be applied here!"

        else:  # user_input = 2
            labels, options, selected_var, selected_term = new_line

            terms_to_replace = select_option(labels[0], options)
            r, msg, new_line, proof_line_updated = \
                continue_proving_predicates_3(pv, type_selected, rule_index, sel_lines,
                                              selected_var, selected_term,terms_to_replace)

            return r, msg, new_line, proof_line_updated
        

def continue_proving_predicates_3(pv, type_selected, rule_index, sel_lines,
                                  selected_var, selected_term, terms_to_replace):
    user_resp = (terms_to_replace, selected_var, selected_term)
    r, msg, user_input, new_line, proof_line_updated = \
        pv.prove(type_selected, rule_index, sel_lines, pv.proof_lines, (0, user_resp,"total"))

    return r, msg, new_line, proof_line_updated
    