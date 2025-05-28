from automata.fa.dfa import DFA
dfa6 = DFA(
    states={'A', 'B', 'C'},
    input_symbols={'a', 'b'},
    transitions={
        'A': {'a': 'B', 'b': 'C'},
        'B': {'a': 'B', 'b': 'B'},
        'C': {'a': 'C', 'b': 'C'}
    },
    initial_state='A',
    final_states={'B'}
)

test_string = "bababa"

if dfa6.accepts_input(test_string):
    print(f"✅ String '{test_string}' is accepted (starts with 'a')")
else:
    print(f"❌ String '{test_string}' is not accepted (does not start with 'a')")
