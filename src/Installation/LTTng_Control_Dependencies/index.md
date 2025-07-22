## LTTng Control Dependencies

The Eclipse LTTng Control feature controls the LTTng tracer through ansshconnection, if the tracer is running locally it can use or bypass thesshconnection.

When usingssh, the target system (where the tracer runs) needs to run ansshserver as well assftpserver (for file transfer) to which you have permission to connect.

On the host side (where Eclipse is running), you also need to have Eclipse Remote Services installed to handle the SSH connection and transport. The Remote Services are installed for you as a dependency of the LTTng Control feature. If necessary, it can be installed manually with the standard way (Help>Install New Software...>General Purpose Tools>Remote Services).