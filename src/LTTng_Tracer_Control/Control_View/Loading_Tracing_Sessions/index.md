### Loading Tracing Sessions

Since LTTng Tools v2.5.0 it is possible to load tracing sessions. The Trace CompassControlview integrations for this feature will allow to load session profiles that are located in the user's Trace Compass workspace, or alternatively, that are located on the remote node. In the first case the session profiles will be uploaded to the remote node before the load command is executed.

To load one or more sessions, select the tree nodeSessionsand press the right mouse button. Then select theLoad...entry of the context-sensitive menu.



A new display will open for loading session profiles.



By default theLocalbutton andforcebuttons are selected and session profile files of the user's workspace will be listed. Select one or more profiles, update theforcebutton if needed and then clickOk. This will upload the session profile files to the remote node. If a session profile file with the same name already exist on the remote node, it will be overwritten. If theforcebutton is selected any existing session with a conflicting name will be destroyed and a new one will be created.

Alternatively, one can select theRemotebutton to list all available session profile files on the remote node. To load one of the remote session profiles, select one or more profiles, update theforcebutton if needed and then clickOk.



Upon successful operation, the tracing sessions of the selected session profiles are created and added under the tree nodeSessionstheControlview.