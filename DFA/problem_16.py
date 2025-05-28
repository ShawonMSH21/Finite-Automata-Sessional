from automata.fa.dfa import DFA

dfa16 = DFA(
    states={'A', 'B', 'C', 'D', 'E'},
    input_symbols={'0', '1'},
    transitions={
        'A': {'0': 'B', '1': 'C'},
        'B': {'0': 'B', '1': 'D'},
        'C': {'0': 'E', '1': 'C'},
        'D': {'0': 'B', '1': 'C'},
        'E': {'0': 'B', '1': 'C'}
    },
    initial_state='A',
    final_states={'D', 'E'}
)

test_string = "11010"

if dfa16.accepts_input(test_string):
    print(f"✅ String '{test_string}' is accepted (ends with '01' or '10')")
else:
    print(f"❌ String '{test_string}' is not accepted (does not end with '01' or '10')")
