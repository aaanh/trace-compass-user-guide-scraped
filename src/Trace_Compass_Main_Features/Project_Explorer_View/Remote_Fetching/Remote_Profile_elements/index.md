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