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