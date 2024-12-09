def parse_disk_map(disk_map):
    """Convert disk map string into list of files and spaces"""
    result = []
    is_file = True  # Alternates between file and space
    for char in disk_map:
        length = int(char)
        result.append((length, is_file))
        is_file = not is_file
    return result

def create_block_representation(parsed_map):
    """Create a list where each element represents one block on disk"""
    blocks = []
    file_id = 0
    
    for length, is_file in parsed_map:
        if is_file:
            blocks.extend([file_id] * length)
            file_id += 1
        else:
            blocks.extend(['.'] * length)
    
    return blocks

def compact_disk(blocks):
    """Move files from right to left to fill gaps"""
    length = len(blocks)
    result = blocks.copy()
    
    # Keep track of the rightmost file we've moved
    rightmost_file_pos = length - 1
    
    # Find and fill each gap from left to right
    for i in range(length):
        if result[i] == '.':  # Found a gap
            # Find the rightmost file that hasn't been moved yet
            while rightmost_file_pos > i and (result[rightmost_file_pos] == '.' or result[rightmost_file_pos] == 'x'):
                rightmost_file_pos -= 1
                
            if rightmost_file_pos <= i:
                break
                
            # Move the file block
            result[i] = result[rightmost_file_pos]
            result[rightmost_file_pos] = 'x'  # Mark as moved
    
    # Clean up the 'x' markers
    return [x if x != 'x' else '.' for x in result]

def calculate_checksum(blocks):
    """Calculate checksum by multiplying position by file ID"""
    checksum = 0
    for pos, block in enumerate(blocks):
        if block != '.':
            checksum += pos * block
    return checksum

def solve_disk_fragmenter(disk_map):
    """Main function to solve the puzzle"""
    # Parse the input
    parsed_map = parse_disk_map(disk_map)
    
    # Create initial block representation
    blocks = create_block_representation(parsed_map)
    
    # Compact the disk
    compacted_blocks = compact_disk(blocks)
    
    # Calculate and return checksum
    return calculate_checksum(compacted_blocks)

# Read input from file
def read_input_file(filename):
    with open(filename, 'r') as file:
        return file.read().strip()

# Main execution
if __name__ == "__main__":
    # Read the input file
    input_data = read_input_file('C:/Users/786/Advent of Code/input.txt')
    
    # Solve the puzzle
    result = solve_disk_fragmenter(input_data)
    print(f"Filesystem checksum: {result}")