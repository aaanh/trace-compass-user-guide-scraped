### Importing a binary or function name mapping file (for LTTng-UST <2.8 traces)

For LTTng-UST 2.8+, if it doesn't resolve symbols automatically, see theSource Lookup's Binary file location configuration.

If you followed the steps in the previous section, you should have a Flame Chart
			View populated with function entries and exits. However, the view will display
			the function addresses instead of names in the intervals, which are not very
			useful by themselves. To get the actual function names, you need to:
- Click theConfigure how addresses are mapped to function names() button in the Flame Chart View.
- Click theConfigure how addresses are mapped to function names() button in the Flame Chart View.

Once again, multiple symbol providers can be available for a unique trace. Each symbol provider can be configured through its own tab. Thus, multiple sources can be used to map the function names to addresses. Below is an image of the basic symbol provider preference page which allows us to import binary or function name mapping files.



Simply click theAdd...button to add one or multiple mapping files. The mapping file could be one of two options:
- : a binary that was used for taking the trace.
- : a binary that was used for taking the trace.
- : a file generated from the binary usingnm myprogram > mapping.txt. Select themapping.txtfile that was just created. If you are dealing with C++ executables, you may want to usenm --demangleinstead to get readable function names.
- : a file generated from the binary usingnm myprogram > mapping.txt. Select themapping.txtfile that was just created. If you are dealing with C++ executables, you may want to usenm --demangleinstead to get readable function names.

The view should now update to display the function names instead. Make sure the
			binary used for taking the trace is the one used for this step too (otherwise,
			there is a good chance of the addresses not being the same).

Lastly, the basic symbol provider introduces the notion of priorities between the mapping files. The resolved symbols from the file at the top of the list will have a higher priority than the files listed below. The files can be moved using theUpandDownbuttons.