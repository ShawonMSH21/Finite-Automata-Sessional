from automata.fa.nfa import NFA

nfa2 = NFA(
    states={'q0', 'q1', 'q2', 'q3'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'1': {'q0', 'q1'}, '0': {'q0'}},
        'q1': {'1': {'q2'}},
        'q2': {'0': {'q3'}},
        'q3': {}
    },
    initial_state='q0',
    final_states={'q3'}
)

test_string = "101010"

if nfa2.accepts_input(test_string):
    print(f"✅ String '{test_string}' is accepted (contains '110')")
else:
    print(f"❌ String '{test_string}' is not accepted (no '110' found)")
