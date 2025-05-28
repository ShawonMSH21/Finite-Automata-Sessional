from automata.fa.dfa import DFA
dfa10 = DFA(
    states={'A', 'B', 'C', 'D'},
    input_symbols={'0', '1'},
    transitions={
        'A': {'0': 'B', '1': 'A'},
        'B': {'0': 'B', '1': 'C'},
        'C': {'0': 'B', '1': 'D'},
        'D': {'0': 'D', '1': 'D'}
    },
    initial_state='A',
    final_states={'D'}
)

test_string = "1001010"

if dfa10.accepts_input(test_string):
    print(f"✅ String '{test_string}' is accepted (contains '011')")
else:
    print(f"❌ String '{test_string}' is not accepted (no '011' substring)")
