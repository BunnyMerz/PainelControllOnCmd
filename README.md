# How to implement it

The only file needed is `interface.py`

Create an Interface(tree) and pass a tree as argument. Tree is in the following pattern:

```py
tree = {
    PromptString:FunctionOrTree,
    PromptString:FunctionOrTree,
    ...,
    }
```

PromptString is always a string

FunctionOrTree may be another {tree} or a function.

Example:

```py
firsttree = {
    'Option 1': lambda : print('This is option one'),
    'Option 2':{
        'Option2-1':lambda : print('This is option two-one')
        'Option2-2':lambda : print('This is option two-two')
        }
    }
```

Which will have the following effect:

```py
================
[0] Exit
[1] Option 1
[2] Option 2
    - Option2-1
    - Option2-2
================
```

Inputting 2 will open it to:

```py
[0] Go back
[1] Option 2-1
[2] Option 2-2
```

Inputting all of the other options will result in a print() onto the Cmd.

Note¹: `[0] Exit` and `[0] Go back` are implicit, no need to put this option in the tree.

Note²: Any error occurred inside the menu will make the menu `Gracefully stop` and not show any error.

To start the menu, simply call Interface's run() method.

```py
menu = Interface(firsttree)
menu.run() 
```

## Other questions?

Take a Look at or Run `example.py` and they may be answered
