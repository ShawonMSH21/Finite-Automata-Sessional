from automata.fa.dfa import DFA
dfa19 = DFA(
    states={'A'},
    input_symbols={'0', '1'},
    transitions={
        'A': {'0': 'A', '1': 'A'}
    },
    initial_state='A',
    final_states={'A'}
)

test_string = "0110102"

if dfa19.accepts_input(test_string):
    print(f"✅ String '{test_string}' is accepted (contains only '0' and '1')")
else:
    print(f"❌ String '{test_string}' is not accepted (contains other symbols)")
