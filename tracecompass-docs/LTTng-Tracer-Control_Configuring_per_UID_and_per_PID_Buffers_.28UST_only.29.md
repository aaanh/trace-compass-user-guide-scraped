### Configuring per UID and per PID Buffers (UST only)

Since LTTng Tools v2.2.0 it is possible to configure the type of buffers forUSTapplication. It is now possible to choose between perUIDbuffers (per user ID) and perPIDbuffers (per process ID) using the dialog box for enabling channels.


- Per PID buffers: To activate the per PID buffers option for UST channels
- Per UID buffers: To activate the per UID buffers option for UST channels
- Per PID buffers: To activate the per PID buffers option for UST channels
- Per UID buffers: To activate the per UID buffers option for UST channels

If no buffer type is selected then the default value of the tracer will be configured.

Note thatGlobal shared buffersis only for kernel channel and is pre-selected whenKernelis selected in the dalog box.