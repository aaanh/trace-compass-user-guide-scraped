### Enabling Python Events On Session Level

For enabling Python loggers, first open the enable events dialog as described in sectionEnabling JUL Events On Session Leveland select domainPython.

To enableLoggers, first select the correspondingSelectbutton, then select either all loggers (selectAll) or select selectively one or more loggers in the displayed tree of loggers. You can also enter the name of your logger in the text field. Finally pressOk.



Upon successful operation, the domainPythonwill be created in the tree (if neccessary). With Python loggers there is no channel, you see the enabled loggers directly under thePythondomain. Note that for the case thatAllloggers were selected the wildcard*is used which will be shown in the Control View as below.



For Python it is possible to enableLoggerevents using log levels. To enableLoggerevents using log levels, check the correspondingSelectbutton, select a log level from the drop down menu, fill in the relevant information (see below) and pressOk.
- loglevel: To specify if a range of log levels (0 to selected log level) shall be configured
- loglevel-only: To specify that only the specified log level shall be configured
- loglevel: To specify if a range of log levels (0 to selected log level) shall be configured
- loglevel-only: To specify that only the specified log level shall be configured