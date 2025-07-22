## Defining an XML XY chart

An XY chart displays series as a set of numerical values over time. The X-axis represents the time and is synchronized with the trace's current time range. The Y-axis can be any numerical value.

Such views can be defined in XML using the data in the state system. The state system itself could have been built by an XML-defined state provider or by any predefined Java analysis. It only requires knowing the structure of the state system, which can be explored using theState System Explorer View(or programmatically using the methods inITmfStateSystem).

We will use the Linux Kernel Analysis on LTTng kernel traces to show an example XY chart. In this state system, the status of each CPU is a numerical value. We will display this value as the Y axis of the series. There will be one series per CPU. The XML to display these entries would be as such:

But first, the view has to be declared. It has an ID, to uniquely identify this view among all the available XML files.

Like for the time graph views, optional header information can be added to the view.analysiselements will associate the view only to the analysis identified by the "id" attribute. It can be either the ID of the state provider, like in this case, or the analysis ID of any analysis defined in Java. If no analysis is specified, the view will appear under every analysis with a state system. Thelabelelement allows to give a more user-friendly name to the view. The label does not have to be unique. As long as the ID is unique, views for different analyses can use the same name.

Here is the full XML for the XY Chart that displays the CPU status over time of an LTTng Kernel Trace:

The following screenshot shows the result of the preceding example on a LTTng Kernel Trace.