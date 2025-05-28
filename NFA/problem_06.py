from automata.fa.nfa import NFA
nfa6 = NFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': {'q0', 'q1'}, '1': {'q0'}},
        'q1': {'1': {'q2'}},
        'q2': {}
    },
    initial_state='q0',
    final_states={'q2'}
)

test_string = "10011"

if nfa6.accepts_input(test_string):
    print(f"✅ String '{test_string}' is accepted (ends with '01')")
else:
    print(f"❌ String '{test_string}' is not accepted (does not end with '01')")
