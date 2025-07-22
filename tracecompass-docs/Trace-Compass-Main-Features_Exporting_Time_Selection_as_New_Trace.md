### Exporting Time Selection as New Trace

If a time range (not a single timestamp) is selected in any of the time-based views, right clicking on the trace or experiment element in theProject Explorerwill showExport Time Selection as New Trace. This option allowstrimmingthe current trace to a subset of its events, while preserving all the states that may have been computed by various analyses using events present before the exported time range.

TheExporting Time Selection as New Traceoption will create a new trace and import it into the current tracing project. A selection dialog will be presented to the user to define where the new trace should be written. This is where the new trace files will be written, as well as any appropriateinitial statefiles.





The new trace will be initially named the same as the original. The user must then free to rename the new trace. The trace can also be removed from the project and re-imported later with no loss of information.



Note: Since trace writing works differently for every trace type, the trimming feature has to be implemented for the target trace's type. If the option remains grayed out even if a time range is selected, it is because the given trace type does not implement the trim feature.