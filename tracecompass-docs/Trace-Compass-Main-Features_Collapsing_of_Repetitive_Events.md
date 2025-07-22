### Collapsing of Repetitive Events

The implementation for collapsing of repetitive events is trace type specific and is only available for certain trace types. For example, a trace type could allow collapsing of consecutive events that have the same event content but not the same timestamp. If a trace type supports this feature then it is possible to select theCollapse Eventsmenu item after pressing the right mouse button in the table.

When the collapsing of events is executing, the table will clear all events and fill itself with all relevant events. If the collapse condition is met, the first column of the table will show the number of times this event was repeated consecutively.



A status row will be displayed before and after the events, dynamically showing how many non-collapsed events were found and how many events were processed so far. Once the collapsing is completed, the status row icon in the left margin will change from a 'stop' to a 'filter' icon.



To remove the collapse filter, press the () icon on theCollapselabel in the header bar, or press the right mouse button in the table and select menu itemClear Filtersin the context sensitive menu (this will also remove any other filters).