# Week 2 List Operations Solution
def main():
    # Create the initial empty container
    number_sequence = []
    
    # First, populate with base values
    number_sequence += [10, 20]
    number_sequence.extend([30, 40])

    # Now insert the middle value at precise position
    number_sequence.insert(1, 15)  # Between 10 and 20

    # Expand the collection with additional elements
    additional_numbers = [50, 60, 70]
    number_sequence = number_sequence + additional_numbers

    # Final adjustments to the sequence
    number_sequence.pop()  # Remove the terminal element
    number_sequence.sort()  # Arrange in order

    # Locate and display the target position
    target_value = 30
    position = number_sequence.index(target_value)
    
    # Output the processed results
    print(f"Final sequence after operations: {number_sequence}")
    print(f"The value {target_value} appears at index: {position}")

if __name__ == "__main__":
    main()