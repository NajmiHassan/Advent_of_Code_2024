from collections import deque
from typing import List, Set, Tuple, Dict

def parse_input(input_str: str) -> List[List[int]]:
    """Parse the input string into a 2D grid of integers."""
    return [[int(c) for c in line.strip()] for line in input_str.strip().split('\n')]

def get_neighbors(x: int, y: int, rows: int, cols: int) -> List[Tuple[int, int]]:
    """Get valid neighboring positions (up, down, left, right)."""
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    return [(x + dx, y + dy) for dx, dy in directions 
            if 0 <= x + dx < rows and 0 <= y + dy < cols]

# Part 1: Finding reachable nines
def find_reachable_nines(grid: List[List[int]], start_x: int, start_y: int) -> int:
    """Find number of height-9 positions reachable from a trailhead."""
    rows, cols = len(grid), len(grid[0])
    visited = set()
    reachable_nines = set()
    queue = deque([(start_x, start_y, 0)])
    visited.add((start_x, start_y, 0))
    
    while queue:
        x, y, height = queue.popleft()
        if grid[x][y] == 9:
            reachable_nines.add((x, y))
            continue
            
        for next_x, next_y in get_neighbors(x, y, rows, cols):
            next_height = grid[next_x][next_y]
            if next_height == height + 1 and (next_x, next_y, next_height) not in visited:
                visited.add((next_x, next_y, next_height))
                queue.append((next_x, next_y, next_height))
    
    return len(reachable_nines)

# Part 2: Counting distinct trails
def count_distinct_trails(grid: List[List[int]], start_x: int, start_y: int) -> int:
    """Count number of distinct hiking trails from a trailhead."""
    rows, cols = len(grid), len(grid[0])
    memo: Dict[Tuple[int, int, int], int] = {}
    
    def dfs(x: int, y: int, height: int) -> int:
        state = (x, y, height)
        if state in memo:
            return memo[state]
        
        if grid[x][y] == 9:
            return 1
        
        trails = 0
        for next_x, next_y in get_neighbors(x, y, rows, cols):
            next_height = grid[next_x][next_y]
            if next_height == height + 1:
                trails += dfs(next_x, next_y, next_height)
        
        memo[state] = trails
        return trails
    
    return dfs(start_x, start_y, 0)

def solve_both_parts(grid: List[List[int]]) -> Tuple[int, int]:
    """Solve both parts of the puzzle for the given grid."""
    rows, cols = len(grid), len(grid[0])
    part1_total = 0
    part2_total = 0
    
    # Find all trailheads (positions with height 0)
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                # Part 1: Count reachable nines
                score = find_reachable_nines(grid, i, j)
                part1_total += score
                
                # Part 2: Count distinct trails
                rating = count_distinct_trails(grid, i, j)
                part2_total += rating
    
    return part1_total, part2_total

# Read and process your input
input_str = """Your Puzzle Input Here"""

# Parse and solve
grid = parse_input(input_str)
part1_result, part2_result = solve_both_parts(grid)

print(f"Part 1 Result: {part1_result}")
print(f"Part 2 Result: {part2_result}")