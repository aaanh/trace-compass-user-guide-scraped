### Deleting Supplementary Files

Supplementary files are by definition trace specific files that accompany a trace. These file could be temporary files, persistent indexes or any other persistent data files created by the LTTng integration in Eclipse during parsing a trace. For the LTTng 2.0 trace viewer a persistent state history of the Linux Kernel is created and is stored under the namestateHistory.ht. The statistics for all traces are stored understatistics.ht. Other state systems may appear in the same folder as more custom views are added.

All supplementary file are hidden from the user and are handled internally by the TMF. However, there is a possibility to delete the supplementary files so that they are recreated when opening a trace.

To delete all supplementary files from one or many traces and experiments, select the relevant traces and experiments in theProject Explorerview and click the right mouse button. Then select theDelete Supplementary Files...menu item from the context-sensitive menu.



A new dialog box will open with a list of supplementary files, grouped under the trace or experiment they belong to. Select the file(s) to delete from the list and pressOK. The traces and experiments that need to be closed in order to do this operation will automatically be closed.