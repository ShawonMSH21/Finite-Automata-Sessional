from automata.fa.nfa import NFA

nfa1 = NFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': {'q0'}, '1': {'q0', 'q1'}},
        'q1': {'0': {'q2'}, '1': {'q2'}},
        'q2': {}
    },
    initial_state='q0',
    final_states={'q1'}
)

test_string = "1100"

if nfa1.accepts_input(test_string):
    print(f"✅ String '{test_string}' is accepted (second last bit is '1')")
else:
    print(f"❌ String '{test_string}' is not accepted (second last bit is not '1')")
