# Operating Systems (OS)

# Dynamic CPU Scheduling Simulator
This project is a Dynamic CPU Scheduling Simulator built with Python and Streamlit. It demonstrates and compares the performance of three CPU scheduling algorithms: FCFS (First Come First Served), SJF (Shortest Job First), and Priority Scheduling. The simulator allows users to input a list of processes with details like arrival time, burst time, and priority, and visualize the execution of each algorithm using a Gantt chart.


# Project Overview
This simulator helps analyze how different scheduling algorithms impact CPU performance metrics, such as:

   - Average Waiting Time
   - Turnaround Time
   - CPU Utilization

The interactive interface, built using Streamlit, also provides a comparative analysis report based on these metrics.


# Features
* Input Interface: Input process details including Process ID, Arrival Time, Burst Time, and Priority.

* Algorithms Supported:
    - FCFS (First Come First Served)
    - SJF (Shortest Job First)
    - Priority Scheduling

* Gantt Chart Visualization: Visualize the scheduling order and execution time of each process.

* Comparative Analysis Report: Compare performance metrics like average waiting time and turnaround time for each algorithm.


# Technologies Used
- Programming Language:
    - Python: Core programming language for logic and implementation
- Libraries:
    - Streamlit: To build the interactive web application
    - Matplotlib: For creating Gantt charts
    - Pandas: For data handling and analysis


# Benefits
This tool helps users understand how different scheduling methods impact CPU performance. 
By using it, you can see which algorithm performs better for different process inputs and understand their efficiency.



# Requirements:
   - pip install streamlit pandas matplotlib (DCSS.py)
   - pip install matplotlib (CPU_DCSS.py)

* in terminal window:
   - streamlit run DCSS.py
   - streamlit run CPU_DCSS.py

* Additional Troubleshooting: Run Streamlit with Python explicitly: If the above steps don’t work, try running Streamlit by calling Python directly:
   - python -m streamlit run DCSS.py
   - python -m streamlit run CPU_DCSS.py



# 
