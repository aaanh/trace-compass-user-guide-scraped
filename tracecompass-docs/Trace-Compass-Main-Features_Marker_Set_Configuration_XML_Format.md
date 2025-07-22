### Marker Set Configuration XML Format

The format of themarkers.xmlfile is defined as follows:

The<marker>element defines a fixed-period marker at the root of the marker set. Optionally, a<marker>can have child<submarker>elements, which split each marker into a number of equal sub-markers, and/or child<segments>elements, which split each marker into segments of defined weights defined by the list of child<segment>elements. Each of these elements can recursively have their own<submarker>and<segments>child elements.

The element attributes are defined as follows:

An example marker set configuration can be found below: