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