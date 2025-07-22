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