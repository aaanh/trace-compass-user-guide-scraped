### Enabling and Disabling Events

To disable one or more enabled events, select the tree nodes of the relevant events and click the right mouse button. Then selectDisable Eventmenu item in the context-sensitive menu.



Upon successful operation, the selected events will beDISABLEDand the icons for these events will be updated.

To enable one or more disabled events, select the tree nodes of the relevant events and press the right mouse button. Then select theEnable Eventmenu item of the context-sensitive menu.



Upon successful operation, the selected events will beENABLEDand the icons for these events will be updated.

Note: There is currently a limitation for kernel event of typeSYSCALL. This kernel event can not be disabled. An error will appear when trying to disable this type of event. A work-around for that is to have the syscall event in a separate channel and disable the channel instead of the event.