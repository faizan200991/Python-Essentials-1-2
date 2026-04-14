import time
import random
try:
    import matplotlib.pyplot as plt
except Exception:
    plt = None

class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.state = "New"
        self.io_wait_time = 0 
        
        # --- NEW VARIABLES FOR CALCULATIONS ---
        self.completion_time = 0   # When did it finish?
        self.total_io_time = 0     # How long did it spend in I/O total?

    def __repr__(self):
        return f"{self.pid}"

def run_simulation(process_list, time_quantum=3):
    current_time = 0
    ready_queue = []
    waiting_queue = []
    completed_processes = []
    
    all_processes = list(process_list)
    
    print(f"{'Time':<6} | {'Process':<8} | {'Old State':<10} | {'New State':<10} | {'Reason'}")
    print("-" * 65)

    running_process = None
    quantum_timer = 0
    # timeline and plotting records (initialized once)
    timeline = []  # record which PID ran at each time unit (or None for idle)
    io_intervals = {p.pid: [] for p in process_list}  # (start, duration)
    events = []  # list of (time, pid, event_type)

    while len(completed_processes) < len(process_list):
        # 1. Check for Arrivals
        for p in all_processes:
            if p.state == "New" and p.arrival_time == current_time:
                p.state = "Ready"
                ready_queue.append(p)
                print(f"{current_time:<6} | {p.pid:<8} | {'New':<10} | {'Ready':<10} | Arrival")

        # 2. Handle Waiting Processes
        for p in waiting_queue[:]:
            p.io_wait_time -= 1
            if p.io_wait_time <= 0:
                p.state = "Ready"
                waiting_queue.remove(p)
                ready_queue.append(p)
                print(f"{current_time:<6} | {p.pid:<8} | {'Waiting':<10} | {'Ready':<10} | I/O Complete")
                # record I/O completion event
                events.append((current_time, p.pid, 'io_end'))

        # 3. CPU Logic
        if running_process:
            running_process.remaining_time -= 1
            quantum_timer += 1

            # Check Termination
            if running_process.remaining_time == 0:
                print(f"{current_time:<6} | {running_process.pid:<8} | {'Running':<10} | {'Terminated':<10} | Task Finished")
                running_process.state = "Terminated"
                
                # --- RECORD COMPLETION TIME ---
                # We use current_time + 1 because the tick just finished
                running_process.completion_time = current_time + 1 
                # record termination event
                events.append((running_process.completion_time, running_process.pid, 'terminated'))
                
                completed_processes.append(running_process)
                running_process = None
                quantum_timer = 0
            
            # Check Random I/O Interrupt
            elif random.randint(1, 10) == 1:
                # --- TRACK I/O DURATION ---
                io_duration = random.randint(2, 4)
                # Print interruption with details: when it stopped and remaining burst
                print(f"{current_time:<6} | {running_process.pid:<8} | {'Running':<10} | {'Waiting':<10} | I/O Request (dur={io_duration}, rem={running_process.remaining_time}, stopped={current_time + 1})")
                running_process.state = "Waiting"
                running_process.io_wait_time = io_duration
                running_process.total_io_time += io_duration # Add to total I/O stats

                # record I/O interval starting at the tick boundary (before clearing running_process)
                io_intervals[running_process.pid].append((current_time + 1, io_duration))
                events.append((current_time + 1, running_process.pid, 'io_start'))

                waiting_queue.append(running_process)
                running_process = None
                quantum_timer = 0

            # Check Time Quantum
            elif quantum_timer >= time_quantum:
                # Print remaining burst time and the time the process stopped
                print(f"{current_time:<6} | {running_process.pid:<8} | {'Running':<10} | {'Ready':<10} | Time Interrupt (rem={running_process.remaining_time}, stopped={current_time + 1})")
                running_process.state = "Ready"
                ready_queue.append(running_process)
                # record the time interrupt event
                events.append((current_time + 1, running_process.pid, 'time_interrupt'))
                running_process = None
                quantum_timer = 0

        # 4. Dispatcher
        if not running_process and ready_queue:
            running_process = ready_queue.pop(0)
            print(f"{current_time:<6} | {running_process.pid:<8} | {'Ready':<10} | {'Running':<10} | Dispatched")
            running_process.state = "Running"
            # record dispatch event
            events.append((current_time, running_process.pid, 'dispatched'))

        # Record who runs during this time unit
        timeline.append(running_process.pid if running_process else None)

        current_time += 1
        # time.sleep(0.1) 
    print("-" * 65)
    print("Simulation Complete.\n")

    # --- CALCULATE AND PRINT METRICS ---
    # We'll print a single combined table with more per-process details
    print(f"{'PID':<6} | {'Arrival':<7} | {'Service(Burst)':<15} | {'Completion':<10} | {'Turnaround':<10} | {'Total I/O':<9} | {'Waiting':<7}")
    print("-" * 90)

    total_turnaround = 0
    total_waiting = 0

    # Sort by PID so the table looks neat
    completed_processes.sort(key=lambda x: x.pid)

    for p in completed_processes:
        # Calculate Metrics
        turnaround_time = p.completion_time - p.arrival_time

        # Waiting Time = Total Time - CPU Time - I/O Time
        waiting_time = turnaround_time - p.burst_time - p.total_io_time
        if waiting_time < 0:
            waiting_time = 0

        total_turnaround += turnaround_time
        total_waiting += waiting_time

        print(f"{p.pid:<6} | {p.arrival_time:<7} | {p.burst_time:<15} | {p.completion_time:<10} | {turnaround_time:<10} | {p.total_io_time:<9} | {waiting_time:<7}")

    print("-" * 90)
    # Calculate Averages
    avg_tat = total_turnaround / len(process_list)
    avg_wt = total_waiting / len(process_list)
    print(f"Average Turnaround Time: {avg_tat:.2f}")
    print(f"Average Waiting Time:    {avg_wt:.2f}")

    # State the scheduling algorithm used
    print(f"Scheduling Algorithm: Round-Robin (Time Quantum = {time_quantum})")

    # --- DRAW DETAILED GANTT-LIKE CHART ---
    if plt is None:
        print("matplotlib is not available — install it with: pip install matplotlib")
        return

    # Build intervals for each process from timeline
    pids = [p.pid for p in process_list]
    pid_to_intervals = {pid: [] for pid in pids}
    t = 0
    total_time = len(timeline)
    while t < total_time:
        val = timeline[t]
        if val is None:
            t += 1
            continue
        start = t
        while t < total_time and timeline[t] == val:
            t += 1
        duration = t - start
        pid_to_intervals[val].append((start, duration))

    # Plot
    fig, ax = plt.subplots(figsize=(10, 1 + len(pids) * 0.6))
    y_height = 9
    y_positions = {pid: i * (y_height + 4) for i, pid in enumerate(pids)}

    colors = plt.cm.tab10.colors
    color_map = {pid: colors[i % len(colors)] for i, pid in enumerate(pids)}

    # running bars
    for pid, intervals in pid_to_intervals.items():
        if intervals:
            ax.broken_barh(intervals, (y_positions[pid], y_height), facecolors=color_map[pid], edgecolor='black')

    # I/O wait bars (different style)
    for pid, intervals in io_intervals.items():
        if intervals:
            ax.broken_barh(intervals, (y_positions[pid], y_height), facecolors='lightgray', hatch='xxx', edgecolor='black')

    # Event markers (only show dispatch and time-interrupt markers)

    # Create custom legend only once per event type
    handles, labels = ax.get_legend_handles_labels()
    unique = dict(zip(labels, handles))
    ax.legend(unique.values(), unique.keys(), loc='upper right')

    ax.set_yticks([y_positions[pid] + y_height / 2 for pid in pids])
    ax.set_yticklabels(pids)
    ax.set_xlabel('Time')
    ax.set_title('Gantt chart: execution for the simulated processes')
    ax.set_xlim(0, len(timeline))
    ax.grid(True, axis='x', linestyle='--', alpha=0.4)

    out_file = 'gantt_detailed.png'
    fig.tight_layout()
    fig.savefig(out_file)
    plt.show()
    print(f"Saved detailed Gantt chart to: {out_file}")

# --- Setup Data ---
p1 = Process("P1", 0, 8)
p2 = Process("P2", 1, 4)
p3 = Process("P3", 3, 6)
p4 = Process("P4", 5, 2)

processes = [p1, p2, p3, p4]

run_simulation(processes)