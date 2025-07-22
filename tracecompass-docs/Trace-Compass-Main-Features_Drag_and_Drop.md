#### Drag and Drop

Traces can be also be imported to a project by dragging from another tracing project and dropping to the project's target trace folder. The trace will be copied and the trace type will be set.

Any resource can be dragged and dropped from a non-tracing project, and any file or folder can be dragged from an external tool, into a tracing project's trace folder. The resource will be copied or imported as a new trace and it will be attempted to detect the trace types of the imported resource. The automatic detection algorithm validates a trace against all known trace types. If multiple trace types are valid, a trace type is chosen based on a confidence criteria. The validation process and the computation of the confidence level are trace type specific. If no trace type is detected the user needs to set the trace type manually.

To import the trace as a link, use the platform-specific key modifier while dragging the source trace. A link will be created in the target project to the trace's location on the file system.

If a folder containing traces is dropped on a trace folder, the full directory structure will be copied or linked to the target trace folder. The trace type of the contained traces will not be auto-detected.

It is also possible to drop a trace, resource, file or folder into an existing experiment. If the item does not already exist as a trace in the project's trace folder, it will first be copied or imported, then the trace will be added to the experiment.