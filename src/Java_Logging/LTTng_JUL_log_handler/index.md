## LTTng JUL log handler

The various log handlers have an overhead on the application. The ConsoleHandler has a visible impact on Trace Compass performance. The FileHandler also has an overhead though less visible, but when logging from multiple threads at the same time, the file becomes a bottleneck, so that logging data cannot be used with accuracy for performance analysis. TheLTTng log handleris much better in a multi-threads context.

LTTng-UST comes with the Java JUL agent in most distros. Otherwise, it is possible to manually compile lttng-ust with options--enable-java-agent-juland install it.

The necessary classes for the java agent will have been installed on the system. Since Equinox (the OSGi implementation used by Eclipse and thus Trace Compass) uses its own classpath and ignores any classpath entered on the command line for security reasons, one needs to specify the agent class path with the bootclasspath argument:

Note that unlike the -classpath argument, -Xbootsclasspath does not follow the dependencies specified by a jar's Manifest, thus it is required to list both the -jul and the -common jars here.

These classes need to load the LTTng JNI library. Because they were loaded from the boot class path by the boot ClassLoader, the library path entered on the command line is ignored. A workaround is to manually copy the library to the jvm's main library path. For example

Or to overwrite the JVM's library path with the following VM argument.

Disclaimer: this last method overwrites the main java library path. It may have unknown side-effects. None were found yet.

LTTng can now be used as a handler for Trace Compass's JUL, by adding the following line to the logger.properties file

The tracepoints will be those logged by a previously defined configuration file. Here is how to setup LTTng to handle JUL logging: