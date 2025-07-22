### Creating a Tracing Session With Advanced Options

LTTng Tools version v2.1.0 introduces the possibility to configure the trace output location at session creation time. The trace can be stored in the (tracer) local file system or can be transferred over the network.

To create a tracing session and configure the trace output, open the trace session dialog as described in chapterCreating a Tracing Session. A dialog box will open for entering information about the session to be created.



The buttonAdvanced >>>will only show if the remote host has LTTng Tools v2.1.0 installed. To configure the trace output select theAdvanced >>>button. The Dialog box will be shown new fields to configure the trace output location.



By default, the buttonUse same protocol and address for data and controlis selected which allows to configure the sameProtocolandAddressfor both data URL and control URL.

If buttonUse same protocol and address for data and controlis selected theProtocolcan benetfor the default network protocol which is TCP (IPv4),net6for the default network protocol which is TCP (IPv6) andfilefor the local file system. Fornetandnet6the port can be configured. Enter a value inPortfor data and control URL or keep them empty for the default port to be used. Usingfileas protocol no port can be configured and the text fields are disabled.

If buttonUse same protocol and address for data and controlis not selected theProtocolcan benetfor the default network protocol which is TCP (IPv4),net6for the default network protocol which is TCP (IPv6),tcpfor the network protocol TCP (IPv4) andtcp6for the network protocol TCP (IPv6). Note that fornetandnet6always the default port is used and hence the port text fields are disabled. To configure non-default ports usetcportcp6.

The text fieldTrace Pathallows for specifying the path relative to the location defined by therelaydor relative to the location specified by theAddresswhen using protocolfile. For more information about therelaydseeLTTng relayd User Manualin chapterReferences.

To create a session with advanced options, fill in the relevant parameters and pressOk. Upon successful operation a new session will be created and added under the tree nodeSessions.