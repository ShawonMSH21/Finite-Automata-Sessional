from automata.fa.dfa import DFA
dfa20 = DFA(
    states={'A', 'B', 'C', 'D'},
    input_symbols={'0', '1'},
    transitions={
        'A': {'0': 'B', '1': 'A'},
        'B': {'0': 'C', '1': 'A'},
        'C': {'0': 'D', '1': 'A'},
        'D': {'0': 'D', '1': 'D'}
    },
    initial_state='A',
    final_states={'D'}
)

test_string = "1001001"

if dfa20.accepts_input(test_string):
    print(f"✅ String '{test_string}' is accepted (contains '000')")
else:
    print(f"❌ String '{test_string}' is not accepted (no '000' substring)")
