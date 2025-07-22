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