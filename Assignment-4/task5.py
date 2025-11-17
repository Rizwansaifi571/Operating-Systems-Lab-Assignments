def avg(l):return round(sum(l)/len(l),2)

def fcfs(bt,at):
 t=0;ct=[]
 for i in range(len(bt)):t=max(t,at[i])+bt[i];ct+=[t]
 tat=[ct[i]-at[i]for i in range(len(bt))];wt=[tat[i]-bt[i]for i in range(len(bt))]
 print("\nFCFS");[print(f"P{i+1}: WT={wt[i]} TAT={tat[i]}")for i in range(len(bt))]
 print("Avg WT=",avg(wt),"Avg TAT=",avg(tat))

def sjf(bt,at):
 n=len(bt);done=[0]*n;t=0;ct=[0]*n
 for _ in range(n):
  r=[i for i in range(n)if not done[i]and at[i]<=t]
  if not r:t=min(at[i]for i in range(n)if not done[i]);r=[i for i in range(n)if at[i]<=t and not done[i]]
  i=min(r,key=lambda x:bt[x]);t+=bt[i];ct[i]=t;done[i]=1
 tat=[ct[i]-at[i]for i in range(n)];wt=[tat[i]-bt[i]for i in range(n)]
 print("\nSJF");[print(f"P{i+1}: WT={wt[i]} TAT={tat[i]}")for i in range(n)]
 print("Avg WT=",avg(wt),"Avg TAT=",avg(tat))

def rr(bt,at,q):
 n=len(bt);r=bt[:];t=0;ct=[0]*n;Q=[]
 while 1:
  for i in range(n):
   if at[i]<=t and r[i]>0 and i not in Q:Q+=[i]
  if not Q:
   if all(x==0 for x in r):break
   t+=1;continue
  i=Q.pop(0);x=min(q,r[i]);r[i]-=x;t+=x
  for j in range(n):
   if at[j]<=t and r[j]>0 and j not in Q:Q+=[j]
  if r[i]>0:Q+=[i]
  else:ct[i]=t
 tat=[ct[i]-at[i]for i in range(n)];wt=[tat[i]-bt[i]for i in range(n)]
 print("\nRound Robin");[print(f"P{i+1}: WT={wt[i]} TAT={tat[i]}")for i in range(n)]
 print("Avg WT=",avg(wt),"Avg TAT=",avg(tat))

def priority(bt,at,pr):
 n=len(bt);done=[0]*n;t=0;ct=[0]*n
 for _ in range(n):
  r=[i for i in range(n)if not done[i]and at[i]<=t]
  if not r:t=min(at[i]for i in range(n)if not done[i]);r=[i for i in range(n)if at[i]<=t and not done[i]]
  i=min(r,key=lambda x:pr[x]);t+=bt[i];ct[i]=t;done[i]=1
 tat=[ct[i]-at[i]for i in range(n)];wt=[tat[i]-bt[i]for i in range(n)]
 print("\nPriority");[print(f"P{i+1}: WT={wt[i]} TAT={tat[i]}")for i in range(n)]
 print("Avg WT=",avg(wt),"Avg TAT=",avg(tat))

bt,at,pr,q=[5,4,2,3],[0,1,2,3],[2,1,3,2],2
fcfs(bt,at);sjf(bt,at);rr(bt,at,q);priority(bt,at,pr)