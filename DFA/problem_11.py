from automata.fa.dfa import DFA
dfa11 = DFA(
    states={'S0', 'S1', 'S2', 'S3'},
    input_symbols={'0', '1'},
    transitions={
        'S0': {'0': 'S1', '1': 'S0'},
        'S1': {'0': 'S2', '1': 'S1'},
        'S2': {'0': 'S3', '1': 'S2'},
        'S3': {'0': 'S3', '1': 'S3'}
    },
    initial_state='S0',
    final_states={'S2'}
)

test_string = "010101"

if dfa11.accepts_input(test_string):
    print(f"✅ String '{test_string}' is accepted (contains exactly two '0's)")
else:
    print(f"❌ String '{test_string}' is not accepted (not exactly two '0's)")
