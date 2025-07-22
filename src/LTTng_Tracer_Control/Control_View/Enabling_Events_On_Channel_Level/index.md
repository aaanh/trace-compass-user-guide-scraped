### Enabling Events On Channel Level

Kernel events can also be enabled on the channel level. If necessary, create a channel as described in sectionsEnabling Channels On Session LevelorEnabling Channels On Domain Level.

Then select the relevant channel tree node, click the right mouse button and the selectEnable Event.... A new dialog box will open for providing information about the events to be enabled. Depending on the domain,KernelorUST global, the domain specific fields are shown and the domain selector is preselected and read-only. Since there is no channel under theJUL,LOG4JorPythondomain you cannot enable those loggers directly from a channel.



To enable events for domainKernelfollow the instructions in sectionEnabling Kernel Events On Session Level, for domainUST globalEnabling UST Events On Session Level.

When enabling events on the channel level, the events will be add to the selected channel.