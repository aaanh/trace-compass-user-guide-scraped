## Synchronize traces in Trace Compass

In order to synchronize traces, create a new experiment and select all traces that need to be synchronized. Right-click on the experiment and selectSynchronize traces. For each trace whose time needs to be transformed, a new trace named as the original but followed by a '_' will be created with the transformed timestamps, and the original trace will be replaced in the experiment. The original trace can still be accessed under theTracesfolder.



When opening the experiment now, all the views will be synchronized. The following screenshot presents the differences in the filtered Control Flow View before and after the time synchronization.



Information on the quality of the synchronization, the timestamp transformation formula and some synchronization statistics can be visualized in theSynchronizationview. To open theSynchronizationview, use the Eclipse Show View dialog (Window->Show View->Other...). Then selectSynchronizationunderTracing.