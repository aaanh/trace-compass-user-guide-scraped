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