from automata.fa.nfa import NFA
nfa5 = NFA(
    states={'q0', 'q1', 'q2', 'q3'},
    input_symbols={'a', 'b', 'c'},
    transitions={
        'q0': {'a': {'q0', 'q1'}},
        'q1': {'b': {'q1', 'q2'}},
        'q2': {'c': {'q2', 'q3'}},
        'q3': {}
    },
    initial_state='q0',
    final_states={'q3'}
)

test_string = "ababbcc"

if nfa5.accepts_input(test_string):
    print(f"✅ String '{test_string}' is accepted (form a⁺b⁺c⁺)")
else:
    print(f"❌ String '{test_string}' is not accepted (not in form a⁺b⁺c⁺)")
