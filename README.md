# QA Engineer Homework

## Part 1: Test Plan

Test plan is in the file named "test_plan.md" which has 15 testcases + 5 edge cases to validate the features of an action camera. It includes detailed procedure and pass/fail criteria.

## Part 2: Practical Implementation

- **Option B**: Background file management script implemented in Python.

### Prerequisites

1. Ensure you have **Python 3.x** installed on your machine.
2. Install any required libraries (if applicable). (Both scripts rely on built-in Python modules on MacOS, so no additional installation is necessary.)

### Running the Scripts

1. Clone the repository:
   ```bash
   git clone https://github.com/addankigouthami/QA-SmartfrogAndCanary.git
   ```
2. Navigate to the project directory:
   ```bash
   cd QA-SmartfrogAndCanary
   ```

#### Background Archiver Script

To monitor the `tmp` folder and automatically archive files when it contains 10 or more:

from the root dir of the project,

```bash
python3 background_archiver.py
```

#### File Creation Script

If you would like to create files automatically for testing the archiver, run the following from the root directory of the project in a **new terminal window**:

```bash
python3 archiver.py
```

### Notes

- Ensure the `tmp` folder is in the same directory as the scripts. If it doesn't exist, the `background_archiver.py` script will create it automatically.
- The `background_archiver.py` script will monitor the folder continuously until 10 files are archived and removed.
- The `archiver.py` script simulates file creation by continuously adding files to the `tmp` folder for testing purposes.

### Repository Structure

```
QA-SmartfrogAndCanary/
|
├── background_archiver.py  # Script for monitoring and archiving files
├── archiver.py             # Script to create test files in the tmp folder
├── tmp/                    # Folder where files are monitored (auto-created by scripts)
├── README.md               # Instructions on running the scripts
├── test_plan.md            # Test cases part 1 of the task
```
