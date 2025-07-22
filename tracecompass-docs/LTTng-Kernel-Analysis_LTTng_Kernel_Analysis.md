# LTTng Kernel Analysis

Historically, LTTng was developed to trace the Linux kernel and, over time, a number of kernel-oriented analysis views were developed and organized in a perspective.

This section presents a description of theOS Tracing Overviewperspective and theLTTng Kernelperspective.

## OS Tracing Overview Perspective

TheOS Tracing Overviewperspective groups the following views:
- Project Explorer View
- Events Editor
- Histogram View
- CPU Usage View
- Disk I/O Activity View
- Kernel Memory Usage View
- Project Explorer View
- Events Editor
- Histogram View
- CPU Usage View
- Disk I/O Activity View
- Kernel Memory Usage View

The perspective can be opened from the Eclipse Open Perspective dialog (Window > Open Perspective... > Other).



This perspective is intended to be used to locate performance issues by observing resource usage.

The perspective can show times resource usage is anomalous. This can help locating the causes of system slowdowns in throughput or response time.

An example can be program that is doing a lot of processing then slows down due to a database access. The user will see a dip in CPU usage and maybe a slight rise in I/O access. The user should consider both spike and slums to be an indication of an area worth investigating.



Once a performance issue has been localized, it can be further investigated with the #LTTng kernel Perspective.

## LTTng Kernel Perspective

TheLTTng Kernelperspective is built upon theTracing Perspective, re-organizes them slightly and adds the following views:
- Control Flow View- to visualize processes state transitions
- Resources View- to visualize system resources state transitions
- LTTng Tracer Control- to configure LTTng tracing sessions remotely
- Control Flow View- to visualize processes state transitions
- Resources View- to visualize system resources state transitions
- LTTng Tracer Control- to configure LTTng tracing sessions remotely



The perspective can be opened from the Eclipse Open Perspective dialog (Window > Open Perspective... > Other).



## Control Flow View

TheControl Flowview is a LTTng-specific view that shows per-process events graphically. The Linux Kernel Analysis is executed the first time a LTTng Kernel is opened. After opening the trace, the elementControl Flowis added under theLinux Kernel Analysistree element in the Project Explorer. To open the view,  double-click theControl Flowtree element.



Alternatively, selectControl FlowunderLTTngwithin theShow Viewwindow (Window->Show View->Other...):

You should get something like this:



The view is divided into the following important sections:process tree and information,control flowand thetoolbar. The time axis is aligned with other views that support automatic time axis alignment (seeAutomatic Time Axis Alignment).

The following sections provide detailed information for each part of the Control Flow View.

### Process tree and information

Processes are organized as a tree within this view. This way, child and parent processes are easy to identify.



The layout is based on the states computed from the trace events.

A given process may be shown at different places within the tree since the nodes areunique (TID, birth time) couples. This means that if process B of parent A dies, you'll still see it in the tree. If process A forks process B again, it will be shown as a different node since it won't have the same birth time (and probably not the same TID). This has the advantage that the tree, once loaded, never changes: horizontal scrolling within thecontrol flowremains possible.

The TID column shows the process node'sthread IDand the PTID column shows itsparent thread ID(nothing is shown if the process has no parent).

It is possible to sort the columns of the tree by clicking on the column header. Subsequent clicking will change the sort order. The hierarchy, i.e. the parent-child relationship is kept. When opening a trace for the first time, the processes are sorted bybirth time. The sort order and column will be preserved when switching between open traces. Note that when opening an experiment the processes will be sorted within each trace.

### Control flow

This part of the Control Flow View is probably the most interesting one. Using the mouse, you can navigate through the trace (go left, right) and zoom on a specific region to inspect its details.

The colored bars you see representstatesfor the associated process node. When a process state changes in time, so does the color. For stateSYSCALLthe name of the system call is displayed in the state bar. States colors legend is available through atoolbar button:



The style can be updated in the legend.

This dark yellow is what you'll see most of the time since scheduling puts processes on hold while others run.

The vertical blue line with T1 above it is thecurrent selection indicator. When a time range is selected, the region between the begin and end time of the selection will be shaded and two lines with T1 and T2 above will be displayed. The time stamps corresponding to T1, T2 and their delta are shown in the status line when the mouse is hovering over the control flow.

Arrows can be displayed that follow the execution of each CPU across processes. The arrows indicate when the scheduler switches from one process to another for a given CPU. The CPU being followed is indicated on the state tooltip. When the scheduler switches to and from the idle process, the arrow skips to the next process which executes on the CPU after the idle process. Note that an appropriate zoom level is required for all arrows to be displayed.

The display of arrows is optional and can be toggled using theHide Arrowstoolbar button. It is also possible to follow a CPU's execution across state changes and the scheduler's process switching using theFollow CPU Forward/Backwardtoolbar buttons.

#### Using the mouse

The following mouse actions are available:
- left-click: select a time or time range begin time
- Shift-left-click or drag: Extend or shrink the selection range
- left-click: select a time or time range begin time
- Shift-left-click or drag: Extend or shrink the selection range
- left-drag horizontally: select a time range or change the time range begin or end time
- middle-drag or Ctrl-left-drag: pan horizontally and/or vertically
- right-drag horizontally:zoom region
- click on a colored bar: the associated process node is selected and the current time indicator is moved where the click happened
- mouse wheel up/down: scroll up or down
- Shift-mouse wheel up/down: scroll left or right
- Ctrl-mouse wheel up/down: zoom in or out horizontally
- Shift-Ctrl-mouse wheel up/down: zoom in or out vertically
- drag the time ruler horizontally: zoom in or out with fixed start time
- double-click the time ruler: reset zoom to full range
- left-drag horizontally: select a time range or change the time range begin or end time
- middle-drag or Ctrl-left-drag: pan horizontally and/or vertically
- right-drag horizontally:zoom region
- click on a colored bar: the associated process node is selected and the current time indicator is moved where the click happened
- mouse wheel up/down: scroll up or down
- Shift-mouse wheel up/down: scroll left or right
- Ctrl-mouse wheel up/down: zoom in or out horizontally
- Shift-Ctrl-mouse wheel up/down: zoom in or out vertically
- drag the time ruler horizontally: zoom in or out with fixed start time
- double-click the time ruler: reset zoom to full range

When the current time indicator is changed (when clicking in the states flow), all the other views aresynchronized. For example, theEvents Editorwill show the event matching the current time indicator. The reverse behaviour is also implemented: selecting an event within the Events View will update the Control Flow View current time indicator.

#### Using the keyboard

The following keyboard shortcuts are available:
- arrow-right key: selects the next state for the selected process
- arrow-left key: selects the previous state for the selected process
- Shift + arrow-right key: updates the selection end time of the current selection range by selecting the next state of the current process
- Shift + arrow-left key: updates the selection end time of the current selection range by selecting the previous state of the current process
- .: selects the next active marker
- ,: selects the previous active marker
- Shift + .: updates the selection end time of the current selection range by selecting the next active marker boundary
- Shift + ,: updates the selection end time of the current selection range by selecting the previous active marker boundary
- arrow-down: selects the next process
- arrow-up: selects the previous process
- Page Down: selects the process down one page
- Page Up: selects the process up one page
- Home: selects the first process
- End: selects the last process
- Enter: toggles the expansion state of the current process in the tree
- +: Zoom-in centered to the selected time range (or window range if time selection is not visible)
- -: Zoom-out centered to the selected time range (or window range if time selection is not visible)
- Ctrl + +: Zoom-in vertically
- Ctrl + -: Zoom-out vertically
- Ctrl + 0: Reset the vertical zoom
- Ctrl + F: Search in the view. (seeSearching in Time Graph Views)
- G: Toggles both vertical and horizontal gridlines
- Z: Zoom to current selected time range (if range is greater than 0)
- arrow-right key: selects the next state for the selected process
- arrow-left key: selects the previous state for the selected process
- Shift + arrow-right key: updates the selection end time of the current selection range by selecting the next state of the current process
- Shift + arrow-left key: updates the selection end time of the current selection range by selecting the previous state of the current process
- .: selects the next active marker
- ,: selects the previous active marker
- Shift + .: updates the selection end time of the current selection range by selecting the next active marker boundary
- Shift + ,: updates the selection end time of the current selection range by selecting the previous active marker boundary
- arrow-down: selects the next process
- arrow-up: selects the previous process
- Page Down: selects the process down one page
- Page Up: selects the process up one page
- Home: selects the first process
- End: selects the last process
- Enter: toggles the expansion state of the current process in the tree
- +: Zoom-in centered to the selected time range (or window range if time selection is not visible)
- -: Zoom-out centered to the selected time range (or window range if time selection is not visible)
- Ctrl + +: Zoom-in vertically
- Ctrl + -: Zoom-out vertically
- Ctrl + 0: Reset the vertical zoom
- Ctrl + F: Search in the view. (seeSearching in Time Graph Views)
- G: Toggles both vertical and horizontal gridlines
- Z: Zoom to current selected time range (if range is greater than 0)

WASD Navigation

Use WASD Navigation in conjunction with the mouse, where one hand changes the mouse
			position and the other hand uses the keyboard shortcuts to zoom or scroll.
- W: Zoom-in horizontally centered to the mouse position
- S: Zoom-out horizontally centered to the mouse position
- A: Scroll left by a quarter of the current window range
- D: Scroll right by a quarter of the current window range
- W: Zoom-in horizontally centered to the mouse position
- S: Zoom-out horizontally centered to the mouse position
- A: Scroll left by a quarter of the current window range
- D: Scroll right by a quarter of the current window range

When the mouse cursor is over entries (left pane):
- -: Collapse selected entry
- +: Expand selected entry
- *: Expand selected entry to the level with at least one collapsed entry
- -: Collapse selected entry
- +: Expand selected entry
- *: Expand selected entry to the level with at least one collapsed entry

Please note that the behavior of some shortcuts can slightly differ based on the operating system.

When the selection indicators are changed, all the other views aresynchronized. For example, theEvents Editorwill show the event matching the current time indicator. The reverse behaviour is also implemented: selecting an event within the Events View will update the Control Flow View current time indicator.

#### Incomplete regions

You'll noticesmall dotsover the colored bars at some places:



Those dots mean the underlying region isincomplete: there's not enough pixels to view all the events. In other words, you have to zoom in.

When zooming in, small dots start to disappear:



When no dots are left, you are viewingall the events and stateswithin that region.

#### Zoom region

To zoom in on a specific region,right-click and dragin order to draw a time range:



The states flow horizontal space will only show the selected region.

#### Tooltips

Hover the cursor over a colored bar and atooltipwill pop up:



The tooltip indicates:
- the process name
- the pointed state name
- the CPU (if applicable)
- the system call name (if applicable)
- the pointed state date and start/stop times
- the pointed state duration (seconds)
- the process name
- the pointed state name
- the CPU (if applicable)
- the system call name (if applicable)
- the pointed state date and start/stop times
- the pointed state duration (seconds)

A browser based tooltip is available that allows users to use hyperlink navigation or to copy text. To enable the feature select

Window->Preferences->Tracingthen checkingUse browser based tooltips. It is known to be unstable on older platforms, if this instability is encountered, please submit your bug here:https://bugs.eclipse.org/bugs/show_bug.cgi?id=547563



#### Dynamics Filters

Dynamic filters are filters that are processed and applied each time the control flow view visible time range changes.

The dynamics filters can be rapidly toggled in their view sub menu.



The dynamics filters  can be fine tuned in the configuration dialog.



Note: Dynamic filters can induce performance degradation.

##### Show Active Threads Only

The Show Active Threads Only filter allow a user to increase the signal to noise ratio by filtering out allinactivethreads.

A thread is considered inactive when it is in the following state:
- non-existing
- unknown
- wait and blocked
- wait and unknown
- non-existing
- unknown
- wait and blocked
- wait and unknown

A user can fine tune this filter by providing ranges of CPUs allowing the filter to only show active thread running on the specified CPUs.



### Toolbar

The Control Flow Viewtoolbar, located at the top right of the view, has shortcut buttons to perform common actions:

View Menu

### Marker Axis

The marker axis is visible only when at least one marker category with markers for the current trace is shown.

The marker axis displays one row per marker category. Each marker's time range and/or label (if applicable) are drawn on the marker axis.

Clicking on any marker's time range or label will set the current time selection to the marker's time or time range. Shift-clicking will extend the current time selection to include the marker's time or time range.

Clicking on the "X" icon to the left of the marker category name will hide this marker category from the time graph. It can be shown again using the correspondingShow Markersmenu item in the view menu.

The marker axis can be collapsed and expanded by clicking on the icon at the top left of the marker axis. The marker axis can be completely removed by hiding all available marker categories.

## Resources View

This view is specific to LTTng kernel traces.  The Linux Kernel Analysis is executed the first time a LTTng Kernel is opened. After opening the trace, the elementResourcesis added under theLinux Kernel Analysistree element of the Project Explorer. To open the view, double-click theResourcestree element.

Alternatively, go inWindow->Show View->Other...and selectLTTng/Resourcesin the list.



This view shows the state of system resources i.e. if changes occurred during the trace either onCPUs,IRQsorsoft IRQs, it will appear in this view. The left side of the view present a list of resources that are affected by at least one event of the trace. The right side illustrate the state in which each resource is at some point in time. For stateUSERMODEit also prints the process name in the state bar. For stateSYSCALLthe name of the system call is
			displayed in the state region.

When anIRQis handled by aCPU, its states are shown under the correspondingCPUentry. Similarly, theCPUthat was handling anIRQis shown under the handledIRQ. Therefore, the trace can be visualized from aCPUpoint of view or from anIRQpoint of view.

Just like other views, according to which trace points and system calls are activated, the content of this view may change from one trace to another.

The time axis is aligned with other views that support automatic time axis alignment (seeAutomatic Time Axis Alignment).

Each state are represented by one color so it is faster to say what is happening.



The style can be updated in the legend.

To go through the state of a resource, you first have to select the resource and the timestamp that interest you. For the latter, you can pick some time before the interesting part of the trace.



Then, by selectingNext Event, it will show the next state transition and the event that occurred at this time.



This view is also synchronized with the others:Histogram View,Events Editor,Control Flow View, etc.

### Follow CPU

It is possible to follow a CPU by right-clicking on its entry in the view, then selectingFollow CPU Xwhere X is the number of the CPU. Following a CPU will filter theCPU Usage Viewto display only usage for the selected CPU. To unfollow a CPU, one needs to right-click on any CPU entry and selectUnfollow CPU.

### Follow thread

It is possible to follow a thread by right-clicking on a thread time event in a CPU thread status line, then selectingFollow TID Xwhere X is the TID number of the thread to follow. Following a thread will display a red box around all the time events belonging to that specific thread. To unfollow a thread, one needs to right-click on any thread time event and selectUnfollow.



### Navigation

See Control Flow View'sUsing the mouse,Using the keyboardandZoom region.

### Incomplete regions

See Control Flow View'sIncomplete regions.

### Toolbar

The Resources Viewtoolbar, located at the top right of the view, has shortcut buttons to perform common actions:

View Menu

### Marker Axis

See Control Flow View'sMarker Axis.

## LTTng CPU Usage View

The CPU Usage analysis and view is specific to LTTng Kernel traces. The CPU usage is derived from a kernel trace as long as thesched_switchevent was enabled during the collection of the trace. This analysis is executed the first time that the CPU Usage view is opened after opening the trace. To open the view, double-click on theCPU Usagetree element under theLinux Kernel Analysistree element of the Project Explorer.



Now, the CPU Usage view will show:



The view is divided into the following important sections:Process Informationand theCPU Usage Chart. The time axis is aligned with other views that support automatic time axis alignment (seeAutomatic Time Axis Alignment).

### Process Information

The Process Information is displayed on the left side of the view and shows all threads that were executing on all available CPUs in the current time range. For each process, it shows in different columns the thread ID (TID), process name (Process), the average (%) execution time and the actual execution time (Time) during the current time range. It shows all threads that were executing on the CPUs in the current time range.

### CPU Usage Chart

The CPU Usage Chart on the right side of the view, plots the total time spent on all CPUs of all processes and the time of the selected process.

#### Tooltips

Hover the cursor over a line of the chart and a tooltip will pop up with the following information:
- Time: current time of mouse position
- total: The total CPU usage
- <process>: CPU usage of selected process
- Time: current time of mouse position
- total: The total CPU usage
- <process>: CPU usage of selected process



#### Using the mouse

The CPU Usage chart is usable with the mouse. The following actions are set:
- left-click: select a time or time range begin time
- Shift-left-click or drag: Extend or shrink the selection range
- left-drag horizontally: select a time range or change the time range begin or end time
- middle-drag or Ctrl-left-drag horizontally: pan left or right
- right-drag horizontally:zoom region
- Shift-mouse wheel up/down: scroll left or right
- Ctrl-mouse wheel up/down: zoom in or out horizontally
- left-click: select a time or time range begin time
- Shift-left-click or drag: Extend or shrink the selection range
- left-drag horizontally: select a time range or change the time range begin or end time
- middle-drag or Ctrl-left-drag horizontally: pan left or right
- right-drag horizontally:zoom region
- Shift-mouse wheel up/down: scroll left or right
- Ctrl-mouse wheel up/down: zoom in or out horizontally

#### Using the keyboard

The following keyboard shortcuts are available, when the mouse cursor is over the graph (right pane):
- +: Zoom-in horizontally centered to the selected time range (or window range if time selection is not visible)
- -: Zoom-out horizontally centered to the selected time range (or window range if time selection is not visible)
- Z: Zoom to the current selection time range, if the selection range is greater than 0
- +: Zoom-in horizontally centered to the selected time range (or window range if time selection is not visible)
- -: Zoom-out horizontally centered to the selected time range (or window range if time selection is not visible)
- Z: Zoom to the current selection time range, if the selection range is greater than 0

WASD Navigation

Use WASD Navigation in conjunction with the mouse, where one hand changes the mouse
			position and the other hand uses the keyboard shortcuts to zoom or scroll.
- W: Zoom-in horizontally centered to the mouse position
- S: Zoom-out horizontally centered to the mouse position
- A: Scroll left by a quarter of the current window range
- D: Scroll right by a quarter of the current window range
- W: Zoom-in horizontally centered to the mouse position
- S: Zoom-out horizontally centered to the mouse position
- A: Scroll left by a quarter of the current window range
- D: Scroll right by a quarter of the current window range

#### Toolbar

The viewtoolbar, located at the top right of the view, has shortcut buttons to perform common actions:

#### View Menu

The CPU Usage Viewview menu, located at the top right of the view, has shortcut buttons to perform common actions:

#### CPU Filtering

Follow a CPUwill filter the CPU Usage View and will display only usage for the followed CPU.

## Kernel Memory Usage View

The Kernel Memory Usage and view is specific to kernel traces. To open the view, double-click on theKernel Memory Usage Analysistree element under theKerneltree element of the Project Explorer.



Now, the Kernel memory usage view will show:



Where:
- TID: The ID of the thread this event belongs to
- Process: The process of the TID that belongs to it
- TID: The ID of the thread this event belongs to
- Process: The process of the TID that belongs to it

The view is divided into the following important sections:Process Informationand theRelative Kernel Memory Usage. The time axis is aligned with other views that support automatic time axis alignment (seeAutomatic Time Axis Alignment).

The filter button:can be used to show only the active threads in the tree viewer. By default only the threads which have had memory usage variations in the visible time range will be shown, clicking the button will reveal all the threads. Threads can be filtered by checking and unchecking them in the left hand side tree.

The time range can be set to fully zoomed out by double-clicking the time axis or the home button.

### Process Information

The Process Information is displayed on the left side of the view and shows all threads that were executing on all available CPUs in the current time range. For each process, it shows in different columns the thread ID (TID) and the process name (Process).

### Navigation

For navigation, see CPU Usage view'sUsing the mouse,Using the keyboardandZoom region.

### Toolbar

The viewtoolbar, located at the top right of the view, has shortcut buttons to perform common actions:

For other toolbar buttons, see CPU Usage view'sToolbar.

### View Menu

The Memory Usage Viewview menu, located at the top right of the view, has shortcut buttons to perform common actions:

### Relative Kernel Memory Chart

The Relative Kernel Memory Chart on the right side of the view plots the relative amount of memory that was allocated and deallocated during that period of time.

#### Navigation

For navigation, see CPU Usage view'sUsing the mouse,Using the keyboardandZoom region.

#### Tooltips

Hover the cursor over a line of the chart and a tooltip will pop up with the following information:
- time: current time of mouse position
- Total: The total CPU usage
- time: current time of mouse position
- Total: The total CPU usage



## Process Wait Analysis

TraceCompass can recover wait causes of local and distributed processes using operating system events. The analysis highlights the tasks and devices causing wait. Wait cause recovery is recursive, comprise all tasks running on the system and works across computers using packet trace synchronization.

The analysis details are available in the paperWait analysis of distributed systems using kernel tracing.

### Prerequisites

The analysis requires a Linux kernel trace. Additional instrumentation may be required for specific kernel version and for distributed tracing. This instrumentation is available inLTTng modules addonson GitHub.

The required events are:
- sched_switch, sched_wakeup: Scheduling events indicate when a process is blocked and the wake-up event indicates the task or resource that unblocked the task. For kernel versions comprised between 3.8 and 4.1, the eventsched_ttwu(which stands for Try To Wake-Up) is provided for backward compatibility in LTTng modules addons.
- IRQ, SoftIRQ and IPI: Interrupt events are required to distinguish the context of the wake-up. When a wake-up occurs inside an interrupt handler, it must be associated with the device causing the interrupt and not the interrupted task. For that reason, interrupt entry and exit events are required.
- inet_sock_local_in, inet_sock_local_out: The network events record a subset of TCP/IP packet header using a netfilter hook in the kernel. The send and receive events are matched to show the communication between distributed processes. Network events are mandatory for analyzing wait in TCP/IP programs, whether they are executing locally or on different computers. They also used to synchronize traces recorded on multiple computers. For further details, refer to theTrace synchronizationsection.
- sched_switch, sched_wakeup: Scheduling events indicate when a process is blocked and the wake-up event indicates the task or resource that unblocked the task. For kernel versions comprised between 3.8 and 4.1, the eventsched_ttwu(which stands for Try To Wake-Up) is provided for backward compatibility in LTTng modules addons.
- IRQ, SoftIRQ and IPI: Interrupt events are required to distinguish the context of the wake-up. When a wake-up occurs inside an interrupt handler, it must be associated with the device causing the interrupt and not the interrupted task. For that reason, interrupt entry and exit events are required.
- inet_sock_local_in, inet_sock_local_out: The network events record a subset of TCP/IP packet header using a netfilter hook in the kernel. The send and receive events are matched to show the communication between distributed processes. Network events are mandatory for analyzing wait in TCP/IP programs, whether they are executing locally or on different computers. They also used to synchronize traces recorded on multiple computers. For further details, refer to theTrace synchronizationsection.

To analyze a distributed program, all computers involved in the processing must be traced simultaneously. The LTTng Tracer Control of TraceCompass can trace a remote computer, but controlling simultaneous tracing is not supported at the moment, meaning that all sessions must be started separately and interactively. TraceCompass will support this feature in the future. For now, it is suggested to uselttng-clustercommand line tool to control simultaneous tracing sessions on multiple computers. This tool is based onFabricand uses SSH to start the tracing sessions, execute a workload, stop the sessions and gather traces on the local computer. For more information, refer to the lttng-cluster documentation.

We use theDjango traceas an example to demonstrate the wait analysis.Djangois a popular Web framework. The application is theDjango Poll app tutorial. The traces were recorded on three computers, namely the client (implemented with Python Mechanize), the Web server (Apache with WSGI) and the database server (PostgreSQL). The client simulates a vote in the poll.

### Running the analysis

To open all three traces simultaneously, we first create an experiment containing these traces and then synchronize the traces, such that they have a common time base. Then, the analysis is done by selecting a task in theControl Flow View. The result is displayed in theCritical Flow View, which works like theControl Flow View. The steps to load the Django example follows.
- Download and extract theDjango tracearchive.
- In TraceCompass, open theLTTng Kernel Perspective.
- Create a new tracing project. SelectFile -> New -> Tracing -> Tracing Project, choose a name and clickFinish.
- Under the created tracing project, right-click onTracesand selectImport.... In the import dialog, select the root directory containing the extracted trace by clicking onBrowse. Three traces should be listed. Select the traces and clickFinish. After the import is completed, the traces should be listed belowTraces.
- Right-click onExperiments, selectNew...and enter a name for the experiment, such asdjango.
- Right-click on thedjangoexperiment and click onSelect Traces.... In the dialog, check the three tracesdjango-client,django-httpdanddjango-db. These traces will appear below the experiment. If the experiment is opened at this stage, the traces are not synchronized and there will be a large time gap between events from different traces.
- To synchronize the traces, right-click on thedjangoexperiment and selectSynchronize Traces. In theSelect reference tracedialog, select any available trace and clickFinish. Once the synchronization is completed, a new entry with an underline suffix will appear for each modified trace. The created trace entries have a function which is applied to the timestamps of events in order to shift the time according to the reference trace. TheProject Explorerafter the import is shown below.
- Open the experimentdjango. TheControl Flowand theResourcesviews should display the three traces simultaneously.
- In the main menu, selectWindow -> Show View -> Other...and underLTTngselectCritical Flow View. The view is empty for the moment.
- In theCritical Flow View, right-click on theProcessentry to analyze and selectFollow, as shown in the figure below.The analysis will execute and the result will appear in theCritical Flow View. For the Django example, use theView Filtersto search for the python process with TID 2327. When zooming on the execution, the view displays the work done by the Web server and the database to process the request of the python client. Vertical arrows represent synchronization and communication between processes. The legenddisplays the colors associated with the processes states.
- Download and extract theDjango tracearchive.
- In TraceCompass, open theLTTng Kernel Perspective.
- Create a new tracing project. SelectFile -> New -> Tracing -> Tracing Project, choose a name and clickFinish.
- Under the created tracing project, right-click onTracesand selectImport.... In the import dialog, select the root directory containing the extracted trace by clicking onBrowse. Three traces should be listed. Select the traces and clickFinish. After the import is completed, the traces should be listed belowTraces.
- Right-click onExperiments, selectNew...and enter a name for the experiment, such asdjango.
- Right-click on thedjangoexperiment and click onSelect Traces.... In the dialog, check the three tracesdjango-client,django-httpdanddjango-db. These traces will appear below the experiment. If the experiment is opened at this stage, the traces are not synchronized and there will be a large time gap between events from different traces.
- To synchronize the traces, right-click on thedjangoexperiment and selectSynchronize Traces. In theSelect reference tracedialog, select any available trace and clickFinish. Once the synchronization is completed, a new entry with an underline suffix will appear for each modified trace. The created trace entries have a function which is applied to the timestamps of events in order to shift the time according to the reference trace. TheProject Explorerafter the import is shown below.
- Open the experimentdjango. TheControl Flowand theResourcesviews should display the three traces simultaneously.
- In the main menu, selectWindow -> Show View -> Other...and underLTTngselectCritical Flow View. The view is empty for the moment.
- In theCritical Flow View, right-click on theProcessentry to analyze and selectFollow, as shown in the figure below.The analysis will execute and the result will appear in theCritical Flow View. For the Django example, use theView Filtersto search for the python process with TID 2327. When zooming on the execution, the view displays the work done by the Web server and the database to process the request of the python client. Vertical arrows represent synchronization and communication between processes. The legenddisplays the colors associated with the processes states.



## Input/Output Analysis

TraceCompass can analyse disk input/output through the read/write system calls to get the read/write per processes, but also with the disk request events, to get the actual reads and writes to disk.

### Get the trace

The following tracepoints should be enabled to get the disk read/write data. Also, enabling syscalls will allow to match the reads and writes per processes.

For full disk request tracking, some extra tracepoints are necessary. They are not required for the I/O analysis, but make the analysis more complete. Here is the procedure to get those tracepoints that are not yet part of the mainline kernel.

Checkout the addons branch, compile and install lttng-modules as per the lttng-modules documentation.

The lttng addons modules must be inserted manually for the extra tracepoints to be available:

And enable the following tracepoint

### Input/Output Views

The following views are available for input/output analyses:

#### Disk I/O Activity View

A time aligned XY chart of the read and write speed for the different disks on the system. This view is useful to see where there was more activity on the disks and whether it was mostly reads or writes.

Disk reads and writes can be selected in the tree on the left hand side.

The time range can be reset by double-clicking the time axis or by clicking the reset button.

#### Navigation

For navigation, see CPU Usage view'sUsing the mouse,Using the keyboardandZoom region.

#### Toolbar

The viewtoolbar, located at the top right of the view, has shortcut buttons to perform common actions.

For details about the see CPU Usage view'sToolbar.

#### View Menu

The Disk I/O Viewview menu, located at the top right of the view, has shortcut buttons to perform common actions:

## System Call Latency Analysis

TheSystem Call Latency Analysismeasures the system call latency between system call entry and exit per type of system call. The durations are visualized using theLatencyviews. For more information about theLatencyviews see chapterLatency Analyses.

## Futex Contention Latency Analysis

TheFutex Contention Latency Analysismeasures the futexes contention latency between futex entry and exit event for a thread. The durations are visualized using theLatencyviews. For more information about theLatencyviews see chapterLatency Analyses.

The following views are also available for the Futex Contention Latency Analysis:

### Uaddr vs Waiter

A timegraph view of the waiters by futex uaddr. This view is useful to see which threads are waiting on a specific futex and understand blocked threads.



### Scenarios

A timegraph view of the futex wait/lock and wake/unlock scenarios (from futex entry to futex exit). This view is useful to suss up the general level of contention in a given trace. It highlights futex lifespans.



## Latency analysis for IRQ handlers

TheLatency analysis for IRQ handlersmeasures the latency between the IRQ handlers entry and exit events.
			The durations are visualized using theLatencyviews. For more information about theLatencyviews see chapterLatency Analyses.

## LTTng Kernel Events Editor

The LTTng Kernel Events editoristhe plain TMFEvents Editor, except that it provides its own specialized viewer to replace the standard one. In short, it has exactly the same behaviour but the layout is slightly different:
- Timestamp: the event timestamp
- Channel: the event channel (data collector)
- CPU: the CPU on which the event was taken
- Event Type: the event type (or kernel marker)
- Contents: the fields (or payload) of this event
- TID: The ID of the thread this event belongs to
- Prio: The priority of the thread this event belongs to
- Timestamp: the event timestamp
- Channel: the event channel (data collector)
- CPU: the CPU on which the event was taken
- Event Type: the event type (or kernel marker)
- Contents: the fields (or payload) of this event
- TID: The ID of the thread this event belongs to
- Prio: The priority of the thread this event belongs to



## Scheduler wake up/Scheduler switch Latency Analysis

TheScheduler wake up/Scheduler switch Latency Analysismeasures the latency between the sched_wakeup (scheduler wake up) and sched_switch (scheduler switch) event. In layman's terms, the analysis measures the time from the moment a process/thread wakes up until it is switched onto the CPU. The durations are visualized using theLatencyviews. For more information about theLatencyviews see chapterLatency Analyses.

Besides the typical latency views, the analysis also provides a Priority/Thread name Statistics view. The view groups latencies using thread names and priorities, and provides statistics for these groups.