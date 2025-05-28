from automata.fa.dfa import DFA

dfa1 = DFA(
    states={'A', 'B', 'C'},
    input_symbols={'0', '1'},
    transitions={
        'A': {'0': 'B', '1': 'A'},
        'B': {'0': 'B', '1': 'C'},
        'C': {'0': 'B', '1': 'A'}
    },
    initial_state='A',
    final_states={'C'}
)

test_string = "10011"

if dfa1.accepts_input(test_string):
    print(f"✅ String '{test_string}' is accepted (ends with '01')")
else:
    print(f"❌ String '{test_string}' is not accepted (does not end with '01')")
