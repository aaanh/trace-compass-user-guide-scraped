### Opening a Trace or Experiment

A trace or experiment can be opened by double-clicking the left mouse button on the trace or experiment in theProject Explorerview. Alternatively, select the trace or experiment in the in theProject Explorerview and click the right mouse button. Then selectOpenmenu item of the context-sensitive menu. If there is no trace type set for a file resource then the file will be opened in the default editor associated with this file type.



If there is a default perspective associated with the opened trace or experiment and it is not the active perspective, the user will be prompted to switch to this perspective. The user can choose to remember this decision. The user preference can be later updated in thePerspectivespreference page. SelectWindow > Preferencesin the main menu, then selectTracing > Perspectivesin the tree, and choose one of the options underOpen the associated perspective when a trace is opened..

When opening a trace or experiment, all currently opened views which are relevant for the corresponding trace type will be updated.

TheProject Explorertree for the opened trace will be updated and will show all the available analysis for and views for the corresponding trace type as in the following image.



If an analysis can't be executed (e.g. due to missing required events) then the analysis will be strike-through. Right-mouse clicking on the analysis tree element and selecting menu itemHelp, will provide more details why the analysis can't be executed.

Double-clicking the left mouse button on the a analysis, will execute the analysis. Alternatively, select an analysis in the in theProject Explorerview and click the right mouse button. Then selectOpenmenu item of the context-sensitive menu. Opening a view tree element underneath the analysis will also trigger the execution of the corresponding analysis.

Note, that some analysis are implemented for automatic execution, so that they are executed when opening the trace.

If a trace resource is a file (and not a directory), then theOpen Withmenu item is available in the context-sensitive menu and can be used to open the trace source file with any applicable internal or external editor. In that case the trace will not be processed by the tracing application.