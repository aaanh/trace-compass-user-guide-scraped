## LTTng integration

One of the main features of Trace Compass is the LTTng integration. LTTng (Linux Trace Toolkit, next generation) is a highly efficient tracing tool for Linux that can be used to track down kernel and application performance issues as well as troubleshoot problems involving multiple concurrent processes and threads. It consists of a set of kernel modules, daemons - to collect the raw tracing data - and a set of tools to control, visualize and analyze the generated data. It also provides support for user space application instrumentation.
			For more information about LTTng, refer to the projectsite

Note: This User Guide covers the integration of the latest LTTng (up to v2.4) in Eclipse.

The LTTng plug-ins provide an integration for the control of the LTTng tracer as well as fetching and visualization of the traces produced. It also provides the foundation for user-defined analysis tools.

At present, the LTTng plug-ins support the following kernel-oriented views:
- Control Flow- to visualize processes state transitions
- Resources- to visualize system resources state transitions
- CPU Usage- to visualize the usage of the processor with respect to the time in traces
- Kernel Memory Usage- to visualize the relative usage of system memory
- IO Usage- to visualize the usage of input/output devices
- System Calls- presents all the system calls in a table view
- System Call Statistics- present all the system calls statistics
- System Call Density- to visualize the system calls displayed by duration
- System Call vs Time- to visualize when system calls occur
- Control Flow- to visualize processes state transitions
- Resources- to visualize system resources state transitions
- CPU Usage- to visualize the usage of the processor with respect to the time in traces
- Kernel Memory Usage- to visualize the relative usage of system memory
- IO Usage- to visualize the usage of input/output devices
- System Calls- presents all the system calls in a table view
- System Call Statistics- present all the system calls statistics
- System Call Density- to visualize the system calls displayed by duration
- System Call vs Time- to visualize when system calls occur

Also, the LTTng plug-ins supports the following User Space traces views:
- Memory Usage- to visualize the memory usage per thread with respect to time in the traces
- Call Stack- to visualize the call stack's evolution over time
- Function Duration Density- to visualize function calls displayed by duration
- Flame Graph- to visualize why the CPU is busy
- Memory Usage- to visualize the memory usage per thread with respect to time in the traces
- Call Stack- to visualize the call stack's evolution over time
- Function Duration Density- to visualize function calls displayed by duration
- Flame Graph- to visualize why the CPU is busy

Finally, the LTTng plug-ins supports the following Control views:
- Control- to control the tracer and configure the tracepoints
- Control- to control the tracer and configure the tracepoints

Although the control and fetching parts are targeted at the LTTng tracer, the underlying framework can also be used to process any trace that complies with theCommon Trace Format(CTF). CTF specifies a very efficient and compact binary trace format that is meant to be application-, architecture-, and language-agnostic.