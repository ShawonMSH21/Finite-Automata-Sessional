from automata.fa.nfa import NFA
nfa3 = NFA(
    states={'q0', 'q1', 'q2', 'q3'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': {'q0'}, '1': {'q0', 'q1'}},
        'q1': {'0': {'q2'}, '1': {'q2'}},
        'q2': {'0': {'q3'}, '1': {'q3'}},
        'q3': {}
    },
    initial_state='q0',
    final_states={'q1'}
)

test_string = "1000110"

if nfa3.accepts_input(test_string):
    print(f"✅ String '{test_string}' is accepted (third last bit is '1')")
else:
    print(f"❌ String '{test_string}' is not accepted (third last bit is not '1')")
