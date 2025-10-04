def sjf(processes, burst_time):
    n = len(processes)
    sorted_proc = sorted(zip(processes, burst_time), key=lambda x: x[1])
    wt, tat = [0] * n, [0] * n

    for i in range(1, n):
        wt[i] = wt[i - 1] + sorted_proc[i - 1][1]

    for i in range(n):
        tat[i] = wt[i] + sorted_proc[i][1]

    print("Process  BT  WT  TAT")
    for i in range(n):
        print(f"P{sorted_proc[i][0]}       {sorted_proc[i][1]}   {wt[i]}   {tat[i]}")

sjf([1, 2, 3], [6, 8, 7])
