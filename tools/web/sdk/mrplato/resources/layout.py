import streamlit as st
from streamlit_modal import Modal
import streamlit.components.v1 as components
from st_tabs import TabBar
import datetime
import time
import pandas as pd

import tools
import forms as fms
import connect_db as cdb




# -----------------------------------------------------------------------------
def prepare_lines(lines):
    prep_lines = []
    i = 0
    for l in lines:
        prep_lines.append(str(i) + ": " + str(l[0]) + " - " + str(l[1]))
        i += 1
    return prep_lines


# -----------------------------------------------------------------------------
def select_lines(lines_options):
    selected_lines = st.session_state.sl_lines_widget
    update_time()

    sel_lines = []
    for l in selected_lines:
        ln_index = get_position(l, lines_options)
        sel_lines.append(ln_index)

    st.session_state.selected_lines = sel_lines

    return

# -----------------------------------------------------------------------------
def select_equiv_rule(l_rte):

    with st.container(border=True, height=200):
        st.toast('Proving Equivalence!', icon='⏳')
        eq_container = st.container(border=True)
        sel_rule = eq_container.radio(':red[Select a rule,please.]', l_rte, index=None,
                                      key='rb_3')
        rule_index = get_position(sel_rule, l_rte)

        st.session_state.selected_rule = ("EQ", rule_index)
    return

# -----------------------------------------------------------------------------
def select_rule(l_rti, l_rte, l_rtp_i, l_rtp_e):
    r_types = ["Hypothesis", "Inf.Rules", "Equiv.Rules", "P.Inf.Rules",
               "P.Equiv.Rules", ]
    rule_types = ["HYP", "INF", "EQ", "PRED_I", "PRED_E"]
    pc = st.get_option('theme.primaryColor')
    bc = st.get_option('theme.backgroundColor')
    # sbc = st.get_option('theme.secondaryBackgroundColor')
    # tc = st.get_option('theme.textColor')
    type_selected = TabBar(tabs=r_types, default=0,
                           background=bc, color="#898CA4", activeColor="red",
                           fontSize="14px")

    with st.container(border=True, height=200):
        if type_selected == 0:  # HYP
            st.toast('Handling hypothesis!', icon='⏳')
            inf_container = st.container(border=True)
            options = [l_rti[0], l_rti[1], l_rti[2]]
            sel_rule = inf_container.radio(':red[Select a rule,please.]', options, index=None,
                                           key='rb_1')
            rule_index = get_position(sel_rule, options)
            # options.index(sel_rule)

        elif type_selected == 1:
            st.toast('Proving Inference!', icon='⏳')
            inf_container = st.container(border=True)
            sel_rule = inf_container.radio(':red[Select a rule,please.]', l_rti[3:], index=None,
                                           key='rb_2')
            rule_index = get_position(sel_rule, l_rti)
            # l_rti.index(sel_rule)

        elif type_selected == 2:
            st.toast('Proving Equivalence!', icon='⏳')
            eq_container = st.container(border=True)
            sel_rule = eq_container.radio(':red[Select a rule,please.]', l_rte, index=None,
                                          key='rb_3')
            rule_index = get_position(sel_rule, l_rte)
            # l_rte.index(sel_rule)

        elif type_selected == 3:
            st.toast('Proving Predicate Inference!', icon='⏳')
            eq_container = st.container(border=True)
            sel_rule = eq_container.radio(':red[Select a rule,please.]', l_rtp_i, index=None,
                                          key='rb_4')
            rule_index = get_position(sel_rule, l_rtp_i)

        elif type_selected == 4:
            st.toast('Proving Predicate Equivalence!', icon='⏳')
            eq_container = st.container(border=True)
            sel_rule = eq_container.radio(':red[Select a rule,please.]', l_rtp_e, index=None,
                                          key='rb_5')
            rule_index = get_position(sel_rule, l_rtp_e)
            # l_rtp_e.index(sel_rule)
        else:
            pass

    st.session_state.selected_rule = (rule_types[type_selected], rule_index)

    return


# -----------------------------------------------------------------------------
def create_layout(pv, l_rti, l_rte, l_rtp_i, l_rtp_e):
    with st.container(border=None):

        if pv.only_equiv_rules:
            select_equiv_rule(l_rte)
            update_time()
        else:
            select_rule(l_rti, l_rte, l_rtp_i, l_rtp_e)
            update_time()

        with st.container(height=250, border=True):
            proof_lines = st.session_state.proof_lines

            line_options = []
            applied_rules = []

            for l in proof_lines:
                line_options.append(str(l[0]))
                applied_rules.append(str(l[1]))

            modal = new_modal("popup")
            col1, col2 = st.columns(2)

            with col1:
                with st.container(border=True):
                    df = write_proof_lines(line_options, applied_rules)
                    update_time()

            with col2:

                if pv.only_equiv_rules:
                    st.session_state.selected_lines = [len(st.session_state.proof_lines)-1]
                    if pv.can_exchange_ant_conseq:
                        pv.can_exchange_ant_conseq = False
                        st.button("Antecedent <=> Consequent",
                                  on_click=exchange_ant_consec,
                                  args=[pv],
                                  key= 'bt_exchange')
                else:
                    st.multiselect(
                        'Select at least one line proof.',
                        line_options,
                        default=None,
                        on_change=select_lines,
                        args=[line_options],
                        key='sl_lines_widget',

                        )

        bts01, bts02, info = st.columns([1.5, 1.5, 7.0])
        rule_type = st.session_state.selected_rule[0]
        if (rule_type == "EQ") or (rule_type == "PRED_E"):
            flag = False
        else:
            flag = True


        with bts01:
            st.button('PROVE', on_click=proof_loop,
                      args=[pv, modal,"total"],
                      key='bt_prove')

            st.button('PARCIAL', on_click=proof_loop,
                      disabled=flag,
                      args=[pv, modal, "partial"],
                      key='bt_parcial')
            st.info(f"Errors: {st.session_state.errors}")

        with bts02:
            st.button('NEXT', on_click=get_next_problem,
                      key='bt_next')

            st.button('BACK', on_click=del_last_line,
                      args=[pv],
                      key='bt_back')
            st.info(f"Backs: {st.session_state.backs}")

        with info:
            with st.container(border=True):

                st.info("|- " + str(st.session_state.argument_conclusion))
                cod, msg = st.session_state.status_message


                if cod == 1:
                    st.error(msg, icon="🚨")
                else :
                    st.info(msg, icon="ℹ️")

                if st.session_state.delay == "":
                    msg = f"Delay: {0:02d}:{0:02d}"
                else:
                    msg = st.session_state.delay
                st.info(msg, icon="⏰")

        ChangeButtonColour('PROVE', 'white', '#0099ff')  # button txt to find, colour to assign
        ChangeButtonColour('PARTIAL', 'white', '#0099ff')  # button txt to find, colour to assign
        ChangeButtonColour('BACK', 'white', 'red')  # button txt to find, colour to assign
        ChangeButtonColour('NEXT', 'white', '#644476')  # button txt to find, colour to assign

    return

# -----------------------------------------------------------------------------
def exchange_ant_consec(pv):


    new_conclusion = pv.argument_conclusion
    pv.argument_conclusion = pv.remove_rule_reference(pv.argument_premisses[0])
    pv.argument_premisses = [(new_conclusion, "P")]
    pv.proof_lines = pv.argument_premisses
    st.session_state.argument_conclusion = pv.argument_conclusion
    st.session_state.argument_premiss = pv.argument_premisses
    st.session_state.proof_lines = pv.proof_lines

    return


# -----------------------------------------------------------------------------
def ChangeButtonColour(widget_label, font_color, background_color='transparent'):
    htmlstr = f"""
        <script>
            var elements = window.parent.document.querySelectorAll('button');
            for (var i = 0; i < elements.length; ++i) {{ 
                if (elements[i].innerText == '{widget_label}') {{ 
                    elements[i].style.color ='{font_color}';
                    elements[i].style.background = '{background_color}'
                }}
            }}
        </script>
        """
    components.html(f"{htmlstr}", height=0, width=0)

# -----------------------------------------------------------------------------
def new_modal(key):
    modal = Modal(key=key,
                  title="",
                  # Optional
                  padding=10,  # default value
                  max_width=400  # default value
                  )

    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    return modal


# -----------------------------------------------------------------------------
def write_proof_lines(line_options, applied_rules):
    df = pd.DataFrame({
        'Formula': line_options,
        'Rules': applied_rules
    })
    st.table(df)
    return df


# -----------------------------------------------------------------------------
def get_position(element, e_list):
    if element in e_list:
        return e_list.index(element)
    else:
        return None


# -----------------------------------------------------------------------------
def continue_proving_inference(pv, type_selected, rule_index, sel_lines, modal):
    tls = tools.UsefullTools()
    ru, msg, prepared_new_formula = tls.prepare_new_formula(st.session_state.new_form)
    if not ru:
        st.session_state.errors += 1
        st.session_state.status_message = (1, msg)
    else:
        r, msg, user_input, new_line, proof_line_updated = \
            pv.prove(type_selected, rule_index, sel_lines, st.session_state.proof_lines,
                     (0, prepared_new_formula, "total"))
        if r:
            final_check(modal, pv, new_line, proof_line_updated)
        else:
            st.session_state.errors += 1
            msg = msg + "\n\n This rule cannot be applied here!"
            st.session_state.status_message = (1, msg)

    return


# -----------------------------------------------------------------------------
def continue_proving_equivalence(total_ou_partial, pv, type_selected, rule_index, sel_lines, modal):
    selection = st.session_state.sub_form_eq
    r, msg, user_input, new_line, proof_line_updated = \
        pv.prove(type_selected, rule_index, sel_lines, st.session_state.proof_lines, (0, selection, total_ou_partial))
    if r:
        final_check(modal, pv, new_line, proof_line_updated)
    else:
        st.session_state.errors += 1
        msg = msg + "\n\n This rule cannot be applied here!"
        st.session_state.status_message = (1, msg)
    return


# -----------------------------------------------------------------------------
def continue_proving_pred_equivalence(total_ou_partial, pv, type_selected, rule_index, sel_lines, modal):


    selection = st.session_state.sub_form_pred_eq

    r, msg, user_input, new_line, proof_line_updated = \
        pv.prove(type_selected, rule_index, sel_lines, st.session_state.proof_lines, (0, selection, total_ou_partial))
    if r:
        final_check(modal, pv, new_line, proof_line_updated)
    else:
        st.session_state.errors += 1
        msg = msg + "\n\n This rule cannot be applied here!"
        st.session_state.status_message = (1, msg)

    return


# -----------------------------------------------------------------------------
def continue_proving_predicates_1(label, options, pv, type_selected, rule_index, sel_lines, modal):
    sub_term = st.session_state.term_sel

    label_c = ':red[' + str(label) + ']'
    # Select a var or a quantifier
    if len(options) > 1:
        modal1 = new_modal("popup_2")

        with modal1.container():
            with st.container(border=True):
                    st.radio(label_c, options, on_change=continue_proving_predicates_2,
                             args=[pv, type_selected, rule_index, sel_lines, sub_term, modal],
                             index=None, key='sel_var')
    else:
        st.session_state.sel_var = options[0]
        continue_proving_predicates_2(pv, type_selected, rule_index, sel_lines, sub_term, modal)

    return


# -----------------------------------------------------------------------------
def continue_proving_predicates_2(pv, type_selected, rule_index, sel_lines, sub_term, modal):

    user_resp = (st.session_state.sel_var, sub_term)

    r, msg, user_input, new_line, proof_line_updated = \
        pv.prove(type_selected, rule_index, sel_lines, st.session_state.proof_lines, (0, user_resp, "total"))
    # print(f"r: {r} - new_line: {new_line}")
    # print(f"user_input: {user_input}")

    if not r:
        st.session_state.errors += 1
        msg = msg + "\n\n This rule cannot be applied here!"
        st.session_state.status_message = (1, msg)
        return
    else:
        if user_input == 0:
            final_check(modal, pv, new_line, proof_line_updated)
        elif user_input == 1:
            user_resp = (new_line[0][0], st.session_state.sel_var, sub_term)

            r, msg, user_input, new_line, proof_line_updated = \
                pv.prove(type_selected, rule_index, sel_lines, st.session_state.proof_lines, (0, user_resp, "total"))
            if r:
                final_check(modal, pv, new_line, proof_line_updated)
            else:
                st.session_state.errors += 1
                msg = msg + "\n\n This rule cannot be applied here!"
                st.session_state.status_message = (1, msg)
            return
        else:  # user_input = 2
            # print(f"user_input: {user_input}")
            labels, options, selected_var, selected_term = new_line
            modal1 = new_modal("popup_1")
            with modal1.container():
                with st.container(border=True):
                    label = ':red[' + str(labels[0]) + ']'
                    st.radio(label, options, on_change=continue_proving_predicates_3,
                             args=[pv, type_selected, rule_index, sel_lines,
                                   selected_var, selected_term, modal],
                             index=None, key='sub_var2')
            return


# -----------------------------------------------------------------------------
def continue_proving_predicates_3(pv, type_selected, rule_index, sel_lines, selected_var, selected_term, modal):
    user_resp = (st.session_state.sub_var2, selected_var, selected_term)
    r, msg, user_input, new_line, proof_line_updated = \
        pv.prove(type_selected, rule_index, sel_lines, st.session_state.proof_lines, (0, user_resp, "total"))
    if r:
        final_check(modal, pv, new_line, proof_line_updated)
    else:
        st.session_state.errors += 1
        msg = msg + "\n\n This rule cannot be applied here!"
        st.session_state.status_message = (1, msg)
    return


# -----------------------------------------------------------------------------
def proof_loop(pv, modal,total_ou_partial):

    update_time()
    type_selected, rule_index = st.session_state.selected_rule
    sel_lines = st.session_state.selected_lines

    st.session_state.status_message = (0, "")

    if (type_selected != "HYP") and ((rule_index is None) or
                                         (sel_lines == [])):
        msg = "Please, select a rule AND one line, at least."
        st.session_state.errors += 1
        st.session_state.status_message = (1, msg)
        return
    else:
        r, msg, user_input, new_line, proof_line_updated = \
            pv.prove(type_selected, rule_index, sel_lines, st.session_state.proof_lines, (0, None, total_ou_partial))

        if not r:
            st.session_state.errors += 1
            msg = msg + "\n\n This rule cannot be applied here!"
            st.session_state.status_message = (1, msg)
        else:
            if user_input > 0:
                if (type_selected == "HYP") or (type_selected == "INF"):
                    modal1 = new_modal("popup_1")
                    with modal1.container():
                        with st.container(border=True):
                            st.text_input(':red[Input a well formed formula, please.]',
                                          on_change=continue_proving_inference,
                                          args=[pv, type_selected, rule_index, sel_lines, modal], key='new_form')
                elif type_selected == "EQ":
                    labels, options = new_line
                    modal1 = new_modal("popup_1")
                    with modal1.container():
                        with st.container(border=True):
                            label = ':red[' + str(labels[0]) + ']'
                            st.radio(label, options[0], on_change=continue_proving_equivalence,
                                     args=[total_ou_partial, pv, type_selected, rule_index, sel_lines, modal],
                                     index=None, key='sub_form_eq')

                elif  type_selected == "PRED_E":
                    labels, options = new_line
                    modal1 = new_modal("popup_1")
                    with modal1.container():
                        with st.container(border=True):
                            label = ':red[' + str(labels[0]) + ']'
                            st.radio(label, options[0], on_change=continue_proving_pred_equivalence,
                                     args=[total_ou_partial, pv, type_selected, rule_index, sel_lines, modal],
                                     index=None, key='sub_form_pred_eq')

                else: #type_selected == "PRED_I"
                    labels, options = new_line
                    modal1 = new_modal("popup_1")
                    with modal1.container():
                        with st.container(border=True):
                            # Select a term
                            st.radio(labels[0], options[0], on_change=continue_proving_predicates_1,
                                     args=[labels[1], options[1],pv, type_selected, rule_index, sel_lines, modal],
                                     index=None, key='term_sel')

            else:
                final_check(modal, pv, new_line, proof_line_updated)

            return


# -----------------------------------------------------------------------------
def final_check(modal, pv, new_line, proof_line_updated):

    st.session_state.proof_lines = proof_line_updated
    r, msg = check_for_success(pv, new_line)  # Check if user found the desired conclusion

    if msg == '':  # Proof not ended
        st.session_state['selected_lines'] = []
        st.session_state['selected_rule'] = None
        return
    else:
        if r:
            update_time()
            s_time = st.session_state.delay
            # print(f"s_time: {s_time}")
            now = f"\'{str(datetime.datetime.now())}\'"
            # print(f"proof_line_updated: {proof_line_updated}")
            # print(f"now: {now}")
            status_msg = f"{s_time} - Errors: {st.session_state.errors} - Backs: {st.session_state.backs}"
            st.session_state.status_message = (0, status_msg)

            # '(id SERIAL PRIMARY KEY, enr_name INTEGER, name TEXT, errors INTEGER,' \
            # ' backs INTEGER, time TEXT, solution text[] );'
            with modal.container():
                st.success(msg, icon="✅")
                df = write_final_proof()
                st.info(status_msg)

            cdb.save_solution(221064, "\'Cedric Luiz de Carvalho\'", 22,
                              st.session_state.errors, st.session_state.backs,
                              now, df, "mrArisDB")
            st.balloons()
            st.session_state.solved_problems.append(st.session_state.selected_problem)
            st.session_state.list_of_problems.remove(st.session_state.selected_problem)
            clear_session_keys()
        else:
            st.session_state.errors += 1
            st.session_state.status_message = (1, msg)

        return

# -----------------------------------------------------------------------------
def update_time():


    secs = time.perf_counter() - st.session_state.start_time
    mm, ss = int(secs // 60), int(secs % 60)
    st.session_state.delay = f"Delay: {mm:02d}:{ss:02d}"
    return

# -----------------------------------------------------------------------------
def check_for_success(pv, new_line):

    tls = tools.UsefullTools()

    conclusion = st.session_state.argument_conclusion
    if conclusion == fms.GlobalConstants.cnf:
        r = tls.is_cnf(new_line)
    elif conclusion == fms.GlobalConstants.dnf:
        r = tls.is_dnf(new_line)
    else:
        # print(f"new_line: {new_line} - type: {type(new_line)}")
        # print(f"conclusion: {conclusion} - type: {type(conclusion)}")
        r = new_line == conclusion
    if (r):
        st.session_state.end = True
        if len(pv.list_of_hypothesis) != 0:
            error_message = 'You got to the conclusion, \n\n' \
                            'but did not remove the last Temporary Hypothesis yet.\n\n' \
                            'It must be removed first!'
            return False, error_message
        else:
            return True, 'DEMONSTRATION ENDED SUCCESSFULLY!'
    else:
        return False, ''  # Proof not ended


# -----------------------------------------------------------------------------
def write_final_proof():
    proof_lines = st.session_state.proof_lines

    line_options = []
    applied_rules = []
    for l in proof_lines:
        line_options.append(str(l[0]))
        applied_rules.append(str(l[1]))

    df = write_proof_lines(line_options, applied_rules)
    return df


# -----------------------------------------------------------------------------
def clear_session_keys():
    st.session_state['proof_lines'] = []
    st.session_state['selected_problem'] = None
    st.session_state['selected_lines'] = []
    st.session_state['selected_rule'] = None
    st.session_state['argument_conclusion'] = ''
    st.session_state.start_time = 0
    st.session_state.delay = ""
    st.session_state.status_message = (0, "")
    st.session_state['errors'] = 0
    st.session_state['backs'] = 0

    return


# -----------------------------------------------------------------------------
def del_last_line(pv):
    if len(st.session_state.proof_lines) > len(st.session_state.argument_premiss):
        st.session_state.proof_lines.pop(-1)
        st.session_state.backs += 1

        ###########Checar BACK DE HIPOTESIS
        if pv.list_of_hypothesis != []:
            pv.list_of_hypothesis.pop()
    else:
        msg = "You got the proving start point."
        st.session_state.status_message = (0, msg)


# -----------------------------------------------------------------------------
def get_next_problem():

    remain_problems = st.session_state.list_of_problems

    if not remain_problems:
        message = "No more problems to solve."
        st.session_state.status_message = (0,message)
        return
    else:
        pv = st.session_state.prover
        pv.resetApp()
        selected_problem = remain_problems[0]
        r, msg = pv.input_an_argument(selected_problem)
        if not r:
            st.session_state.status_message = (1, msg)
            return
        else:
            st.session_state.selected_problem = selected_problem
            st.session_state.proof_lines = pv.proof_lines
            st.session_state.argument_conclusion = pv.argument_conclusion
            return
