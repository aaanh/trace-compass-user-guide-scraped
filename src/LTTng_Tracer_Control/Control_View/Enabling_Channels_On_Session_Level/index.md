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