# Part 1: Test Plan

Test plan is in the file named "test_plan.md" which has 15 testcases + 5 edge cases to validate the features of an action camera. It includes detailed procedure and pass/fail criteria.

# Part 2: Practical Implementation

- **Option B**: Background file management script implemented in Python.

## Prerequisites

1\. Ensure you have **Python 3.x** installed on your machine.

2\. Archiver script and test script to generate files only use in built Python modules, so no additional installation of dependencies is necessary

## Running the Scripts

1\. Clone the repository:

```bash

git clone https://github.com/addankigouthami/QA-SmartfrogAndCanary.git

```

2\. go to the project directory:

```bash

cd QA-SmartfrogAndCanary

```

## Background Archiver Script

To monitor the `tmp` folder and automatically archive files when it reaches 10 and exit after all the files are archived in tmp:

from the root dir of the project,

```bash

python3 background_archiver.py

```

if there are more than 10 files, the files will be created in batches with time stamp so the zip is not replaced and all the files are retained.

To monitor the `tmp` folder and automatically archive files when files number reaches 10 and for the process to keep running in the backgrounnd even if the terminal is closed.

```bash

python3 background_archiver.py &

```

The logs of the files archived and the message "files collected" for every run will be logged in console after the archive is generated.

## Tests

### File Creation Script

To create files automatically for testing the archiver, run the following from the root directory of the project in a **new terminal window**:

```bash

python3 archiver.py

```

To create a specific number of files for tests

```bash

python3 archiver.py <number of files to be created>

```

## Notes

- `tmp` dir should also be in the root dir. If it doesn't exist, the `background_archiver.py` script will create it automatically when run.

- running the archiver in the background will monitor the folder continuously until 10 files are archived and the files will be removed from `tmp` and archived to `files_YYYYMMDD_HHMMSS.tar.gz`

- The `archiver.py` creates files by continuously adding N files specified during the run in the cli to the `tmp` folder for testing purposes. Defaulted to 10.

- If the script is run in the background, you have to do a kill -9 <PID of background_archiver.py> to kill the process

## Repository Structure

```

QA-SmartfrogAndCanary/

|

├── background_archiver.py  # Script for monitoring and archiving files

├── archiver.py            # Script to create test files in the tmp folder

├── tmp/                   # dir where files are monitored (auto-created by scripts)

├── README.md              # Instructions on running the scripts

└── test_plan.md          # Test cases part 1 of the task

```
