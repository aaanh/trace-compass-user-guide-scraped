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