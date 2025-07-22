## Statistics View

The Statistics View displays the various event counters that are collected when analyzing a trace. After opening a trace, the elementStatisticsis added under theTmf Statistics Analysistree element in the Project Explorer. To open the view, double-click theStatisticstree element. Alternatively, selectStatisticsunderTracingwithin theShow Viewwindow (Window->Show View->Other...). The statistics is collected for the whole trace. This view is part of theTracing and Monitoring Framework (TMF)and is generic. It will work for any trace type extensions.

The view is separated in two sides. The left side of the view presents the Statistics in a table. The table shows 3 columns:LevelEvents totalandEvents in selected time range. The data is organized per trace. After parsing a trace the view will display the number of events per event type in the second column and in the third, the currently selected time range's event type distribution is shown. The cells where the number of events are printed also contain a colored bar with a number that indicates the percentage of the event count in relation to the total number of events.



The right side illustrates the proportion of types of events into two pie charts. The legend of each pie chart gives the representation of each color in the chart.
- TheGlobalpie chart displays the general proportion of the events in the trace.
- When there is a range selection, theEvents in selectionpie chart appears next to theGlobalpie chart and displays the proportion the event in the selected range of the trace.
- TheGlobalpie chart displays the general proportion of the events in the trace.
- When there is a range selection, theEvents in selectionpie chart appears next to theGlobalpie chart and displays the proportion the event in the selected range of the trace.



By default, the statistics use a state system, therefore will load very quickly once the state system is written to the disk as a supplementary file.