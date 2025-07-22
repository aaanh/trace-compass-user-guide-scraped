#### Selecting remote traces

Back in theRemote Profileswizard page, select the desired profile and clickNext >. ClickingFinishat this point will automatically select and download all matching traces.



If required, the selected remote connections are created and connection is established. The user may be prompted for a password. This can be avoided by storing the password for the connection in theRemote Connectionspreference page.



The root path of every Trace Group is scanned for matching files. The result is shown in theRemote Traceswizard page.



Select the traces to fetch by checking or unchecking the desired connection node, trace group, folder or individual trace. ClickFinishto complete the operation.

If any name conflict occurs, the user will be prompted to rename, overwrite or skip the trace, unless theOverwrite existing trace without warningoption was checked in theRemote Profileswizard page.

The downloaded traces will be imported to the initially selected project folder. They will be stored under a folder structure with the pattern<connection name>/<path>/<trace name>where the path is the trace's remote path relative to its trace group's root path.