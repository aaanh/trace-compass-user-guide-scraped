### Enabling UST Events On Session Level

For enabling UST events, first open the enable events dialog as described in sectionEnabling Kernel Events On Session Leveland select domainUST.

To enableTracepointevents, first select the correspondingSelectbutton, then select either all tracepoins (selectAll) or select selectively one or more tracepoints in the displayed tree of tracepoints and finally pressOk.



Upon successful operation, the domainUST globalwill be created in the tree (if neccessary), the default channel with name "channel0" will be added under the domain (if necessary) as well as all requested events under the channel. The channel and events will beENABLED. Note that for the case thatAlltracepoints were selected the wildcard*is used which will be shown in the Control View as below.



For UST it is possible to enableTracepointevents using a wildcard. To enableTracepointevents with a wildcard, select first the correspondingSelectbutton, fill theWildcardfield and pressOk.



Upon successful operation, the event with the given wildcard and event typeTRACEPOINTwill be added under the default channel (channel0). If necessary the domainUST globaland the channelchannel0will be created.



When enablingTracepointwith wildcard, it is possible to specify event(s) (comma separated list) that we want toexcludefrom that wildcard selection. ToexcludeTracepointevents, check the correspondingSelectcheck box, fill theEvent Namesfield and pressOk.



For UST it is possible to enableTracepointevents using log levels. To enableTracepointevents using log levels, select first the correspondingSelectbutton, select a log level from the drop down menu, fill in the relevant information (see below) and pressOk.
- Event Name: Name to display
- loglevel: To specify if a range of log levels (0 to selected log level) shall be configured
- loglevel-only: To specify that only the specified log level shall be configured
- Event Name: Name to display
- loglevel: To specify if a range of log levels (0 to selected log level) shall be configured
- loglevel-only: To specify that only the specified log level shall be configured



Upon successful operation, the event with the given event name and event typeTRACEPOINTwill be added under the default channel (channel0). If necessary the domainUST globaland the channelchannel0will be created.