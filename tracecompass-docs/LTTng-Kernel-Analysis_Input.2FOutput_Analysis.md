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