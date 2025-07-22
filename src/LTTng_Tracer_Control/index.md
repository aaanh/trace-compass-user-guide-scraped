# LTTng Tracer Control

The LTTng Tracer Control in Eclipse for the LTTng Tracer toolchain version v2.0 (or later) is done using SSH and requires an SSH server to be running on the remote host. For the SSH connection the SSH implementation of Remote Services is used. The functions to control the LTTng tracer (e.g. start and stop), either locally or remotely, are available from a dedicated Control View.

In the following sections the LTTng 2.0 tracer control integration in Eclipse is described. Please refer to the LTTng 2.0 tracer control command line manual for more details and descriptions about all commands and their command line parametersReferences.

## Control View

To open the Control View, select'Window->Show View->Other...->LTTng->Control View.



### Creating a New Connection to a Remote Host

To connect to a remote host, select theNew Connectionbutton in the Control View.



A new dialog is opened for selecting a remote connection. You can also edit or define a remote connection from here.



To define a new remote host using the default SSH service, selectBuit-in SSHand then selectCreate.... This will start the standardNew Connectionwizard provided by the Remote Services plugin. Similar, to edit the definition of a remote connection, selectEdit...and use theEdit Connectionwizard provided by the SSH service. In case you have installed an additional adapter for the Remote Services, you can choose to define a remote connection based on this adapter.



To use an existing connection definition, select the relevant entry in the tree and then selectOk.



A new display will show for providing the user name and password. This display only opens if no password had been saved before. Enter user name and password in thePassword Requireddialog box and selectOk.



After pressingOkthe SSH connection will be established and after successful login the Control View implementation retrieves the LTTng Tracer Control information. This information will be displayed in the Control View in form of a tree structure.



The top level tree node is the representation of the remote connection (host). The connection name of the connection will be displayed. Depending on the connection state different icons are displayed. If the node isCONNECTEDthe icon is shown, otherwise (statesCONNECTING,DISCONNNECTINGorDISCONNECTEDthe icon is.

Under the host level two folder groups are located. The first one is theProvidergroup. The second one is theSessionsgroup.

Under theProvidergroup all trace providers are displayed. Trace providers areKerneland any user space application that supports UST tracing. Under each provider a corresponding list of events are displayed.

Under theSessionsgroup all current sessions will be shown. The level under the sessions show the configured domains. Currently the LTTng Tracer Toolchain supports domainKernel,UST global,JUL,Log4jandPython. Under the domainsKernelandUST Globalthe configured channels will be displayed. The last level is under the channels where the configured events are displayed.

Each session can beACTIVEorINACTIVE. Active means that tracing has been started, inactive means that the tracing has been stopped. Depending on the state of a session a different icon is displayed. The icon for an active session is. The icon for an inactive session is.

Each channel can beENABLEDorDISABLED. An enabled channel means that all configured events of that channel will be traced and a disabled channel won't trace any of its configured events. Different icons are displayed depending on the state of the channel. The icon for an enabled channel isand the icon for a disabled channel is.

Events within a channel can be in stateENABLEDorDISABLED. Enabled events are stored in the trace when passed during program execution. Disabled events on the other hand won't be traced. Depending on the state of the event the icons for the event is different. An enabled event has the iconand a disabled event the icon.

### Disconnecting from a Remote Host

To disconnect from a remote host, select the host in the Control View and press theDisconnectbutton. Alternatively, press the right mouse button. A context-sensitive menu will show. Select theDisconnectbutton.



### Connecting to a Remote Host

To connect to a remote host, select the host in the Control View and press theConnectbutton. Alternatively, press the right mouse button. A context-sensitive menu will show. Select theConnectbutton. This will start the connection process as discribed inCreating a New Connection to a Remote Host.



### Deleting to a Remote Host Connection

To delete a remote host connection, select the host in the Control View and press theDeletebutton. Alternatively, press the right mouse button. A context-sensitive menu will show. Select theDeletebutton. For that command to be active the connection state has to beDISCONNECTEDand the trace has to be closed.



### Creating a Tracing Session

To create a tracing session, select the tree nodeSessionsand press the right mouse button. Then select theCreate Session...button of the context-sensitive menu.



A dialog box will open for entering information about the session to be created.



Fill in theSession Nameand optionally theSession Pathand pressOk. Upon successful operation a new session will be created and added under the tree nodeSessions.

### Creating a Tracing Session With Advanced Options

LTTng Tools version v2.1.0 introduces the possibility to configure the trace output location at session creation time. The trace can be stored in the (tracer) local file system or can be transferred over the network.

To create a tracing session and configure the trace output, open the trace session dialog as described in chapterCreating a Tracing Session. A dialog box will open for entering information about the session to be created.



The buttonAdvanced >>>will only show if the remote host has LTTng Tools v2.1.0 installed. To configure the trace output select theAdvanced >>>button. The Dialog box will be shown new fields to configure the trace output location.



By default, the buttonUse same protocol and address for data and controlis selected which allows to configure the sameProtocolandAddressfor both data URL and control URL.

If buttonUse same protocol and address for data and controlis selected theProtocolcan benetfor the default network protocol which is TCP (IPv4),net6for the default network protocol which is TCP (IPv6) andfilefor the local file system. Fornetandnet6the port can be configured. Enter a value inPortfor data and control URL or keep them empty for the default port to be used. Usingfileas protocol no port can be configured and the text fields are disabled.

If buttonUse same protocol and address for data and controlis not selected theProtocolcan benetfor the default network protocol which is TCP (IPv4),net6for the default network protocol which is TCP (IPv6),tcpfor the network protocol TCP (IPv4) andtcp6for the network protocol TCP (IPv6). Note that fornetandnet6always the default port is used and hence the port text fields are disabled. To configure non-default ports usetcportcp6.

The text fieldTrace Pathallows for specifying the path relative to the location defined by therelaydor relative to the location specified by theAddresswhen using protocolfile. For more information about therelaydseeLTTng relayd User Manualin chapterReferences.

To create a session with advanced options, fill in the relevant parameters and pressOk. Upon successful operation a new session will be created and added under the tree nodeSessions.

### Creating a Snapshot Tracing Session

LTTng Tools version v2.3.0 introduces the possibility to create snapshot tracing sessions. After starting tracing the trace events are not stored on disk or over the network. They are only transfered to disk or over the network when the user records a snapshot. To create such a snapshot session, open the trace session dialog as described in chapterCreating a Tracing Session.



Fill in all necessary information, select the radio button forSnapshot Modeand pressOk. By default, the location for the snapshot output will be on the host where the host is located.

Refer to chapterRecording a Snapshotfor how to create a snapshot.

### Enabling Channels - General

Enabling channels can be done using a session tree node when the domain hasn't be created in the session or, alternatively on a domain tree node of a session in case the domain is already available.

### Enabling Channels On Session Level

To enable a channel, select the tree node of the relevant session and press the right mouse button. Then select theEnable Channel...button of the context-sensitive menu.



A dialog box will open for entering information about the channel to be created.



By default the domainKernelis selected. To create a UST channel, selectUSTunder the domain section. The label <Default> in any text box indicates that the default value of the tracer will be configured. To initialize the dialog box press buttonDefault.

Note: You cannot create a channel under theJUL,LOG4JandPythondomain. Instead those domains uses a default channel under theUST globaldomain namedlttng_jul_channel,lttng_log4j_channelorlttng_python_channel. Those are the channels that LTTng uses to trace Java or Python application and you cannot addUSTevents to those channels.

If required update the following channel information and then pressOk.
- Channel Name: The name of the channel.
- Sub Buffer size: The size of the sub-buffers of the channel (in bytes).
- Number of Sub Buffers: The number of sub-buffers of the channel.
- Switch Timer Interval: The switch timer interval.
- Read Timer Interval: The read timer interval.
- Discard Mode:Overwriteevents in buffer orDiscardnew events when buffer is full.
- Channel Name: The name of the channel.
- Sub Buffer size: The size of the sub-buffers of the channel (in bytes).
- Number of Sub Buffers: The number of sub-buffers of the channel.
- Switch Timer Interval: The switch timer interval.
- Read Timer Interval: The read timer interval.
- Discard Mode:Overwriteevents in buffer orDiscardnew events when buffer is full.

Upon successful operation, the requested domain will be created under the session tree node as well as the requested channel will be added under the domain. The channel will beENABLED.

### Configuring Trace File Rotation

Since LTTng Tools v2.2.0 it is possible to set the maximum size of trace files and the maximum number of them. These options are located in the same dialog box that is used for enabling channels.


- Maximum size of trace files: The maximum size of trace files
- Maximum number of trace files: The maximum number of trace files
- Maximum size of trace files: The maximum size of trace files
- Maximum number of trace files: The maximum number of trace files

### Configuring per UID and per PID Buffers (UST only)

Since LTTng Tools v2.2.0 it is possible to configure the type of buffers forUSTapplication. It is now possible to choose between perUIDbuffers (per user ID) and perPIDbuffers (per process ID) using the dialog box for enabling channels.


- Per PID buffers: To activate the per PID buffers option for UST channels
- Per UID buffers: To activate the per UID buffers option for UST channels
- Per PID buffers: To activate the per PID buffers option for UST channels
- Per UID buffers: To activate the per UID buffers option for UST channels

If no buffer type is selected then the default value of the tracer will be configured.

Note thatGlobal shared buffersis only for kernel channel and is pre-selected whenKernelis selected in the dalog box.

### Configuring Periodical Flush for metadata Channel

Since LTTng Tools v2.2.0 it is possible to configure periodical flush for the metadata channel. To set this, use the checkboxConfigure metadata channelthen fill the switch timer interval.



### Enabling Channels On Domain Level

Once a domain is available, channels can be enabled directly using the domain. To enable a channel under an existing domain, select the tree node of the relevant domain and press the right mouse button. Then select theEnable Channel...button of the context-sensitive menu.



The dialog box for enabling channel will open for entering information about the channel to be created. Note that the domain is pre-selected and cannot be changed. Fill the relevant information and pressOk.

### Enabling and Disabling Channels

To disable one or more enabled channels, select the tree nodes of the relevant channels and press the right mouse button. Then select theDisable Channelmenu item of the context-sensitive menu.



Upon successful operation, the selected channels will beDISABLEDand the icons for the channels will be updated.

To enable one or more disabled channels, select the tree nodes of the relevant channels and press the right mouse button. Then select theEnable Channelmenu item of the context-sensitive menu.



Upon successful operation, the selected channels will beENABLEDand the icons for the channels will be updated.

### Enabling Events - General

Enabling events can be done using different levels in the tree node. It can be done on the session, domain level and channel level. For the case of session or domain, i.e. when no specific channels is assigned then enabling of events is done on the default channel with the namechannel0which created, if not already exists, by the LTTng tracer control on the server side.

### Enabling Kernel Events On Session Level

To enable events, select the tree node of the relevant session and press the right mouse button. Then select theEnable Event (default channel)...button of the context-sensitive menu.



A dialog box will open for entering information about events to be enabled.



By default the domainKernelis selected and the kernel specific data sections are created. From this dialog box kernelTracepointevents,System calls (Syscall), aDynamic Probeor aDynamic Function entry/returnprobe can be enabled. Note that events of one of these types at a time can be enabled.

To enable allTracepointsand allSystem calls (Syscall), select the buttonSelectof sectionAll Tracepoint Events and Syscallsand pressOk.



Upon successful operation, the domainKernelwill be created in the tree (if neccessary), the default channel with name "channel0" will be added under the domain (if necessary) as well as all a wildcard event*of typeTRACEPOINTunder the channel and a wildcard event*of typeSYSCALL. The channel and events will beENABLED.

To enableTracepointevents, first select the correspondingSelectbutton, then select either all tracepoins (selectAll) or select selectively one or more tracepoints in the displayed tree of tracepoints. You can also enter directly the name of the events you want to enable (comma separated list and wildcards are supported). Finally pressOk.



Upon successful operation, the domainKernelwill be created in the tree (if neccessary), the default channel with name "channel0" will be added under the domain (if necessary) as well as all requested events of typeTRACEPOINTunder the channel. The channel and events will beENABLED.



To enableSyscallevents, first select the correspondingSelectbutton, then select either all syscalls (selectAll) or select selectively one or more syscalls in the displayed tree of syscalls. You can also enter directly the name of the events you want to enable (comma separated list and wildcards are supported). Finally pressOk.



Upon successful operation, the domainKernelwill be created in the tree (if neccessary), the default channel with name "channel0" will be added under the domain (if necessary) as well as all requested events of typeSYSCALLunder the channel. The channel and events will beENABLED.



To enable aDynamic Probeevent, select the correspondingSelectbutton, fill theEvent NameandProbefields and pressOk. Note that the probe can be an address, symbol or a symbol+offset where the address and offset can be octal (0NNN...), decimal (NNN...) or hexadecimal (0xNNN...).



Upon successful operation, the dynamic probe event with the given name and event typePROBEwill be added under the default channel (channel0). If necessary the domainKerneland the channelchannel0will be created.



To enable aDynamic Function entry/return Probeevent, select the correspondingSelectbutton, fill theEvent NameandFunctionfields and pressOk. Note that the funtion probe can be an address, symbol or a symbol+offset where the address and offset can be octal (0NNN...), decimal (NNN...) or hexadecimal (0xNNN...).



Upon successful operation, the dynamic function probe event with the given name and event typePROBEwill be added under the default channel (channel0). If necessary the domainKerneland the channelchannel0will be created.



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



### Enabling JUL Events On Session Level

For enabling JUL loggers, first open the enable events dialog as described in sectionEnabling Kernel Events On Session Leveland select domainJUL.

To enableLoggers, first select the correspondingSelectbutton, then select either all loggers (selectAll) or select selectively one or more loggers in the displayed tree of loggers and finally pressOk.



Upon successful operation, the domainJULwill be created in the tree (if neccessary). With JUL loggers there is no channel, you see the enabled loggers directly under theJULdomain. Note that for the case thatAllloggers were selected the wildcard*is used which will be shown in the Control View as below.



For JUL it is possible to enableLoggerevents using log levels. To enableLoggerevents using log levels, check the correspondingSelectbutton, select a log level from the drop down menu, fill in the relevant information (see below) and pressOk.
- loglevel: To specify if a range of log levels (0 to selected log level) shall be configured
- loglevel-only: To specify that only the specified log level shall be configured
- loglevel: To specify if a range of log levels (0 to selected log level) shall be configured
- loglevel-only: To specify that only the specified log level shall be configured



### Enabling LOG4J Events On Session Level

For enabling LOG4J loggers, first open the enable events dialog as described in sectionEnabling JUL Events On Session Leveland select domainLOG4J.

To enableLoggers, first select the correspondingSelectbutton, then select either all loggers (selectAll) or select selectively one or more loggers in the displayed tree of loggers and finally pressOk.



Upon successful operation, the domainLOG4Jwill be created in the tree (if neccessary). With LOG4J loggers there is no channel, you see the enabled loggers directly under theLOG4Jdomain. Note that for the case thatAllloggers were selected the wildcard*is used which will be shown in the Control View as below.



For LOG4J it is possible to enableLoggerevents using log levels. To enableLoggerevents using log levels, check the correspondingSelectbutton, select a log level from the drop down menu, fill in the relevant information (see below) and pressOk.
- loglevel: To specify if a range of log levels (0 to selected log level) shall be configured
- loglevel-only: To specify that only the specified log level shall be configured
- loglevel: To specify if a range of log levels (0 to selected log level) shall be configured
- loglevel-only: To specify that only the specified log level shall be configured



### Enabling Python Events On Session Level

For enabling Python loggers, first open the enable events dialog as described in sectionEnabling JUL Events On Session Leveland select domainPython.

To enableLoggers, first select the correspondingSelectbutton, then select either all loggers (selectAll) or select selectively one or more loggers in the displayed tree of loggers. You can also enter the name of your logger in the text field. Finally pressOk.



Upon successful operation, the domainPythonwill be created in the tree (if neccessary). With Python loggers there is no channel, you see the enabled loggers directly under thePythondomain. Note that for the case thatAllloggers were selected the wildcard*is used which will be shown in the Control View as below.



For Python it is possible to enableLoggerevents using log levels. To enableLoggerevents using log levels, check the correspondingSelectbutton, select a log level from the drop down menu, fill in the relevant information (see below) and pressOk.
- loglevel: To specify if a range of log levels (0 to selected log level) shall be configured
- loglevel-only: To specify that only the specified log level shall be configured
- loglevel: To specify if a range of log levels (0 to selected log level) shall be configured
- loglevel-only: To specify that only the specified log level shall be configured



### Enabling Events On Domain Level

Kernel events can also be enabled on the domain level. For that select the relevant domain tree node, click the right mouse button and the selectEnable Event (default channel).... A new dialog box will open for providing information about the events to be enabled. Depending on the domain,Kernel,UST global,JUL,LOG4JorPython, the domain specific fields are shown and the domain selector is preselected and read-only.



Instructions for enalbing events for a particular domain can be found here:
- Kerneldomain:Enabling Kernel Events On Session Level
- UST globaldomain:Enabling UST Events On Session Level
- JULdomain:Enabling JUL Events On Session Level
- LOG4Jdomain:Enabling LOG4J Events On Session Level
- Pythondomain:Enabling Python Events On Session Level
- Kerneldomain:Enabling Kernel Events On Session Level
- UST globaldomain:Enabling UST Events On Session Level
- JULdomain:Enabling JUL Events On Session Level
- LOG4Jdomain:Enabling LOG4J Events On Session Level
- Pythondomain:Enabling Python Events On Session Level

The events will be added to the default channelchannel0. This channel will be created by on the server side if necessary.

### Enabling Events On Channel Level

Kernel events can also be enabled on the channel level. If necessary, create a channel as described in sectionsEnabling Channels On Session LevelorEnabling Channels On Domain Level.

Then select the relevant channel tree node, click the right mouse button and the selectEnable Event.... A new dialog box will open for providing information about the events to be enabled. Depending on the domain,KernelorUST global, the domain specific fields are shown and the domain selector is preselected and read-only. Since there is no channel under theJUL,LOG4JorPythondomain you cannot enable those loggers directly from a channel.



To enable events for domainKernelfollow the instructions in sectionEnabling Kernel Events On Session Level, for domainUST globalEnabling UST Events On Session Level.

When enabling events on the channel level, the events will be add to the selected channel.

### Enabling and Disabling Events

To disable one or more enabled events, select the tree nodes of the relevant events and click the right mouse button. Then selectDisable Eventmenu item in the context-sensitive menu.



Upon successful operation, the selected events will beDISABLEDand the icons for these events will be updated.

To enable one or more disabled events, select the tree nodes of the relevant events and press the right mouse button. Then select theEnable Eventmenu item of the context-sensitive menu.



Upon successful operation, the selected events will beENABLEDand the icons for these events will be updated.

Note: There is currently a limitation for kernel event of typeSYSCALL. This kernel event can not be disabled. An error will appear when trying to disable this type of event. A work-around for that is to have the syscall event in a separate channel and disable the channel instead of the event.

### Enabling Tracepoint Events From Provider

It is possible to enable events of typeTracepointdirectly from the providers and assign the enabled event to a session and channel. Before doing that a session has to be created as described in sectionCreating a Tracing Session. Also, if other than default channelchannel0is required, create a channel as described in sectionsEnabling Channels On Session LevelorEnabling Channels On Domain Level.

To assign tracepoint events to a session and channel, select the events to be enabled under the provider (e.g. providerKernel), click right mouse button and then selectEnable Event...menu item from the context sensitive menu.



A new display will open for defining the session and channel.



Select a session from theSession Listdrop-down menu, a channel from theChannel Listdrop-down menu and the pressOk. Upon successful operation, the selected events will be added to the selected session and channel of the domain that the selected provider belongs to. In case that there was no channel available, the domain and the default channelchannel0will be created for corresponding session. The newly added events will beENABLED.



### Configuring Filter Expression When Enabling Events

It is possible to provide a filter expression when enabling events for UST or Kernel. This feature has been available for UST since LTTng v2.1.0 and for Kernel since v2.7.0. To configure a filter expression, open the enable event dialog as described in previous chaptersEnabling UST Events On Session Level,Enabling Kernel Events On Session Level,Enabling Events On Domain LevelorEnabling Events On Channel Level. Then configure the relevant events and enter the filter expression in theFilter Expressiontext field.



Alternatively, open the dialog box for assigning events to a session and channel described inEnabling Tracepoint Events From Providerand enter the filter expression in theFilter Expressiontext field.



For the syntax of the filter expression refer to theLTTng Tracer Control Command Line Tool User Manualof chapterReferences.

### Adding Contexts to Channels and Events of a Domain

It is possible to add contexts to channels and events. Adding contexts on channels and events from the domain level, will enable the specified contexts to all channels of the domain and all their events. To add contexts on the domain level, select a domain, click right mouse button on a domain tree node (e.g. providerKernel) and select the menu itemAdd Context...from the context-sensitive menu.



A new display will open for selecting one or more contexts to add.



The tree shows all available context that can be added. Select one or more context and the pressOk. Upon successful operation, the selected context will be added to all channels and their events of the selected domain.

Note: The LTTng UST tracer only supports  contextsprocname,pthread_id,vpidvtid. Adding any other contexts in the UST domina will fail.

### Adding Contexts to All Events of a Channel

Adding contexts on channels and events from the channel level, will enable the specified contexts to all events of the selected channel. To add contexts on the channel level, select a channel, click right mouse button on a channel tree node and select the menu itemAdd Context...from the context-sensitive menu.



A new display will open for selecting one or more contexts to add. Select one or more contexts as described in chapterAdding Contexts to Channels and Events of a Domain. Upon successful operation, the selected context will be added to all channels and their events of the selected domain.Notethat the LTTng 2.0 tracer control on the remote host doesn't provide a way to retrieve added contexts. Hence it's not possible to display the context information in the GUI.

### Adding Contexts to an Event of a Specific Channel

Adding contexts to an event of a channel is only available in LTTng Tools versions v2.0.0-2.1.x. The menu option won't be visible for LTTng Tools version v2.2.0 or later. To add contexts on an event select an event of a channel, click right mouse button on the corresponding event tree node and select the menu itemAdd Context...from the context-sensitive menu.



A new display will open for selecting one or more contexts to add. Select one or more contexts as described in chapterAdding Contexts to Channels and Events of a Domain. Upon successful operation, the selected context will be added to the selected event.

### Start Tracing

To start tracing, select one or more sessions to start in the Control View and press theStartbutton. Alternatively, press the right mouse button on the session tree nodes. A context-sensitive menu will show. Then select theStartmenu item.



Upon successful operation, the tracing session will beACTIVEand the icon of the session will be updated.

### Recording a Snapshot

LTTng Tools version v2.3.0 introduces the possibility to create snapshot tracing sessions. After creating a snapshot session (seeCreating a Snapshot Tracing Session) and starting tracing (seeStart Tracing) it possible to record snapshots. To record a snapshot select one or more sessions and press theRecord Snapshotbutton. Alternatively, press the right mouse button on the session tree nodes. A context-sensitive menu will show. Then select theRecored Snapshotmenu item.



This action can be executed many times. It is possible to import the recorded snpshots to a tracing project. The trace session might beACTIVEorINACTIVEfor that. Refer to sectionImporting Session Traces to a Tracing Projecton how to import a trace to a tracing project.

### Stop Tracing

To stop tracing, select one or more sessions to stop in the Control View and press theStopbutton. Alternatively, click the right mouse button on the session tree node. A context-sensitive menu will show. Then select theStopmenu item.



Upon successful operation, the tracing session will beINACTIVEand the icon of the session will be updated.

### Destroying a Tracing Session

To destroy a tracing session, select one or more sessions to destroy in the Control View and press theDestroybutton. Alternatively, click the right mouse button on the session tree node. A context-sensitive menu will show. Then select theDestroy...menu item. Note that the session has to beINACTIVEfor this operation.



A confirmation dialog box will open. Click onOkto destroy the session otherwise click onCancel.



Upon successful operation, the tracing session will be destroyed and removed from the tree.

### Refreshing the Node Information

To refresh the remote host information, select any node in the tree of the Control View and press theRefreshbutton. Alternatively, click the right mouse button on any tree node. A context-sensitive menu will show. Then select theRefreshmenu item.



Upon successful operation, the tree in the Control View will be refreshed with the remote host configuration.

### Importing Session Traces to a Tracing Project

To import traces from a tracing session, select the relevant session and click on theImportButton. Alternatively, click the right mouse button on the session tree node and select the menu itemImport...from the context-sensitive menu.



A new display will open for selecting the traces to import.



By default all traces are selected. A default project with the nameRemoteis selected which will be created if necessary. Update the list of traces to be imported, if necessary, by selecting and deselecting the relevant traces in the tree viewer. Use buttonsSelect AllorDeselect Allto select or deselect all traces. Also if needed, change the tracing project from theAvailable Projectscombo box. The optionCreate Experimentwill create an experiment with all imported traces. By default, the experiment name is the session name. One can change the experiment name by typing a new name in the text box beside the option.

Then press buttonFinish. Upon successful import operation the selected traces will be stored in theTracesdirectory of the specified tracing project. A directory with the connection name will be created under theTracesdirectory. Underneath that, the session directory structure as well as the trace names will be preserved in the destination tracing project. ForKerneltraces the trace typeLinux Kernel Traceand forUSTtraces the trace typeLTTng UST Tracewill be set. From theProject Explorerview, the trace can be analyzed further.

Note: If a trace already exists with the same name in the destination directory, the user can choose to rename the imported trace, overwrite the original trace or skip the trace. When rename is chosen, a number is appended to the trace name, for example kernel becomes kernel(2).



If one selectsRename All,Overwrite AllorSkip Allthe choice will be applied for all traces with a name conflict.

### Importing Network Traces to a Tracing Project

Since LTTng Tools v2.1.0 it is possible to store traces over the network. To import network traces, execute theImportaction as described in chapterImporting Session Traces to a Tracing Project. For network traces theImport Trace Wizardwill be displayed. Follow the instructions in chapterImportingto import the network traces of the current session.

### Saving Tracing Sessions

Since LTTng Tools v2.5.0 it is possible to save tracing sessions. The LTTng Tools command-line tool will save the sessions to XML files located by default in a subdirectory of the user's home directory. The Trace CompassControlview integration for this feature will also store this session profile file into the user's Trace Compass workspace. This will allow user's to re-use session profiles across remote nodes. To save one or more sessions, select the tree nodes of the relevant sessions and press the right mouse button. Then select theSave...entry of the context-sensitive menu.



A new display will open for saving the sessions.



By default theforcebutton is selected that will overwrite any conflicting session profile files on the remote node. Click onOkto save the session(s) otherwise click onCancel. Upon successful operation, the session profile files will be saved on the remote node and then will be downloaded to the user's Trace Compass workspace. In the case that a session XML file already exists in the workspace the user will be prompted to skip or overwrite the existing profile file.

### Loading Tracing Sessions

Since LTTng Tools v2.5.0 it is possible to load tracing sessions. The Trace CompassControlview integrations for this feature will allow to load session profiles that are located in the user's Trace Compass workspace, or alternatively, that are located on the remote node. In the first case the session profiles will be uploaded to the remote node before the load command is executed.

To load one or more sessions, select the tree nodeSessionsand press the right mouse button. Then select theLoad...entry of the context-sensitive menu.



A new display will open for loading session profiles.



By default theLocalbutton andforcebuttons are selected and session profile files of the user's workspace will be listed. Select one or more profiles, update theforcebutton if needed and then clickOk. This will upload the session profile files to the remote node. If a session profile file with the same name already exist on the remote node, it will be overwritten. If theforcebutton is selected any existing session with a conflicting name will be destroyed and a new one will be created.

Alternatively, one can select theRemotebutton to list all available session profile files on the remote node. To load one of the remote session profiles, select one or more profiles, update theforcebutton if needed and then clickOk.



Upon successful operation, the tracing sessions of the selected session profiles are created and added under the tree nodeSessionstheControlview.

### Managing Tracing Session Profiles

TheLTTng Remote Profilespreference page is used to manage the list of LTTng session profiles that are stored in the user's Trace Compass workspace. To open the preference page, select theManage...button of theLoad Sessionsdialog described in chapterLoading Tracing Sessions. Alternatively, selectWindow -> Preferencesfrom the top level menu and go toTracing -> LTTng Remote Profiles.



The following actions can be performed from this dialog:
- Delete
- Delete

Select one or more LTTng session profiles from the list and click theDeletebutton to remove the profile from the Trace Compass workspace. The user will be prompted to confirm the deletion.
- Import...
- Import...

Click theImport...button and select a file from the opened file dialog to import a session profile file. If the file name conflicts with an existing profile file, the user will be prompted to skip or overwrite the existing profile file.
- Export...
- Export...

Select one or more session profile files from the list, click theExport...button and enter or select a directory in the opened directory dialog to export the profile files. If the file name conflicts with an existing profile file in the destination directory, the user will be prompted to skip or overwrite the existing profile file.

## Properties View

The Control View provides property information of selected tree component. Depending on the selected tree component different properties are displayed in the property view. For example, when selecting the node level the property view will be filled as followed:



List of properties:
- HostPropertiesConnection Name: The alias name to be displayed in the Control View.Host Name: The IP address or DNS name of the remote system.State: The state of the connection (CONNECTED,CONNECTING,DISCONNNECTINGorDISCONNECTED).
- Connection Name: The alias name to be displayed in the Control View.
- Host Name: The IP address or DNS name of the remote system.
- State: The state of the connection (CONNECTED,CONNECTING,DISCONNNECTINGorDISCONNECTED).
- Kernel ProviderPropertiesProvider Name: The name of the provider.
- Provider Name: The name of the provider.
- UST ProviderPropertiesProvider Name: The name of the provider.Process ID: The process ID of the provider.
- Provider Name: The name of the provider.
- Process ID: The process ID of the provider.
- EventProperties (Provider)Event Name: The name of the event.Event Type: The event type (TRACEPOINTonly).Fields: Shows a list of fields defined for the selected event. (UST only, since support for LTTng Tools v2.1.0)Log Level: The log level of the event.
- Event Name: The name of the event.
- Event Type: The event type (TRACEPOINTonly).
- Fields: Shows a list of fields defined for the selected event. (UST only, since support for LTTng Tools v2.1.0)
- Log Level: The log level of the event.
- LoggerProperties (Provider)Logger Name: The name of the logger.Logger Type: The event type (TRACEPOINTonly).
- Logger Name: The name of the logger.
- Logger Type: The event type (TRACEPOINTonly).
- SessionPropertiesSession Name: The name of the Session.Session Path: The path on the remote host where the traces will be stored. (Not shown for snapshot sessions).State: The state of the session (ACTIVEorINACTIVE)Snapshot ID: The snapshot ID. (Only shown for snapshot sessions).Snapshot Name: The name of the snapshot output configuration. (Only shown for snapshot sessions).Snapshot Path: The path where the snapshot session is located. (Only shown for snapshot sessions).
- Session Name: The name of the Session.
- Session Path: The path on the remote host where the traces will be stored. (Not shown for snapshot sessions).
- State: The state of the session (ACTIVEorINACTIVE)
- Snapshot ID: The snapshot ID. (Only shown for snapshot sessions).
- Snapshot Name: The name of the snapshot output configuration. (Only shown for snapshot sessions).
- Snapshot Path: The path where the snapshot session is located. (Only shown for snapshot sessions).
- DomainPropertiesDomain Name: The name of the domain.Buffer Type: The buffer type of the domain.
- Domain Name: The name of the domain.
- Buffer Type: The buffer type of the domain.
- ChannelPropertiesChannel Name: The name of the channel.Number of Sub Buffers: The number of sub-buffers of the channel.Output type: The output type for the trace (e.g.splice()ormmap())Overwrite Mode: The channel overwrite mode (truefor overwrite mode,falsefor discard)Read Timer Interval: The read timer interval.State: The channel state (ENABLEDorDISABLED)Sub Buffer size: The size of the sub-buffers of the channel (in bytes).Switch Timer Interval: The switch timer interval.Number of Discarded Events: The number of discarded events of the channel.Number of Lost Packets: The number of lost packets of the channel.
- Channel Name: The name of the channel.
- Number of Sub Buffers: The number of sub-buffers of the channel.
- Output type: The output type for the trace (e.g.splice()ormmap())
- Overwrite Mode: The channel overwrite mode (truefor overwrite mode,falsefor discard)
- Read Timer Interval: The read timer interval.
- State: The channel state (ENABLEDorDISABLED)
- Sub Buffer size: The size of the sub-buffers of the channel (in bytes).
- Switch Timer Interval: The switch timer interval.
- Number of Discarded Events: The number of discarded events of the channel.
- Number of Lost Packets: The number of lost packets of the channel.
- EventProperties (Channel)Event Name: The name of the event.Event Type: The event type (TRACEPOINT,SYSCALLorPROBE).Log Level: The log level of the event. (For LTTng Tools v2.4.0 or later,<=prior the log level name will indicate a range of log levels and==a single log level.)State: The Event state (ENABLEDorDISABLED)Filter: Showswith filterif a filter expression is configured else propertyFilteris omitted. (since support for LTTng Tools v2.1.0)
- Event Name: The name of the event.
- Event Type: The event type (TRACEPOINT,SYSCALLorPROBE).
- Log Level: The log level of the event. (For LTTng Tools v2.4.0 or later,<=prior the log level name will indicate a range of log levels and==a single log level.)
- State: The Event state (ENABLEDorDISABLED)
- Filter: Showswith filterif a filter expression is configured else propertyFilteris omitted. (since support for LTTng Tools v2.1.0)
- LoggerProperties (Domain)Logger Name: The name of the logger.Logger Type: The logger type (TRACEPOINT).Log Level: The log level of the logger. (For LTTng Tools v2.4.0 or later,<=prior the log level name will indicate a range of log levels and==a single log level.)State: The logger state (ENABLEDorDISABLED)
- Logger Name: The name of the logger.
- Logger Type: The logger type (TRACEPOINT).
- Log Level: The log level of the logger. (For LTTng Tools v2.4.0 or later,<=prior the log level name will indicate a range of log levels and==a single log level.)
- State: The logger state (ENABLEDorDISABLED)
- HostPropertiesConnection Name: The alias name to be displayed in the Control View.Host Name: The IP address or DNS name of the remote system.State: The state of the connection (CONNECTED,CONNECTING,DISCONNNECTINGorDISCONNECTED).
- Connection Name: The alias name to be displayed in the Control View.
- Host Name: The IP address or DNS name of the remote system.
- State: The state of the connection (CONNECTED,CONNECTING,DISCONNNECTINGorDISCONNECTED).
- Connection Name: The alias name to be displayed in the Control View.
- Host Name: The IP address or DNS name of the remote system.
- State: The state of the connection (CONNECTED,CONNECTING,DISCONNNECTINGorDISCONNECTED).
- Connection Name: The alias name to be displayed in the Control View.
- Host Name: The IP address or DNS name of the remote system.
- State: The state of the connection (CONNECTED,CONNECTING,DISCONNNECTINGorDISCONNECTED).
- Kernel ProviderPropertiesProvider Name: The name of the provider.
- Provider Name: The name of the provider.
- Provider Name: The name of the provider.
- Provider Name: The name of the provider.
- UST ProviderPropertiesProvider Name: The name of the provider.Process ID: The process ID of the provider.
- Provider Name: The name of the provider.
- Process ID: The process ID of the provider.
- Provider Name: The name of the provider.
- Process ID: The process ID of the provider.
- Provider Name: The name of the provider.
- Process ID: The process ID of the provider.
- EventProperties (Provider)Event Name: The name of the event.Event Type: The event type (TRACEPOINTonly).Fields: Shows a list of fields defined for the selected event. (UST only, since support for LTTng Tools v2.1.0)Log Level: The log level of the event.
- Event Name: The name of the event.
- Event Type: The event type (TRACEPOINTonly).
- Fields: Shows a list of fields defined for the selected event. (UST only, since support for LTTng Tools v2.1.0)
- Log Level: The log level of the event.
- Event Name: The name of the event.
- Event Type: The event type (TRACEPOINTonly).
- Fields: Shows a list of fields defined for the selected event. (UST only, since support for LTTng Tools v2.1.0)
- Log Level: The log level of the event.
- Event Name: The name of the event.
- Event Type: The event type (TRACEPOINTonly).
- Fields: Shows a list of fields defined for the selected event. (UST only, since support for LTTng Tools v2.1.0)
- Log Level: The log level of the event.
- LoggerProperties (Provider)Logger Name: The name of the logger.Logger Type: The event type (TRACEPOINTonly).
- Logger Name: The name of the logger.
- Logger Type: The event type (TRACEPOINTonly).
- Logger Name: The name of the logger.
- Logger Type: The event type (TRACEPOINTonly).
- Logger Name: The name of the logger.
- Logger Type: The event type (TRACEPOINTonly).
- SessionPropertiesSession Name: The name of the Session.Session Path: The path on the remote host where the traces will be stored. (Not shown for snapshot sessions).State: The state of the session (ACTIVEorINACTIVE)Snapshot ID: The snapshot ID. (Only shown for snapshot sessions).Snapshot Name: The name of the snapshot output configuration. (Only shown for snapshot sessions).Snapshot Path: The path where the snapshot session is located. (Only shown for snapshot sessions).
- Session Name: The name of the Session.
- Session Path: The path on the remote host where the traces will be stored. (Not shown for snapshot sessions).
- State: The state of the session (ACTIVEorINACTIVE)
- Snapshot ID: The snapshot ID. (Only shown for snapshot sessions).
- Snapshot Name: The name of the snapshot output configuration. (Only shown for snapshot sessions).
- Snapshot Path: The path where the snapshot session is located. (Only shown for snapshot sessions).
- Session Name: The name of the Session.
- Session Path: The path on the remote host where the traces will be stored. (Not shown for snapshot sessions).
- State: The state of the session (ACTIVEorINACTIVE)
- Snapshot ID: The snapshot ID. (Only shown for snapshot sessions).
- Snapshot Name: The name of the snapshot output configuration. (Only shown for snapshot sessions).
- Snapshot Path: The path where the snapshot session is located. (Only shown for snapshot sessions).
- Session Name: The name of the Session.
- Session Path: The path on the remote host where the traces will be stored. (Not shown for snapshot sessions).
- State: The state of the session (ACTIVEorINACTIVE)
- Snapshot ID: The snapshot ID. (Only shown for snapshot sessions).
- Snapshot Name: The name of the snapshot output configuration. (Only shown for snapshot sessions).
- Snapshot Path: The path where the snapshot session is located. (Only shown for snapshot sessions).
- DomainPropertiesDomain Name: The name of the domain.Buffer Type: The buffer type of the domain.
- Domain Name: The name of the domain.
- Buffer Type: The buffer type of the domain.
- Domain Name: The name of the domain.
- Buffer Type: The buffer type of the domain.
- Domain Name: The name of the domain.
- Buffer Type: The buffer type of the domain.
- ChannelPropertiesChannel Name: The name of the channel.Number of Sub Buffers: The number of sub-buffers of the channel.Output type: The output type for the trace (e.g.splice()ormmap())Overwrite Mode: The channel overwrite mode (truefor overwrite mode,falsefor discard)Read Timer Interval: The read timer interval.State: The channel state (ENABLEDorDISABLED)Sub Buffer size: The size of the sub-buffers of the channel (in bytes).Switch Timer Interval: The switch timer interval.Number of Discarded Events: The number of discarded events of the channel.Number of Lost Packets: The number of lost packets of the channel.
- Channel Name: The name of the channel.
- Number of Sub Buffers: The number of sub-buffers of the channel.
- Output type: The output type for the trace (e.g.splice()ormmap())
- Overwrite Mode: The channel overwrite mode (truefor overwrite mode,falsefor discard)
- Read Timer Interval: The read timer interval.
- State: The channel state (ENABLEDorDISABLED)
- Sub Buffer size: The size of the sub-buffers of the channel (in bytes).
- Switch Timer Interval: The switch timer interval.
- Number of Discarded Events: The number of discarded events of the channel.
- Number of Lost Packets: The number of lost packets of the channel.
- Channel Name: The name of the channel.
- Number of Sub Buffers: The number of sub-buffers of the channel.
- Output type: The output type for the trace (e.g.splice()ormmap())
- Overwrite Mode: The channel overwrite mode (truefor overwrite mode,falsefor discard)
- Read Timer Interval: The read timer interval.
- State: The channel state (ENABLEDorDISABLED)
- Sub Buffer size: The size of the sub-buffers of the channel (in bytes).
- Switch Timer Interval: The switch timer interval.
- Number of Discarded Events: The number of discarded events of the channel.
- Number of Lost Packets: The number of lost packets of the channel.
- Channel Name: The name of the channel.
- Number of Sub Buffers: The number of sub-buffers of the channel.
- Output type: The output type for the trace (e.g.splice()ormmap())
- Overwrite Mode: The channel overwrite mode (truefor overwrite mode,falsefor discard)
- Read Timer Interval: The read timer interval.
- State: The channel state (ENABLEDorDISABLED)
- Sub Buffer size: The size of the sub-buffers of the channel (in bytes).
- Switch Timer Interval: The switch timer interval.
- Number of Discarded Events: The number of discarded events of the channel.
- Number of Lost Packets: The number of lost packets of the channel.
- EventProperties (Channel)Event Name: The name of the event.Event Type: The event type (TRACEPOINT,SYSCALLorPROBE).Log Level: The log level of the event. (For LTTng Tools v2.4.0 or later,<=prior the log level name will indicate a range of log levels and==a single log level.)State: The Event state (ENABLEDorDISABLED)Filter: Showswith filterif a filter expression is configured else propertyFilteris omitted. (since support for LTTng Tools v2.1.0)
- Event Name: The name of the event.
- Event Type: The event type (TRACEPOINT,SYSCALLorPROBE).
- Log Level: The log level of the event. (For LTTng Tools v2.4.0 or later,<=prior the log level name will indicate a range of log levels and==a single log level.)
- State: The Event state (ENABLEDorDISABLED)
- Filter: Showswith filterif a filter expression is configured else propertyFilteris omitted. (since support for LTTng Tools v2.1.0)
- Event Name: The name of the event.
- Event Type: The event type (TRACEPOINT,SYSCALLorPROBE).
- Log Level: The log level of the event. (For LTTng Tools v2.4.0 or later,<=prior the log level name will indicate a range of log levels and==a single log level.)
- State: The Event state (ENABLEDorDISABLED)
- Filter: Showswith filterif a filter expression is configured else propertyFilteris omitted. (since support for LTTng Tools v2.1.0)
- Event Name: The name of the event.
- Event Type: The event type (TRACEPOINT,SYSCALLorPROBE).
- Log Level: The log level of the event. (For LTTng Tools v2.4.0 or later,<=prior the log level name will indicate a range of log levels and==a single log level.)
- State: The Event state (ENABLEDorDISABLED)
- Filter: Showswith filterif a filter expression is configured else propertyFilteris omitted. (since support for LTTng Tools v2.1.0)
- LoggerProperties (Domain)Logger Name: The name of the logger.Logger Type: The logger type (TRACEPOINT).Log Level: The log level of the logger. (For LTTng Tools v2.4.0 or later,<=prior the log level name will indicate a range of log levels and==a single log level.)State: The logger state (ENABLEDorDISABLED)
- Logger Name: The name of the logger.
- Logger Type: The logger type (TRACEPOINT).
- Log Level: The log level of the logger. (For LTTng Tools v2.4.0 or later,<=prior the log level name will indicate a range of log levels and==a single log level.)
- State: The logger state (ENABLEDorDISABLED)
- Logger Name: The name of the logger.
- Logger Type: The logger type (TRACEPOINT).
- Log Level: The log level of the logger. (For LTTng Tools v2.4.0 or later,<=prior the log level name will indicate a range of log levels and==a single log level.)
- State: The logger state (ENABLEDorDISABLED)
- Logger Name: The name of the logger.
- Logger Type: The logger type (TRACEPOINT).
- Log Level: The log level of the logger. (For LTTng Tools v2.4.0 or later,<=prior the log level name will indicate a range of log levels and==a single log level.)
- State: The logger state (ENABLEDorDISABLED)

## LTTng Tracer Control Preferences

Several LTTng 2.0 tracer control preferences exists which can be configured. To configure these preferences, selectWindow -> Preferencesfrom the top level menu. The preference display will open. Then selectTracing -> LTTng Tracer Control Preferences. This preferences page allows the user to specify the tracing group of the user and to specify the command execution timeout as well as it allows the user to configure the logging of LTTng 2.0 tracer control commands and results to a file.



To change the tracing group of the user which will be specified on each command line, enter the new group name in theTracing Grouptext field and click buttonOK. The default tracing group istracingand can be restored by pressing theRestore Defaultsbutton.



To configure logging of trace control commands and the corresponding command result to a file, selected the buttonLogging. To append to an existing log file, select theAppendbutton. Deselect theAppendbutton to overwrite any existing log file. It's possible to specify a verbose level. There are 3 levels with inceasing verbosity fromLevel 1toLevel 3. To change the verbosity level, select the relevant level or selectNone. IfNoneis selected only commands and command results are logged. Then press on buttonOK. The log file will be stored in the users home directory with the namelttng_tracer_control.log. The name and location cannot be changed. To reset to default preferences, click on the buttonRestore Defaults.



To configure the LTTng command execution timeout, selectTracing -> Remote Connection Preferencesand enter a timeout value into the text fieldCommand Timeout (in seconds). Then press on buttonOK. To reset to the default value of 15 seconds, click on the buttonRestore Defaults.