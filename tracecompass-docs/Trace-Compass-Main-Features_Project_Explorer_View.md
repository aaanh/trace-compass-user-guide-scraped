## Project Explorer View

The Project Explorer view is the standard Eclipse Project Explorer.Tracingprojects are well integrated in the Eclipse's Common Navigator Framework. The Project Explorer showsTracingproject with a small "T" decorator in the upper right of the project folder icon.

### Creating a Tracing Project

A newTracingproject can be created using the New Tracing Project wizard. To create a newTracingselectFile > New > Project...from the main menu bar or alternatively form the context-sensitive menu (click with right mouse button in theProject Explorer.

The first page of project wizard will open.



In the list of project categories, expand categoryTracingand selectTracing Projectand the click onNext >. A second page of the wizard will show. Now enter the a name in the fieldProject Name, select a location if required and the press onFinish.



A new project will appear in theProject Explorerview.



Tracing projects have two sub-folders:Traceswhich holds the individual traces, andExperimentswhich holds sets of traces that we want to correlate.

### Configuring a Project as Tracing Project

It is possible to configure an existing project, for example C/C++ or Java project, as a Tracing project. All Trace Compass related features will be available within the same project. To configure a project as Tracing project, right-click on the project in the Project Explorer and select menu itemConfigure > Configure or convert to Tracing Project.



Upon successful configuration, the project tree will be updated and theTrace Compasstop-level node will be added. Expanding theTrace Compassnode will show theTracesandExperimentsnodes from the Tracing project.



### Importing Traces to the Project

TheTracesfolder holds the set of traces available for a tracing project. It can optionally contain a tree of trace folders to organize traces into sub-folders. The following chapters will explain different ways to import traces to theTracesfolder of a tracing project.
- Opening a Trace
- Importing
- Drag and Drop
- Opening a Trace
- Importing
- Drag and Drop

#### Opening a Trace

To open a trace, right-click on a target trace folder and selectOpen Trace....



A new dialog will show for selecting a trace to open. Select a trace file and then click onOK. Note that for traces that are directories (such as Common Trace Format (CTF) traces) any file in the trace directory can be selected to open the trace. Now, the trace viewer will attempt to detect the trace types of the selected trace. The auto detection algorithm will validate the trace against all known trace types. If multiple trace types are valid, a trace type is chosen based on a confidence criteria. The validation process and the computation of the confidence level are trace type specific. After successful validation the trace will be linked into the selected target trace folder and then opened with the detected trace type.

Depending of the trace types enabled in theTrace Types preference page, the list of available trace types can vary.

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

#### Drag and Drop

Traces can be also be imported to a project by dragging from another tracing project and dropping to the project's target trace folder. The trace will be copied and the trace type will be set.

Any resource can be dragged and dropped from a non-tracing project, and any file or folder can be dragged from an external tool, into a tracing project's trace folder. The resource will be copied or imported as a new trace and it will be attempted to detect the trace types of the imported resource. The automatic detection algorithm validates a trace against all known trace types. If multiple trace types are valid, a trace type is chosen based on a confidence criteria. The validation process and the computation of the confidence level are trace type specific. If no trace type is detected the user needs to set the trace type manually.

To import the trace as a link, use the platform-specific key modifier while dragging the source trace. A link will be created in the target project to the trace's location on the file system.

If a folder containing traces is dropped on a trace folder, the full directory structure will be copied or linked to the target trace folder. The trace type of the contained traces will not be auto-detected.

It is also possible to drop a trace, resource, file or folder into an existing experiment. If the item does not already exist as a trace in the project's trace folder, it will first be copied or imported, then the trace will be added to the experiment.

### Trace Package Exporting and Importing

A trace package is an archive file that contains the trace itself and can also contain its bookmarks and its supplementary files. Including supplementary files in the package can improve performance of opening an imported trace but at the expense of package size.

#### Exporting

TheExport Trace Package Wizardallows users to select a trace and export its files and bookmarks to an archive on a media.

TheTracesfolder holds the set of traces available for a tracing project. To export traces contained in theTracesfolder, one can open theExport...menu from theFilemain menu. Then selectTrace Package Export



At this point, theTrace Package Exportis opened. The project containing the traces has to be selected first then the traces to be exported.



One can also open the wizard and skip the first page by expanding the project, selecting traces or trace folders under theTracesfolder, then right-clicking and selecting theExport Trace Package...menu item in the context-sensitive menu.



Next, the user can choose the content to export and various format options for the resulting file.



TheTraceitem is always selected and represents the files that constitute the trace. TheSupplementary filesitems represent files that are typically generated when a trace is opened by the viewer. Sharing these files can speed up opening a trace dramatically but also increases the size of the exported archive file. TheSizecolumn can help to decide whether or not to include these files. Lastly, by selectingBookmarks, the user can export all the bookmarks so that they can be shared along with the trace.

TheTo archive filefield is used to specify the location where to save the resulting archive.

TheOptionssection allows the user to choose between a tar archive or a zip archive. Compression can also be toggled on or off.

When Finish button is clicked, the package is generated and saved to the media. The folder structure of the selected traces relative to theTracesfolder is preserved in the trace package.

#### Importing

TheImport Trace Package Wizardallows users to select a previously exported trace package from their media and import the content of the package in the workspace.

TheTracesfolder holds the set of traces for a tracing project. To import a trace package to theTracesfolder, one can open theImport...menu from theFilemain menu. Then selectTrace Package Import.



One can also open the wizard by expanding the project name, right-clicking on a target folder under theTracesfolder then selectingImport Trace Package...menu item in the context-sensitive menu.



At this point, theTrace Package Import Wizardis opened.



TheFrom archive filefield is used to specify the location of the trace package to export. The user can choose the content to import in the tree.

If the wizard was opened using the File menu, the destination project has to be selected in theInto projectfield.

When Finish is clicked, the trace is imported in the target folder. The folder structure from the trace package is restored in the target folder.

### Refreshing of Trace and Trace Folder

Traces and trace folders in the workspace might be updated on the media. To refresh the content, right-click the trace or trace folder and select menu itemRefresh. Alternatively, select the trace or trace folder and press keyF5.

### Remote Fetching

It is possible to import traces automatically from one or more remote hosts according to a predefined remote profile by using theFetch Remote Traceswizard.

To start the wizard, right-click on a target trace folder and selectFetch Remote Traces....



The wizard opens on theRemote Profilepage.



If the remote profile already exists, it can be selected in theProfile namecombo box. Otherwise, clickManage Profilesto open theRemote Profilespreferences page.

#### Remote Profile elements



ClickAddto create a new remote profile. A default remote profile template appears.



##### Profile

Edit theProfile namefield to give a unique name to the new profile.

Under the Profile element, at least one Connection Node element must be defined.

##### Connection Node

Node name: Unique name for the connection within the scope of the Remote Services provider.

URI: URI for the connection. Its scheme maps to a particular Remote Services provider. If the connection name already exists for that provider, the URI must match its connection information. The schemesshcan be used for the Built-In SSH provider. The schemefilecan be used for the local file system.

To view or edit existing connections, see theRemote Development>Remote Connectionspreferences page. On this page the user can enter a password for the connection.

Under the Connection Node element, at least one Trace Group element must be defined.

##### Trace Group

Root path: The absolute root path from where traces will be fetched. For example,/home/useror/C/Users/user.

Recursive: Check this box to search for traces recursively in the root path.

Under the Trace Group element, at least one Trace element must be defined.

##### Trace

File pattern: A regular expression pattern to match against the file name of traces found under the root path. If theRecursiveoption is used, the pattern must match against the relative path of the trace, using forward-slash as a path separator. Files that do not match this pattern are ignored. If multiple Trace elements have a matching pattern, the first matching element will be used, and therefore the most specific patterns should be listed first. Following are some pattern examples:
- .*matches any trace in any folder
- [^/]*\.logmatches traces with .log extension in the root path folder
- .*\.logmatches traces with .log extension in any folder
- folder-[^/]*/[^/]*\.logmatches traces with .log extension in folders matching a pattern
- (.*/)?filenamematches traces with a specific name in any folder
- .*matches any trace in any folder
- [^/]*\.logmatches traces with .log extension in the root path folder
- .*\.logmatches traces with .log extension in any folder
- folder-[^/]*/[^/]*\.logmatches traces with .log extension in folders matching a pattern
- (.*/)?filenamematches traces with a specific name in any folder

Trace Type: The trace type to assign to the traces after fetching, or<Automatic Detection>to determine the trace type automatically. Note that traces whose trace type can not be assigned according to this setting are not deleted after fetching.

#### Profile editing and management

Right-click a profile element to bring up its context menu. ANewchild element of the appropriate type can be created. SelectDeleteto delete a node, orCut,CopyandPasteto move or copy elements from one profile element to another. The keyboard shortcuts can also be used.

Press theAddbutton to create a new element of the same type and following the selected element, or a new profile if the selection is empty.

Press theRemovebutton to delete the selected profile elements.

Press theImportbutton to import profiles from a previously exported XML file.

Press theExportbutton to export the selected profiles to an XML file.

Press theMove UporMove Downbuttons to reorder the selected profile element.

The filter text box can be used to filter profiles based on the profile name or connection node.

When the remote profile information is valid and complete, press theOKbutton to save the remote profiles preferences.



#### Selecting remote traces

Back in theRemote Profileswizard page, select the desired profile and clickNext >. ClickingFinishat this point will automatically select and download all matching traces.



If required, the selected remote connections are created and connection is established. The user may be prompted for a password. This can be avoided by storing the password for the connection in theRemote Connectionspreference page.



The root path of every Trace Group is scanned for matching files. The result is shown in theRemote Traceswizard page.



Select the traces to fetch by checking or unchecking the desired connection node, trace group, folder or individual trace. ClickFinishto complete the operation.

If any name conflict occurs, the user will be prompted to rename, overwrite or skip the trace, unless theOverwrite existing trace without warningoption was checked in theRemote Profileswizard page.

The downloaded traces will be imported to the initially selected project folder. They will be stored under a folder structure with the pattern<connection name>/<path>/<trace name>where the path is the trace's remote path relative to its trace group's root path.



### Selecting a Trace Type

If no trace type was selected a trace type has to be associated to a trace before it can be opened. To select a trace type select the relevant trace and click the right mouse button. In the context-sensitive menu, selectSelect Trace Type...menu item. A sub-menu will show will all available trace type categories. From the relevant category select the required trace type. The examples, below show how to select theCommon Trace FormattypesLinux Kernel TraceandGeneric CTF trace.





After selecting the trace type, the trace icon will be updated with the corresponding trace type icon.



The user can edit theTrace Types preference pageto choose which trace types will be available under theSelect Trace Type...menu.

### Trace Types Preference Page

TheTrace Typespreference page lists all the available trace types and allows the user to enable/disable the trace types.

Trace type is an extension point of theTracing and Monitoring Framework (TMF). Depending on which features are loaded and which custom parsers have been created, the list of trace types can vary.

The user needs to press theApplybutton orOK' to save the changes.

Only the enabled trace types will be used for trace importing, auto-detection, as well as shown under theSelect Trace Type...menu.

To access theTrace Typespreference page, select theWindowmenu. Then SelectPreferencesand search forTrace TypeunderTracinggroup. The example below shows theTrace Typespreference page.



### Opening a Trace or Experiment

A trace or experiment can be opened by double-clicking the left mouse button on the trace or experiment in theProject Explorerview. Alternatively, select the trace or experiment in the in theProject Explorerview and click the right mouse button. Then selectOpenmenu item of the context-sensitive menu. If there is no trace type set for a file resource then the file will be opened in the default editor associated with this file type.



If there is a default perspective associated with the opened trace or experiment and it is not the active perspective, the user will be prompted to switch to this perspective. The user can choose to remember this decision. The user preference can be later updated in thePerspectivespreference page. SelectWindow > Preferencesin the main menu, then selectTracing > Perspectivesin the tree, and choose one of the options underOpen the associated perspective when a trace is opened..

When opening a trace or experiment, all currently opened views which are relevant for the corresponding trace type will be updated.

TheProject Explorertree for the opened trace will be updated and will show all the available analysis for and views for the corresponding trace type as in the following image.



If an analysis can't be executed (e.g. due to missing required events) then the analysis will be strike-through. Right-mouse clicking on the analysis tree element and selecting menu itemHelp, will provide more details why the analysis can't be executed.

Double-clicking the left mouse button on the a analysis, will execute the analysis. Alternatively, select an analysis in the in theProject Explorerview and click the right mouse button. Then selectOpenmenu item of the context-sensitive menu. Opening a view tree element underneath the analysis will also trigger the execution of the corresponding analysis.

Note, that some analysis are implemented for automatic execution, so that they are executed when opening the trace.

If a trace resource is a file (and not a directory), then theOpen Withmenu item is available in the context-sensitive menu and can be used to open the trace source file with any applicable internal or external editor. In that case the trace will not be processed by the tracing application.

### Creating an Experiment

An experiment consists in an arbitrary number of aggregated traces for purpose of correlation. In the degenerate case, an experiment can consist of a single trace. The experiment provides a unified, time-ordered stream of the individual trace events.

To create an experiment, select the folderExperimentsand click the right mouse button. Then selectNew....



A new display will open for entering the experiment name. Type the name of the experiment in the text fieldExperiment Nameand the click onOK.



### Selecting Traces for an Experiment

After creating an experiment, traces need to be added to the experiment. To select traces for an experiment select the newly create experiment and click the right mouse button. SelectSelect Traces...from the context sensitive menu.



A new dialog box will open with a list of available traces. The filter text box can be used to quickly find traces. Use buttonsSelect AllorDeselect Allto select or deselect all traces. Select the traces to add from the list and then click onFinishor you can go a step further by activating the time range filtering option. Enter the time range using the following format: 'yyyy-MM-dd HH:mm:ss.SSS SSS SSS' and click onFinish. By using this option, only traces, among your selected trace, that are in or overlap the range will be added to the experiment.



Now the selected traces will be linked to the experiment and will be shown under theExperimentsfolder. Expanding of theViewsfolder will show all available analysis that are defined either for the experiment or for contained traces.  If there are multiple traces of the same trace type the "Views" folder will aggregate all available analysis that are the same to one entry in the tree. Each analysis output (view) can be opened from the experiment context.



Alternatively, traces can be added to an experiment usingDrag and Drop.

### Creating an Experiment from Selection

An experiment can be quickly created and opened automatically by selecting one or more traces and/or trace folders in theProject Explorerview, and then selecting theOpen as Experiment...context menu. A sub-menu with the available experiment types is opened. Select the desired experiment type from the sub-menu. All selected traces and traces recursively found in selected trace folders will be added to the experiment.

If a single trace or trace folder is selected, its name will be used for the experiment, otherwise a default name will be used, possibly appended with a number to avoid name clashes.

If an experiment with the same name and traces already exists, it will be reopened (or selected if it is already opened). Otherwise, a new experiment will be created and opened.

### Removing Traces from an Experiment

To remove one or more traces from an experiment select the trace(s) to remove under the Experiment folder and click the right mouse button. SelectRemovefrom the context sensitive menu.



After that the selected trace(s) are removed from the experiment. Note that the traces are still in theTracesfolder.

### Deleting Traces from an Experiment

To delete one or more traces from an experiment select the trace(s) to delete under the Experiment folder and click the right mouse button. SelectDeletefrom the context sensitive menu.



After that, the selected trace(s) are removed from the experiment. Note that the traces are also deleted from theTracesfolder.

### Renaming a Trace or Experiment

Traces and Experiment can be renamed from theProject Explorerview. To rename a trace or experiment select the relevant trace and click the right mouse button. Then selectRename...from the context sensitive menu. The trace or experiment needs to be closed in order to do this operation.



A new dialog box will show for entering a new name. Enter a new trace or experiment name respectively in the relevant text field and click onOK. If the new name already exists the dialog box will show an error and a different name has to be entered.





After successful renaming the new name will show in theProject Explorer. In case of a trace all reference links to that trace will be updated too. Note that linked traces only changes the display name, the underlying trace resource will stay the original name.

Note that all supplementary files will be also handled accordingly (see alsoDeleting Supplementary Files).

### Copying a Trace or Experiment

To copy a trace or experiment select the relevant trace or experiment in theProject Explorerview and click the right mouse button. Then selectCopy...from the context sensitive menu.



A new dialog box will show for entering a new name. Enter a new trace or experiment name respectively in the relevant text field and click onOK. In case of a linked trace two options are available,Copy as a linkorCopy as a new trace. The first option, default one, the copied trace will be a link to the original trace. The second option, will make a copy of the original trace in your workspace. If the new name already exists the dialog box will show an error and a different name has to be entered.





After successful copy operation the new trace or experiment respectively will show in theProject Explorer.

Note that the directory for all supplementary files will be copied, too. (see alsoDeleting Supplementary Files).

### Deleting a Trace or Experiment

To delete a trace or experiment select the relevant trace or experiment in theProject Explorerview and click the right mouse button. Then selectDelete...from the context sensitive menu. The trace or experiment needs to be closed in order to do this operation.



A confirmation dialog box will open. To perform the deletion pressOKotherwise selectCancel.



After successful operation the selected trace or experiment will be removed from the project. In case of a linked trace only the link will be removed. The actual trace resource remain on the disk.

Note that the directory for all supplementary files will be deleted, too. (see alsoDeleting Supplementary Files).

### Deleting Supplementary Files

Supplementary files are by definition trace specific files that accompany a trace. These file could be temporary files, persistent indexes or any other persistent data files created by the LTTng integration in Eclipse during parsing a trace. For the LTTng 2.0 trace viewer a persistent state history of the Linux Kernel is created and is stored under the namestateHistory.ht. The statistics for all traces are stored understatistics.ht. Other state systems may appear in the same folder as more custom views are added.

All supplementary file are hidden from the user and are handled internally by the TMF. However, there is a possibility to delete the supplementary files so that they are recreated when opening a trace.

To delete all supplementary files from one or many traces and experiments, select the relevant traces and experiments in theProject Explorerview and click the right mouse button. Then select theDelete Supplementary Files...menu item from the context-sensitive menu.



A new dialog box will open with a list of supplementary files, grouped under the trace or experiment they belong to. Select the file(s) to delete from the list and pressOK. The traces and experiments that need to be closed in order to do this operation will automatically be closed.



### Displaying the trace's time range

The trace's time range can be displayed alongside the trace's name. The time is displayed in the Time Format from Tracing preferences.

To enable this feature, head toPreferences > Tracingand check the boxShow trace time range in Project Explorer.



If a trace is empty or its type unknown, nothing will be shown. It the range has not been fully read from the trace or the supplementary files,[...]will be shown. If the trace is being read and only its start timestartis known,[start - ...]will be shown. Finally, when the end timeendis also known,[start - end]will be shown.



### Link with Editor

The tracing projects support the featureLink With Editorof the Project Explorer view. With this feature it is now possible to
- select a trace element in the Project Explorer view and the correspondingEvents Editorwill get focus if the relevant trace is open.
- select anEvents Editorand the corresponding trace element will be highlighted in the Project Explorer view.
- select a trace element in the Project Explorer view and the correspondingEvents Editorwill get focus if the relevant trace is open.
- select anEvents Editorand the corresponding trace element will be highlighted in the Project Explorer view.

To enable or disable this feature toggle theLink With Editorbutton of the Project Explorer view as shown below.



### Exporting Time Selection as New Trace

If a time range (not a single timestamp) is selected in any of the time-based views, right clicking on the trace or experiment element in theProject Explorerwill showExport Time Selection as New Trace. This option allowstrimmingthe current trace to a subset of its events, while preserving all the states that may have been computed by various analyses using events present before the exported time range.

TheExporting Time Selection as New Traceoption will create a new trace and import it into the current tracing project. A selection dialog will be presented to the user to define where the new trace should be written. This is where the new trace files will be written, as well as any appropriateinitial statefiles.





The new trace will be initially named the same as the original. The user must then free to rename the new trace. The trace can also be removed from the project and re-imported later with no loss of information.



Note: Since trace writing works differently for every trace type, the trimming feature has to be implemented for the target trace's type. If the option remains grayed out even if a time range is selected, it is because the given trace type does not implement the trim feature.