### Definitions and example

Before we start, we'll define a few terms used in the following sections. The interested reader should read theTmf Developer Guidefor more complete description of the state system and state providers.
- Thestate systemcan be viewed as a model of the system, where the different elements (attributes) can be seen as a tree, and their evolution (states) is tracked through time.
- Thestate systemcan be viewed as a model of the system, where the different elements (attributes) can be seen as a tree, and their evolution (states) is tracked through time.
- Attribute: An attribute is the smallest element of the model that can be in any particular state. Since many attributes may have the same name, each attribute is represented by its full path in the attribute tree.
- Attribute: An attribute is the smallest element of the model that can be in any particular state. Since many attributes may have the same name, each attribute is represented by its full path in the attribute tree.
- State: A state is a value assigned to an attribute at a given time. Each model has its own state values.
- State: A state is a value assigned to an attribute at a given time. Each model has its own state values.
- Attribute tree: Elements in the model can be placed in a tree-like structure, for logical grouping. Each element in the tree can have both children and a state. Also, the tree is just a logical structure, all elements may be top-level elements.
- Attribute tree: Elements in the model can be placed in a tree-like structure, for logical grouping. Each element in the tree can have both children and a state. Also, the tree is just a logical structure, all elements may be top-level elements.
- State history: Whereas the attribute tree may be seen as the first dimension of the state system, the state history is the second dimension, over time. It tracks the intervals at which an attribute was in a given state.
- State history: Whereas the attribute tree may be seen as the first dimension of the state system, the state history is the second dimension, over time. It tracks the intervals at which an attribute was in a given state.

In the following sections, we'll use an example trace with the following events:
- start(number): A new task with ID 'number' just started.
- execute(number, fct_name): The task with ID 'number' is executing a critical section named 'fct_name'.
- wait(number): The task with ID 'number' cannot execute a critical section and needs to wait for it.
- exec_end(fct_name): A task finished executing the critical section named 'fct_name'.
- stop(number): The task with ID 'number' has just finished.
- start(number): A new task with ID 'number' just started.
- execute(number, fct_name): The task with ID 'number' is executing a critical section named 'fct_name'.
- wait(number): The task with ID 'number' cannot execute a critical section and needs to wait for it.
- exec_end(fct_name): A task finished executing the critical section named 'fct_name'.
- stop(number): The task with ID 'number' has just finished.