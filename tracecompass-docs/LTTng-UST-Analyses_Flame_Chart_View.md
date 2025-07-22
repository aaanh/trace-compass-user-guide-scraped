## Flame Chart View

The Flame Chart view allows the user to visualize the call stack per thread over time, if the application and trace provide this information.

To open this view go inWindow->Show View, if in the eclipse plug-in then clickOther...and selectTracing/Flame Chartin the list. The view shows the call stack information for the currently selected trace. Conversely, you can select a trace and expand it in theProject Explorerthen expandLTTng-UST CallStack Analysis(the trace must be loaded) and openFlame Chart.

The table on the left-hand side of the view shows the threads and call stack. The function name, depth, entry and exit time and duration are shown for the call stack at the selected time.

Double-clicking on a function entry in the table will zoom the time graph to the selected function's range of execution.

The time graph on the right-hand side of the view shows the call stack state graphically over time. The function name is visible on each call stack event if size permits. The color of each call stack event is randomly assigned based on the function name, allowing for easy identification of repeated calls to the same function.

Clicking on the time graph will set the current time and consequently update the table with the current call stack information.

Shift-clicking on the time graph will select a time range. When the selection is a time range, the begin time is used to update the stack information.

Double-clicking on a call stack event will zoom the time graph to the selected function's range of execution.

Clicking theSelect Next State ChangeorSelect Previous State Changeor using the left and right arrows will navigate to the next or previous call stack event, and select the function currently at the top of the call stack. Note that pressing theShiftkey at the same time will update the selection end time of the current selection.

Clicking theConfigure how addresses are mapped to function names() icon will open the symbol providers dialog. Depending on the available symbol providers for the given trace, you can specify: 1) a text or binary file containing mappings from function addresses to function names or 2) the root location of the binaries of the trace target. If the call stack provider for the current trace type only provides function addresses, a mapping file will be required to get the function names in the view. See the following sections for an example with LTTng-UST traces.

### Using the Flame Chart View with LTTng-UST traces

There is support in the LTTng-UST integration plugin to display the callstack
			of applications traced with theliblttng-ust-cyg-profile.solibrary (see
			theliblttng-ust-cyg-profileman page for additional information). To do
			so, you need to:
- Recompile your application with "-g -finstrument-functions".
- Set up a tracing session with the thevpid,vtidandprocnamecontexts. See theEnabling UST Events On Session LevelandAdding Contexts to Channels and Events of a Domainsections. Or if using the command-line:lttng enable-event -u -alttng add-context -u -t vpid -t vtid -t procname
- lttng enable-event -u -a
- lttng add-context -u -t vpid -t vtid -t procname
- Preload theliblttng-ust-cyg-profilelibrary when running your program:LD_PRELOAD=/usr/lib/liblttng-ust-cyg-profile.so ./myprogram
- LD_PRELOAD=/usr/lib/liblttng-ust-cyg-profile.so ./myprogram
- Recompile your application with "-g -finstrument-functions".
- Set up a tracing session with the thevpid,vtidandprocnamecontexts. See theEnabling UST Events On Session LevelandAdding Contexts to Channels and Events of a Domainsections. Or if using the command-line:lttng enable-event -u -alttng add-context -u -t vpid -t vtid -t procname
- lttng enable-event -u -a
- lttng add-context -u -t vpid -t vtid -t procname
- lttng enable-event -u -a
- lttng add-context -u -t vpid -t vtid -t procname
- lttng enable-event -u -a
- lttng add-context -u -t vpid -t vtid -t procname
- Preload theliblttng-ust-cyg-profilelibrary when running your program:LD_PRELOAD=/usr/lib/liblttng-ust-cyg-profile.so ./myprogram
- LD_PRELOAD=/usr/lib/liblttng-ust-cyg-profile.so ./myprogram
- LD_PRELOAD=/usr/lib/liblttng-ust-cyg-profile.so ./myprogram
- LD_PRELOAD=/usr/lib/liblttng-ust-cyg-profile.so ./myprogram

Once you load the resulting trace, the Flame Chart View should be populated with
			the relevant information.

Note that for non-trivial applications,liblttng-ust-cyg-profilegenerates alotof events! You may need to increase the channel's subbuffer size to
			avoid lost events. Refer to theLTTng documentation.

For traces taken with LTTng-UST 2.8 or later, the Flame Chart View should show the
			function names automatically, since it will make use of the debug information
			statedump events (which are enabled when usingenable-event -u -a).

For traces taken with prior versions of UST, you would need to set the path to
			the binary file or mapping manually:

### Importing a binary or function name mapping file (for LTTng-UST <2.8 traces)

For LTTng-UST 2.8+, if it doesn't resolve symbols automatically, see theSource Lookup's Binary file location configuration.

If you followed the steps in the previous section, you should have a Flame Chart
			View populated with function entries and exits. However, the view will display
			the function addresses instead of names in the intervals, which are not very
			useful by themselves. To get the actual function names, you need to:
- Click theConfigure how addresses are mapped to function names() button in the Flame Chart View.
- Click theConfigure how addresses are mapped to function names() button in the Flame Chart View.

Once again, multiple symbol providers can be available for a unique trace. Each symbol provider can be configured through its own tab. Thus, multiple sources can be used to map the function names to addresses. Below is an image of the basic symbol provider preference page which allows us to import binary or function name mapping files.



Simply click theAdd...button to add one or multiple mapping files. The mapping file could be one of two options:
- : a binary that was used for taking the trace.
- : a binary that was used for taking the trace.
- : a file generated from the binary usingnm myprogram > mapping.txt. Select themapping.txtfile that was just created. If you are dealing with C++ executables, you may want to usenm --demangleinstead to get readable function names.
- : a file generated from the binary usingnm myprogram > mapping.txt. Select themapping.txtfile that was just created. If you are dealing with C++ executables, you may want to usenm --demangleinstead to get readable function names.

The view should now update to display the function names instead. Make sure the
			binary used for taking the trace is the one used for this step too (otherwise,
			there is a good chance of the addresses not being the same).

Lastly, the basic symbol provider introduces the notion of priorities between the mapping files. The resolved symbols from the file at the top of the list will have a higher priority than the files listed below. The files can be moved using theUpandDownbuttons.

### Navigation

See Control Flow View'sUsing the mouse,Using the keyboardandZoom region.

### Marker Axis

See Control Flow View'sMarker Axis.