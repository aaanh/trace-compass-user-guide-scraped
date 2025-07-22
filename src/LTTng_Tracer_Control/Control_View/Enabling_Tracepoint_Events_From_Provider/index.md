### Enabling Tracepoint Events From Provider

It is possible to enable events of typeTracepointdirectly from the providers and assign the enabled event to a session and channel. Before doing that a session has to be created as described in sectionCreating a Tracing Session. Also, if other than default channelchannel0is required, create a channel as described in sectionsEnabling Channels On Session LevelorEnabling Channels On Domain Level.

To assign tracepoint events to a session and channel, select the events to be enabled under the provider (e.g. providerKernel), click right mouse button and then selectEnable Event...menu item from the context sensitive menu.



A new display will open for defining the session and channel.



Select a session from theSession Listdrop-down menu, a channel from theChannel Listdrop-down menu and the pressOk. Upon successful operation, the selected events will be added to the selected session and channel of the domain that the selected provider belongs to. In case that there was no channel available, the domain and the default channelchannel0will be created for corresponding session. The newly added events will beENABLED.