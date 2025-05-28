from automata.fa.dfa import DFA
dfa5 = DFA(
    states={'A', 'B', 'C', 'D'},
    input_symbols={'a', 'b'},
    transitions={
        'A': {'a': 'B', 'b': 'D'},
        'B': {'a': 'C', 'b': 'C'},
        'C': {'a': 'C', 'b': 'C'},
        'D': {'a': 'D', 'b': 'D'}
    },
    initial_state='A',
    final_states={'C'}
)

test_string = "babbab"

if dfa5.accepts_input(test_string):
    print(f"✅ String '{test_string}' is accepted (starts with 'ab')")
else:
    print(f"❌ String '{test_string}' is not accepted (does not start with 'ab')")
