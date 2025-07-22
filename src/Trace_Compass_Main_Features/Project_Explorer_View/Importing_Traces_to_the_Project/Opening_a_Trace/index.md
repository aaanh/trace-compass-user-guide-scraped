#### Opening a Trace

To open a trace, right-click on a target trace folder and selectOpen Trace....



A new dialog will show for selecting a trace to open. Select a trace file and then click onOK. Note that for traces that are directories (such as Common Trace Format (CTF) traces) any file in the trace directory can be selected to open the trace. Now, the trace viewer will attempt to detect the trace types of the selected trace. The auto detection algorithm will validate the trace against all known trace types. If multiple trace types are valid, a trace type is chosen based on a confidence criteria. The validation process and the computation of the confidence level are trace type specific. After successful validation the trace will be linked into the selected target trace folder and then opened with the detected trace type.

Depending of the trace types enabled in theTrace Types preference page, the list of available trace types can vary.