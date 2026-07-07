import atomic_dictionary

def calculate_weight(elements_with_count: dict[str, int]):
    weight = 0
    for elem in elements_with_count:
        count = elements_with_count[elem]
        weight += atomic_dictionary.weights[elem] * count
    
    return weight