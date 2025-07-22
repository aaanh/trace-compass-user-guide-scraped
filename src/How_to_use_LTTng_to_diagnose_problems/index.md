# How to use LTTng to diagnose problems

LTTng is a tracer, it will give an enormous amount of information about the system it is running on. This means it can solve many types of problems.

The following are examples of problems that can be solved with a tracer.

## Random stutters

Bob is running a computer program and it stutters periodically every 2 minutes. The CPU load is relatively low and Bob isn't running low on RAM.

He decides to trace his complete system for 10 minutes. He opens the LTTng view in eclipse. From the control, he creates a session and enables all kernel tracepoints.

He now has a 10 GB trace file. He imports the trace to his viewer and loads it up.

A cursory look at the histogram bar on the bottom show relatively even event distribution, there are no interesting spikes, so he will have to dig deeper to find the issue. If he had seen a spike every 2 minutes, there would be strong chances this would be the first thing to investigate as it would imply a lot of kernel activity at the same period as his glitch, this would have been a path to investigate.

As Bob suspects that he may be having some hardware raising IRQs or some other hardware based issue and adding delays. He looks at the ressource view and doesn't see anything abnormal.

Bob did note an exact second one glitch occurred: 11:58:03. He zooms into the time range or 11:58:02-11:58:04 using the histogram. He is happy to see the time is human readable local wall clock time and no longer in "nanseconds since the last reboot".In the resource view, once again, he sees many soft irqs being raised at the same time, around the time his GUI would freeze. He changes views and looks at the control flow view at that time and sees a process spending a lot of time in the kernel: FooMonitor- his temperature monitoring software.

At this point he closes FooMonitor and notices the bug disappeared. He could call it a day but he wants to see what was causing the system to freeze. He cannot justify closing a piece of software without understanding the issue. It may be a conflict that HIS software is causing after all.

The system freezes around the time this program is running. He clicks on the process in the control flow view and looks at the corresponding events in the detailed events view. He sees: open - read - close repeated hundreds of times on the same file. The file being read was /dev/HWmonitor. He sends a report to the FooMonitor team and warns his team that FooMonitor was glitching their performance.

The FooMonitor team finds that they were calling a system bus call that would halt a CPU while reading the temperature so that the core would not induce an 0.1 degree error in the reading, by disabling this feature, they improve their software and stop the glitches from occurring on their custommer's machine. They also optimize their code to open the file read and clone it once.

By using system wide kernel tracing, even without deep kernel knowledge Bob was able to isolate a bug in a rogue piece of software in his system.

## Slow I/O

Alice is running her server. She noticed that one of her nodes was slowing down, and wasn't sure why, upon reading the trace she noticed that her time between a block request and complete was around 10ms.

This is abnormal, normally her server handles IOs in under 100us, since they are quite local.

She walks up to the server and hears the hard drive thrashing, This prompts her to look up in the events view the sectors being read in the block complete requests. There are her requests interleaved with other ones at the opposite side of the hard drive.

She sees the tracer writing but there is another process that is writing to the server disk non stop. She looks in the control flow view and sees that there's a program from another fellow engineer, "Wally" that is writing in his home in a loop "All work and no play makes Jack a dull boy.".

Alice kills the program, and immediately the server speeds up. She then goes to discuss this with Wally and implements strict hard disk quotas on the server.