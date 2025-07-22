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