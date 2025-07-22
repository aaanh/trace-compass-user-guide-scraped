## Histogram View

The Histogram View displays the trace events distribution with respect to time. When streaming a trace, this view is dynamically updated as the events are received. The time axis is aligned with other views that support automatic time axis alignment (seeAutomatic Time Axis Alignment).



TheAlign Viewstoggle buttonin the view menu allows to disable and enable the automatic time axis alignment of time-based views. Disabling the alignment in the Histogram view will disable this feature across all the views because it's a workspace preference.

TheHide Lost Eventstoggle buttonin the local toolbar allows to hide the bars of lost events. When the button is selected it can be toggled again to show the lost events.

TheActivate Trace Coloringtoggle buttonin the local toolbar allows to use separate colors for each trace of an experiment. Note that this feature is not available if your experiment contains more than twenty two traces. When activated, a legend is displayed at the bottom on the histogram view.

On the top left, there are three text controls:
- Selection Start: Displays the start time of the current selection
- Selection End: Displays the end time of the current selection
- Window Span: Displays the current zoom window size in seconds
- Selection Start: Displays the start time of the current selection
- Selection End: Displays the end time of the current selection
- Window Span: Displays the current zoom window size in seconds

The controls can be used to modify their respective value. After validation, the other controls and views will be synchronized and updated accordingly. To modify both selection times simultaneously, press the link iconwhich disables theSelection Endcontrol input.

The large (full) histogram, at the bottom, shows the event distribution over the whole trace or set of traces. It also has a smaller semi-transparent orange window, with a cross-hair, that shows the current zoom window.

The smaller (zoom) histogram, on top right, corresponds to the current zoom window, a sub-range of the event set. The window size can be adjusted by dragging the sash left beside the zoom window.

The x-axis of each histogram corresponds to the event timestamps. The axis is now the same as the other views for a better visualization of the range. The y-axis shows the maximum number of events in the corresponding histogram bars.

The vertical blue line(s) show the current selection time (or range). If applicable, the region in the selection range will be shaded. In addition, when a selection is performed the status line (line placed at the very left bottom corner of Trace Compass) is now updated with the cursor position, the selection time or range and the delta for a range.



The mouse can be used to control the histogram:
- Left-click: Set a selection time
- Left-drag: Set a selection range
- Shift-left-click or drag: Extend or shrink the selection range
- Left-click: Set a selection time
- Left-drag: Set a selection range
- Shift-left-click or drag: Extend or shrink the selection range
- Middle-click or Ctrl-left-click: Center the zoom window on mouse (full histogram only)
- Middle-drag or Ctrl-left-drag: Move the zoom window
- Middle-click or Ctrl-left-click: Center the zoom window on mouse (full histogram only)
- Middle-drag or Ctrl-left-drag: Move the zoom window
- Right-drag: Set the zoom window
- Shift-right-click or drag: Extend or shrink the zoom window (full histogram only)
- Right-drag: Set the zoom window
- Shift-right-click or drag: Extend or shrink the zoom window (full histogram only)
- Mouse wheel up: Zoom in
- Mouse wheel down: Zoom out
- Mouse wheel up: Zoom in
- Mouse wheel down: Zoom out

Hovering the mouse over an histogram bar pops up an information window that displays the start/end time of the corresponding bar, as well as the number of events (and lost events) it represents. If the mouse is over the selection range, the selection span in seconds is displayed.

In each histogram, the following keys are handled:
- Left Arrow: Moves the current event to the previous non-empty bar
- Right Arrow: Moves the current event to the next non-empty bar
- Home: Sets the current time to the first non-empty bar
- End: Sets the current time to the last non-empty histogram bar
- Plus (+): Zoom in
- Minus (-): Zoom out
- Left Arrow: Moves the current event to the previous non-empty bar
- Right Arrow: Moves the current event to the next non-empty bar
- Home: Sets the current time to the first non-empty bar
- End: Sets the current time to the last non-empty histogram bar
- Plus (+): Zoom in
- Minus (-): Zoom out