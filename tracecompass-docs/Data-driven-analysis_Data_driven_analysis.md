# Data driven analysis

It is possible to define custom trace analyses and a way to view them in an XML format. These kind of analyses allow doing more with the trace data than what the default analyses shipped with TMF offer. It can be customized to a specific problem, and fine-tuned to show exactly what you're looking for.

## Managing XML files containing analyses

TheManage XML Analysespreference page is used to manage the list of XML files containing analyses. To open the preference page, selectWindow > Preferencesfrom the main menu bar, then click onXML Analysesunder theTracingsection. The preference page can also be opened using the Project Explorer as described here:
- Open theProject Explorerview.
- SelectManage XML Analyses...from theTracesfolder context menu.
- Open theProject Explorerview.
- SelectManage XML Analyses...from theTracesfolder context menu.



The list of currently imported XML files is displayed on the left side of the dialog.

The following actions can be performed from this dialog:
- Import
- Import

Click theImportbutton and select a file from the opened file dialog to import an XML file containing an analysis. The file will be validated before importing it and if successful, the new file will be enabled and its analyses and views will be shown under the traces for which they apply.
- Enable/disable
- Enable/disable

To enable a file and its analyses, check the box to the left of the file, then pressApplyorApply and closeto save the changes. Unchecking a box and saving the changes will disable the corresponding file. When selecting an enabled file, a confirmation message will be displayed to the user. Note that invalid files cannot be enabled; if one is selected, an error message will be displayed to the user.
- Export
- Export

Select an XML file from the list, click theExportbutton and enter or select a file in the opened file dialog to export the XML analysis. Note that if an existing file containing an analysis is selected, its content will be replaced with the analysis to export.
- Edit
- Edit

Select an XML file from the list, click theEditto open the XML editor. When the file is saved after being modified, it is validated and traces that are affected by this file are closed.
- Delete
- Delete

Select one or more XML files from the list and click theDeletebutton to remove them. Deleting an XML file will close all the traces for which the analyses apply and remove the analyses.

## Defining XML components

To define XML components, you need to create a new XML file and use the XSD that comes with the XML plugin.

For now, the XSD is only available through the source code in org.eclipse.tracecompass.tmf.analysis.xml.core/src/org/eclipse/tracecompass/tmf/analysis/xml/core/module/xmlDefinition.xsd.

An empty file, with no content yet would look like this:

## Defining an XML state provider

The state system is a component of TMF which can track the states of different elements of the system over the duration of a trace. To build this state system, events have to go chronologically through a state provider, which defines what changes are caused by the event to the system.

The state system obtained by the state provider can then be used to populate data-driven views without having to re-read the trace, or to query specific timestamps in the trace without needing to access the trace file.

### Definitions and example

Before we start, we'll define a few terms used in the following sections. The interested reader should read theTmf Developer Guidefor more complete description of the state system and state providers.
- Thestate systemcan be viewed as a model of the system, where the different elements (attributes) can be seen as a tree, and their evolution (states) is tracked through time.
- Thestate systemcan be viewed as a model of the system, where the different elements (attributes) can be seen as a tree, and their evolution (states) is tracked through time.
- Attribute: An attribute is the smallest element of the model that can be in any particular state. Since many attributes may have the same name, each attribute is represented by its full path in the attribute tree.
- Attribute: An attribute is the smallest element of the model that can be in any particular state. Since many attributes may have the same name, each attribute is represented by its full path in the attribute tree.
- State: A state is a value assigned to an attribute at a given time. Each model has its own state values.
- State: A state is a value assigned to an attribute at a given time. Each model has its own state values.
- Attribute tree: Elements in the model can be placed in a tree-like structure, for logical grouping. Each element in the tree can have both children and a state. Also, the tree is just a logical structure, all elements may be top-level elements.
- Attribute tree: Elements in the model can be placed in a tree-like structure, for logical grouping. Each element in the tree can have both children and a state. Also, the tree is just a logical structure, all elements may be top-level elements.
- State history: Whereas the attribute tree may be seen as the first dimension of the state system, the state history is the second dimension, over time. It tracks the intervals at which an attribute was in a given state.
- State history: Whereas the attribute tree may be seen as the first dimension of the state system, the state history is the second dimension, over time. It tracks the intervals at which an attribute was in a given state.

In the following sections, we'll use an example trace with the following events:
- start(number): A new task with ID 'number' just started.
- execute(number, fct_name): The task with ID 'number' is executing a critical section named 'fct_name'.
- wait(number): The task with ID 'number' cannot execute a critical section and needs to wait for it.
- exec_end(fct_name): A task finished executing the critical section named 'fct_name'.
- stop(number): The task with ID 'number' has just finished.
- start(number): A new task with ID 'number' just started.
- execute(number, fct_name): The task with ID 'number' is executing a critical section named 'fct_name'.
- wait(number): The task with ID 'number' cannot execute a critical section and needs to wait for it.
- exec_end(fct_name): A task finished executing the critical section named 'fct_name'.
- stop(number): The task with ID 'number' has just finished.

### Determining the state system structure

The first thing to do is to determine the attribute tree we'll use to represent the model of the system. The attribute tree is like a file system with directories and files, where files are logically gathered in the same parent directory. There is no one good way to build a tree, the logic will depend on the situation and on the person defining it.

The generated state system may be used later on to populate views, so attributes of the tree could be grouped in such a way as to make it easy to reach them with a simple path. The view will then be more simple.

In our example case, we'll want to track the status of each task and, for each critical section, which task is running them.

Then we determine how each event will affect the state of the attributes. But first, let's ask ourselves what values should each state take.

Let's see with the tree:

Then we determine how each event will affect the state of the attributes. In the attribute paths below, elements in {} are values coming from the trace event, while strings are constants. For the sake of simplicity, we'll say "update attribute", but if an attribute does not exist, it will be created.
- start(number): Update state value of attribute "Tasks/{number}" to "RUNNING".
- execute(number, fct_name): Update state value of attribute "Tasks/{number}" to "CRITICAL" and Update attribute "Critical section/{fct_name}" to "{number}".
- wait(number): Update state value of attribute "Tasks/{number}" to "WAITING".
- exec_end(fct_name): Update state value of attribute "Tasks/{valueOf Critical section/{fct_name}}" to RUNNING and update "Critical section/{fct_name}" to null.
- stop(number): Update state value of attribute "Tasks/{number}" to null.
- start(number): Update state value of attribute "Tasks/{number}" to "RUNNING".
- execute(number, fct_name): Update state value of attribute "Tasks/{number}" to "CRITICAL" and Update attribute "Critical section/{fct_name}" to "{number}".
- wait(number): Update state value of attribute "Tasks/{number}" to "WAITING".
- exec_end(fct_name): Update state value of attribute "Tasks/{valueOf Critical section/{fct_name}}" to RUNNING and update "Critical section/{fct_name}" to null.
- stop(number): Update state value of attribute "Tasks/{number}" to null.

### Writing the XML state provider

Once the model is done at a high level, it is time to translate it to an XML data-driven analysis. For details on how to use each XML element, refer to the documentation available in the XSD files. Some elements will be commented on below.

First define the state provider element.

The "version" attribute indicates which version of the state system is defined here. Once a state provider has been defined for a trace type, it will typically be used by a team of people and it may be modified over time. This version number should be bumped each time a new version of the state provider is published. This will force a rebuild of any existing state histories (if applicable) whose version number is different from the current one.

The "id" attribute uniquely identifies this state provider, and the analysis that will contain it.

Optional header information can be added to the state provider. A "traceType" should be defined to tell TMF which trace type this analysis will apply to. If no tracetype is specified, the analysis will appear under every trace. A "label" can optionally be added to have a more user-friendly name for the analysis.

If predefined values will be used in the state provider, they must be defined before the state providers. They can then be referred to in the state changes by name, preceded by the '$' sign. It is not necessary to use predefined values, the state change can use values like (100, 101, 102) directly.

The following event handler shows what to do with the event namedstart. It causes one state change. The sequence ofstateAttributeelements represents the path to the attribute in the attribute tree, each element being one level of the tree. ThestateValueindicates which value to assign to the attribute at the given path. The "$RUNNING" value means it will use the predefined value named RUNNING above.

Suppose the actual event isstart(3). The result of this state change is that at the time of the event, the state system attribute "Tasks/3" will have value 100.

The full XML file for the example above would look like this:

### Debugging the XML state provider

To debug the state system that was generated by the XML state provider, one could use theState System Explorer View, along with the events editor. By selecting an event, you can see what changes this event caused and the states of other attributes at the time.

If there are corrections to make, you may modify the XML state provider file, and re-import it. To re-run the analysis, you must first delete the supplementary files by right-clicking on your trace, and selectingDelete supplementary files.... Check your analysis' .ht file, so that the analysis will be run again when the trace is reopened. The supplementary file deletion will have closed the trace, so it needs to be opened again to use the newly imported analysis file.

If modifications are made to the XML state provider after it has been "published", theversionattribute of thexmlStateProviderelement should be updated. This avoids having to delete each trace's supplementary file manually. If the saved state system used a previous version, it will automatically be rebuilt from the XML file.

## Defining an XML pattern provider

There are patterns within a trace that can provide high level details about the system execution. Apatternis a particular combination of events or states that are expected to occur within a trace. It may be composed of several state machines that inherit or communicate through a common state system.

We may have multiple instances (scenarios) of a running state machine within a pattern. Each scenario which has its own path in the state system can generate segments to populate the data-driven views

### The state system structure

The pattern analysis generates a predefined attribute tree described as follows:

The user can add custom data in this tree or determine its own attribute tree beside of this one.

### Writing the XML pattern provider

Details about the XML structure are available in the XSD files.

First define the pattern element. As the state provider element described inWriting the XML state provider, it has a "version" attribute and an "id" attribute.

Optional header information as well as predefined values like described inWriting the XML state providercan be added.

Stored values can be added before the pattern handler. The predefined actionsaveStoredFieldtriggers the updates of the stored fields and the predefined actionclearStoredFieldsreset the values.

Theidof the stored field is used as the field name in the event. If the field is not available, a null value will be saved for it. Thealiasis the name by which this field will be accessible in the state system.

The behavior of the pattern and the models it needs are described in the pattern handler element.

The structure of the state machine (FSM) is based on the SCXML structure. The following example describe an FSM that matches all the system call in an LTTng kernel trace.

The value of thetargetattribute corresponds to the 'id' of a state in the same FSM. Similarly, the value of theactionattribute corresponds to the 'id' of an action element described in the XML file and is a reference to it. Multiple actions can be executed by separating their names by ':', likeaction1:action2

Conditions are used in the transitions to switch between the state of an FSM. They can be specified by setting thecondattribute in the transition and they correspond to atestelement. Two types of conditions are allowed:Data conditionandTime condition. It is possible to combine several conditions using a logical operator (OR, AND, ...).

Data conditions tests the ongoing event information against the data in the state system or constant values. The following condition tests whether the current thread of the event is also the ongoing scenario thread.

Two types of time conditions are available:
- Time range conditions test whether the ongoing event happens between a specific range of time. The following condition tests whether the ongoing event happens between 1 nanosecond and 3 nanoseconds.
- Time range conditions test whether the ongoing event happens between a specific range of time. The following condition tests whether the ongoing event happens between 1 nanosecond and 3 nanoseconds.
- Elapsed time conditions tests the value of the time spent since a specific state of an fsm. The following condition tests whether the ongoing event happens less than 3 nanoseconds after that the scenario reaches the state "syscall_entry_x".
- Elapsed time conditions tests the value of the time spent since a specific state of an fsm. The following condition tests whether the ongoing event happens less than 3 nanoseconds after that the scenario reaches the state "syscall_entry_x".

Two types of actions are allowed:
- State changes update values of attributes into the state system. The following example set the value of the thread for the current scenario.
- State changes update values of attributes into the state system. The following example set the value of the thread for the current scenario.
- Generate segments. The following example represents a system call segment.
- Generate segments. The following example represents a system call segment.

When existing, the stored fields will be added as fields for the generated segments.

Here is the complete XML file by combining all the examples models above:

Here is an another example of XML analysis that creates a segment for each event read based on a field namedtestField:

Here is the associated trace:

This will produce 4 segments described below:
- name=seg1, start time = 1, end time = 10;
- name=seg1, start time = 3, end time = 100;
- name=seg1, start time = 5, end time = 20;
- name=seg1, start time = 7, end time = 200;
- name=seg1, start time = 1, end time = 10;
- name=seg1, start time = 3, end time = 100;
- name=seg1, start time = 5, end time = 20;
- name=seg1, start time = 7, end time = 200;

### Representing the scenarios

Segments generated by the pattern analysis are used to populate latency views. A description of these views can be found inLatency Analyses.

The full XML analysis example described above will generate the following views:
- Latency Table
- Latency Table


- Latency vs Time
- Latency vs Time


- Latency Statistics
- Latency Statistics


- Latency vs Count
- Latency vs Count



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

## Defining an XML XY chart

An XY chart displays series as a set of numerical values over time. The X-axis represents the time and is synchronized with the trace's current time range. The Y-axis can be any numerical value.

Such views can be defined in XML using the data in the state system. The state system itself could have been built by an XML-defined state provider or by any predefined Java analysis. It only requires knowing the structure of the state system, which can be explored using theState System Explorer View(or programmatically using the methods inITmfStateSystem).

We will use the Linux Kernel Analysis on LTTng kernel traces to show an example XY chart. In this state system, the status of each CPU is a numerical value. We will display this value as the Y axis of the series. There will be one series per CPU. The XML to display these entries would be as such:

But first, the view has to be declared. It has an ID, to uniquely identify this view among all the available XML files.

Like for the time graph views, optional header information can be added to the view.analysiselements will associate the view only to the analysis identified by the "id" attribute. It can be either the ID of the state provider, like in this case, or the analysis ID of any analysis defined in Java. If no analysis is specified, the view will appear under every analysis with a state system. Thelabelelement allows to give a more user-friendly name to the view. The label does not have to be unique. As long as the ID is unique, views for different analyses can use the same name.

Here is the full XML for the XY Chart that displays the CPU status over time of an LTTng Kernel Trace:

The following screenshot shows the result of the preceding example on a LTTng Kernel Trace.