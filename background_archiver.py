import os
import time
import tarfile
import logging
from pathlib import Path
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

class TempFolderManager:
    """Context manager for handling temporary folder operations"""
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.is_valid = False

    def __enter__(self):
        self.ensure_folder()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is FileNotFoundError:
            logging.warning("Directory was deleted, attempting to recover")
            self.ensure_folder()
            return True  # Suppress the exception
        return False

    def ensure_folder(self):
        """Create tmp folder and make it persistent"""
        self.folder_path.mkdir(exist_ok=True)
        self.is_valid = True
        logging.info("tmp doesn't exist. creating... : %s", self.folder_path)

    def count_files(self):
        """Count number of files in the folder with error handling"""
        if not self.is_valid:
            self.ensure_folder()
        try:
            return sum(1 for item in self.folder_path.iterdir() if item.is_file())
        except FileNotFoundError:
            self.is_valid = False
            return 0

    def get_files(self):
        """Get list of files in the folder"""
        if not self.is_valid:
            self.ensure_folder()
        try:
            return [f.name for f in self.folder_path.iterdir() if f.is_file()]
        except FileNotFoundError:
            self.is_valid = False
            return []

def create_archive(folder_path, files_to_archive):
    """Create tar.gz archive with timestamp in name"""
    # Generate timestamp for archive name
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    archive_name = f'files_{timestamp}.tar.gz'
    archive_path = Path.cwd() / archive_name
    
    try:
        with tarfile.open(archive_path, 'w:gz') as tar:
            for file_name in files_to_archive:
                file_path = folder_path / file_name
                if file_path.exists():
                    tar.add(file_path, arcname=file_name)
        
        logging.info("Created archive: %s", archive_name)
        for file_name in files_to_archive:
            logging.info(file_name)
            
    except Exception as e:
        logging.error(f"Failed to create archive: {e}")
        return False
        
    return archive_name

def remove_files(folder_path, files_to_remove, archive_name):
    """Remove archived files from the folder"""
    for file_name in files_to_remove:
        try:
            file_path = folder_path / file_name
            if file_path.exists():
                file_path.unlink()
        except Exception as e:
            logging.error(f"Failed to remove file {file_name}: {e}")
    logging.info(f"Removed archived files from tmp folder - archived in: {archive_name}")

def main():
    REQUIRED_FILES = 10
    tmp_folder = Path.cwd() / 'tmp'
    
    with TempFolderManager(tmp_folder) as folder_mgr:
        while True:
            try:
                #count files in tmp
                num_files = folder_mgr.count_files()
                
                #only proceed if we have exactly 10 files
                if num_files >= REQUIRED_FILES:
                    # Get list of all files
                    all_files = folder_mgr.get_files()
                    
                    #wait for 10 files and create archive with 10 files
                    files_to_archive = all_files[:REQUIRED_FILES]
                    
                    #create archive
                    archive_name = create_archive(tmp_folder, files_to_archive)
                    if archive_name:
                        #only delete files from tmp if archive was created successfully
                        remove_files(tmp_folder, files_to_archive, archive_name)
                        logging.info("Archived the following files:")
                        for file_name in files_to_archive:
                            logging.info(f"  - {file_name}")
                        logging.info("Files collected")
                
            except Exception as e:
                logging.error(f"An error occurred in main loop: {e}")
                time.sleep(5)  # Wait longer on error before retrying
                continue
                
            #wait time before next check and archive
            time.sleep(1)

if __name__ == "__main__":
    main()