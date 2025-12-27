 
<div align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Domain-Operating%20Systems-informational" alt="OS Domain">
  <img src="https://img.shields.io/badge/Status-Active-success" alt="Status">
  <img src="https://img.shields.io/badge/Author-Mohd%20Rizwan-orange" alt="Author">
</div>

<h1 align="center">🚀 Operating Systems Lab — Concept to Code</h1>
<p align="center"><b>A concise, instructor‑friendly and student‑ready collection of Python simulations & demos for core OS concepts: processes, states, system calls, scheduling, and multiprocessing.</b></p>

---

## � Table of Contents
1. Overview
2. Concepts Covered
3. Architecture & Flow (Process Lifecycle)
4. Repository Map
5. Quick Start
6. Usage by Topic
7. Scheduling Algorithms (At a Glance)
8. Multiprocessing Mini-Series
9. Windows / WSL Notes
10. Extend & Experiment Ideas
11. Academic Integrity
12. License & Author

---

## 1. 🌍 Overview
Four assignment clusters:
* **Assignment‑1:** Low-level process primitives (creation, exec, states, priority, `/proc`).
* **Assignment‑2:** CPU scheduling strategies + safe multiprocessing patterns.
* **Assignment‑3:** Advanced scheduling algorithms + memory management techniques.
* **Assignment‑4:** System utilities, process management, and comprehensive scheduling comparisons.

> Goal: Make invisible OS behaviors visible through minimal, readable scripts.

---

## 2. 🔧 Concepts Covered
| Theme | Subtopics | Representative File(s) |
|-------|-----------|------------------------|
| Process Creation | `fork()`, PID/PPID | `task1.py` |
| Program Replacement | `execvp()` | `task2.py` |
| Process States | Zombie, Orphan | `task3.py` |
| Introspection | `/proc/<pid>` metadata | `task4.py` |
| Scheduling Effect | `nice()` priority hints | `task5.py` |
| CPU Scheduling | FCFS, SJF, SRTF, RR | `fcfs.py`, `sjfnp.py`, `sjfp.py`, `rr.py` |
| Multiprocessing | Spawn, start, join, logging | `subtask*.py` |
| Advanced Scheduling | Priority (Non-preemptive), Round Robin | Assignment-3/`task1.py` |
| Memory Allocation | First Fit, Best Fit, Worst Fit | Assignment-3/`task2.py` |
| Memory Management | MFT, MVT | Assignment-3/`task3.py` |
| Script Execution | Subprocess management, script orchestration | Assignment-4/`task1.py` |
| System Logging | Multiprocessing with structured logging | Assignment-4/`task2.py`, `task3.py` |
| System Information | Platform detection, virtualization detection | Assignment-4/`task4.py` |
| Scheduling Comparison | FCFS, SJF, RR performance analysis | Assignment-4/`task5.py` |

---

## 3. 🔄 Architecture & Flow (Process Lifecycle)
```
 Parent Process
     |
     | fork()
     v
  Child Created ----> (Optional) execvp() → Replaced Image
     |                           |
     | exits quickly             | continues
     v                           v
  (Zombie until wait())       Running Process
     |                           |
 wait() reaps                   Parent exits early
     v                           v
  Cleaned Up                Orphan → Adopted by init (PID 1)
```

---

## 4. 🗂️ Repository Map
```
Assignment-1/
  task1.py  task2.py  task3.py  task4.py  task5.py
Assignment-2/
  fcfs.py  sjfnp.py  sjfp.py  rr.py  subtask1..4.py
Assignment-3/
  task1.py  task2.py  task3.py
Assignment-4/
  task1.py  task2.py  task3.py  task4.py  task5.py
Scheduling_Algorithm/
  fcfs.py  rr.py  sjfnp.py  sjfp.py
LICENSE
README.md
```

---

## 5. ⚡ Quick Start
Unix / WSL:
```bash
git clone <repo-url>
cd Operating-Systems-Lab-Assignments
python3 Assignment-1/task1.py
python3 Assignment-2/fcfs.py
python3 Assignment-3/task1.py
python3 Assignment-4/task1.py
```

PowerShell (scheduling, memory management, and system utilities):
```powershell
python Assignment-2\rr.py
python Assignment-3\task2.py
python Assignment-4\task5.py
```

---

## 6. 🛠️ Usage by Topic
| Topic | Run Example | Expected Observation |
|-------|-------------|----------------------|
| Process Forking | `python3 Assignment-1/task1.py` | Multiple child PIDs + orderly wait. |
| Exec Replacement | `python3 Assignment-1/task2.py` | Child prints then command output replaces process. |
| Zombie/Orphan | `python3 Assignment-1/task3.py` | Delay shows zombie (inspect via `ps`), then orphan adoption. |
| /proc Introspection | `python3 Assignment-1/task4.py` | Name/State/VmSize + open FDs. |
| Priority / nice() | `python3 Assignment-1/task5.py` | Different finish ordering (not guaranteed, but illustrative). |
| Round Robin | `python3 Assignment-2/rr.py` | Fair time-slice distribution. |
| SRTF | `python3 Assignment-2/sjfp.py` | Frequent preemption when shorter job arrives. |
| Priority Scheduling | `python3 Assignment-3/task1.py` | Non-preemptive priority-based process execution. |
| Memory Allocation | `python3 Assignment-3/task2.py` | First/Best/Worst fit allocation strategies with fragmentation analysis. |
| Memory Management | `python3 Assignment-3/task3.py` | MFT and MVT techniques for memory partitioning. |
| Script Orchestration | `python3 Assignment-4/task1.py` | Sequential execution of multiple Python scripts via subprocess. |
| System Logging | `python3 Assignment-4/task2.py` | Multiprocessing with structured logging to system_log.txt. |
| System Information | `python3 Assignment-4/task4.py` | Platform detection and virtualization environment identification. |
| Scheduling Comparison | `python3 Assignment-4/task5.py` | Side-by-side FCFS, SJF, and RR performance metrics. |

---

## 7. ⏱️ Scheduling Algorithms (At a Glance)
Symbols: BT = Burst Time, AT = Arrival Time, WT = Waiting Time, TAT = Turnaround Time, CT = Completion Time.

| Algorithm | Preemptive? | Core Idea | Key Relation |
|-----------|------------|-----------|--------------|
| FCFS | No | Queue order | `WT[i] = Σ BT[0..i-1]` |
| SJF (Non‑P) | No | Shortest next job | Minimizes average WT (theoretical) |
| SRTF | Yes | Always choose job w/ smallest remaining BT | Dynamic preemption |
| Round Robin | Yes (quantum) | Time slices rotate | Fairness; context switch overhead |
| Priority (Non‑P) | No | Highest priority first | Lower number = higher priority |

**Memory Management Strategies:**
| Strategy | Description | Trade-off |
|----------|-------------|-----------|
| First Fit | First available block ≥ process size | Fast allocation, high fragmentation |
| Best Fit | Smallest available block ≥ process size | Reduced fragmentation, slower search |
| Worst Fit | Largest available block ≥ process size | Large remaining blocks, high fragmentation |

Average metrics (you can extend):
```
Avg WT = (Σ WT[i]) / n
Avg TAT = (Σ TAT[i]) / n
```

---

## 8. 🧵 Multiprocessing Mini‑Series
Progression:
1. `subtask1.py` – Configure logging.
2. `subtask2.py` – Define workload function.
3. `subtask3.py` – Start processes (no join → possible premature parent exit).
4. `subtask4.py` – Join processes → deterministic, clean shutdown.

Inspect `process_log.txt` to analyze execution ordering.

---

## 9. 🪟 Windows / WSL Notes
| Feature | Native Windows | Use WSL? | Reason |
|---------|----------------|---------|--------|
| `fork()` | ❌ | ✅ | Windows lacks POSIX fork. |
| `/proc` | ❌ | ✅ | Linux procfs only. |
| `nice()` | Inconsistent | ✅ | Priority semantics differ. |
| Scheduling Simulations | ✅ | Pure Python arithmetic. |
| Multiprocessing Demo | ✅ | Implemented with spawn method on Windows. |

WSL Install (PowerShell):
```powershell
wsl --install
```

---

## 10. 🧪 Extend & Experiment
| Idea | Description |
|------|-------------|
| CLI Params | Use `argparse` to accept dynamic burst/arrival times. |
| Gantt Chart | Print ASCII timeline for RR / SRTF. |
| Metrics Suite | Compute Avg WT, Avg TAT automatically. |
| Priority Scheduling | Add static and dynamic priority algorithm. |
| I/O Burst Simulation | Alternate CPU/I-O phases in SRTF model. |
| Logging Enhancements | Per‑process JSON logs. |
| Memory Compaction | Add defragmentation algorithms to memory management. |
| Paging Simulation | Implement page replacement algorithms (LRU, FIFO, OPT). |
| Deadlock Detection | Add Banker's algorithm and resource allocation graphs. |
| System Monitoring | Real-time CPU, memory, and process monitoring dashboard. |
| Performance Benchmarks | Compare scheduling algorithms with various workload patterns. |
| Configuration Management | Dynamic system configuration through config files. |

---

## 11. 🎓 Academic Integrity
These scripts are educational references. If submitting for coursework, ensure you:
* Understand each line before reuse.
* Cite this repository if institution policy requires.
* Avoid blind copy–paste in graded exams.

---

## 12. 📄 License & 👤 Author
Licensed under MIT — see `LICENSE`.

<div align="center">
  <b>Mohd Rizwan</b><br>
  <i>B.Tech CSE (Data Science) | Operating Systems Lab</i><br>
  <sub>Feel free to open issues or suggestions.</sub>
</div>

