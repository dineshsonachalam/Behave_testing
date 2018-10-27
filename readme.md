# Behave
It uses test written in natural language style, backed up by python code.

#### Folder structure
    features/
            steps/
                steps.py
                __init__.py
            dealer.feature
            dealer_game_of_two.feature
            dealer_play_by_rule.feature
    twentyone.py
    
    
    A feature is based upon 3 parts.
    (i) given -> Were you initalize a input state.
    (ii) when -> It describes set of action performed with the given input.
    (iii) then -> It compares the output we got, with the expected output.
    
    steps.py -> Behave runs python that link descriptive test in .feature files.
    