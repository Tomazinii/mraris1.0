"""
Created on Tue Nov 07 08:19: 2023

@author: cedric
"""



from web.sdk.mrplato.resources import tools_file as tools
from web.sdk.mrplato.resources import forms as fms

import tokenize


# -----------------------------------------------------------------------------
def is_arg_wff(l_premisses,conclusion):
    '''

           '''

    r1, msg1, lprep_premisses = prepare_list_of_premisses(l_premisses)
    # print(f"r1: {r1} - msg: {msg1} - P: {lprep_premisses}")
    if not r1:
        return r1, msg1, []
    else:
        r2, msg2, prep_conclusion = prepare_conclusion(conclusion)
        # print(f"r2: {r1} - msg2: {msg2} - P: {l_premisses} - C: {prep_conclusion}")
        if not r2:
            return r2, msg2, []
        else:
            return True, '', [lprep_premisses,prep_conclusion]


# -----------------------------------------------------------------------------
def prepare_list_of_premisses(l_premisses):

    tls = tools.UsefullTools()
    l_prep_premisses = []

    # Preparing the list of premisses
    for p in l_premisses:
        prem = " ".join(p)
        # print(f'prem antes: {prem}')
        prem = tls.insert_spaces(prem)
        # print(f'prem depois: {prem}')
        list_prem = prem.split()
        # Variables in predicates must be separated by COMMAS WITHOUT spaces between it
        list_prem = list(filter((',').__ne__, list_prem))  # remove all occurrences of ',' from the input_string
        # print(f'list_prem: {list_prem}')
        r, msg, prep_premiss = is_wff(list_prem)  # Include a new premiss
        l_prep_premisses.append(prep_premiss)
        if not r:
            return r, msg, []
    return True, '', l_prep_premisses


# -----------------------------------------------------------------------------
def prepare_conclusion(conclusion):

    tls = tools.UsefullTools()
    s_conclusion = " ".join(conclusion)
    s_conclusion = tls.insert_spaces(s_conclusion)
    # print(f's_conclusion1: <{s_conclusion}> - type: {type(s_conclusion)}')
    list_s_conclusion = s_conclusion.split()
    list_s_conclusion = list(
        filter((',').__ne__, list_s_conclusion))  # remove all occurrences of ',' from the input_string

    if list_s_conclusion[0] in [fms.GlobalConstants.eqv, fms.GlobalConstants.cnf,
                                fms.GlobalConstants.dnf, fms.GlobalConstants.ics,
                                fms.GlobalConstants.true, fms.GlobalConstants.false]:
        return True, '', list_s_conclusion[0]

    else:
        r, msg, prep_conclusion = is_wff(list_s_conclusion)  # Include conclusion
        if not r:
            return False, msg, ""
        else:
            return True, '', s_conclusion


# -----------------------------------------------------------------------------
def is_wff(formula):  # formula is in string format
    '''
        Input a new premiss.
        The parameter form is just to check if the text ( a string ) in the input screen
        has been changed.
        The input to be processed into a new premiss is stored in the 'self.ids.in_arg_label.text'
        property.
    '''

    tls = tools.UsefullTools()
    r1, error_message, new_formula = tls.remove_parenthesis(formula)
    if not r1:
        return r1, error_message, ""
    else:
        # print(f'new_formula: {new_formula}')
        r2, error_message, prep_formula = fms.generate_represent(new_formula)
        # print(f'r2: {r2} - error_message: {error_message} ')
        # print(f'prep_formula: {prep_formula}')
        if not r2:
            return r2, error_message, ""
        else:
            return True, '', formula


# -----------------------------------------------------------------------------
def load_list_of_problems(lp_name):
    tokens = tokenize.tokenize(lp_name.readline)
    l_strings = []
    try :
        for token in tokens:
            # print(f"token: {token}")
            l_strings.append((token.type,token.string))
    except:
        # msg = "Error in processing file at: "+token.line
        msg = "Wrong number of parenthesis at: "+token.line
        print(f"msg: {msg}")
        return False, [msg], [], ""

    r, l_msgs, l_args, author = check_input(l_strings)
    # for a in l_args:
    #     print(f"arg: {a}")

    if r:
        msg = f"All arguments are WELL FORMED FORMULAS!"
        return r, l_msgs, l_args, author
    else:
        print(f"Not all argument IS A WELL FORMED FORMULA!")
        return r, l_msgs, l_args, author

# -----------------------------------------------------------------------------
def check_input(l_strings):
    '''

            '''

    l_msgs = []
    wff_largs = []
    r1 = r2 = True
    # print(f"l_string_in: {l_strings}")
    nl_strings, author = drop_unusefull_tokens(l_strings)

    # print(f"nl_string_in: {nl_strings}")
    if nl_strings == []:
        msg = "Empty file."
        return False, [msg], [], author

    l_args = split_arguments(nl_strings)

    ind = 0
    for a in l_args:
        msg = f"Checking line[{ind}]: {a}"
        print(msg)
        ind = ind+1

        r0, msg0, l_premisses, conclusion = get_l_premisses_conclusion(a)
        # print(f"r0: {r0} - msg0: {msg0} - P: {l_premisses} - C: {conclusion}")

        # Premisses and conclusion are not empty lists
        if not r0:
            l_msgs.append(msg0)
            return r0, l_msgs, a, author
        else:
            r1, msg1, formatted_arg = is_arg_wff(l_premisses, conclusion)
            # print(f"formatted_arg: {formatted_arg}")
            if not r1:
                l_msgs.append(msg1)
                break
            else:
                msg = f"Line[{ind}] is a WELL FORMED FORMULA."
                print(msg)

    return r1 , l_msgs, l_args, author

# -----------------------------------------------------------------------------
def drop_unusefull_tokens(l_strings):

    n_lstrings = []
    author = "Anonymous"
    i = 0
    while i < len(l_strings):
        # print(f"l_strings[{i}]: {l_strings[i]} :")
        if l_strings[i][0] in [0,2,6,61,62,63]:
            # print(f"drop: {l_strings[i][0]} : {l_strings[i][1]}")
            pass
        elif l_strings[i][1] == " ":
            # print("drop")
            pass
        elif l_strings[i][1] == "-":
            # print("drop")
            pass
        elif l_strings[i][1] == "<":
            if l_strings[i+1][1] == "->":
                n_lstrings.append("<->")
                i = i+1
            else:
                pass
        elif l_strings[i][1] == '@':
            j = i+1
            n_author = ''
            while j < len(l_strings):
                if l_strings[j][1] == '\n': break
                else:
                    n_author = n_author+' '+ l_strings[j][1]
                j=j+1
            author = n_author
            i = j
            # print(f"author: {author}")
        else:
            if l_strings[i][0] == 60 and l_strings[i][1] not in ['∀','∃','!']:
                # print(f"drop: {l_strings[i][0]} : {l_strings[i][1]}")
                pass
            else:
                n_lstrings.append(l_strings[i][1])
                # print(f"token: {l_strings[i]}")
        i= i+1

    # print(f"author: {author}")
    return n_lstrings, author

# -----------------------------------------------------------------------------
def split_arguments(l_strings):
    l_args = []
    i = 0
    while i < len(l_strings):
        arg = []
        j = i
        while l_strings[j] != '\n' : # type = 4: new line
            arg.append(l_strings[j])
            j = j + 1
            if j == len(l_strings): break
        l_args.append(arg)
        i = j+1
    return l_args


# -----------------------------------------------------------------------------
def get_l_premisses_conclusion(s_arg):
    # print(f"s_arg: {s_arg}")

    l_premisses = []
    i = 0
    while i < len(s_arg):
        premiss = []
        j = i
        # print(f"s_arg[{j}]: {s_arg[j]}")
        while (s_arg[j] != '&') and (s_arg[j] != '|='):
            premiss.append(s_arg[j])
            j = j+1
            if j == len(s_arg): break

        # print(f"premiss: {premiss}")

        if premiss == []:
            msg = "Premiss is missing."
            res = False
            return res, msg, l_premisses, []
        else:
            l_premisses.append(premiss)
            # print(f"l_premisses: {l_premisses}")
            if j < len(s_arg):
                i = j+1
                if s_arg[j] == '|=': break
            else:
                res = False
                msg = "Wrong argument. Symbol \'|=\' is missing."
                return res, msg, l_premisses, []

    if l_premisses == []:
        msg = "No premiss were found."
        res = False
        return res, msg, l_premisses, []
    else:
        # print(f"i: {i}")
        conclusion = []
        while i < len(s_arg):
            conclusion.append(s_arg[i])
            i = i+1

        # print(f"conclusion: {conclusion}")
        if conclusion == []:
            msg = "Conclusion is missing."
            res = False
            return res, msg, l_premisses, []
        else:
            res = True
            msg = ""

    return res, msg, l_premisses, conclusion
