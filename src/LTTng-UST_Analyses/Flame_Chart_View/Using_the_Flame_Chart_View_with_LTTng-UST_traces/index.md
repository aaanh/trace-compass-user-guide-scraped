### Using the Flame Chart View with LTTng-UST traces

There is support in the LTTng-UST integration plugin to display the callstack
			of applications traced with theliblttng-ust-cyg-profile.solibrary (see
			theliblttng-ust-cyg-profileman page for additional information). To do
			so, you need to:
- Recompile your application with "-g -finstrument-functions".
- Set up a tracing session with the thevpid,vtidandprocnamecontexts. See theEnabling UST Events On Session LevelandAdding Contexts to Channels and Events of a Domainsections. Or if using the command-line:lttng enable-event -u -alttng add-context -u -t vpid -t vtid -t procname
- lttng enable-event -u -a
- lttng add-context -u -t vpid -t vtid -t procname
- Preload theliblttng-ust-cyg-profilelibrary when running your program:LD_PRELOAD=/usr/lib/liblttng-ust-cyg-profile.so ./myprogram
- LD_PRELOAD=/usr/lib/liblttng-ust-cyg-profile.so ./myprogram
- Recompile your application with "-g -finstrument-functions".
- Set up a tracing session with the thevpid,vtidandprocnamecontexts. See theEnabling UST Events On Session LevelandAdding Contexts to Channels and Events of a Domainsections. Or if using the command-line:lttng enable-event -u -alttng add-context -u -t vpid -t vtid -t procname
- lttng enable-event -u -a
- lttng add-context -u -t vpid -t vtid -t procname
- lttng enable-event -u -a
- lttng add-context -u -t vpid -t vtid -t procname
- lttng enable-event -u -a
- lttng add-context -u -t vpid -t vtid -t procname
- Preload theliblttng-ust-cyg-profilelibrary when running your program:LD_PRELOAD=/usr/lib/liblttng-ust-cyg-profile.so ./myprogram
- LD_PRELOAD=/usr/lib/liblttng-ust-cyg-profile.so ./myprogram
- LD_PRELOAD=/usr/lib/liblttng-ust-cyg-profile.so ./myprogram
- LD_PRELOAD=/usr/lib/liblttng-ust-cyg-profile.so ./myprogram

Once you load the resulting trace, the Flame Chart View should be populated with
			the relevant information.

Note that for non-trivial applications,liblttng-ust-cyg-profilegenerates alotof events! You may need to increase the channel's subbuffer size to
			avoid lost events. Refer to theLTTng documentation.

For traces taken with LTTng-UST 2.8 or later, the Flame Chart View should show the
			function names automatically, since it will make use of the debug information
			statedump events (which are enabled when usingenable-event -u -a).

For traces taken with prior versions of UST, you would need to set the path to
			the binary file or mapping manually: