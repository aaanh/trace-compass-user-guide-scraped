## LTTng Tracer Control Preferences

Several LTTng 2.0 tracer control preferences exists which can be configured. To configure these preferences, selectWindow -> Preferencesfrom the top level menu. The preference display will open. Then selectTracing -> LTTng Tracer Control Preferences. This preferences page allows the user to specify the tracing group of the user and to specify the command execution timeout as well as it allows the user to configure the logging of LTTng 2.0 tracer control commands and results to a file.



To change the tracing group of the user which will be specified on each command line, enter the new group name in theTracing Grouptext field and click buttonOK. The default tracing group istracingand can be restored by pressing theRestore Defaultsbutton.



To configure logging of trace control commands and the corresponding command result to a file, selected the buttonLogging. To append to an existing log file, select theAppendbutton. Deselect theAppendbutton to overwrite any existing log file. It's possible to specify a verbose level. There are 3 levels with inceasing verbosity fromLevel 1toLevel 3. To change the verbosity level, select the relevant level or selectNone. IfNoneis selected only commands and command results are logged. Then press on buttonOK. The log file will be stored in the users home directory with the namelttng_tracer_control.log. The name and location cannot be changed. To reset to default preferences, click on the buttonRestore Defaults.



To configure the LTTng command execution timeout, selectTracing -> Remote Connection Preferencesand enter a timeout value into the text fieldCommand Timeout (in seconds). Then press on buttonOK. To reset to the default value of 15 seconds, click on the buttonRestore Defaults.