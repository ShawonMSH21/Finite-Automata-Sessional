from automata.fa.nfa import NFA
nfa10 = NFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'1': {'q1'}},
        'q1': {'1': {'q2'}},
        'q2': {'0': {'q3'}},
        'q3': {'0': {'q4'}},
        'q4': {}
    },
    initial_state='q0',
    final_states={'q4'}
)

test_string = "11100"

if nfa10.accepts_input(test_string):
    print(f"✅ String '{test_string}' is accepted (exactly '1100')")
else:
    print(f"❌ String '{test_string}' is not accepted (not exactly '1100')")
