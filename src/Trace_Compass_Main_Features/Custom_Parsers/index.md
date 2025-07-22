## Custom Parsers

Custom parser wizards allow the user to define their own parsers for text or XML traces. The user defines how the input should be parsed into internal trace events and identifies the event fields that should be created and displayed. Traces created using a custom parser can be correlated with other built-in traces or traces added by plug-in extension.

### Creating a custom text parser

TheNew Custom Text Parserwizard can be used to create a custom parser for text logs. It can be launched several ways:
- SelectFile>New>Other...>Tracing>Custom Text Parser
- Open theManage Custom Parsersdialog, select theTextradio button and click theNew...button
- SelectFile>New>Other...>Tracing>Custom Text Parser
- Open theManage Custom Parsersdialog, select theTextradio button and click theNew...button



Fill out the first wizard page with the following information:
- Category: Enter a category name for the trace type.
- Trace type: Enter a name for the trace type, which is also the name of the custom parser. This will also be the default event type name.
- Time Stamp format: Enter the date and time pattern that will be used to output the Time Stamp, or leave blank to use the default Time Format preference.
- Category: Enter a category name for the trace type.
- Trace type: Enter a name for the trace type, which is also the name of the custom parser. This will also be the default event type name.
- Time Stamp format: Enter the date and time pattern that will be used to output the Time Stamp, or leave blank to use the default Time Format preference.

Note: information about date and time patterns can be found here:TmfTimestampFormat

Click theAdd next line,Add child lineorRemove linebuttons to create a new line of input or delete it. For each line of input, enter the following information:
- Regular expression: Enter a regular expression that should match the input line in the log, using capturing groups to extract the data.
- Regular expression: Enter a regular expression that should match the input line in the log, using capturing groups to extract the data.

Note: information about regular expression patterns can be found here:http://docs.oracle.com/javase/8/docs/api/java/util/regex/Pattern.html
- Cardinality: Enter the minimum and maximum number of lines matching this line's regular expression that must be found in the log. At least the minimum number of lines must be found before the parser will consider the next line. Child lines will always be considered first.
- Cardinality: Enter the minimum and maximum number of lines matching this line's regular expression that must be found in the log. At least the minimum number of lines must be found before the parser will consider the next line. Child lines will always be considered first.
- Event type: Optionally enable this text field to enter an event type name that will override the default (trace type) when this line matches.
- Event type: Optionally enable this text field to enter an event type name that will override the default (trace type) when this line matches.

Important note:The custom parsers identify a log entry when the first line's regular expression matches (Root Line n). Each subsequent text line in the log is attempted to be matched against the regular expression of the parser's input lines in the order that they are defined (Line n.*). Only the first matching input line will be used to process the captured data to be stored in the log entry. When a text line matches a Root Line's regular expression, a new log entry is started.

Click theAdd grouporRemove groupbuttons to define the data extracted from the capturing groups in the line's regular expression. For each group, enter the following information:
- Name combo: Select a name for the extracted data:Timestamp: Select this option to identify the timestamp data. The input's data and time pattern must be entered in the format: text box.Event type: Select this option to identify the event type name. This will override the default or line-specific event type name.Message: Select this option to identify the main log entry's message. This is usually a group which could have text of greater length.Other: Select this option to identify any non-standard data. The name must be entered in the name: text box.
- Timestamp: Select this option to identify the timestamp data. The input's data and time pattern must be entered in the format: text box.
- Event type: Select this option to identify the event type name. This will override the default or line-specific event type name.
- Message: Select this option to identify the main log entry's message. This is usually a group which could have text of greater length.
- Other: Select this option to identify any non-standard data. The name must be entered in the name: text box.
- Name combo: Select a name for the extracted data:Timestamp: Select this option to identify the timestamp data. The input's data and time pattern must be entered in the format: text box.Event type: Select this option to identify the event type name. This will override the default or line-specific event type name.Message: Select this option to identify the main log entry's message. This is usually a group which could have text of greater length.Other: Select this option to identify any non-standard data. The name must be entered in the name: text box.
- Timestamp: Select this option to identify the timestamp data. The input's data and time pattern must be entered in the format: text box.
- Event type: Select this option to identify the event type name. This will override the default or line-specific event type name.
- Message: Select this option to identify the main log entry's message. This is usually a group which could have text of greater length.
- Other: Select this option to identify any non-standard data. The name must be entered in the name: text box.
- Timestamp: Select this option to identify the timestamp data. The input's data and time pattern must be entered in the format: text box.
- Event type: Select this option to identify the event type name. This will override the default or line-specific event type name.
- Message: Select this option to identify the main log entry's message. This is usually a group which could have text of greater length.
- Other: Select this option to identify any non-standard data. The name must be entered in the name: text box.
- Timestamp: Select this option to identify the timestamp data. The input's data and time pattern must be entered in the format: text box.
- Event type: Select this option to identify the event type name. This will override the default or line-specific event type name.
- Message: Select this option to identify the main log entry's message. This is usually a group which could have text of greater length.
- Other: Select this option to identify any non-standard data. The name must be entered in the name: text box.
- Action combo: Select the action to be performed on the extracted data:Set: Select this option to overwrite the data for the chosen name when there is a match for this group.Append: Select this option to append to the data with the chosen name, if any, when there is a match for this group.Append with |: Select this option to append to the data with the chosen name, if any, when there is a match for this group, using a | separator between matches.
- Set: Select this option to overwrite the data for the chosen name when there is a match for this group.
- Append: Select this option to append to the data with the chosen name, if any, when there is a match for this group.
- Append with |: Select this option to append to the data with the chosen name, if any, when there is a match for this group, using a | separator between matches.
- Action combo: Select the action to be performed on the extracted data:Set: Select this option to overwrite the data for the chosen name when there is a match for this group.Append: Select this option to append to the data with the chosen name, if any, when there is a match for this group.Append with |: Select this option to append to the data with the chosen name, if any, when there is a match for this group, using a | separator between matches.
- Set: Select this option to overwrite the data for the chosen name when there is a match for this group.
- Append: Select this option to append to the data with the chosen name, if any, when there is a match for this group.
- Append with |: Select this option to append to the data with the chosen name, if any, when there is a match for this group, using a | separator between matches.
- Set: Select this option to overwrite the data for the chosen name when there is a match for this group.
- Append: Select this option to append to the data with the chosen name, if any, when there is a match for this group.
- Append with |: Select this option to append to the data with the chosen name, if any, when there is a match for this group, using a | separator between matches.
- Set: Select this option to overwrite the data for the chosen name when there is a match for this group.
- Append: Select this option to append to the data with the chosen name, if any, when there is a match for this group.
- Append with |: Select this option to append to the data with the chosen name, if any, when there is a match for this group, using a | separator between matches.

ThePreview inputtext box can be used to enter any log data that will be processed against the defined custom parser. When the wizard is invoked from a selected log file resource, this input will be automatically filled with the file contents.

ThePreview: text field of each capturing group and of the Time Stamp will be filled from the parsed data of the first matching log entry.

In thePreview inputtext box, the matching entries are highlighted with different colors:
- Yellow: indicates uncaptured text in a matching line.
- Green: indicates a captured group in the matching line's regular expression for which a custom parser group is defined. This data will be stored by the custom parser.
- Magenta: indicates a captured group in the matching line's regular expression for which there is no custom parser group defined. This data will be lost.
- White: indicates a non-matching line.
- Yellow: indicates uncaptured text in a matching line.
- Green: indicates a captured group in the matching line's regular expression for which a custom parser group is defined. This data will be stored by the custom parser.
- Magenta: indicates a captured group in the matching line's regular expression for which there is no custom parser group defined. This data will be lost.
- White: indicates a non-matching line.

The first line of a matching entry is highlighted with darker colors.

By default only the first matching entry will be highlighted. To highlight all matching entries in the preview input data, click theHighlight Allbutton. This might take a few seconds to process, depending on the input size.

Click theNext >button to go to the second page of the wizard.



On this page, the list of default and custom data is shown, along with a preview of the custom parser log table output.

The custom data output can be modified by the following options:
- Visibility: Select or unselect the checkbox to display the custom data or hide it.
- Visibility: Select or unselect the checkbox to display the custom data or hide it.
- Column order: ClickMove beforeorMove afterto change the display order of custom data.
- Column order: ClickMove beforeorMove afterto change the display order of custom data.

The table at the bottom of the page shows a preview of the custom parser log table output according to the selected options, using the matching entries of the previous page'sPreview inputlog data.

Click theFinishbutton to close the wizard and save the custom parser.

### Creating a custom XML parser

TheNew Custom XML Parserwizard can be used to create a custom parser for XML logs. It can be launched several ways:
- SelectFile>New>Other...>Tracing>Custom XML Parser
- Open theManage Custom Parsersdialog, select theXMLradio button and click theNew...button
- SelectFile>New>Other...>Tracing>Custom XML Parser
- Open theManage Custom Parsersdialog, select theXMLradio button and click theNew...button



Fill out the first wizard page with the following information:
- Category: Enter a category name for the trace type.
- Trace type: Enter a name for the trace type, which is also the name of the custom parser. This will also be the default event type name.
- Time Stamp format: Enter the date and time pattern that will be used to output the Time Stamp, or leave blank to use the default Time Format preference.
- Category: Enter a category name for the trace type.
- Trace type: Enter a name for the trace type, which is also the name of the custom parser. This will also be the default event type name.
- Time Stamp format: Enter the date and time pattern that will be used to output the Time Stamp, or leave blank to use the default Time Format preference.

Note: information about date and time patterns can be found here:TmfTimestampFormat

Click theAdd document elementbutton to create a new document element and enter a name for the root-level document element of the XML file.

Click theAdd childbutton to create a new element of input to the document element or any other element. For each element, enter the following information:
- Element name: Enter a name for the element that must match an element of the XML file.
- Log entry: Select this checkbox to identify an element which represents a log entry. Each element with this name in the XML file will be parsed to a new log entry. At least one log entry element must be identified in the XML document. Log entry elements cannot be nested.
- Name combo: Select a name for the extracted data:Ignore: Select this option to ignore the extracted element's data at this level. It is still possible to extract data from this element's child elements.Event type: Select this option to identify the event type name. This will override the default or element-specific event type name.Timestamp: Select this option to identify the timestamp data. The input's data and time pattern must be entered in the format: text box.Message: Select this option to identify the main log entry's message. This is usually an input which could have text of greater length.Other: Select this option to identify any non-standard data. The name must be entered in the name: text box. It does not have to match the element name.
- Ignore: Select this option to ignore the extracted element's data at this level. It is still possible to extract data from this element's child elements.
- Event type: Select this option to identify the event type name. This will override the default or element-specific event type name.
- Timestamp: Select this option to identify the timestamp data. The input's data and time pattern must be entered in the format: text box.
- Message: Select this option to identify the main log entry's message. This is usually an input which could have text of greater length.
- Other: Select this option to identify any non-standard data. The name must be entered in the name: text box. It does not have to match the element name.
- Action combo: Select the action to be performed on the extracted data:Set: Select this option to overwrite the data for the chosen name when there is a match for this element.Append: Select this option to append to the data with the chosen name, if any, when there is a match for this element.Append with |: Select this option to append to the data with the chosen name, if any, when there is a match for this element, using a | separator between matches.
- Set: Select this option to overwrite the data for the chosen name when there is a match for this element.
- Append: Select this option to append to the data with the chosen name, if any, when there is a match for this element.
- Append with |: Select this option to append to the data with the chosen name, if any, when there is a match for this element, using a | separator between matches.
- Event type: Optionally enable this text field to enter an event type name that will override the default (trace type) when this element is present.
- Element name: Enter a name for the element that must match an element of the XML file.
- Log entry: Select this checkbox to identify an element which represents a log entry. Each element with this name in the XML file will be parsed to a new log entry. At least one log entry element must be identified in the XML document. Log entry elements cannot be nested.
- Name combo: Select a name for the extracted data:Ignore: Select this option to ignore the extracted element's data at this level. It is still possible to extract data from this element's child elements.Event type: Select this option to identify the event type name. This will override the default or element-specific event type name.Timestamp: Select this option to identify the timestamp data. The input's data and time pattern must be entered in the format: text box.Message: Select this option to identify the main log entry's message. This is usually an input which could have text of greater length.Other: Select this option to identify any non-standard data. The name must be entered in the name: text box. It does not have to match the element name.
- Ignore: Select this option to ignore the extracted element's data at this level. It is still possible to extract data from this element's child elements.
- Event type: Select this option to identify the event type name. This will override the default or element-specific event type name.
- Timestamp: Select this option to identify the timestamp data. The input's data and time pattern must be entered in the format: text box.
- Message: Select this option to identify the main log entry's message. This is usually an input which could have text of greater length.
- Other: Select this option to identify any non-standard data. The name must be entered in the name: text box. It does not have to match the element name.
- Ignore: Select this option to ignore the extracted element's data at this level. It is still possible to extract data from this element's child elements.
- Event type: Select this option to identify the event type name. This will override the default or element-specific event type name.
- Timestamp: Select this option to identify the timestamp data. The input's data and time pattern must be entered in the format: text box.
- Message: Select this option to identify the main log entry's message. This is usually an input which could have text of greater length.
- Other: Select this option to identify any non-standard data. The name must be entered in the name: text box. It does not have to match the element name.
- Ignore: Select this option to ignore the extracted element's data at this level. It is still possible to extract data from this element's child elements.
- Event type: Select this option to identify the event type name. This will override the default or element-specific event type name.
- Timestamp: Select this option to identify the timestamp data. The input's data and time pattern must be entered in the format: text box.
- Message: Select this option to identify the main log entry's message. This is usually an input which could have text of greater length.
- Other: Select this option to identify any non-standard data. The name must be entered in the name: text box. It does not have to match the element name.
- Action combo: Select the action to be performed on the extracted data:Set: Select this option to overwrite the data for the chosen name when there is a match for this element.Append: Select this option to append to the data with the chosen name, if any, when there is a match for this element.Append with |: Select this option to append to the data with the chosen name, if any, when there is a match for this element, using a | separator between matches.
- Set: Select this option to overwrite the data for the chosen name when there is a match for this element.
- Append: Select this option to append to the data with the chosen name, if any, when there is a match for this element.
- Append with |: Select this option to append to the data with the chosen name, if any, when there is a match for this element, using a | separator between matches.
- Set: Select this option to overwrite the data for the chosen name when there is a match for this element.
- Append: Select this option to append to the data with the chosen name, if any, when there is a match for this element.
- Append with |: Select this option to append to the data with the chosen name, if any, when there is a match for this element, using a | separator between matches.
- Set: Select this option to overwrite the data for the chosen name when there is a match for this element.
- Append: Select this option to append to the data with the chosen name, if any, when there is a match for this element.
- Append with |: Select this option to append to the data with the chosen name, if any, when there is a match for this element, using a | separator between matches.
- Event type: Optionally enable this text field to enter an event type name that will override the default (trace type) when this element is present.

Note: An element's extracted data 'value' is a parsed string representation of all its attributes, children elements and their own values. To extract more specific information from an element, ignore its data value and extract the data from one or many of its attributes and children elements.

Click theAdd attributebutton to create a new attribute input from the document element or any other element. For each attribute, enter the following information:
- Attribute name: Enter a name for the attribute that must match an attribute of this element in the XML file.
- Name combo: Select a name for the extracted data:Timestamp: Select this option to identify the timestamp data. The input's data and time pattern must be entered in the format: text box.Event type: Select this option to identify the event type name. This will override the default or element-specific event type name.Message: Select this option to identify the main log entry's message. This is usually an input which could have text of greater length.Other: Select this option to identify any non-standard data. The name must be entered in the name: text box. It does not have to match the element name.
- Timestamp: Select this option to identify the timestamp data. The input's data and time pattern must be entered in the format: text box.
- Event type: Select this option to identify the event type name. This will override the default or element-specific event type name.
- Message: Select this option to identify the main log entry's message. This is usually an input which could have text of greater length.
- Other: Select this option to identify any non-standard data. The name must be entered in the name: text box. It does not have to match the element name.
- Action combo: Select the action to be performed on the extracted data:Set: Select this option to overwrite the data for the chosen name when there is a match for this element.Append: Select this option to append to the data with the chosen name, if any, when there is a match for this element.Append with |: Select this option to append to the data with the chosen name, if any, when there is a match for this element, using a | separator between matches.
- Set: Select this option to overwrite the data for the chosen name when there is a match for this element.
- Append: Select this option to append to the data with the chosen name, if any, when there is a match for this element.
- Append with |: Select this option to append to the data with the chosen name, if any, when there is a match for this element, using a | separator between matches.
- Attribute name: Enter a name for the attribute that must match an attribute of this element in the XML file.
- Name combo: Select a name for the extracted data:Timestamp: Select this option to identify the timestamp data. The input's data and time pattern must be entered in the format: text box.Event type: Select this option to identify the event type name. This will override the default or element-specific event type name.Message: Select this option to identify the main log entry's message. This is usually an input which could have text of greater length.Other: Select this option to identify any non-standard data. The name must be entered in the name: text box. It does not have to match the element name.
- Timestamp: Select this option to identify the timestamp data. The input's data and time pattern must be entered in the format: text box.
- Event type: Select this option to identify the event type name. This will override the default or element-specific event type name.
- Message: Select this option to identify the main log entry's message. This is usually an input which could have text of greater length.
- Other: Select this option to identify any non-standard data. The name must be entered in the name: text box. It does not have to match the element name.
- Timestamp: Select this option to identify the timestamp data. The input's data and time pattern must be entered in the format: text box.
- Event type: Select this option to identify the event type name. This will override the default or element-specific event type name.
- Message: Select this option to identify the main log entry's message. This is usually an input which could have text of greater length.
- Other: Select this option to identify any non-standard data. The name must be entered in the name: text box. It does not have to match the element name.
- Timestamp: Select this option to identify the timestamp data. The input's data and time pattern must be entered in the format: text box.
- Event type: Select this option to identify the event type name. This will override the default or element-specific event type name.
- Message: Select this option to identify the main log entry's message. This is usually an input which could have text of greater length.
- Other: Select this option to identify any non-standard data. The name must be entered in the name: text box. It does not have to match the element name.
- Action combo: Select the action to be performed on the extracted data:Set: Select this option to overwrite the data for the chosen name when there is a match for this element.Append: Select this option to append to the data with the chosen name, if any, when there is a match for this element.Append with |: Select this option to append to the data with the chosen name, if any, when there is a match for this element, using a | separator between matches.
- Set: Select this option to overwrite the data for the chosen name when there is a match for this element.
- Append: Select this option to append to the data with the chosen name, if any, when there is a match for this element.
- Append with |: Select this option to append to the data with the chosen name, if any, when there is a match for this element, using a | separator between matches.
- Set: Select this option to overwrite the data for the chosen name when there is a match for this element.
- Append: Select this option to append to the data with the chosen name, if any, when there is a match for this element.
- Append with |: Select this option to append to the data with the chosen name, if any, when there is a match for this element, using a | separator between matches.
- Set: Select this option to overwrite the data for the chosen name when there is a match for this element.
- Append: Select this option to append to the data with the chosen name, if any, when there is a match for this element.
- Append with |: Select this option to append to the data with the chosen name, if any, when there is a match for this element, using a | separator between matches.

Note: A log entry can inherited input data from its parent elements if the data is extracted at a higher level.

Click theFeeling luckybutton to automatically and recursively create child elements and attributes for the current element, according to the XML element data found in thePreview inputtext box, if any.

Click theRemove elementorRemove attributebuttons to remove the extraction of this input data. Take note that all children elements and attributes are also removed.

ThePreview inputtext box can be used to enter any XML log data that will be processed against the defined custom parser. When the wizard is invoked from a selected log file resource, this input will be automatically filled with the file contents.

ThePreview: text field of each capturing element and attribute and of the Time Stamp will be filled from the parsed data of the first matching log entry. Also, when creating a new child element or attribute, its element or attribute name will be suggested if possible from the preview input data.

Click theNext >button to go to the second page of the wizard.



On this page, the list of default and custom data is shown, along with a preview of the custom parser log table output.

The custom data output can be modified by the following options:
- Visibility: Select or unselect the checkbox to display the custom data or hide it.
- Column order: ClickMove beforeorMove beforeto change the display order of custom data.
- Visibility: Select or unselect the checkbox to display the custom data or hide it.
- Column order: ClickMove beforeorMove beforeto change the display order of custom data.

The table at the bottom of the page shows a preview of the custom parser log table output according to the selected options, using the matching entries of the previous page'sPreview inputlog data.

Click theFinishbutton to close the wizard and save the custom parser.

### Managing custom parsers

TheManage Custom Parsersdialog is used to manage the list of custom parsers used by the tool. To open the dialog:
- Open theProject Explorerview.
- SelectManage Custom Parsers...from theTracesfolder context menu, or from a trace'sSelect Trace Type...context sub-menu.
- Open theProject Explorerview.
- SelectManage Custom Parsers...from theTracesfolder context menu, or from a trace'sSelect Trace Type...context sub-menu.



The ordered list of currently defined custom parsers for the selected type is displayed on the left side of the dialog.

To change the type of custom parser to manage, select theTextorXMLradio button.

The following actions can be performed from this dialog:
- New...
- New...

Click theNew...button to launch theNew Custom Parserwizard.
- Edit...
- Edit...

Select a custom parser from the list and click theEdit...button to launch theEdit Custom Parserwizard.
- Delete
- Delete

Select a custom parser from the list and click theDeletebutton to remove the custom parser.
- Import...
- Import...

Click theImport...button and select a file from the opened file dialog to import all its custom parsers. If any parser conflicts with an existing built-in or custom trace type, the user will be prompted to skip or rename the imported parser.
- Export...
- Export...

Select a custom parser from the list, click theExport...button and enter or select a file in the opened file dialog to export the custom parser. Note that if an existing file containing custom parsers is selected, the custom parser will be appended to the file.

### Opening a trace using a custom parser

Once a custom parser has been created, anyimported tracefile can be opened and parsed using it.

To do so:
- Select a trace in theProject Explorerview
- Right-click the trace and selectSelect Trace Type...>category name>parser name
- Double-click the trace or right-click it and selectOpen
- Select a trace in theProject Explorerview
- Right-click the trace and selectSelect Trace Type...>category name>parser name
- Double-click the trace or right-click it and selectOpen

The trace will be opened in an editor showing the events table, and an entry will be added for it in the Time Chart view.