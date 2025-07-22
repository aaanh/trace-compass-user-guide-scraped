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