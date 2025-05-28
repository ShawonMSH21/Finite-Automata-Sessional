from automata.fa.dfa import DFA
dfa13 = DFA(
    states={'S0', 'S1', 'S2'},
    input_symbols={'0', '1'},
    transitions={
        'S0': {'0': 'S1', '1': 'S0'},
        'S1': {'0': 'S2', '1': 'S1'},
        'S2': {'0': 'S2', '1': 'S2'}
    },
    initial_state='S0',
    final_states={'S2'}
)

test_string = "1101"

if dfa13.accepts_input(test_string):
    print(f"✅ String '{test_string}' is accepted (at least two '0's)")
else:
    print(f"❌ String '{test_string}' is not accepted (fewer than two '0's)")
