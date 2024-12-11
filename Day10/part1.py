from collections import deque
from typing import List, Set, Tuple

def parse_map(grid_str: str) -> List[List[int]]:
    """Parse the input string into a 2D grid of integers."""
    return [[int(c) for c in line.strip()] 
            for line in grid_str.strip().split('\n')]

def get_neighbors(x: int, y: int, rows: int, cols: int) -> List[Tuple[int, int]]:
    """Get valid neighboring positions (up, down, left, right)."""
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    neighbors = []
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < rows and 0 <= new_y < cols:
            neighbors.append((new_x, new_y))
    return neighbors

def find_reachable_nines(grid: List[List[int]], start_x: int, start_y: int) -> int:
    """
    Find number of height-9 positions reachable from a trailhead using valid hiking trails.
    Uses BFS to explore all possible paths that increase by exactly 1 at each step.
    """
    rows, cols = len(grid), len(grid[0])
    visited = set()  # Track visited positions with their current height
    reachable_nines = set()  # Set of reachable height-9 positions
    
    # Queue stores: (x, y, current_height)
    queue = deque([(start_x, start_y, 0)])
    visited.add((start_x, start_y, 0))
    
    while queue:
        x, y, height = queue.popleft()
        
        # If we've reached height 9, add to reachable_nines
        if grid[x][y] == 9:
            reachable_nines.add((x, y))
            continue
        
        # Check all neighboring positions
        for next_x, next_y in get_neighbors(x, y, rows, cols):
            next_height = grid[next_x][next_y]
            
            # Only follow path if it increases by exactly 1
            if next_height == height + 1:
                if (next_x, next_y, next_height) not in visited:
                    visited.add((next_x, next_y, next_height))
                    queue.append((next_x, next_y, next_height))
    
    return len(reachable_nines)

def solve_hiking_trails(input_str: str) -> int:
    """
    Find the sum of scores for all trailheads in the topographic map.
    """
    # Parse input into grid
    grid = parse_map(input_str)
    rows, cols = len(grid), len(grid[0])
    total_score = 0
    
    # Find all trailheads (positions with height 0)
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                # Calculate score for this trailhead
                score = find_reachable_nines(grid, i, j)
                total_score += score
    
    return total_score

# Test with the example from the problem
test_input = """Your Puzzle Input Here"""

result = solve_hiking_trails(test_input)
print(f"Test result: {result}")  # Should print 36