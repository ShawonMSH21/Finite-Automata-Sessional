from automata.fa.dfa import DFA
dfa17 = DFA(
    states={'A', 'B', 'C', 'D'},
    input_symbols={'0', '1'},
    transitions={
        'A': {'0': 'B', '1': 'C'},
        'B': {'0': 'B', '1': 'D'},
        'C': {'0': 'D', '1': 'C'},
        'D': {'0': 'D', '1': 'D'}
    },
    initial_state='A',
    final_states={'D'}
)

test_string = "1111"

if dfa17.accepts_input(test_string):
    print(f"✅ String '{test_string}' is accepted (contains '01' or '10')")
else:
    print(f"❌ String '{test_string}' is not accepted (no '01' or '10' found)")
