import calculator

def parse_formula(formula: str):
    elements = {

    }
    active = False
    current_elem = ""
    for c in formula:
        if c.isdigit() and active:
            elements[current_elem] = int(c)
            active = False
            current_elem = ""
            continue
        
        if c.isupper():
            if active:
                elements[c] = 1
                current_elem = ""
            else:
                current_elem += c
                active = True
            continue
        
        current_elem += c
    
    if active:
        elements[current_elem] = 1
    
    return elements


if __name__ == "__main__":
    test_formula = "H2O3Fe3"
    test_elements = parse_formula(test_formula)

    w = calculator.calculate_weight(test_elements)
    
    print(test_elements)
    print(f"%.3fg" % w)