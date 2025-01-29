from pathlib import Path
import logging
from datetime import datetime
import argparse

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def create_test_files(num_files):
    # Setup tmp directory
    tmp = Path.cwd() / 'tmp'
    if not tmp.exists():
        logging.info("'tmp' directory not found - creating new directory")
        tmp.mkdir()
        logging.info("Created 'tmp' directory at: %s", tmp)
    else:
        logging.info("Using existing 'tmp' directory at: %s", tmp)

    # Generate timestamp for unique filenames
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

    # Create test files with timestamp
    created_files = []
    for i in range(num_files):
        filename = f'test{i}_{timestamp}.txt'
        file_path = tmp / filename
        file_path.write_text(f'test file {i}')
        created_files.append(filename)

    logging.info("Created %d new test files:", len(created_files))
    for filename in created_files:
        logging.info("- %s", filename)

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Create test files in tmp directory')
    parser.add_argument('num_files', type=int, nargs='?', default=10, 
                       help='Number of test files to create (default: 10)')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Create files
    create_test_files(args.num_files)

if __name__ == "__main__":
    main()