import calculator

def parse_formula(formula: str):
    elements = {

    }
    current_elem = ""
    current_count = ""

    for c in formula:
        if c.isdigit():
            current_count += c
            continue
        
        if c.isupper():
            if current_elem:
                if not current_count:
                    current_count = "1"
                
                elements[current_elem] = int(current_count)
                
            current_elem = c
            current_count = ""
            continue
    
        current_elem += c
    
    if current_elem:
        if not current_count:
            current_count = "1"
        elements[current_elem] = int(current_count)
    
    return elements


if __name__ == "__main__":
    test_formula = "Fe13HO5"
    test_elements = parse_formula(test_formula)

    print(test_elements)

    w = calculator.calculate_weight(test_elements)
    
    print(f"%.3fg" % w)