## Searching in Time Graph Views

Search for an entry in aTime Graph view, e.g.Control Flow VieworResources View, using theFinddialog. To use the dialog:
- Select the time graph view you want to search in
- PressCtrl + F. The following screen will be shown:
- Select the time graph view you want to search in
- PressCtrl + F. The following screen will be shown:


- Enter the string to find in theFindtext drop down and select theOptionsandDirectionyou need.
- Press theFindbutton orEnterorAlt + n. The next match in the selected time graph view will be selected.
- Enter the string to find in theFindtext drop down and select theOptionsandDirectionyou need.
- Press theFindbutton orEnterorAlt + n. The next match in the selected time graph view will be selected.

Various options are available in theOptionsgroup:
- Case sensitivemakes the search case sensitive.
- Wrap searchrestarts the search from the first index, depending of the direction, when no entry were found.
- Whole wordallows to search for whole words, delimited by spaces or special character, that are identical to the search text.
- Regular expressionspecifies that the search text is a regular expression or not.
- Case sensitivemakes the search case sensitive.
- Wrap searchrestarts the search from the first index, depending of the direction, when no entry were found.
- Whole wordallows to search for whole words, delimited by spaces or special character, that are identical to the search text.
- Regular expressionspecifies that the search text is a regular expression or not.

TheDirectiongroup allows to select the search direction:ForwardorBackward.

### Filtering Time Events in Time Graph Views

Filtering time events in aTime Graph view, e.g.Control Flow VieworResources View, using theTime Event Filterdialog box. To do so:
- Select theTime Graph viewyou want to filter in
- Press/. TheTime Event Filterdialog box will show on the bottom right corner of the view.
- Enter the string to use as filter in the opened dialog box. The view updates its content as the user enter the string. The filter is applied and unsuccessful time events are dimmed.
- Select theTime Graph viewyou want to filter in
- Press/. TheTime Event Filterdialog box will show on the bottom right corner of the view.
- Enter the string to use as filter in the opened dialog box. The view updates its content as the user enter the string. The filter is applied and unsuccessful time events are dimmed.



Note thatRegular expressionis supported.

It is possible to save multiple filters. They will be all activated at the same time in the view. To save a filter:
- SelectTime Event Filterdialog box
- Enter the filter string to save. The view is updated and new unsuccessful time events are dimmed.
- With the focus on the dialog box, pressENTER. Thesaved filterwill appear at the left of the dialog box and the text in the dialog box is cleared. The view is updated and previous unsuccessful dimmed time events are removed from the view and entries that have no time events to show are removed too.
- SelectTime Event Filterdialog box
- Enter the filter string to save. The view is updated and new unsuccessful time events are dimmed.
- With the focus on the dialog box, pressENTER. Thesaved filterwill appear at the left of the dialog box and the text in the dialog box is cleared. The view is updated and previous unsuccessful dimmed time events are removed from the view and entries that have no time events to show are removed too.



Note that user can still use the dialog box to filter the remaining visible time events in the view.

Note that the view has a limit of 4 saved filters.

Note that alllinksare dimmed when a filter is applied and completely removed when there is activesaved filters.

To remove asaved filter, click on the remove button next to the filter.

The time event filtering uses its owndomain-specific language (DSL). Various logical operators are suppported:
- &&performs a logical AND operation between two filter expressions. Example:ioctl && 5755
- ||performs a logical OR operation between two filter expressions. Example:ioctl || splice
- !performs a logical NOT operation between two filter expressions. Example:!ioctl
- &&performs a logical AND operation between two filter expressions. Example:ioctl && 5755
- ||performs a logical OR operation between two filter expressions. Example:ioctl || splice
- !performs a logical NOT operation between two filter expressions. Example:!ioctl

Filter expressionshave the following patternfieldoperatorargumentin general. Several relational operators are available:
- ==test whether the value of the specified field is equal to the given argument. Example:TID == 5755
- !=test whether the value of the specified field is not equal to the given argument. Example:TID != 5755
- matchestest whether the value of the specified field matches to the given argument. Example:TID matches 5.*5$
- containstest whether the value of the specified field contains to the given argument. Example:TID contains 7
- >test whether the value of the specified field is greater than the given argument. Example:"SOFT IRQ" > 4
- <test whether the value of the specified field is less than the given argument. Example:"SOFT IRQ" < 4
- ==test whether the value of the specified field is equal to the given argument. Example:TID == 5755
- !=test whether the value of the specified field is not equal to the given argument. Example:TID != 5755
- matchestest whether the value of the specified field matches to the given argument. Example:TID matches 5.*5$
- containstest whether the value of the specified field contains to the given argument. Example:TID contains 7
- >test whether the value of the specified field is greater than the given argument. Example:"SOFT IRQ" > 4
- <test whether the value of the specified field is less than the given argument. Example:"SOFT IRQ" < 4

Filter expressionscan have the following patternfieldoperator. The available relational operators for this pattern is:
- presenttest whether the specified field exist. Example:TID present
- presenttest whether the specified field exist. Example:TID present

The DSL allows the possibility to realize complex filters, combining severalFilter expressionsand using parenthesis. Example:TID != 5755 && (System_call contains select)

Note thatfieldparameter with whitespace should be specified using quotes mark. Example:"SOFT IRQ" present

### Filtering of Empty Rows Time Graph Views

Time Graph Views support filtering of empty rows using a dynamic filter. Empty rows are rows with no time events nor row markers in the current visible time range. To hide empty rows, check theHide Empty Rowstoolbar button or view menu entry. Unchecking it will show empty rows again. When changing the current visible time range, the list of visible rows will be dynamically updated.