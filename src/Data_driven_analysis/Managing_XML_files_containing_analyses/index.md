## Managing XML files containing analyses

TheManage XML Analysespreference page is used to manage the list of XML files containing analyses. To open the preference page, selectWindow > Preferencesfrom the main menu bar, then click onXML Analysesunder theTracingsection. The preference page can also be opened using the Project Explorer as described here:
- Open theProject Explorerview.
- SelectManage XML Analyses...from theTracesfolder context menu.
- Open theProject Explorerview.
- SelectManage XML Analyses...from theTracesfolder context menu.



The list of currently imported XML files is displayed on the left side of the dialog.

The following actions can be performed from this dialog:
- Import
- Import

Click theImportbutton and select a file from the opened file dialog to import an XML file containing an analysis. The file will be validated before importing it and if successful, the new file will be enabled and its analyses and views will be shown under the traces for which they apply.
- Enable/disable
- Enable/disable

To enable a file and its analyses, check the box to the left of the file, then pressApplyorApply and closeto save the changes. Unchecking a box and saving the changes will disable the corresponding file. When selecting an enabled file, a confirmation message will be displayed to the user. Note that invalid files cannot be enabled; if one is selected, an error message will be displayed to the user.
- Export
- Export

Select an XML file from the list, click theExportbutton and enter or select a file in the opened file dialog to export the XML analysis. Note that if an existing file containing an analysis is selected, its content will be replaced with the analysis to export.
- Edit
- Edit

Select an XML file from the list, click theEditto open the XML editor. When the file is saved after being modified, it is validated and traces that are affected by this file are closed.
- Delete
- Delete

Select one or more XML files from the list and click theDeletebutton to remove them. Deleting an XML file will close all the traces for which the analyses apply and remove the analyses.