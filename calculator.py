

def calculate_weight(elements_with_count: dict[str, int]):
    for elem in elements_with_count:
        count = elements_with_count[elem]
        print(elem, count)

if __name__ == "__main__":
    test_elements = {
        "H": 2,
        "O": 4
    }

    calculate_weight(test_elements)