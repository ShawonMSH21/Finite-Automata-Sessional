from automata.fa.dfa import DFA
dfa3 = DFA(
    states={'A', 'B', 'C', 'D', 'E'},
    input_symbols={'a', 'b'},
    transitions={
        'A': {'a': 'B', 'b': 'A'},
        'B': {'a': 'B', 'b': 'C'},
        'C': {'a': 'B', 'b': 'D'},
        'D': {'a': 'E', 'b': 'C'},
        'E': {'a': 'B', 'b': 'C'}
    },
    initial_state='A',
    final_states={'E'}
)

test_string = "aabbab"

if dfa3.accepts_input(test_string):
    print(f"✅ String '{test_string}' is accepted (ends with 'abba')")
else:
    print(f"❌ String '{test_string}' is not accepted (does not end with 'abba')")
