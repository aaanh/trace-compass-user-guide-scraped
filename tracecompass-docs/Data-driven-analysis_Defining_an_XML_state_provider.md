## Defining an XML state provider

The state system is a component of TMF which can track the states of different elements of the system over the duration of a trace. To build this state system, events have to go chronologically through a state provider, which defines what changes are caused by the event to the system.

The state system obtained by the state provider can then be used to populate data-driven views without having to re-read the trace, or to query specific timestamps in the trace without needing to access the trace file.

### Definitions and example

Before we start, we'll define a few terms used in the following sections. The interested reader should read theTmf Developer Guidefor more complete description of the state system and state providers.
- Thestate systemcan be viewed as a model of the system, where the different elements (attributes) can be seen as a tree, and their evolution (states) is tracked through time.
- Thestate systemcan be viewed as a model of the system, where the different elements (attributes) can be seen as a tree, and their evolution (states) is tracked through time.
- Attribute: An attribute is the smallest element of the model that can be in any particular state. Since many attributes may have the same name, each attribute is represented by its full path in the attribute tree.
- Attribute: An attribute is the smallest element of the model that can be in any particular state. Since many attributes may have the same name, each attribute is represented by its full path in the attribute tree.
- State: A state is a value assigned to an attribute at a given time. Each model has its own state values.
- State: A state is a value assigned to an attribute at a given time. Each model has its own state values.
- Attribute tree: Elements in the model can be placed in a tree-like structure, for logical grouping. Each element in the tree can have both children and a state. Also, the tree is just a logical structure, all elements may be top-level elements.
- Attribute tree: Elements in the model can be placed in a tree-like structure, for logical grouping. Each element in the tree can have both children and a state. Also, the tree is just a logical structure, all elements may be top-level elements.
- State history: Whereas the attribute tree may be seen as the first dimension of the state system, the state history is the second dimension, over time. It tracks the intervals at which an attribute was in a given state.
- State history: Whereas the attribute tree may be seen as the first dimension of the state system, the state history is the second dimension, over time. It tracks the intervals at which an attribute was in a given state.

In the following sections, we'll use an example trace with the following events:
- start(number): A new task with ID 'number' just started.
- execute(number, fct_name): The task with ID 'number' is executing a critical section named 'fct_name'.
- wait(number): The task with ID 'number' cannot execute a critical section and needs to wait for it.
- exec_end(fct_name): A task finished executing the critical section named 'fct_name'.
- stop(number): The task with ID 'number' has just finished.
- start(number): A new task with ID 'number' just started.
- execute(number, fct_name): The task with ID 'number' is executing a critical section named 'fct_name'.
- wait(number): The task with ID 'number' cannot execute a critical section and needs to wait for it.
- exec_end(fct_name): A task finished executing the critical section named 'fct_name'.
- stop(number): The task with ID 'number' has just finished.

### Determining the state system structure

The first thing to do is to determine the attribute tree we'll use to represent the model of the system. The attribute tree is like a file system with directories and files, where files are logically gathered in the same parent directory. There is no one good way to build a tree, the logic will depend on the situation and on the person defining it.

The generated state system may be used later on to populate views, so attributes of the tree could be grouped in such a way as to make it easy to reach them with a simple path. The view will then be more simple.

In our example case, we'll want to track the status of each task and, for each critical section, which task is running them.

Then we determine how each event will affect the state of the attributes. But first, let's ask ourselves what values should each state take.

Let's see with the tree:

Then we determine how each event will affect the state of the attributes. In the attribute paths below, elements in {} are values coming from the trace event, while strings are constants. For the sake of simplicity, we'll say "update attribute", but if an attribute does not exist, it will be created.
- start(number): Update state value of attribute "Tasks/{number}" to "RUNNING".
- execute(number, fct_name): Update state value of attribute "Tasks/{number}" to "CRITICAL" and Update attribute "Critical section/{fct_name}" to "{number}".
- wait(number): Update state value of attribute "Tasks/{number}" to "WAITING".
- exec_end(fct_name): Update state value of attribute "Tasks/{valueOf Critical section/{fct_name}}" to RUNNING and update "Critical section/{fct_name}" to null.
- stop(number): Update state value of attribute "Tasks/{number}" to null.
- start(number): Update state value of attribute "Tasks/{number}" to "RUNNING".
- execute(number, fct_name): Update state value of attribute "Tasks/{number}" to "CRITICAL" and Update attribute "Critical section/{fct_name}" to "{number}".
- wait(number): Update state value of attribute "Tasks/{number}" to "WAITING".
- exec_end(fct_name): Update state value of attribute "Tasks/{valueOf Critical section/{fct_name}}" to RUNNING and update "Critical section/{fct_name}" to null.
- stop(number): Update state value of attribute "Tasks/{number}" to null.

### Writing the XML state provider

Once the model is done at a high level, it is time to translate it to an XML data-driven analysis. For details on how to use each XML element, refer to the documentation available in the XSD files. Some elements will be commented on below.

First define the state provider element.

The "version" attribute indicates which version of the state system is defined here. Once a state provider has been defined for a trace type, it will typically be used by a team of people and it may be modified over time. This version number should be bumped each time a new version of the state provider is published. This will force a rebuild of any existing state histories (if applicable) whose version number is different from the current one.

The "id" attribute uniquely identifies this state provider, and the analysis that will contain it.

Optional header information can be added to the state provider. A "traceType" should be defined to tell TMF which trace type this analysis will apply to. If no tracetype is specified, the analysis will appear under every trace. A "label" can optionally be added to have a more user-friendly name for the analysis.

If predefined values will be used in the state provider, they must be defined before the state providers. They can then be referred to in the state changes by name, preceded by the '$' sign. It is not necessary to use predefined values, the state change can use values like (100, 101, 102) directly.

The following event handler shows what to do with the event namedstart. It causes one state change. The sequence ofstateAttributeelements represents the path to the attribute in the attribute tree, each element being one level of the tree. ThestateValueindicates which value to assign to the attribute at the given path. The "$RUNNING" value means it will use the predefined value named RUNNING above.

Suppose the actual event isstart(3). The result of this state change is that at the time of the event, the state system attribute "Tasks/3" will have value 100.

The full XML file for the example above would look like this:

### Debugging the XML state provider

To debug the state system that was generated by the XML state provider, one could use theState System Explorer View, along with the events editor. By selecting an event, you can see what changes this event caused and the states of other attributes at the time.

If there are corrections to make, you may modify the XML state provider file, and re-import it. To re-run the analysis, you must first delete the supplementary files by right-clicking on your trace, and selectingDelete supplementary files.... Check your analysis' .ht file, so that the analysis will be run again when the trace is reopened. The supplementary file deletion will have closed the trace, so it needs to be opened again to use the newly imported analysis file.

If modifications are made to the XML state provider after it has been "published", theversionattribute of thexmlStateProviderelement should be updated. This avoids having to delete each trace's supplementary file manually. If the saved state system used a previous version, it will automatically be rebuilt from the XML file.