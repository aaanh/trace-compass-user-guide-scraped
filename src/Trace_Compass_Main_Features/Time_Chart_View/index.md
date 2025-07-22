## Time Chart View



The Time Chart view allows the user to visualize every open trace in a common time chart. Each trace is display in its own row and ticks are display for every punctual event. As the user zooms using the mouse wheel or by right-clicking and dragging in the time scale, more detailed event data is computed from the traces. The time axis is aligned with other views that support automatic time axis alignment (seeAutomatic Time Axis Alignment).

Time synchronization is enabled between the time chart view and other trace viewers such as the events table.

Color settings defined in the Colors view can be used to change the tick color of events displayed in the Time Chart view.

When a search is applied in the events table, the ticks corresponding to matching events in the Time Chart view are decorated with a marker below the tick.

When a bookmark is applied in the events table, the ticks corresponding to the bookmarked event in the Time Chart view is decorated with a bookmark above the tick.

When a filter is applied in the events table, the non-matching ticks are removed from the Time Chart view.

The Time Chart only supports traces that are opened in an editor. The use of an editor is specified in the plug-in extension for that trace type, or is enabled by default for custom traces.

TheAlign Viewstoggle buttonin the view menu allows to disable and enable the automatic time axis alignment of time-based views. Disabling the alignment in the this view will disable this feature across all the views because it's a workspace preference.