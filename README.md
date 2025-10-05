
<div align="center">
	<img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python" alt="Python">
	<img src="https://img.shields.io/badge/Operating%20Systems-Lab%20Assignments-success" alt="OS Lab Assignments">
	<img src="https://img.shields.io/badge/Author-Mohd%20Rizwan-orange" alt="Author">
</div>

# 🚀 Operating Systems Lab Assignments

<p align="center"><b>Hands‑on Python implementations of core OS concepts: process creation, system calls, states, scheduling, and multiprocessing.</b></p>

---

## 📚 Overview
This repository is organized in two parts:

**Assignment‑1 (Process Fundamentals)**
* Process creation with `fork()`
* Executing external programs (`execvp`)
* Zombie & orphan process states
* Reading process metadata from `/proc`
* Priority (nice value) effects

**Assignment‑2 (Scheduling & Multiprocessing)**
* Classical CPU scheduling algorithms (FCFS, SJF Non‑Preemptive, SRTF Preemptive, Round Robin)
* Basic multiprocessing primitives (process spawn, start, join)
* Logging of process activity

All code is concise and runnable for demonstration / academic review.

---

## 🗂️ Repository Structure

```
Assignment-1/
  task1.py   # Create multiple child processes
  task2.py   # Execute shell commands in children
  task3.py   # Demonstrate zombie & orphan states
  task4.py   # Inspect /proc/<pid> info
  task5.py   # Spawn workers with different nice priorities

Assignment-2/
  fcfs.py        # First-Come, First-Served scheduling
  sjfnp.py       # Shortest Job First (non-preemptive)
  sjfp.py        # Shortest Remaining Time First (preemptive SJF)
  rr.py          # Round Robin scheduling
  subtask1.py    # Initialize logging config
  subtask2.py    # Define simulated system_process
  subtask3.py    # Start processes (no join)
  subtask4.py    # Start processes and join (graceful shutdown)
```

---

## 🧪 Assignment‑1 Details
| File | Concept | What To Observe |
|------|---------|-----------------|
| `task1.py` | Process Creation | Each child prints its PID & parent PID. Parent waits for all. |
| `task2.py` | Exec System Call | Children replace image with commands (`ls`, `date`, `ps -el`). |
| `task3.py` | Zombie / Orphan | Delay before `wait()` shows zombie; exiting parent adopts child → orphan. |
| `task4.py` | `/proc` Introspection | Name, State, VmSize, executable path, open file descriptors. |
| `task5.py` | Priority / Nice | Different `nice` values influence completion ordering (may vary). |

> NOTE: `os.fork()`, `/proc`, and `os.nice()` require a Unix-like environment (Linux, WSL, macOS). They will NOT work natively on standard Windows PowerShell without WSL.

### Run Examples (Unix / WSL)
```bash
python3 Assignment-1/task1.py
python3 Assignment-1/task3.py   # Watch timing for zombie, orphan demo
```

---

## 🧮 Assignment‑2 Scheduling Algorithms
| File | Algorithm | Key Idea |
|------|-----------|----------|
| `fcfs.py` | FCFS | Non-preemptive, arrival order. Waiting Time accumulates sequentially. |
| `sjfnp.py` | SJF Non-Preemptive | Always pick shortest next job (after completion). |
| `sjfp.py` | SRTF (Preemptive SJF) | Continuously preempt if new shorter remaining job arrives. |
| `rr.py` | Round Robin | Time slicing with fixed quantum. |

Each prints a table with Burst Time (BT), optional Arrival Time (AT), Waiting Time (WT), Turnaround Time (TAT).

### Sample Run
```bash
python3 Assignment-2/fcfs.py
python3 Assignment-2/rr.py
```

> Feel free to modify the arrays at the bottom of each file to test different workloads.

---

## 🧵 Multiprocessing Subtasks (Assignment‑2)
| File | Focus | Difference |
|------|-------|------------|
| `subtask1.py` | Logging Setup | Creates `process_log.txt` configuration. |
| `subtask2.py` | Task Definition | Defines `system_process` with start/end logs. |
| `subtask3.py` | Process Start | Starts processes but does not `join()` (may exit before children finish). |
| `subtask4.py` | Proper Shutdown | Uses `join()` ensuring deterministic termination. |

Run the final version for a clean lifecycle:
```bash
python3 Assignment-2/subtask4.py
```
Check `process_log.txt` for timestamped entries.

---

## 🖥️ Windows Users (Important)
| Feature | Works Natively? | Workaround |
|---------|-----------------|-----------|
| `fork()` / `os.fork()` | ❌ | Use WSL (Windows Subsystem for Linux) or a Linux VM. |
| `/proc` filesystem | ❌ | Use WSL / Linux container. |
| `os.nice()` | Partial / ❌ | Run inside WSL for consistent behavior. |
| Scheduling scripts (`fcfs.py`, etc.) | ✅ | Pure Python—works everywhere. |
| Multiprocessing subtasks | ✅ | Works (protect entry with `if __name__ == '__main__':`). |

WSL Quick Start (PowerShell):
```powershell
wsl --install
# Reboot if prompted, then place repo inside your Linux filesystem (e.g., ~/os-lab)
```

---

## ▶️ How to Run (Cross‑Platform Summary)
1. Install Python 3.10+.
2. (Windows) Use WSL for Assignment‑1 tasks 1–5 except scheduling algorithms.
3. Clone or download the repo.
4. Execute desired script:

```bash
python3 Assignment-2/rr.py
```

Or (PowerShell for scheduling algorithms only):
```powershell
python Assignment-2\fcfs.py
```

---

## 🔍 Extending / Experiment Ideas
* Add Arrival Times to FCFS / SJF NP simulation.
* Compute and print average WT & TAT.
* Add Gantt chart text timeline for RR & SRTF.
* Parameterize inputs via `argparse`.
* Measure real execution time differences for `nice` values (use `time` module).

---

## 🛠️ Prerequisites
* Python 3.10+
* Linux / WSL for process state & `/proc` demos
* No third‑party dependencies required

---

## 📄 License
Distributed under the MIT License. See `LICENSE` for details.

---

## 🏆 Author
<div align="center">
  <b>Mohd Rizwan</b><br>
  <i>B.Tech CSE (Data Science) | Operating Systems Lab</i>
</div>
