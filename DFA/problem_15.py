from automata.fa.dfa import DFA
dfa15 = DFA(
    states={'A', 'B', 'C', 'D'},
    input_symbols={'0', '1'},
    transitions={
        'A': {'1': 'A', '0': 'B'},
        'B': {'1': 'C', '0': 'D'},
        'C': {'1': 'A', '0': 'B'},
        'D': {'0': 'D', '1': 'D'}
    },
    initial_state='A',
    final_states={'A'}
)

test_string = "11011011"

if dfa15.accepts_input(test_string):
    print(f"✅ String '{test_string}' is accepted (every '0' is between '1's)")
else:
    print(f"❌ String '{test_string}' is not accepted (isolated '0' detected)")
