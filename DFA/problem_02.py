from automata.fa.dfa import DFA
dfa2 = DFA(
    states={'A', 'B', 'C', 'D'},
    input_symbols={'a', 'b'},
    transitions={
        'A': {'a': 'B', 'b': 'A'},
        'B': {'a': 'B', 'b': 'C'},
        'C': {'a': 'B', 'b': 'D'},
        'D': {'a': 'B', 'b': 'C'}
    },
    initial_state='A',
    final_states={'D'}
)

test_string = "aabab"

if dfa2.accepts_input(test_string):
    print(f"✅ String '{test_string}' is accepted (ends with 'abb')")
else:
    print(f"❌ String '{test_string}' is not accepted (does not end with 'abb')")
