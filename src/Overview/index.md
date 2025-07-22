# Overview

Trace Compass is a Java tool for viewing and analyzing any type of logs or traces. Its goal is to provide views, graphs, metrics, etc. to help extract useful information from traces, in a way that is more user-friendly and informative than huge text dumps.

## About Tracing

Tracing is a troubleshooting technique used to understand the behavior of an instrumented application by collecting information on its execution path. A tracer is the software used for tracing. Tracing can be used to troubleshoot a wide range of bugs that are otherwise extremely challenging. These include, for example, performance problems in complex parallel systems or real-time systems.

Tracing is similar to logging: it consists in recording events that happen in a system at selected execution locations. However, compared to logging, it is generally aimed at developers and it usually records low-level events at a high rate. Tracers can typically generate thousands of events per second. The generated traces can easily contain millions of events and have sizes from many megabytes to tens of gigabytes. Tracers must therefore be optimized to handle a lot of data while having a small impact on the system.

Traces may include events from the operating system kernel (IRQ handler entry/exit, system call entry/exit, scheduling activity, network activity, etc). They can also consists of application events (a.k.a UST - User Space Tracing) or a mix of the two.

For the maximum level of detail, tracing events may be viewed like a log file. However, trace analyzers and viewers are available to derive useful information from the raw data coupled with knowledge of the traced program. These programs must be specially designed to handle quickly the enormous amount of data a trace may contain.

Warning: Please be aware tracing is a powerful tool. It can extract information and make problems obvious, it can do the same with user information. The user is responsible for making sure the data provided to Trace Compass is used responsibly. Trace Compass can read whatever is provided to it. This can mean in the context of tracing certain identifiable fields e.g.: user names, IP addresses, file names, file access patterns, and web access patterns can be seen. The user needs to apply caution with the data it is providing the tool, as well as remembering to delete old data regularly and when a user requests it.

## Features

Trace Compass has a number of features to allow efficient handling of very large traces (and sets of large traces):
- Support for arbitrarily large traces (larger than available memory)
- Support for correlating multiple time-ordered traces
- Support for zooming down to the nanosecond on any part of a trace or set of traces
- Views synchronization of currently selected time or time range, and window time range
- Efficient searching and filtering of events
- Support for trace bookmarks
- Support for importing and exporting trace packages
- Support for arbitrarily large traces (larger than available memory)
- Support for correlating multiple time-ordered traces
- Support for zooming down to the nanosecond on any part of a trace or set of traces
- Views synchronization of currently selected time or time range, and window time range
- Efficient searching and filtering of events
- Support for trace bookmarks
- Support for importing and exporting trace packages

There is also support for the integration of non-LTTng trace types:
- Built-in CTF parser
- Dynamic creation of customized parsers (for XML and text traces)
- Dynamic creation of customized state systems (from XML files)
- Dynamic creation of customized views (from XML files)
- Built-in CTF parser
- Dynamic creation of customized parsers (for XML and text traces)
- Dynamic creation of customized state systems (from XML files)
- Dynamic creation of customized views (from XML files)

Trace Compass provides the following main views:
- Project Explorer- an extension to the standard Eclipse Project view tailored for tracing projects
- Events- a versatile view that presents the raw events in tabular format with support for searching, filtering and bookmarking
- Statistics- a view that that provides simple statistics on event occurrences by type
- Histogram- a view that displays the event density with respect to time in traces
- Project Explorer- an extension to the standard Eclipse Project view tailored for tracing projects
- Events- a versatile view that presents the raw events in tabular format with support for searching, filtering and bookmarking
- Statistics- a view that that provides simple statistics on event occurrences by type
- Histogram- a view that displays the event density with respect to time in traces

These views can be extended or tailored for specific trace types (e.g. kernel, HW, user app).

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