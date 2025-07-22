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