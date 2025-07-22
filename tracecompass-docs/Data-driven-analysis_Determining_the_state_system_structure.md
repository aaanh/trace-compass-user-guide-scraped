### Determining the state system structure

The first thing to do is to determine the attribute tree we'll use to represent the model of the system. The attribute tree is like a file system with directories and files, where files are logically gathered in the same parent directory. There is no one good way to build a tree, the logic will depend on the situation and on the person defining it.

The generated state system may be used later on to populate views, so attributes of the tree could be grouped in such a way as to make it easy to reach them with a simple path. The view will then be more simple.

In our example case, we'll want to track the status of each task and, for each critical section, which task is running them.

Then we determine how each event will affect the state of the attributes. But first, let's ask ourselves what values should each state take.

Let's see with the tree:

Then we determine how each event will affect the state of the attributes. In the attribute paths below, elements in {} are values coming from the trace event, while strings are constants. For the sake of simplicity, we'll say "update attribute", but if an attribute does not exist, it will be created.
- start(number): Update state value of attribute "Tasks/{number}" to "RUNNING".
- execute(number, fct_name): Update state value of attribute "Tasks/{number}" to "CRITICAL" and Update attribute "Critical section/{fct_name}" to "{number}".
- wait(number): Update state value of attribute "Tasks/{number}" to "WAITING".
- exec_end(fct_name): Update state value of attribute "Tasks/{valueOf Critical section/{fct_name}}" to RUNNING and update "Critical section/{fct_name}" to null.
- stop(number): Update state value of attribute "Tasks/{number}" to null.
- start(number): Update state value of attribute "Tasks/{number}" to "RUNNING".
- execute(number, fct_name): Update state value of attribute "Tasks/{number}" to "CRITICAL" and Update attribute "Critical section/{fct_name}" to "{number}".
- wait(number): Update state value of attribute "Tasks/{number}" to "WAITING".
- exec_end(fct_name): Update state value of attribute "Tasks/{valueOf Critical section/{fct_name}}" to RUNNING and update "Critical section/{fct_name}" to null.
- stop(number): Update state value of attribute "Tasks/{number}" to null.