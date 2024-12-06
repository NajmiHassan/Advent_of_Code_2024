from collections import defaultdict, deque

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

def reorder_update(update, rules):
    # Build a graph and calculate in-degrees based on the rules
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    # Only consider pages present in the current update
    pages_in_update = set(update)
    
    for x, y in rules:
        if x in pages_in_update and y in pages_in_update:
            graph[x].append(y)
            in_degree[y] += 1
            if x not in in_degree:
                in_degree[x] = 0
    
    # Perform topological sort using Kahn's algorithm
    queue = deque([node for node in pages_in_update if in_degree[node] == 0])
    sorted_order = []
    
    while queue:
        current = queue.popleft()
        sorted_order.append(current)
        
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_order

def solve(input_data):
    # Parse input data
    rules, updates = parse_input(input_data)
    
    # Process each update to identify invalid ones and reorder them
    reordered_updates = []
    
    for update in updates:
        if not is_update_valid(update, rules):
            reordered_updates.append(reorder_update(update, rules))
    
    # Find middle pages of reordered updates and calculate their sum
    middle_pages_sum = sum(find_middle_page(update) for update in reordered_updates)
    
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
82|99
82|62
82|91
82|49
65|73
65|86
65|59
65|69
65|37
65|11

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
54,93,71,29,67,81,82,35,18,85,17,91,62,36,57,65,76,86,14,72,26
93,85,67,57,36,72,35,65,45,18,76,24,86,82,94,29,54,14,17,62,71
13,78,77,31,69,87,66,21,11,16,73,46,58,15,39,97,94,24,54,71,29
53,75,31,49,73,14,77,11,21,26,76,72,86,87,46,13,16,78,69,37,12,99,66
87,66,11,16,75,46,58,95,15,97,94,24,54,93,29,67,82,35,18""" #You Puzzle Input

# Solve the problem and print the result for Part Two
result = solve(input_data)
print("Sum of middle pages after reordering:", result)