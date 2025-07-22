## Flame Graph View

This is an aggregate view of the function calls from theFlame Chart View. This shows a bird's eye view of what are the main
			time sinks in the traced applications. Each entry in theFlame Graphrepresents an aggregation of all the calls to a function
			in a certain depth of the call stack having the same caller. So, functions in theFlame Graphare aggregated by depth and
			caller. This enables the user to find the most executed code path easily.
- In aFlame Graph, each entry (box) represents a function in the stack.
- If one takes a single vertical line in the view, it represents a full call stack with parents calling children.
- Thex-axisrepresents total duration (execution time) and not absolute time, so it is not aligned with the other views.
- The width of an entry is the total time spent in that function, including time spent calling the children.
- The total time can exceed the longest duration, if the program is pre-empted and not running during its trace time.
- Each thread traced makes its own flame graph.
- In aFlame Graph, each entry (box) represents a function in the stack.
- If one takes a single vertical line in the view, it represents a full call stack with parents calling children.
- Thex-axisrepresents total duration (execution time) and not absolute time, so it is not aligned with the other views.
- The width of an entry is the total time spent in that function, including time spent calling the children.
- The total time can exceed the longest duration, if the program is pre-empted and not running during its trace time.
- Each thread traced makes its own flame graph.

The function name is visible on each Flame graph event if the size permits. Each box in theFlame Graphhas the same color as the box representing the same function in theFlame Chart.

To open this view, select a trace, expand it in theProject Explorer, then expand theCall Graph Analysis(the trace must be loaded) and open theFlame Graph.
			It's also possible to go inWindow->Show View->Tracingthen
			selectFlame Graphin the list.



To use theFlame graph, one can navigate it and find which function is consuming the most self-time.
			This can be seen as a large plateau. Then the entry can be inspected. At this point, the worst offender in
			terms of CPU usage will be highlighted, however, it is not a single call to investigate, but rather the
			aggregation of all the calls. Right mouse-clicking on that entry will open a context sensitive menu.
			SelectingGo to minimumorGo to maximumwill take the user to the minimum or maximum
			recorded times in the trace. This is interesting to compare and contrast the two.

Hovering over a function will show a tooltip with the statistics on a per-function basis. One can see the total and self times
			(worst-case,best-case,average,total time,standard deviation,number of calls) for that function.

If one wishes to explore at a medium detail level between the "classic" flame graph view and the call stack view, a per-thread flame
			graph view is available by selecting the coarser menu and clicking onContent PresentationthenPer-thread. To return to
			the default mode, return to that menu and click onAggregate Threads.

### How to use a Flame Graph

Observing the time spent in each function can show where most of the time is spent and where one could optimize.
			An example in the image above: one can see thatmp_sortis a recursive sort function, it takes approximately
			40% of the execution time of the program. That means that perfectly parallelizing it can yield a gain of 20% for 2 threads, 33% for 3
			and so forth. Looking at the functionprint_current_files, it takes about 30% of the time, and it has a childprint_many_per_linethat has a large
			self time (above 10%). This could be another area that can be targeted for optimization. Knowing this in advance helps developers
			know where to aim their efforts.

It is recommended to have a kernel trace as well as a user space trace in an experiment
			while using theFlame Graphas it will show what is causing the largest delays.
			When using theFlame Graphtogether with a call stack and a kernel trace,
			an example work flow would be to find the worst offender in terms of time taken for a function
			that seems to be taking too long. Then, using the context menuGo to maximum, one can navigate
			to the maximum duration and see if the OS is, for example, preempting the function for too long,
			or if the issue is in the code being executed.