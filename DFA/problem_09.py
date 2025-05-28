from automata.fa.dfa import DFA
dfa9 = DFA(
    states={'A', 'B', 'C', 'D', 'E'},
    input_symbols={'a', 'b'},
    transitions={
        'A': {'a': 'B', 'b': 'C'},
        'B': {'a': 'D', 'b': 'E'},
        'C': {'a': 'E', 'b': 'D'},
        'D': {'a': 'D', 'b': 'D'},
        'E': {'a': 'E', 'b': 'E'}
    },
    initial_state='A',
    final_states={'D'}
)

test_string = "abbb"

if dfa9.accepts_input(test_string):
    print(f"✅ String '{test_string}' is accepted (starts with 'aa' or 'bb')")
else:
    print(f"❌ String '{test_string}' is not accepted")
