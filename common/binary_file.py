
def read_binary_file(inputfile: str) -> bytes:
    # Method for reading the input file.
    # It takes the input file path as input and returns the file content.
    try:
        with open(inputfile, 'rb') as input_file:
            content = input_file.read()
            return content

    except FileNotFoundError:
        raise FileNotFoundError(f"Error: Input file '{inputfile}' does not exist.")
