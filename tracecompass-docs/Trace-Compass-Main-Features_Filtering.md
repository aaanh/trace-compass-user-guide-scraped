#### Filtering

When a new filter is applied, the table will clear all events and fill itself with matching events as they are found from the beginning of the trace. The characters in each column which match the regular expression will be highlighted.

A status row will be displayed before and after the matching events, dynamically showing how many matching events were found and how many events were processed so far. Once the filtering is completed, the status row icon in the left margin will change from a 'stop' to a 'filter' icon.



PressEscto stop an ongoing filtering. In this case the status row icon will remain as a 'stop' icon to indicate that not all events were processed.

The header bar will be displayed above the table and will show a label for each applied filter. Clicking on a label will highlight the matching strings in the events that correspond to this filter condition. Pressing theDeletekey will clear this highlighting.

To remove a specific filter, click on theicon on its label in the header bar. The table will be updated with the events matching the remaining filters.

The header bar can be collapsed and expanded by clicking on theicons in the top-left corner or on its background. In collapsed mode, a minimized version of the filter labels will be shown that can also be used to highlight or remove the corresponding filter.

Right-click on the table and selectClear Filtersfrom the context menu to remove all filters. All trace events will be now shown in the table. Note that the currently selected event will remain selected even after the filters are removed.

You can also search on the subset of filtered events by entering a search condition in the header row while a filter is applied. Searching and filtering conditions are independent of each other.