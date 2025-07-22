# Installation

This section describes the installation of the LTTng tracer and the Trace Compass plug-ins as well as their dependencies.

## LTTng Tracer

While the Eclipse plug-ins can run on the standard Eclipse platforms (Linux, Mac, Windows), the LTTng tracer and its accompanying tools run on Linux.

The tracer and tools have been available for download in Ubuntu since 12.04. They can easily be installed with the following command:

For other distributions, older Ubuntu distributions, or the latest, bleeding edge LTTng tracer, please refer to theLTTng websitefor installation information.

Note: The LTTng tracer (and accompanying tools) is required only if you want to create your own traces (the usual case). If you intend to simply analyze existing traces then it is not necessary to install the tracer.

## Trace Compass Plug-ins

The easiest way to install the Trace Compass plug-ins for Eclipse is through the Install New Software menu. For information on how to use this menu, refer to thislink.

The Trace Compass main plug-ins are structured as a stack of features/plug-ins as following:
- CTF- A CTF parser that can also be used as a standalone componentFeature: org.eclipse.tracecompass.ctfPlug-ins: org.eclipse.tracecompass.ctf.core, org.eclipse.tracecompass.ctf.parser
- Feature: org.eclipse.tracecompass.ctf
- Plug-ins: org.eclipse.tracecompass.ctf.core, org.eclipse.tracecompass.ctf.parser
- CTF- A CTF parser that can also be used as a standalone componentFeature: org.eclipse.tracecompass.ctfPlug-ins: org.eclipse.tracecompass.ctf.core, org.eclipse.tracecompass.ctf.parser
- Feature: org.eclipse.tracecompass.ctf
- Plug-ins: org.eclipse.tracecompass.ctf.core, org.eclipse.tracecompass.ctf.parser
- Feature: org.eclipse.tracecompass.ctf
- Plug-ins: org.eclipse.tracecompass.ctf.core, org.eclipse.tracecompass.ctf.parser
- Feature: org.eclipse.tracecompass.ctf
- Plug-ins: org.eclipse.tracecompass.ctf.core, org.eclipse.tracecompass.ctf.parser
- State System Core- State system for TMFPlug-ins: org.eclipse.tracecompass.statesystem.core
- Plug-ins: org.eclipse.tracecompass.statesystem.core
- State System Core- State system for TMFPlug-ins: org.eclipse.tracecompass.statesystem.core
- Plug-ins: org.eclipse.tracecompass.statesystem.core
- Plug-ins: org.eclipse.tracecompass.statesystem.core
- Plug-ins: org.eclipse.tracecompass.statesystem.core
- TMF-Tracing and Monitoring Frameworka framework for generic trace processingFeature: org.eclipse.tracecompass.tmfPlug-ins: org.eclipse.tracecompass.tmf.core, org.eclipse.tracecompass.tmf.ui. org.eclipse.tracecompass.tmf.analysis.xml.core, org.eclipse.tracecompass.tmf.analysis.xml.ui
- Feature: org.eclipse.tracecompass.tmf
- Plug-ins: org.eclipse.tracecompass.tmf.core, org.eclipse.tracecompass.tmf.ui. org.eclipse.tracecompass.tmf.analysis.xml.core, org.eclipse.tracecompass.tmf.analysis.xml.ui
- TMF-Tracing and Monitoring Frameworka framework for generic trace processingFeature: org.eclipse.tracecompass.tmfPlug-ins: org.eclipse.tracecompass.tmf.core, org.eclipse.tracecompass.tmf.ui. org.eclipse.tracecompass.tmf.analysis.xml.core, org.eclipse.tracecompass.tmf.analysis.xml.ui
- Feature: org.eclipse.tracecompass.tmf
- Plug-ins: org.eclipse.tracecompass.tmf.core, org.eclipse.tracecompass.tmf.ui. org.eclipse.tracecompass.tmf.analysis.xml.core, org.eclipse.tracecompass.tmf.analysis.xml.ui
- Feature: org.eclipse.tracecompass.tmf
- Plug-ins: org.eclipse.tracecompass.tmf.core, org.eclipse.tracecompass.tmf.ui. org.eclipse.tracecompass.tmf.analysis.xml.core, org.eclipse.tracecompass.tmf.analysis.xml.ui
- Feature: org.eclipse.tracecompass.tmf
- Plug-ins: org.eclipse.tracecompass.tmf.core, org.eclipse.tracecompass.tmf.ui. org.eclipse.tracecompass.tmf.analysis.xml.core, org.eclipse.tracecompass.tmf.analysis.xml.ui
- CTF support for TMF- CTF support for the TMF FeatureFeature: org.eclipse.tracecompass.tmf.ctfPlug-ins: org.eclipse.tracecompass.tmf.ctf.core
- Feature: org.eclipse.tracecompass.tmf.ctf
- Plug-ins: org.eclipse.tracecompass.tmf.ctf.core
- CTF support for TMF- CTF support for the TMF FeatureFeature: org.eclipse.tracecompass.tmf.ctfPlug-ins: org.eclipse.tracecompass.tmf.ctf.core
- Feature: org.eclipse.tracecompass.tmf.ctf
- Plug-ins: org.eclipse.tracecompass.tmf.ctf.core
- Feature: org.eclipse.tracecompass.tmf.ctf
- Plug-ins: org.eclipse.tracecompass.tmf.ctf.core
- Feature: org.eclipse.tracecompass.tmf.ctf
- Plug-ins: org.eclipse.tracecompass.tmf.ctf.core
- LTTng Control- The wrapper for the LTTng tracer control. Can be used for kernel or application tracing.Feature: org.eclipse.tracecompass.lttng2.controlPlug-ins: org.eclipse.tracecompass.lttng2.control.core, org.eclipse.tracecompass.lttng2.control.ui
- Feature: org.eclipse.tracecompass.lttng2.control
- Plug-ins: org.eclipse.tracecompass.lttng2.control.core, org.eclipse.tracecompass.lttng2.control.ui
- LTTng Control- The wrapper for the LTTng tracer control. Can be used for kernel or application tracing.Feature: org.eclipse.tracecompass.lttng2.controlPlug-ins: org.eclipse.tracecompass.lttng2.control.core, org.eclipse.tracecompass.lttng2.control.ui
- Feature: org.eclipse.tracecompass.lttng2.control
- Plug-ins: org.eclipse.tracecompass.lttng2.control.core, org.eclipse.tracecompass.lttng2.control.ui
- Feature: org.eclipse.tracecompass.lttng2.control
- Plug-ins: org.eclipse.tracecompass.lttng2.control.core, org.eclipse.tracecompass.lttng2.control.ui
- Feature: org.eclipse.tracecompass.lttng2.control
- Plug-ins: org.eclipse.tracecompass.lttng2.control.core, org.eclipse.tracecompass.lttng2.control.ui
- LTTng Kernel- Analysis components specific to Linux kernel tracesFeature: org.eclipse.tracecompass.lttng2.kernelPlug-ins: org.eclipse.tracecompass.analysis.os.linux.core, org.eclipse.tracecompass.analysis.os.linux.ui, org.eclipse.tracecompass.lttng2.kernel.core, org.eclipse.tracecompass.lttng2.kernel.ui
- Feature: org.eclipse.tracecompass.lttng2.kernel
- Plug-ins: org.eclipse.tracecompass.analysis.os.linux.core, org.eclipse.tracecompass.analysis.os.linux.ui, org.eclipse.tracecompass.lttng2.kernel.core, org.eclipse.tracecompass.lttng2.kernel.ui
- LTTng Kernel- Analysis components specific to Linux kernel tracesFeature: org.eclipse.tracecompass.lttng2.kernelPlug-ins: org.eclipse.tracecompass.analysis.os.linux.core, org.eclipse.tracecompass.analysis.os.linux.ui, org.eclipse.tracecompass.lttng2.kernel.core, org.eclipse.tracecompass.lttng2.kernel.ui
- Feature: org.eclipse.tracecompass.lttng2.kernel
- Plug-ins: org.eclipse.tracecompass.analysis.os.linux.core, org.eclipse.tracecompass.analysis.os.linux.ui, org.eclipse.tracecompass.lttng2.kernel.core, org.eclipse.tracecompass.lttng2.kernel.ui
- Feature: org.eclipse.tracecompass.lttng2.kernel
- Plug-ins: org.eclipse.tracecompass.analysis.os.linux.core, org.eclipse.tracecompass.analysis.os.linux.ui, org.eclipse.tracecompass.lttng2.kernel.core, org.eclipse.tracecompass.lttng2.kernel.ui
- Feature: org.eclipse.tracecompass.lttng2.kernel
- Plug-ins: org.eclipse.tracecompass.analysis.os.linux.core, org.eclipse.tracecompass.analysis.os.linux.ui, org.eclipse.tracecompass.lttng2.kernel.core, org.eclipse.tracecompass.lttng2.kernel.ui
- LTTng UST- Analysis components specific to Linux userspace tracesFeature: org.eclipse.tracecompass.lttng2.ustPlug-ins: org.eclipse.tracecompass.lttng2.ust.core, org.eclipse.tracecompass.lttng2.ust.ui
- Feature: org.eclipse.tracecompass.lttng2.ust
- Plug-ins: org.eclipse.tracecompass.lttng2.ust.core, org.eclipse.tracecompass.lttng2.ust.ui
- LTTng UST- Analysis components specific to Linux userspace tracesFeature: org.eclipse.tracecompass.lttng2.ustPlug-ins: org.eclipse.tracecompass.lttng2.ust.core, org.eclipse.tracecompass.lttng2.ust.ui
- Feature: org.eclipse.tracecompass.lttng2.ust
- Plug-ins: org.eclipse.tracecompass.lttng2.ust.core, org.eclipse.tracecompass.lttng2.ust.ui
- Feature: org.eclipse.tracecompass.lttng2.ust
- Plug-ins: org.eclipse.tracecompass.lttng2.ust.core, org.eclipse.tracecompass.lttng2.ust.ui
- Feature: org.eclipse.tracecompass.lttng2.ust
- Plug-ins: org.eclipse.tracecompass.lttng2.ust.core, org.eclipse.tracecompass.lttng2.ust.ui

## LTTng Control Dependencies

The Eclipse LTTng Control feature controls the LTTng tracer through ansshconnection, if the tracer is running locally it can use or bypass thesshconnection.

When usingssh, the target system (where the tracer runs) needs to run ansshserver as well assftpserver (for file transfer) to which you have permission to connect.

On the host side (where Eclipse is running), you also need to have Eclipse Remote Services installed to handle the SSH connection and transport. The Remote Services are installed for you as a dependency of the LTTng Control feature. If necessary, it can be installed manually with the standard way (Help>Install New Software...>General Purpose Tools>Remote Services).

## Installation Verification

If you do not have any traces, sample LTTng traces can be found herehttp://lttng.org/files/samples. This page contains links to some sample LTTng 2.0 kernel traces. The trace needs to be uncompressed to be opened. The traces can also be imported directly as archive, see theImportingsection for more detail.

Here are the quick steps to verify that your installation is functional using a LTTng trace:
- Start Eclipse
- Open the LTTng Kernel perspective
- Create a Tracing projectRight-click in the Project Explorer view and select New, Tracing ProjectEnter the name of your project (e.g. "MyLTTngProject")The project will be created. It will contain 2 empty folders: "Traces" and "Experiments"
- Right-click in the Project Explorer view and select New, Tracing Project
- Enter the name of your project (e.g. "MyLTTngProject")
- The project will be created. It will contain 2 empty folders: "Traces" and "Experiments"
- Open and visualize a sample traceRight-click on the newly created project "Traces" folder and select "Open Trace..."Navigate to the sample LTTng trace that you want to visualize and select any file in the trace folderThe newly imported trace should appear under the Traces folderThe trace should load and the views be populated
- Right-click on the newly created project "Traces" folder and select "Open Trace..."
- Navigate to the sample LTTng trace that you want to visualize and select any file in the trace folder
- The newly imported trace should appear under the Traces folder
- The trace should load and the views be populated
- Start Eclipse
- Open the LTTng Kernel perspective
- Create a Tracing projectRight-click in the Project Explorer view and select New, Tracing ProjectEnter the name of your project (e.g. "MyLTTngProject")The project will be created. It will contain 2 empty folders: "Traces" and "Experiments"
- Right-click in the Project Explorer view and select New, Tracing Project
- Enter the name of your project (e.g. "MyLTTngProject")
- The project will be created. It will contain 2 empty folders: "Traces" and "Experiments"
- Right-click in the Project Explorer view and select New, Tracing Project
- Enter the name of your project (e.g. "MyLTTngProject")
- The project will be created. It will contain 2 empty folders: "Traces" and "Experiments"
- Right-click in the Project Explorer view and select New, Tracing Project
- Enter the name of your project (e.g. "MyLTTngProject")
- The project will be created. It will contain 2 empty folders: "Traces" and "Experiments"
- Open and visualize a sample traceRight-click on the newly created project "Traces" folder and select "Open Trace..."Navigate to the sample LTTng trace that you want to visualize and select any file in the trace folderThe newly imported trace should appear under the Traces folderThe trace should load and the views be populated
- Right-click on the newly created project "Traces" folder and select "Open Trace..."
- Navigate to the sample LTTng trace that you want to visualize and select any file in the trace folder
- The newly imported trace should appear under the Traces folder
- The trace should load and the views be populated
- Right-click on the newly created project "Traces" folder and select "Open Trace..."
- Navigate to the sample LTTng trace that you want to visualize and select any file in the trace folder
- The newly imported trace should appear under the Traces folder
- The trace should load and the views be populated
- Right-click on the newly created project "Traces" folder and select "Open Trace..."
- Navigate to the sample LTTng trace that you want to visualize and select any file in the trace folder
- The newly imported trace should appear under the Traces folder
- The trace should load and the views be populated

If an error message is displayed, you might want to double-check that the trace type is correctly set (right-click on the trace and "Select Trace Type...").

Refer toTracing Perspectivefor detailed description of the views and their usage.