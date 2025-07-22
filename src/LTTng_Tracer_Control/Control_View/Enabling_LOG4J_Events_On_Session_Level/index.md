### Enabling LOG4J Events On Session Level

For enabling LOG4J loggers, first open the enable events dialog as described in sectionEnabling JUL Events On Session Leveland select domainLOG4J.

To enableLoggers, first select the correspondingSelectbutton, then select either all loggers (selectAll) or select selectively one or more loggers in the displayed tree of loggers and finally pressOk.



Upon successful operation, the domainLOG4Jwill be created in the tree (if neccessary). With LOG4J loggers there is no channel, you see the enabled loggers directly under theLOG4Jdomain. Note that for the case thatAllloggers were selected the wildcard*is used which will be shown in the Control View as below.



For LOG4J it is possible to enableLoggerevents using log levels. To enableLoggerevents using log levels, check the correspondingSelectbutton, select a log level from the drop down menu, fill in the relevant information (see below) and pressOk.
- loglevel: To specify if a range of log levels (0 to selected log level) shall be configured
- loglevel-only: To specify that only the specified log level shall be configured
- loglevel: To specify if a range of log levels (0 to selected log level) shall be configured
- loglevel-only: To specify that only the specified log level shall be configured