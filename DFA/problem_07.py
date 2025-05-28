from automata.fa.dfa import DFA
dfa7 = DFA(
    states={'A', 'B', 'C', 'D', 'E'},
    input_symbols={'0', '1'},
    transitions={
        'A': {'1': 'B', '0': 'E'},
        'B': {'0': 'C', '1': 'E'},
        'C': {'1': 'D', '0': 'E'},
        'D': {'0': 'D', '1': 'D'},
        'E': {'0': 'E', '1': 'E'}
    },
    initial_state='A',
    final_states={'D'}
)

test_string = "110110"

if dfa7.accepts_input(test_string):
    print(f"✅ String '{test_string}' is accepted (starts with '101')")
else:
    print(f"❌ String '{test_string}' is not accepted (does not start with '101')")
