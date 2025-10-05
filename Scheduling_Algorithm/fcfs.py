def fcfs(processes, burst_time):
    n = len(processes)
    wt = [0] * n
    tat = [0] * n

    for i in range(1, n):
        wt[i] = wt[i - 1] + burst_time[i - 1]

    for i in range(n):
        tat[i] = wt[i] + burst_time[i]

    print("Process  BT  WT  TAT")
    for i in range(n):
        print(f"P{processes[i]}       {burst_time[i]}   {wt[i]}   {tat[i]}")

fcfs([1, 2, 3], [5, 9, 6])
