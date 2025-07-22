## Obtain synchronizable traces

To synchronize traces from different machines, they need to exchange packets through the network and have events enabled such that the data can be matched from one trace to the other. For now, only TCP packets can be matched between two traces.

LTTng traces that can be synchronized are obtained using one of three methods below. All methods are compatible so a trace on one host taken with one method can be synchronized with a trace on another host taken with another method:

### Use LTTng-modules 2.9+

As of LTTng-modules 2.9, thenet_dev_queueandnet_if_receive_skbtracepoints contain all the necessary data to synchronize the traces.

### LTTng-module network tracepoint with complete data

The tracepointsnet_dev_queueandnetif_receive_skbwill be used for synchronization. Both tracepoints are available in lttng-modules since version 2.2, but they do not contain sufficient data to be used to synchronize traces.

An experimental branch introduces this extra data: lttng-modules will need to be compiled by hand.

Obtain the source code for the experimental lttng-modules

Checkout thenet_data_experimentalbranch, compile and install lttng-modules as per the lttng-modules documentation

This experimental branch adds IP, IPv6 and TCP header data to the tracepoints. Packets received and sent with other protocols do not have this extra header data, but all packets are captured.

### LTTng-modules addons kernel module with dynamic tracepoints

This method adds dynamic instrumentation on TCP packets via extra kernel modules. Only TCP packets are captured.

Obtain the source code, along with lttng-modules

Checkout the addons branch, compile and install lttng-modules as per the lttng-modules documentation. Themakecommand will fail at first with a message about the unset SYSMAP variable. Instructions on how to generate a System.map are mentioned in the error message.

The lttng-addons modules must be inserted manually for the TCP tracepoints to be made available.

The following tracepoints will be available

The ones used for trace synchronization areinet_sock_local_inandinet_sock_local_out.