# Counters Analysis

TheCounters Viewallows the user to inspect the values of hardware performance counters during the trace's lifetime. The counters store data concerning hardware-related activities such as page faults. The Counters View is currently available for LTTng UST and kernel traces.
			The Counters View supports experiments.

## Creating an LTTng trace with performance counters

For the Counters View to display any data, the trace needs to collect information related to performance counters. There are two ways to configure a trace for this type of logging. On the command line, add a new context field to an LTTng channel using thelttng-add-contextcommand (for more information, refer to theLTTng documentation). On the LTTng Tracer Control, add a new context field using the ''Add Context..." window (seeAdding Contexts to Channels and Events of a Domain).

## Counters View

To open the view, double-click on theCounterstree element of theProject Exploreror type "Counters" in theQuick Accesssearch bar.



The Counters View contains a filtered checkbox tree on the left-hand side and a chart on the right-hand side. The checkbox tree also contains aLegendcolumn whose purpose is to display the styling of the entry in the chart. Thus, when checking a tree element, its data will appear in the chart and its styling will appear next to the element. An entry will conserve the same styling whether it is displayed on the chart or not.



The counters data can also be visualized cumulatively throughout time thanks to thetool bar button.
			By default the view is displayed differentially, with each data point's value being the counter value at that point's timestamp minus that of the previous point's timestamp.



The view's checkbox tree has enhanced functionalities. First, the checkboxes have three visual states. They are determined according to the visible elements of the tree.

- The entry is not checked.- The entry is checked, but not all of its children.- The entry and all of its children are checked.

Second, the checkbox tree has a search bar which allows users to apply filters on the tree elements. Multiple filters need to be separated with the "/" symbol. A match is detected when the subsequence of a tree element matches the pattern entered by the user. When checking an element of a filtered tree, the check state is only propagated to the visible elements. Below are different examples of filters being applied to the same tree:



Finally, the tree's checkboxes are remembered when switching from one trace to another.

### Navigation

For navigation, see CPU Usage view'sUsing the mouse,Using the keyboardandZoom region.

### Toolbar

The viewtoolbar, located at the top right of the view, has shortcut buttons to perform common actions:

For other toolbar buttons, see CPU Usage view'sToolbar.

### View Menu

The Counters Viewview menu, located at the top right of the view, has shortcut buttons to perform common actions: