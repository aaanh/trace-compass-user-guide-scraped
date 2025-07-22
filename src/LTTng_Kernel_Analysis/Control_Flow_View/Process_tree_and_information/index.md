### Process tree and information

Processes are organized as a tree within this view. This way, child and parent processes are easy to identify.



The layout is based on the states computed from the trace events.

A given process may be shown at different places within the tree since the nodes areunique (TID, birth time) couples. This means that if process B of parent A dies, you'll still see it in the tree. If process A forks process B again, it will be shown as a different node since it won't have the same birth time (and probably not the same TID). This has the advantage that the tree, once loaded, never changes: horizontal scrolling within thecontrol flowremains possible.

The TID column shows the process node'sthread IDand the PTID column shows itsparent thread ID(nothing is shown if the process has no parent).

It is possible to sort the columns of the tree by clicking on the column header. Subsequent clicking will change the sort order. The hierarchy, i.e. the parent-child relationship is kept. When opening a trace for the first time, the processes are sorted bybirth time. The sort order and column will be preserved when switching between open traces. Note that when opening an experiment the processes will be sorted within each trace.