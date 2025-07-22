## OS Tracing Overview Perspective

TheOS Tracing Overviewperspective groups the following views:
- Project Explorer View
- Events Editor
- Histogram View
- CPU Usage View
- Disk I/O Activity View
- Kernel Memory Usage View
- Project Explorer View
- Events Editor
- Histogram View
- CPU Usage View
- Disk I/O Activity View
- Kernel Memory Usage View

The perspective can be opened from the Eclipse Open Perspective dialog (Window > Open Perspective... > Other).



This perspective is intended to be used to locate performance issues by observing resource usage.

The perspective can show times resource usage is anomalous. This can help locating the causes of system slowdowns in throughput or response time.

An example can be program that is doing a lot of processing then slows down due to a database access. The user will see a dip in CPU usage and maybe a slight rise in I/O access. The user should consider both spike and slums to be an indication of an area worth investigating.



Once a performance issue has been localized, it can be further investigated with the #LTTng kernel Perspective.