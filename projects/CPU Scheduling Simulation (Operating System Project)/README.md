# CPU Scheduling Simulation (Operating System Project)

This project simulates CPU scheduling using the Round-Robin algorithm with random I/O interrupts. It visualizes process execution and I/O wait times using a Gantt chart.

## Features
- Simulates process scheduling with Round-Robin (configurable time quantum)
- Handles random I/O interrupts for processes
- Tracks process states, waiting times, turnaround times, and I/O times
- Prints detailed logs and summary tables
- Generates a Gantt chart showing CPU and I/O intervals for each process

## Requirements
- Python 3.x
- matplotlib (for Gantt chart visualization)

Install matplotlib if not already installed:
```bash
pip install matplotlib
```

## Usage
Run the simulation with the default processes:
```bash
python OS1_updated.py
```

## Output
- The simulation prints a detailed log of process state transitions and a summary table with metrics.
- A Gantt chart image (`gantt_detailed.png`) is generated in the project directory.

## Example Gantt Chart
Below is an example of the generated Gantt chart:

![Gantt Chart](gantt_detailed.png)

## Customization
You can modify the process list in `OS1_updated.py` to simulate different scenarios:
```python
# Example:
p1 = Process("P1", 0, 8)
p2 = Process("P2", 1, 4)
p3 = Process("P3", 3, 6)
p4 = Process("P4", 5, 2)
processes = [p1, p2, p3, p4]
```

## License
This project is for educational purposes.
