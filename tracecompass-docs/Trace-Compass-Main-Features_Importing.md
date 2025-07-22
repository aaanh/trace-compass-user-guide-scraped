#### Importing

To import a set of traces to a trace folder, right-click on the target folder and selectImport...from the context-sensitive menu.



At this point, theImport Trace Wizardwill show for selecting traces to import. By default, it shows the correct destination directory where the traces will be imported to. Now, specify the location of the traces in theRoot directory. For that click on the buttonBrowse, browse the media to the location of the traces and click onOK. Then select the traces to import in the list of files and folders. If the selected files include archive files (tar, zip), they will be extracted automatically and imported as well.

Traces can also be imported directly from an archive file such as a zip or a tar file by selecting theSelect archive fileoption then by clickingBrowse. Then select the traces to import in the list of files and folders as usual.

Optionally, select theTrace Typefrom the drop-down menu. IfTrace Typeis set to<Automatic Detection>, the wizard will attempt to detect the trace types of the selected files. The automatic detection algorithm validates a trace against all the trace types enabled in theTrace Types preference page. If multiple trace types are valid, a trace type is chosen based on a confidence criteria. The validation process and the computation of the confidence level are trace type specific. Optionally,Import unrecognized tracescan be selected to import trace files that could not be automatically detected by<Automatic Detection>.

Select or deselect the checkboxes forOverwrite existing trace without warning,Create links in workspaceandPreserve folder structure. When all options are configured, click onFinish.

Note that traces of certain types (e.g. LTTng Kernel) are actually a composite of multiple channel traces grouped under a folder. Either the folder or its files can be selected to import the trace.

The optionPreserve folder structurewill create, if necessary, the structure of folders relative to (and excluding) the selectedRoot directory(orArchive file) into the target trace folder.

The optionCreate Experimentwill create an experiment with all imported traces. By default, the experiment name is theRoot directoryname, when importing from directory, or theArchive filename, when importing from archive. One can change the experiment name by typing a new name in the text box beside the option.

The optionTime Range filteringwill filter your previously selected traces using the given time range. A trace will be imported into the project only if its time range is included or overlap the provided range.



If a trace already exists with the same name in the target trace folder, the user can choose to rename the imported trace, overwrite the original trace or skip the trace. When rename is chosen, a number is appended to the trace name, for example smalltrace becomes smalltrace(2).



If one selectsRename All,Overwrite AllorSkip Allthe choice will be applied for all traces with a name conflict.

Upon successful importing, the traces will be stored in the target trace folder. If a trace type was associated to a trace, then the corresponding icon will be displayed. If no trace type is detected the default editor icon associated with this file type will be displayed. Linked traces will have a little arrow as decorator on the right bottom corner.

Depending of the trace types enabled in theTrace Types preference page, the list of available trace types can vary.

Alternatively, one can open theImport...menu from theFilemain menu, then selectTracing>Trace Importand click onNext >.



At this point, theImport Trace Wizardwill show. To import traces to the tracing project, follow the instructions that were described above.