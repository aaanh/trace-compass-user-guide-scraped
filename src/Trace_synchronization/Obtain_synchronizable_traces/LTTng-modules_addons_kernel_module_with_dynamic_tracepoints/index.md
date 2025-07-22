### LTTng-modules addons kernel module with dynamic tracepoints

This method adds dynamic instrumentation on TCP packets via extra kernel modules. Only TCP packets are captured.

Obtain the source code, along with lttng-modules

Checkout the addons branch, compile and install lttng-modules as per the lttng-modules documentation. Themakecommand will fail at first with a message about the unset SYSMAP variable. Instructions on how to generate a System.map are mentioned in the error message.

The lttng-addons modules must be inserted manually for the TCP tracepoints to be made available.

The following tracepoints will be available

The ones used for trace synchronization areinet_sock_local_inandinet_sock_local_out.