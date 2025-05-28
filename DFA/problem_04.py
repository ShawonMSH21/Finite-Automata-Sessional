from automata.fa.dfa import DFA
dfa4 = DFA(
    states={'A', 'B', 'C', 'D', 'E'},
    input_symbols={'0', '1'},
    transitions={
        'A': {'0': 'B', '1': 'A'},
        'B': {'0': 'C', '1': 'A'},
        'C': {'0': 'C', '1': 'D'},
        'D': {'0': 'B', '1': 'E'},
        'E': {'0': 'B', '1': 'A'}
    },
    initial_state='A',
    final_states={'E'}
)

test_string = "1100111"

if dfa4.accepts_input(test_string):
    print(f"✅ String '{test_string}' is accepted (ends with '0011')")
else:
    print(f"❌ String '{test_string}' is not accepted (does not end with '0011')")
