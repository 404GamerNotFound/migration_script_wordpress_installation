import tarfile

def extract_tbz(file_path, extract_to='.'):
    """
    Extract a .tbz file.
    
    :param file_path: Path to the .tbz file
    :param extract_to: Directory to extract the files into
    """
    # Open the .tbz file
    with tarfile.open(file_path, 'r:bz2') as tar:
        # Extract all the contents of the tar file into the directory
        tar.extractall(path=extract_to)
        print(f'Extracted {file_path} to {extract_to}')

# Usage
file_path = 'wp-dump.tbz'
extract_tbz(file_path)
