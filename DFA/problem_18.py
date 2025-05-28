from automata.fa.dfa import DFA
dfa18 = DFA(
    states={'A', 'B'},
    input_symbols={'0', '1'},
    transitions={
        'A': {'0': 'A', '1': 'B'},
        'B': {'0': 'B', '1': 'B'}
    },
    initial_state='A',
    final_states={'A'}
)

test_string = "00100"

if dfa18.accepts_input(test_string):
    print(f"✅ String '{test_string}' is accepted (contains only '0')")
else:
    print(f"❌ String '{test_string}' is not accepted (contains '1')")
