

from web.sdk.mrplato.get_current_status_prover import filter_new_lines


def back_state_mrplato(prover_instance):


    lines = []
    for element in prover_instance.argument_premisses:
        formate = {"content": f"{element[0]}", "methods_used_info":f"{element[1]}", "type":"default",}
        lines.append(formate)

    s = str(prover_instance.argument_conclusion)

    new_lines = filter_new_lines(prover_instance.proof_lines)

    if len(prover_instance.list_of_hypothesis) and "ADHYP" in new_lines[len(new_lines) - 1]["methods_used_info"]:
        prover_instance.list_of_hypothesis.pop()

    if(len(prover_instance.proof_lines) != 0):
        prover_instance.proof_lines.pop()


    if(len(new_lines) != 0):
        new_lines.pop()

    output = {
        "premisses": lines, 
        "conclusion":s,
        "new_lines": new_lines,
        "prover_instance": prover_instance
    }


    return output
