### Importing Session Traces to a Tracing Project

To import traces from a tracing session, select the relevant session and click on theImportButton. Alternatively, click the right mouse button on the session tree node and select the menu itemImport...from the context-sensitive menu.



A new display will open for selecting the traces to import.



By default all traces are selected. A default project with the nameRemoteis selected which will be created if necessary. Update the list of traces to be imported, if necessary, by selecting and deselecting the relevant traces in the tree viewer. Use buttonsSelect AllorDeselect Allto select or deselect all traces. Also if needed, change the tracing project from theAvailable Projectscombo box. The optionCreate Experimentwill create an experiment with all imported traces. By default, the experiment name is the session name. One can change the experiment name by typing a new name in the text box beside the option.

Then press buttonFinish. Upon successful import operation the selected traces will be stored in theTracesdirectory of the specified tracing project. A directory with the connection name will be created under theTracesdirectory. Underneath that, the session directory structure as well as the trace names will be preserved in the destination tracing project. ForKerneltraces the trace typeLinux Kernel Traceand forUSTtraces the trace typeLTTng UST Tracewill be set. From theProject Explorerview, the trace can be analyzed further.

Note: If a trace already exists with the same name in the destination directory, the user can choose to rename the imported trace, overwrite the original trace or skip the trace. When rename is chosen, a number is appended to the trace name, for example kernel becomes kernel(2).



If one selectsRename All,Overwrite AllorSkip Allthe choice will be applied for all traces with a name conflict.