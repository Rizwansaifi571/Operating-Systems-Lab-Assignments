def srtf(processes, bt, at):
    n = len(processes)
    rt = bt[:]
    complete, t, wt, tat = 0, 0, [0]*n, [0]*n

    while complete < n:
        shortest, minm = -1, 9999
        for j in range(n):
            if at[j] <= t and rt[j] < minm and rt[j] > 0:
                minm = rt[j]; shortest = j
        if shortest == -1:
            t += 1; continue
        rt[shortest] -= 1
        if rt[shortest] == 0:
            complete += 1
            finish_time = t + 1
            wt[shortest] = finish_time - bt[shortest] - at[shortest]
            tat[shortest] = wt[shortest] + bt[shortest]
        t += 1

    print("Process  BT  AT  WT  TAT")
    for i in range(n):
        print(f"P{processes[i]}       {bt[i]}   {at[i]}   {wt[i]}   {tat[i]}")

srtf([1,2,3], [8,4,9], [0,1,2])
