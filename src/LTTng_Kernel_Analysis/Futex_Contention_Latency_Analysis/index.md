## Futex Contention Latency Analysis

TheFutex Contention Latency Analysismeasures the futexes contention latency between futex entry and exit event for a thread. The durations are visualized using theLatencyviews. For more information about theLatencyviews see chapterLatency Analyses.

The following views are also available for the Futex Contention Latency Analysis:

### Uaddr vs Waiter

A timegraph view of the waiters by futex uaddr. This view is useful to see which threads are waiting on a specific futex and understand blocked threads.



### Scenarios

A timegraph view of the futex wait/lock and wake/unlock scenarios (from futex entry to futex exit). This view is useful to suss up the general level of contention in a given trace. It highlights futex lifespans.