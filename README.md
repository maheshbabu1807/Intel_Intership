# Intel_Intership
# Innovators
![logo](https://github.com/user-attachments/assets/956be19e-4190-4ada-bc17-83a3d5d660a5)

# Power Manager Telemetry
# Project Overview
Power Manager Telemetry is a project aimed at monitoring and optimizing power consumption in modern computing environments, especially in the context of 5G and edge computing deployments. This project focuses on collecting telemetry data from various system components, simulating load using Docker, and analyzing the data to provide insights into system power utilization.
# Table of Contents
 - [Features](#Features) 
 - [Technologies_Used](#Technologies_Used)
 - [Installation](#Installation)
 - [Usage](#Usage)
 - [Contributing](#Contributing)
 - [Team_Members_and_Contributions](#Team_Members_and_Contributions)
 - [Architecture_Diagram](#Architecture_Diagram)
 - [Conclusion](#Conclusion)
 - [File_Structure](#File_Structure)
# Features
. Collection of telemetry data from CPU, memory, NIC, and TDP.

. Load simulation using Docker to generate controlled CPU loads.

. Analysis of telemetry data to calculate key metrics and generate insightful reports. 

. Detailed project documentation and user guides.

# Technologies_Used 
## 1. Programming Languages:
. Python (with libraries such as psutil, json, threading, subprocess) 
## 2. Containerization:
. Docker (for creating and managing containers) 
## 3. Data:
. CSV, JSON (for structured data storage) 
## 4. Operating Systems:
. Linux (preferred for telemetry data collection and Docker operations) - Windows (supported with necessary adjustments) 
## 5. Documentation:
. Markdown (for project documentation)

# Installation
## Prerequisites
Python 3.8 or higher: You can download Python from the official Python website.

Docker Desktop: Docker is required for running the load simulation. You can download Docker from the official Docker website.

Git: Git is used for version control and cloning the repository. You can download Git from the official Git website.
## Steps
1. Clone the repository:
```sh
git clone https://github.com/deekshi173/Innovators.git
cd power_manager_telemetry
```
## Install Python dependencies:
```sh
pip install psutil
```
## Build the Docker image:
```sh
docker build -t load_simulator .
```
# Usage
## Running Telemetry Data Collection
1. Run the telemetry data collection script:
```sh
python telemetry_data.py
```
2. Run the measure system power utilization script:
```sh
python measure_system_power_utilization.py
```
The telemetry data will be logged into a CSV file.

## Running Load Simulation
3. Run the Docker container to simulate load:
```sh
docker build -t load_simulator .
```

# Generating Reports

## Run the report generation script:
```sh
python generate_report.py
```
The report will be generated in report.txt.

# Contributing
Contributions are welcome! Please follow these steps to contribute:
1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes.
4. Commit your changes (git commit -m 'Add new feature').
5. Push to the branch (git push origin feature-branch).
6. Create a new Pull Request.
   
# Team Members and Contributions
## Y. Deekshitha
Project planning, data analysis algorithms, report generation script.
## V. Mahesh Babu
Telemetry data collection script, multi-threading implementation, system architecture.
## Vidyashree K J 
Dockerfile creation, load simulation script, Docker environment management.
##  B. Mohith
Project documentation, user guides, frontend interface for scripts.
## T. Jayavardhan Reddy
Testing, bug fixing, validation of telemetry data and reports.

# Process flow:
![process flow](https://github.com/user-attachments/assets/63d4d1ab-7b83-4311-9730-fd512392e37a)


# Architecture Diagram
![Power manager architecture (1)](https://github.com/user-attachments/assets/668a0216-d4eb-4ba8-8d50-965375038338)

# Result
![report (2)](https://github.com/user-attachments/assets/9339b502-636a-4e16-bdd8-b5e16fdc3071)
![Result 1 (1)](https://github.com/user-attachments/assets/44e75153-dd2a-410b-979d-02f333f6b6e0)
![Result 1 (2)](https://github.com/user-attachments/assets/a18eaceb-f718-4025-ac06-afb1db1d04d9)


# Conclusion
The Power Manager Telemetry project addresses the critical issue of power consumption in modern computing environments. By collecting detailed telemetry data, simulating loads, and analyzing the data, this project provides valuable insights into system power utilization. The project aligns with sustainability goals and offers a scalable framework for ongoing research and development.


# File Structure
power_manager_telemetry/

├── measure_system_power_utilization.py

├── load_simulator.py

├── generate_report.py

├── Dockerfile

├── telemetry_data.py

├── README.md

├── .gitignore

├── src/
