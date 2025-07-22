### Configuring Filter Expression When Enabling Events

It is possible to provide a filter expression when enabling events for UST or Kernel. This feature has been available for UST since LTTng v2.1.0 and for Kernel since v2.7.0. To configure a filter expression, open the enable event dialog as described in previous chaptersEnabling UST Events On Session Level,Enabling Kernel Events On Session Level,Enabling Events On Domain LevelorEnabling Events On Channel Level. Then configure the relevant events and enter the filter expression in theFilter Expressiontext field.



Alternatively, open the dialog box for assigning events to a session and channel described inEnabling Tracepoint Events From Providerand enter the filter expression in theFilter Expressiontext field.



For the syntax of the filter expression refer to theLTTng Tracer Control Command Line Tool User Manualof chapterReferences.