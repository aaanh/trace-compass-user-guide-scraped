## Slow I/O

Alice is running her server. She noticed that one of her nodes was slowing down, and wasn't sure why, upon reading the trace she noticed that her time between a block request and complete was around 10ms.

This is abnormal, normally her server handles IOs in under 100us, since they are quite local.

She walks up to the server and hears the hard drive thrashing, This prompts her to look up in the events view the sectors being read in the block complete requests. There are her requests interleaved with other ones at the opposite side of the hard drive.

She sees the tracer writing but there is another process that is writing to the server disk non stop. She looks in the control flow view and sees that there's a program from another fellow engineer, "Wally" that is writing in his home in a loop "All work and no play makes Jack a dull boy.".

Alice kills the program, and immediately the server speeds up. She then goes to discuss this with Wally and implements strict hard disk quotas on the server.