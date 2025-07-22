### Event Source Lookup

Some trace types can optionally embed information in the trace to indicate the source of a trace event. This is accessed through the event context menu by right-clicking on an event in the table.

#### Source Code

If a source file is available in the trace for the selected event, the itemOpen Source Codeis shown in the context menu. Selecting this menu item will attempt to find the source file in all opened projects in the workspace. If multiple candidates exist, a selection dialog will be shown to the user. The selected source file will be opened, at the correct line, in its default language editor. If no candidate is found, an error dialog is shown displaying the source code information.

#### EMF Model

If an EMF model URI is available in the trace for the selected event, the itemOpen Model Elementis shown in the context menu. Selecting this menu item will attempt to open the model file in the project specified in the URI. The model file will be opened in its default model editor. If the model file is not found, an error dialog is shown displaying the URI information.