## Events Editor

The Events editor shows the basic trace data elements (events) in a tabular format. The editors can be dragged in the editor area so that several traces may be shown side by side. These traces are synchronized by timestamp.



The header displays the current trace (or experiment) name.

The columns of the table are defined by the fields (aspects) of the specific trace type. These are the defaults:
- Timestamp: the event timestamp
- Event Type: the event type
- Contents: the fields (or payload) of this event
- Timestamp: the event timestamp
- Event Type: the event type
- Contents: the fields (or payload) of this event

The first row of the table is the header row a.k.a. the Search and Filter row.

The highlighted event is thecurrent eventand is synchronized with the other views. If you select another event, the other views will be updated accordingly. The properties view will display a more detailed view of the selected event.

An event range can be selected by holding theShiftkey while clicking another event or using any of the cursor keys (Up',Down,PageUp,PageDown,Home,End). The first and last events in the selection will be used to determine the current selected time range for synchronization with the other views.



The Events editor can be closed, disposing a trace. When this is done, all the views displaying the information will be updated with the trace data of the next event editor tab. If all the editor tabs are closed, then the views will display their empty states.

Column order and size is preserved when changed. If a column is lost due to it being resized to 0 pixels, right click on the context menu and selectShow All, it will be restored to a visible size.

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



### Copy to Clipboard

The text of selected events can be copied to the clipboard by right-clicking on the table and selectingCopy to Clipboardin the context menu. The clipboard contents will be prefixed by the column header names. For every event in the table selection, the column text will be copied to the clipboard. The column text will be tab-separated. Hidden columns will not be included in the clipboard contents.

### Event Source Lookup

Some trace types can optionally embed information in the trace to indicate the source of a trace event. This is accessed through the event context menu by right-clicking on an event in the table.

#### Source Code

If a source file is available in the trace for the selected event, the itemOpen Source Codeis shown in the context menu. Selecting this menu item will attempt to find the source file in all opened projects in the workspace. If multiple candidates exist, a selection dialog will be shown to the user. The selected source file will be opened, at the correct line, in its default language editor. If no candidate is found, an error dialog is shown displaying the source code information.

#### EMF Model

If an EMF model URI is available in the trace for the selected event, the itemOpen Model Elementis shown in the context menu. Selecting this menu item will attempt to open the model file in the project specified in the URI. The model file will be opened in its default model editor. If the model file is not found, an error dialog is shown displaying the URI information.

### Exporting To Text

It is possible to export the content of the trace to a text file based on the columns displayed in the events table. If a filter (seeFiltering) was defined prior exporting only events that match the filter will be exported to the file. To export the trace to text, press the right mouse button on the events table. A context-sensitive menu will show. Select theExport To Text...menu option. A file locater dialog will open. Fill in the file name and location and then press onOK. A window with a progress bar will open till the export is finished.

Note: The columns in the text file are separated by tabs.

### Refreshing of Trace

It's possible to refresh the content of the trace and resume indexing in case the current open trace was updated on the media. To refresh the trace, right-click into the table and select menu itemRefresh. Alternatively, press keyF5.

### Collapsing of Repetitive Events

The implementation for collapsing of repetitive events is trace type specific and is only available for certain trace types. For example, a trace type could allow collapsing of consecutive events that have the same event content but not the same timestamp. If a trace type supports this feature then it is possible to select theCollapse Eventsmenu item after pressing the right mouse button in the table.

When the collapsing of events is executing, the table will clear all events and fill itself with all relevant events. If the collapse condition is met, the first column of the table will show the number of times this event was repeated consecutively.



A status row will be displayed before and after the events, dynamically showing how many non-collapsed events were found and how many events were processed so far. Once the collapsing is completed, the status row icon in the left margin will change from a 'stop' to a 'filter' icon.



To remove the collapse filter, press the () icon on theCollapselabel in the header bar, or press the right mouse button in the table and select menu itemClear Filtersin the context sensitive menu (this will also remove any other filters).

### Customization

The table columns can be reordered by the user by dragging the column headers. This column order is saved when the editor is closed. The setting applies to all traces of the same trace type.

The table columns can be hidden or restored by right-clicking on any column header and clicking on an item in the context menu to toggle its state. ClickingShow Allwill restore all table columns.

The table font can be customized by the user by changing the preference inWindow>Preferences>General>Appearance>Colors and Fonts>Tracing>Trace event table font.

The search and filter highlight color can be customized by the user by changing the preference inWindow>Preferences>General>Appearance>Colors and Fonts>Tracing>Trace event table highlight color.