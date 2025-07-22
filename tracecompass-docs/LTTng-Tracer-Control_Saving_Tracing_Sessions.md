### Saving Tracing Sessions

Since LTTng Tools v2.5.0 it is possible to save tracing sessions. The LTTng Tools command-line tool will save the sessions to XML files located by default in a subdirectory of the user's home directory. The Trace CompassControlview integration for this feature will also store this session profile file into the user's Trace Compass workspace. This will allow user's to re-use session profiles across remote nodes. To save one or more sessions, select the tree nodes of the relevant sessions and press the right mouse button. Then select theSave...entry of the context-sensitive menu.



A new display will open for saving the sessions.



By default theforcebutton is selected that will overwrite any conflicting session profile files on the remote node. Click onOkto save the session(s) otherwise click onCancel. Upon successful operation, the session profile files will be saved on the remote node and then will be downloaded to the user's Trace Compass workspace. In the case that a session XML file already exists in the workspace the user will be prompted to skip or overwrite the existing profile file.