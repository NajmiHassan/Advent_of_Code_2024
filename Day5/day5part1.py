def parse_input(input_data):
    # Split input into rules and updates
    rules_section, updates_section = input_data.strip().split("\n\n")
    
    # Parse ordering rules
    rules = []
    for rule in rules_section.splitlines():
        x, y = map(int, rule.split('|'))
        rules.append((x, y))
    
    # Parse updates
    updates = []
    for update in updates_section.splitlines():
        updates.append(list(map(int, update.split(','))))
    
    return rules, updates

def is_update_valid(update, rules):
    # Create a dictionary to store the index of each page in the update
    page_index = {page: i for i, page in enumerate(update)}
    
    # Check all rules that apply to this update
    for x, y in rules:
        if x in page_index and y in page_index:
            if page_index[x] >= page_index[y]:
                return False  # Rule is violated
    return True

def find_middle_page(update):
    # Find the middle page number
    n = len(update)
    return update[n // 2]

def solve(input_data):
    # Parse input data
    rules, updates = parse_input(input_data)
    
    # Process each update and check if it's valid
    valid_updates = []
    for update in updates:
        if is_update_valid(update, rules):
            valid_updates.append(update)
    
    # Find middle pages of valid updates and calculate their sum
    middle_pages_sum = sum(find_middle_page(update) for update in valid_updates)
    
    return middle_pages_sum

# Example input (replace this with your actual puzzle input)
input_data = """99|31
26|21
26|69
69|35
69|75
69|95
59|58
59|73
59|87
59|94
82|72


75,94,71,16,31,95,11,73,97,77,81
17,91,62,86,14,26,12,99,37,59,49,13,77
62,36,12,37,49,78,77,31,87,21,11
59,13,31,16,75,58,95,15,39,24,54
95,15,39,97,94,24,54,93,67,81,82,35,18,45,85,17,91,27,62,36,65
36,53,67,14,62,26,99,35,81,65,29,82,76,17,57,27,37,18,72,86,91
46,15,39,71,81,82,35,45,85,91,36
16,91,15,29,46,17,67
49,77,31,46,53,58,73,95,75,78,99,21,15,13,59
73,46,95,15,97,54,71,81,45,85,62
14,72,26,12,99,59,49,78,77,31,69,87,21,11,16,75,95
54,93,71,29,67,81,82,35,18,85,17,91,62,36,57,65,76,86,14,72,26"""  #You Puzzle Input

# Solve the problem and print the result
result = solve(input_data)
print("Sum of middle pages:", result)