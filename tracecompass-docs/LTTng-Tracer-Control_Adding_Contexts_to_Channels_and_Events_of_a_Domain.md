### Adding Contexts to Channels and Events of a Domain

It is possible to add contexts to channels and events. Adding contexts on channels and events from the domain level, will enable the specified contexts to all channels of the domain and all their events. To add contexts on the domain level, select a domain, click right mouse button on a domain tree node (e.g. providerKernel) and select the menu itemAdd Context...from the context-sensitive menu.



A new display will open for selecting one or more contexts to add.



The tree shows all available context that can be added. Select one or more context and the pressOk. Upon successful operation, the selected context will be added to all channels and their events of the selected domain.

Note: The LTTng UST tracer only supports  contextsprocname,pthread_id,vpidvtid. Adding any other contexts in the UST domina will fail.