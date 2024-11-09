import matplotlib.pyplot as plt


class Process:
    def __init__(self, pid, arrival_time, burst_time, priority=0):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0
        self.start_time = -1  # To record when the process actually starts


def fcfs(processes):
    processes.sort(key=lambda x: x.arrival_time)
    current_time = 0
    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time

        process.start_time = current_time
        process.completion_time = current_time + process.burst_time
        current_time += process.burst_time
    return processes


def sjf(processes):
    current_time = 0
    completed = []
    ready_queue = []

    while processes or ready_queue:
        while processes and processes[0].arrival_time <= current_time:
            ready_queue.append(processes.pop(0))

        if ready_queue:
            ready_queue.sort(key=lambda x: x.burst_time)
            current_process = ready_queue.pop(0)

            if current_time < current_process.arrival_time:
                current_time = current_process.arrival_time

            current_process.start_time = current_time
            current_process.completion_time = current_time + current_process.burst_time
            current_time += current_process.burst_time
            completed.append(current_process)
        else:
            current_time += 1

    return completed


def priority_scheduling(processes):
    current_time = 0
    completed = []
    ready_queue = []

    while processes or ready_queue:
        while processes and processes[0].arrival_time <= current_time:
            ready_queue.append(processes.pop(0))

        if ready_queue:
            ready_queue.sort(key=lambda x: x.priority)
            current_process = ready_queue.pop(0)

            if current_time < current_process.arrival_time:
                current_time = current_process.arrival_time

            current_process.start_time = current_time
            current_process.completion_time = current_time + current_process.burst_time
            current_time += current_process.burst_time
            completed.append(current_process)
        else:
            current_time += 1

    return completed


def calculate_metrics(processes):
    for process in processes:
        process.turnaround_time = process.completion_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time


def visualize_detailed_gantt_chart(processes, algorithm_name):
    fig, gnt = plt.subplots()
    gnt.set_title(f"Gantt Chart for {algorithm_name}")
    gnt.set_xlabel('Time')
    gnt.set_ylabel('Process ID')

    max_time = max(p.completion_time for p in processes)
    gnt.set_xlim(0, max_time)
    gnt.set_ylim(0, len(processes))

    plt.xticks(range(0, max_time + 1))  # Show time ticks as integers

    for idx, process in enumerate(processes):
        # Plot burst time (execution time) only
        gnt.broken_barh([(process.start_time, process.burst_time)],
                        (idx, 1), facecolors=('tab:blue'))  # Execution time in blue

        plt.text(process.start_time + process.burst_time / 2, idx + 0.5, f'P{process.pid}', ha='center')

    plt.show()


def print_report(processes, algorithm_name):
    print(f"Report for {algorithm_name}")
    print(
        f"{'PID':<5}{'Arrival':<10}{'Burst':<10}{'Priority':<10}{'Completion':<15}{'Turnaround':<15}{'Waiting':<10}")
    for process in processes:
        print(f"{process.pid:<5}{process.arrival_time:<10}{process.burst_time:<10}{process.priority:<10}"
              f"{process.completion_time:<15}{process.turnaround_time:<15}{process.waiting_time:<10}")
    avg_waiting_time = sum(p.waiting_time for p in processes) / len(processes)
    avg_turnaround_time = sum(p.turnaround_time for p in processes) / len(processes)
    print(f"Average Turnaround Time: {avg_turnaround_time}")
    print(f"Average Waiting Time: {avg_waiting_time}")


def get_user_input():
    processes = []
    num_processes = int(input("Enter the number of processes: "))

    for _ in range(num_processes):
        pid = int(input(f"\nEnter Process ID : "))
        arrival_time = int(input(f"Enter Arrival Time for process {pid}: "))
        burst_time = int(input(f"Enter Burst Time for process {pid}: "))
        priority = int(input(f"Enter Priority for process {pid} (Higher number means lower priority): "))

        processes.append(Process(pid, arrival_time, burst_time, priority))

    return processes


def main():
    processes = get_user_input()

    algorithms = {'FCFS': fcfs, 'SJF': sjf, 'Priority': priority_scheduling}

    for name, algorithm in algorithms.items():
        print(f"\nRunning {name} Scheduling")
        scheduled_processes = algorithm(processes.copy())
        calculate_metrics(scheduled_processes)
        visualize_detailed_gantt_chart(scheduled_processes, name)
        print_report(scheduled_processes, name)


if __name__ == '__main__':
    main()
