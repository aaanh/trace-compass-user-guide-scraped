## Source Lookup (for LTTng-UST 2.8+)

Starting with LTTng 2.8, the tracer can now provide enough information to
			associate trace events with their location in the original source code.

To make use of this feature, first make sure your binaries are compiled with
			debug information (-g), so that the instruction pointers can be mapped to source
			code locations. This lookup is made using theaddr2lineandnmcommand-line utilities,
			which need to be installed and on the$PATHof the system running Trace
			Compass.addr2lineandnmare available in most Linux distributions, Mac OS X, Windows using Cygwin and others.

The following trace events need to be present in the trace:
- lttng_ust_statedump:start
- lttng_ust_statedump:end
- lttng_ust_statedump:bin_info
- lttng_ust_statedump:build_id
- lttng_ust_statedump:start
- lttng_ust_statedump:end
- lttng_ust_statedump:bin_info
- lttng_ust_statedump:build_id

as well as the following contexts:
- vpid
- ip
- vpid
- ip

For ease of use, you can simply enable all the UST events when setting up your
			session:

Note that you can also create and configure your session using theControl View.

If you want to track source locations in shared libraries loaded by the
			application, you also need to enable the "lttng_ust_dl:*" events, as well
			as preload the UST library providing them when running your program:

If all the required information is present, then theSource Locationcolumn
			of the Event Table should be populated accordingly, and theOpen Source Codeaction should be available. Refer to the sectionEvent Source Lookupfor
			more details.

TheBinary Locationinformation should be present even if the original
			binaries are not available, since it only makes use of information found in the
			trace. A+denotes a relative address (i.e. an offset within the object
			itself), whereas a@denotes an absolute address, for
			non-position-independent objects.



Example of a trace with debug info and corresponding Source Lookup information, showing a tracepoint originating from a shared library

### Binary file location configuration

To resolve addresses to function names and source code locations, the analysis
			makes use of the binary files (executables or shared libraries) present on the
			system. By default, it will look for the file paths as they are found in the
			trace, which means that it should work out-of-the-box if the trace was taken on
			the same machine that Trace Compass is running.

It is possible to configure aroot directorythat will be used as a prefix
			for all file path resolutions. The button to open the configuration dialog is
			calledConfigure how addresses are mapped to function namesand is
			currently located in theFlame Chart View. Note that the Call Stack View
			will also make use of this configuration to resolve its function names.



The symbol configuration dialog for LTTng-UST 2.8+ traces

This can be useful if a trace was taken on a remote target, and an image of that
			target is available locally.

If a binary file is being traced on a target, the paths in the trace will refer
			to the paths on the target. For example, if they are:
- /usr/bin/program
- /usr/lib/libsomething.so
- /usr/local/lib/libcustom.so
- /usr/bin/program
- /usr/lib/libsomething.so
- /usr/local/lib/libcustom.so

and an image of that target is copied locally on the system at/home/user/project/image, which means the binaries above end up at:
- /home/user/project/image/usr/bin/program
- /home/user/project/image/usr/lib/libsomething.so
- /home/user/project/image/usr/local/lib/libcustom.so
- /home/user/project/image/usr/bin/program
- /home/user/project/image/usr/lib/libsomething.so
- /home/user/project/image/usr/local/lib/libcustom.so

Then selecting the/home/user/project/imagedirectory in the configuration
			dialog above will allow Trace Compass to read the debug symbols correctly.

Note that this path prefix will apply to both binary file and source file
			locations, which may or may not be desirable.