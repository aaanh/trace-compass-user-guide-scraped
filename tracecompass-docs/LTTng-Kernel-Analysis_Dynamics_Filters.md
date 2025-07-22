#### Dynamics Filters

Dynamic filters are filters that are processed and applied each time the control flow view visible time range changes.

The dynamics filters can be rapidly toggled in their view sub menu.



The dynamics filters  can be fine tuned in the configuration dialog.



Note: Dynamic filters can induce performance degradation.

##### Show Active Threads Only

The Show Active Threads Only filter allow a user to increase the signal to noise ratio by filtering out allinactivethreads.

A thread is considered inactive when it is in the following state:
- non-existing
- unknown
- wait and blocked
- wait and unknown
- non-existing
- unknown
- wait and blocked
- wait and unknown

A user can fine tune this filter by providing ranges of CPUs allowing the filter to only show active thread running on the specified CPUs.