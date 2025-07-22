## Filters View



The Filters view allows the user to define preset filters that can be applied to any events table.

The filters can be more complex than what can be achieved with the filter header row in the events table. The filter is defined in a tree node structure, where the node types can be any ofTRACETYPE,AND,OR,CONTAINS,EQUALS,MATCHESorCOMPARE. Some nodes types have restrictions on their possible children in the tree.

TheTRACETYPEnode filters against the trace type of the trace as defined in a plug-in extension or in a custom parser. When used, any child node will have itstypecombo box fixed and itsaspectcombo box restricted to the possible aspects of that trace type. Depending of the Trace Types enabled in theTrace Types preference page, the list of available trace types for the filtering can vary.

TheANDnode applies the logicalandcondition on all of its children. All children conditions must be true for the filter to match. Anotoperator can be applied to invert the condition.

TheORnode applies the logicalorcondition on all of its children. At least one children condition must be true for the filter to match. Anotoperator can be applied to invert the condition.

TheCONTAINSnode matches when the specified eventaspectvalue contains the specifiedvaluestring. Anotoperator can be applied to invert the condition. The condition can be case sensitive or insensitive. Thetypecombo box restricts the possible aspects to those of the specified trace type.

TheEQUALSnode matches when the specified eventaspectvalue equals exactly the specifiedvaluestring. Anotoperator can be applied to invert the condition. The condition can be case sensitive or insensitive. Thetypecombo box restricts the possible aspects to those of the specified trace type.

TheMATCHESnode matches when the specified eventaspectvalue matches against the specifiedregular expression. Anotoperator can be applied to invert the condition. Thetypecombo box restricts the possible aspects to those of the specified trace type.

TheCOMPAREnode matches when the specified eventaspectvalue compared with the specifiedvaluegives the specifiedresult. The result can be set tosmaller than,equalorgreater than. The type of comparison can be numerical, alphanumerical or based on time stamp. Anotoperator can be applied to invert the condition. Thetypecombo box restricts the possible aspects to those of the specified trace type.

For numerical comparisons, strings prefixed by "0x", "0X" or "#" are treated as hexadecimal numbers and strings prefixed by "0" are treated as octal numbers.

For time stamp comparisons, strings are treated as seconds with or without fraction of seconds. This corresponds to theTTTformat in theTime Formatpreferences. The value for a selected event can be found in thePropertiesview under theTimestampproperty. The common 'Timestamp' aspect can always be used for time stamp comparisons regardless of its time format.

Filters can be added, deleted, imported and exported using the buttons in the Filters view toolbar. The nodes in the view can be Cut (Ctrl-X), Copied (Ctrl-C) and Pasted (Ctrl-V) by using the buttons in the toolbar or by using the key bindings. This makes it easier to quickly build new filters from existing ones. Changes to the preset filters are only applied and persisted to disk when theSave filtersbutton is pressed.

To apply a saved preset filter in an events table, right-click on the table and selectApply preset filter...>filter name.