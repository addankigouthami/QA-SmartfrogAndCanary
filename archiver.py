"""Run this file to create 10 text files in tmp folder for testing"""
from pathlib import Path
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

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
for i in range(10):
    filename = f'test{i}_{timestamp}.txt'
    file_path = tmp / filename
    file_path.write_text(f'test file {i}')
    created_files.append(filename)

logging.info("Created %d new test files:", len(created_files))
for filename in created_files:
    logging.info("- %s", filename)