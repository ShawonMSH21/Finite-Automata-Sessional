from automata.fa.dfa import DFA
dfa8 = DFA(
    states={'A', 'B', 'C', 'D'},
    input_symbols={'0', '1'},
    transitions={
        'A': {'0': 'B', '1': 'D'},
        'B': {'0': 'C', '1': 'D'},
        'C': {'0': 'C', '1': 'C'},
        'D': {'0': 'D', '1': 'D'}
    },
    initial_state='A',
    final_states={'C'}
)

test_string = "100110"

if dfa8.accepts_input(test_string):
    print(f"✅ String '{test_string}' is accepted (starts with '00')")
else:
    print(f"❌ String '{test_string}' is not accepted (does not start with '00')")
