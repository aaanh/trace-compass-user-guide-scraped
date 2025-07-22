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