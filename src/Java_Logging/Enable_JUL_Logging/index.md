## Enable JUL Logging

By default, all the logging of the Trace Compass namespace is disabled. To enable it, one needs to add the following property to thevmargs:-Dorg.eclipse.tracecompass.logging=true.

The log levels and components can be controlled via a configuration file whose path is specified also in thevmargslike this:-Djava.util.logging.config.file=/path/to/logger.properties. An example configuration file can be found in the next section.

If running the RCP, these arguments can be appended at the end of thetracecompass.inifile located in the folder where the executable is located. If running from Eclipse in development mode, in theRun configurations..., the arguments should be added in theArgumentstab in theVM argsbox.