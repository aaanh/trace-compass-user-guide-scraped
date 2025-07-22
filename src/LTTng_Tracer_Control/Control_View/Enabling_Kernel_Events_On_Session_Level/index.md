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