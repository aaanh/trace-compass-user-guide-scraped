## Memory Usage

The Memory Usage view allows the user to visualize the active memory usage per thread over time, if the application and trace provide this information.

The view shows the memory consumption for the currently selected trace.

The time chart plots heap memory usage graphically over time. There is one line per process, unassigned memory usage is mapped to "Other". Processes can be checked and unchecked in the tree on the left hand side.

The filter button:can be used to show only the active threads in the tree viewer. By default only the threads which have had memory usage variations in the visible time range will be shown, clicking the button will reveal all the threads.

In this implementation, the user needs to trace while hooking theliblttng-ust-libc-wrapperby runningLD_PRELOAD=liblttng-ust-libc-wrapper.so<exename>. This will add tracepoints to memory allocation and freeing to the heap, NOT shared memory or stack usage. If the contextsvtidandprocnameare enabled, then the view will associate the heap usage to processes. As detailed earlier, to enable the contexts, see theAdding Contexts to Channels and Events of a Domainsection. Or if using the command-line:
- lttng add-context -u -t vtid -t procname
- lttng add-context -u -t vtid -t procname

If thread information is available the view will look like this:



If thread information is not available it will look like this:



The time axis is aligned with other views that support automatic time axis alignment (seeAutomatic Time Axis Alignment).

The time range can be fully zoomed out by double-clicking the time axis or the home button.

Please note this view will not show shared memory or stack memory usage.

### Navigation

For navigation, see CPU Usage view'sUsing the mouse,Using the keyboardandZoom region.

### Toolbar

The viewtoolbar, located at the top right of the view, has shortcut buttons to perform common actions.

For details about the see CPU Usage view'sToolbar.

### View Menu

The Memory Usage Viewview menu, located at the top right of the view, has shortcut buttons to perform common actions:



Please note this view will not show shared memory or stack memory usage.