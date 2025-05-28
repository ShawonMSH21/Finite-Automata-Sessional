from automata.fa.nfa import NFA
nfa9 = NFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'1': {'q0', 'q1'}, '0': {'q0'}},
        'q1': {'0': {'q2'}},
        'q2': {'1': {'q3'}},
        'q3': {'0': {'q4'}},
        'q4': {}
    },
    initial_state='q0',
    final_states={'q4'}
)

test_string = "101101"

if nfa9.accepts_input(test_string):
    print(f"✅ String '{test_string}' is accepted (contains '1010')")
else:
    print(f"❌ String '{test_string}' is not accepted (no '1010' found)")
