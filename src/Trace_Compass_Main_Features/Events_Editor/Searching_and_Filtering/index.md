### Searching and Filtering

Searching and filtering of events in the table can be performed by entering matching conditions in one or multiple columns in the header row (the first row below the column header).

To apply a matching condition to a specific column, click on the column's header row cell, type in aregular expression. You can also enter a simple text string and it will be automatically be replaced with a 'contains' regular expression.

Press theEnterkey to apply the condition as a search condition. It will be added to any existing search conditions.

Press theCtrl+Enterkey to immediately add the condition (and any other existing search conditions) as a filter instead.

When matching conditions are applied to two or more columns, all conditions must be met for the event to match (i.e. 'and' behavior).

A preset filter created in theFiltersview can also be applied by right-clicking on the table and selectingApply preset filter...>filter name

#### Searching

When a searching condition is applied to the header row, the table will select the next matching event starting from the top currently displayed event. Wrapping will occur if there is no match until the end of the trace.

All matching events will have a 'search match' icon in their left margin. Non-matching events will be dimmed. The characters in each column which match the regular expression will be highlighted.



Pressing theEnterkey will search and select the next matching event. Pressing theShift+Enterkey will search and select the previous matching event. Wrapping will occur in both directions.

PressEscto cancel an ongoing search.

To add the currently applied search condition(s) as filter(s), click theAdd as Filterbutton in the header row margin, or press theCtrl+Enterkey.

PressDeleteto clear the header row and reset all events to normal.

#### Filtering

When a new filter is applied, the table will clear all events and fill itself with matching events as they are found from the beginning of the trace. The characters in each column which match the regular expression will be highlighted.

A status row will be displayed before and after the matching events, dynamically showing how many matching events were found and how many events were processed so far. Once the filtering is completed, the status row icon in the left margin will change from a 'stop' to a 'filter' icon.



PressEscto stop an ongoing filtering. In this case the status row icon will remain as a 'stop' icon to indicate that not all events were processed.

The header bar will be displayed above the table and will show a label for each applied filter. Clicking on a label will highlight the matching strings in the events that correspond to this filter condition. Pressing theDeletekey will clear this highlighting.

To remove a specific filter, click on theicon on its label in the header bar. The table will be updated with the events matching the remaining filters.

The header bar can be collapsed and expanded by clicking on theicons in the top-left corner or on its background. In collapsed mode, a minimized version of the filter labels will be shown that can also be used to highlight or remove the corresponding filter.

Right-click on the table and selectClear Filtersfrom the context menu to remove all filters. All trace events will be now shown in the table. Note that the currently selected event will remain selected even after the filters are removed.

You can also search on the subset of filtered events by entering a search condition in the header row while a filter is applied. Searching and filtering conditions are independent of each other.

#### Bookmarking

Any event of interest can be tagged with a bookmark.

To add a bookmark, double-click the left margin next to an event, or right-click the margin and selectAdd bookmark.... Alternatively use theEdit>Add bookmark...menu. Edit the bookmark description as desired and pressOK.

The bookmark will be displayed in the left margin, and hovering the mouse over the bookmark icon will display the description in a tooltip.

The bookmark will be added to theBookmarksview. In this view the bookmark description can be edited, and the bookmark can be deleted. Double-clicking the bookmark or selectingGo tofrom its context menu will open the trace or experiment and go directly to the event that was bookmarked.

To remove a bookmark, double-click its icon, selectRemove Bookmarkfrom the left margin context menu, or selectDeletefrom the Bookmarks view.