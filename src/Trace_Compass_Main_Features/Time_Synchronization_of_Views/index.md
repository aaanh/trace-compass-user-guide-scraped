## Time Synchronization of Views

All time-based views that show the same trace are synchronized in time to show the same window range and time selection. This also applies to the selected event(s) in theEvents Editor.

By default, changing the window range or time selection for one trace does not affect the window range or time selection of other opened traces.

To allow a specific trace to be synchronized with (and react to) the window range or time selection from other traces, check theFollow time updates from other tracestoggle option in that trace'sEvent Editorcontext menu. This does not affect whether this trace's time updates will be propagated to other traces.

Time synchronization will only occur if the updated window range or time selection from the other trace overlaps with the full time range of the following trace. It will occur even if the following trace is not the active trace.

Note that two opened instances of the same trace are never time synchronized with each other, regardless of the toggle option.