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