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