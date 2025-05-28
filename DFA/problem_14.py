from automata.fa.dfa import DFA
dfa14 = DFA(
    states={'A', 'B', 'C', 'D'},
    input_symbols={'0', '1'},
    transitions={
        'A': {'0': 'B', '1': 'C'},
        'B': {'0': 'D', '1': 'C'},
        'C': {'0': 'B', '1': 'D'},
        'D': {'0': 'D', '1': 'D'}
    },
    initial_state='A',
    final_states={'A', 'B', 'C'}
)

test_string = "011101"

if dfa14.accepts_input(test_string):
    print(f"✅ String '{test_string}' is accepted (no '00' or '11' substrings)")
else:
    print(f"❌ String '{test_string}' is not accepted (contains '00' or '11')")
