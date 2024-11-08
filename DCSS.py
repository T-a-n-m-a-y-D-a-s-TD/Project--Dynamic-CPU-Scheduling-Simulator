import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# Sample scheduling functions - placeholders for real logic
def fcfs(processes):
    # Sort by arrival time
    processes.sort(key=lambda x: x['Arrival Time'])
    return calculate_metrics(processes)


def sjf(processes):
    # Sort by burst time, then arrival time
    processes.sort(key=lambda x: (x['Burst Time'], x['Arrival Time']))
    return calculate_metrics(processes)


def priority_scheduling(processes):
    # Sort by priority, then arrival time
    processes.sort(key=lambda x: (x['Priority'], x['Arrival Time']))
    return calculate_metrics(processes)


def calculate_metrics(processes):
    # Calculate completion, waiting, and turnaround times
    current_time = 0
    for process in processes:
        process['Start Time'] = max(current_time, process['Arrival Time'])
        process['Completion Time'] = process['Start Time'] + process['Burst Time']
        process['Turnaround Time'] = process['Completion Time'] - process['Arrival Time']
        process['Waiting Time'] = process['Turnaround Time'] - process['Burst Time']
        current_time = process['Completion Time']
    return processes


def visualize_gantt_chart(processes, algorithm_name):
    fig, ax = plt.subplots(figsize=(10, 5))
    for process in processes:
        ax.broken_barh([(process['Start Time'], process['Burst Time'])],
                       (process['Process ID'] * 10, 9), facecolors=('tab:blue'))
    ax.set_ylim(0, (len(processes) + 1) * 10)
    ax.set_xlim(0, max(p['Completion Time'] for p in processes) + 10)
    ax.set_xlabel('Time')
    ax.set_ylabel('Process ID')
    ax.set_yticks([p['Process ID'] * 10 + 5 for p in processes])
    ax.set_yticklabels([f"P{p['Process ID']}" for p in processes])
    ax.set_title(f"Gantt Chart for {algorithm_name} Scheduling")
    return fig


# Streamlit app setup
st.title("Dynamic CPU Scheduling Simulator")
st.write("""
This simulator demonstrates and compares the performance of three scheduling algorithms: 
- **FCFS** (First-Come, First-Served)
- **SJF** (Shortest Job First)
- **Priority Scheduling**

Input process details, select an algorithm, and view the scheduling results and Gantt chart.
""")

# User inputs
num_processes = st.sidebar.number_input("Number of processes:", min_value=1, max_value=10, step=1)
processes = []

st.sidebar.header("Process Details")
for i in range(num_processes):
    st.sidebar.subheader(f"Process {i + 1}")
    arrival_time = st.sidebar.number_input(f"Arrival Time (P{i + 1})", min_value=0)
    burst_time = st.sidebar.number_input(f"Burst Time (P{i + 1})", min_value=1)
    priority = st.sidebar.number_input(f"Priority (P{i + 1})", min_value=1, max_value=10)
    processes.append({
        'Process ID': i + 1,
        'Arrival Time': arrival_time,
        'Burst Time': burst_time,
        'Priority': priority
    })

# Choose scheduling algorithm
algorithm = st.selectbox("Select Scheduling Algorithm:", ['FCFS', 'SJF', 'Priority'])

# Run simulation on button click
if st.button("Run Simulation"):
    # Execute the chosen scheduling algorithm
    if algorithm == "FCFS":
        results = fcfs(processes)
    elif algorithm == "SJF":
        results = sjf(processes)
    elif algorithm == "Priority":
        results = priority_scheduling(processes)

    # Convert results to a DataFrame for better display
    results_df = pd.DataFrame(results)
    st.write(f"### Results for {algorithm} Scheduling")
    st.write(results_df[['Process ID', 'Arrival Time', 'Burst Time', 'Priority', 'Start Time',
                         'Completion Time', 'Waiting Time', 'Turnaround Time']])

    # Display Gantt chart
    fig = visualize_gantt_chart(results, algorithm)
    st.pyplot(fig)

    # Comparison report
    avg_waiting_time = sum(p['Waiting Time'] for p in results) / len(results)
    avg_turnaround_time = sum(p['Turnaround Time'] for p in results) / len(results)

    st.write("### Comparison Report")
    st.write(f"- **Average Waiting Time**: {avg_waiting_time:.2f}")
    st.write(f"- **Average Turnaround Time**: {avg_turnaround_time:.2f}")

    st.write("""
    These metrics help compare the efficiency of different scheduling algorithms in minimizing waiting and turnaround times.
    """)