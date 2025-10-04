def round_robin(processes, bt, quantum):
    n = len(processes)
    rem_bt, t, wt, tat = bt[:], 0, [0]*n, [0]*n
    while True:
        done = True
        for i in range(n):
            if rem_bt[i] > 0:
                done = False
                if rem_bt[i] > quantum:
                    t += quantum
                    rem_bt[i] -= quantum
                else:
                    t += rem_bt[i]
                    wt[i] = t - bt[i]
                    rem_bt[i] = 0
        if done: break
    for i in range(n):
        tat[i] = bt[i] + wt[i]

    print("Process  BT  WT  TAT")
    for i in range(n):
        print(f"P{processes[i]}       {bt[i]}   {wt[i]}   {tat[i]}")

round_robin([1,2,3], [24,3,3], 4)
