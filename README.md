# Manager-Worker Architecture

This repository implements a robust Manager-Worker architecture in Python, designed to handle background tasks efficiently. It separates the job management logic from the job processing logic, allowing for scalability and easy maintenance.

## Overview

The system consists of a **Manager** that orchestrates multiple **Workers**. The Manager is responsible for fetching jobs from a data source (e.g., a database) and assigning them to available Workers. Workers process these jobs and report the results back to the Manager, which then updates the data source.

## Components

### 1. Manager (`manager.py`)
The `Manager` class is the central controller. It:
- Initializes and manages a pool of worker threads.
- Acts as an intermediary between the workers and the data source.
- Provides methods for workers to request jobs (`getJob`) and submit results (`submitJob`).
- Ensures thread safety using locks when accessing shared resources.

### 2. Worker (`worker.py`)
The `Worker` class represents a worker thread. It:
- Inherits from a custom `Thread` class.
- Continuously polls the Manager for new jobs.
- Processes assigned jobs (e.g., AI/ML tasks, data processing).
- Handles success and failure scenarios by submitting results back to the Manager.

### 3. Database Operations (`database.py`)
The `DBOperations` class abstracts the data access layer. It provides methods to:
- `get_job_for_worker()`: Fetch unprocessed jobs.
- `submit_job_result()`: Save successful job results.
- `submit_job_for_failure()`: Handle and log failed jobs.

### 4. Thread Wrapper (`Thread.py`)
A custom wrapper around Python's `threading.Thread` class. It provides enhanced control over thread execution, including:
- Methods to check if the thread is running (`isRunning`).
- Mechanisms to pause and resume threads (`wait`, `notify`).
- A clean way to stop threads (`stop`).

## How It Works

1.  **Initialization**: The `Manager` starts and initializes the defined number of `Worker` threads.
2.  **Job Request**: A `Worker` requests a job from the `Manager`.
3.  **Job Assignment**: The `Manager` fetches a pending job from the `DBOperations` layer and assigns it to the `Worker`.
4.  **Processing**: The `Worker` processes the job (e.g., runs an algorithm).
5.  **Completion**: The `Worker` submits the result (success or failure) back to the `Manager`.
6.  **Update**: The `Manager` updates the job status in the `DBOperations` layer.

## Usage

To start the system, run the `manager.py` file:

```bash
python manager.py
```

This will initialize the Manager and start the Worker threads, which will begin polling for jobs.

## Extensibility

-   **Adding New Workers**: You can define new worker types and their counts in the `Worker_detail_dict` within `manager.py`.
-   **Custom Logic**: Implement specific job processing logic inside the `run` method of `worker.py`.
-   **Data Source**: Modify `database.py` to connect to your specific database or API.