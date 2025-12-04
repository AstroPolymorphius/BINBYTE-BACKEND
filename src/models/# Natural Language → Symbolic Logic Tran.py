# Natural Language → Symbolic Logic Translator
# Supports: AND, OR, IF...THEN, & NOT

symbol_table = {}          # Maps English propositions → letters
symbol_counter = 0         # Next unused letter index (P, Q, R, ...)


def normalize(text):
    text = text.lower().strip()
    while "  " in text:
        text = text.replace("  ", " ")
    return text

#Add the propositions along with their variable letters to the dictionnary
def assign_symbol(proposition):
    """
    Assigns a letter to each UNIQUE atomic proposition.
    Returns the symbol letter.
    """
    global symbol_counter

    #Checks if the proposition is already stored in the dictionary
    if proposition not in symbol_table:
        #Makes the variable letters start from p onwards
        symbol_table[proposition] = chr(ord('p') + symbol_counter)
        symbol_counter += 1

    return symbol_table[proposition]


def contains_embedded_not(sentence):
    return " not " in sentence


# Recursive translator
def translate(sentence):
    sentence = normalize(sentence)
    
    # IF ... THEN (supports comma form too)
    if "if" in sentence and ("then" in sentence or "," in sentence):

        if "then" in sentence:
            before_then = sentence.split("then", 1)[0]
            antecedent_text = before_then.split("if", 1)[1].strip()
            consequent_text = sentence.split("then", 1)[1].strip()

        else:  # using comma syntax
            before_comma = sentence.split(",", 1)[0]
            antecedent_text = before_comma.split("if", 1)[1].strip()
            consequent_text = sentence.split(",", 1)[1].strip()

        left = translate(antecedent_text)
        right = translate(consequent_text)

        return f"({left} → {right})"

    # logic for detecting and handling conjunctions (AND) in the sentence
    if " and " in sentence:
        parts = [p.strip() for p in sentence.split(" and ")]
        translated = [translate(p) for p in parts]
        return "(" + " ∧ ".join(translated) + ")"

    # logic for detecting and handling disjunctions (OR) in the sentence
    if " or " in sentence:
        parts = [p.strip() for p in sentence.split(" or ")]
        translated = [translate(p) for p in parts]
        return "(" + " ∨ ".join(translated) + ")"

    # logic for detecting and handling negation (NOT) in the sentence
    if contains_embedded_not(sentence):
        positive_form = sentence.replace(" not ", " ", 1)
        symbol = assign_symbol(positive_form)
        return f"¬{symbol}"

    # Atomic proposition
    return assign_symbol(sentence)


# Program loop
if __name__ == "__main__":
    while True:
        symbol_table.clear()
        symbol_counter = 0

        user_input = input("\nEnter an English statement (or 'quit'): ")
        if user_input.lower() == "quit":
            break

        symbolic = translate(user_input)
        print("\nSymbolic form:", symbolic)

        print("\nLegend:")
        for proposition, symbol in symbol_table.items():
            print(f"{symbol} = {proposition}")