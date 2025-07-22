### LTTng-module network tracepoint with complete data

The tracepointsnet_dev_queueandnetif_receive_skbwill be used for synchronization. Both tracepoints are available in lttng-modules since version 2.2, but they do not contain sufficient data to be used to synchronize traces.

An experimental branch introduces this extra data: lttng-modules will need to be compiled by hand.

Obtain the source code for the experimental lttng-modules

Checkout thenet_data_experimentalbranch, compile and install lttng-modules as per the lttng-modules documentation

This experimental branch adds IP, IPv6 and TCP header data to the tracepoints. Packets received and sent with other protocols do not have this extra header data, but all packets are captured.