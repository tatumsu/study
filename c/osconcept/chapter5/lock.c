/*
A solution to the critical - section problem must satisfy the following three
requirements :
1. Mutual exclusion.If process Pi is executing in its critical section, then no
other processes can be executing in their critical sections.

2. Progress.If no process is executing in its critical section and some
processes wish to enter their critical sections, then only those processes
that are not executing in their remainder sections can participate in
deciding which will enter its critical section next, and this selection cannot
be postponed indefinitely.

3. Bounded waiting.There exists a bound, or limit, on the number of times
that other processes are allowed to enter their critical sections after a
*/

do {
    waiting[i] = true;
    key = true;
    while (waiting[i] && key)
        key = test and set(&lock);
    waiting[i] = false;
    /* critical section */
    j = (i + 1) % n;
    while ((j != i) && !waiting[j])
        j = (j + 1) % n;
    if (j == i)
        lock = false;
    else
        waiting[j] = false;
    /* remainder section */
} while (true);

boolean waiting[n];
boolean lock;