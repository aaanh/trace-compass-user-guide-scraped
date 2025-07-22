## Defining an XML time graph view

A time graph view is a view divided in two, with a tree viewer on the left showing information on the different entries to display and a Gantt-like viewer on the right, showing the state of the entries over time. TheControl Flow Viewis an example of a time graph view.

Such views can be defined in XML using the data in the state system. The state system itself could have been built by an XML-defined state provider or by any predefined Java analysis. It only requires knowing the structure of the state system, which can be explored using theState System Explorer View(or programmatically using the methods inITmfStateSystem).

In the example above, suppose we want to display the status for each task. In the state system, it means the path of the entries to display is "Tasks/*". The attribute whose value should be shown in the Gantt chart is the entry attribute itself. So the XML to display these entries would be as such:

But first, the view has to be declared. It has an ID, to uniquely identify this view among all the available XML files.

Optional header information can be added to the view.analysiselements will associate the view only to the analysis identified by the "id" attribute. It can be either the ID of the state provider, like in this case, or the analysis ID of any analysis defined in Java. If no analysis is specified, the view will appear under every analysis with a state system. Thelabelelement allows to give a more user-friendly name to the view. The label does not have to be unique. As long as the ID is unique, views for different analyses can use the same name.

Also, if the values of the attributes to display are known, they can be defined, along with a text to explain them and a color to draw them with. Note that the values are the same as defined in the state provider, but the name does not have to be the same. While in the state provider, a simple constant string makes sense to use in state changes. But in the view, the name will appear in the legend, so a user-friendly text is more appropriate.

Here is the full XML for the time graph view:

The following screenshot shows the result of the preceding example on a test trace. The trace used, as well as the XML file are availablehere.



#### Using the keyboard
- Ctrl + F: Search in the view. (seeSearching in Time Graph Views)
- Ctrl + F: Search in the view. (seeSearching in Time Graph Views)