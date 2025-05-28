from automata.fa.nfa import NFA
nfa4 = NFA(
    states={'q0', 'q1'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': {'q1'}},
        'q1': {'1': {'q0'}}
    },
    initial_state='q0',
    final_states={'q0'}
)

test_string = "0101011"

if nfa4.accepts_input(test_string) and test_string != "":
    print(f"✅ String '{test_string}' is accepted (form (01)^n)")
else:
    print(f"❌ String '{test_string}' is not accepted (not in (01)^n)")
