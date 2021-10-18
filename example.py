from interface import Interface

tree_of_options = {
    "Help":{
        "How it works":{
            "Classes":{
                "Interface": lambda : print("Simply runs the first option via run()"),
                "Options": lambda : print("Has two lists, options (which are the texts) and the functions. By picking a number, it will run the function of that number.\nYou can nest Options inside options to make submenus by passing a prompt like 'Submenu' to menu's options list and the Option.activate to the menu's function list.")
            },
            "Idea":lambda : print("Make nested options for easier testing"),
        },
        "Why should I use it":lambda : print("Makes a easily creatable and editable menu and submenus wich include actions via using Lambda or any function"),
        "FAQ":{
            "Question 1": lambda : print("Answer 1"),
            "Question 2": lambda : print("Answer 2"),
            "Question 3": lambda : print("Answer 3"),
            "Question 4": lambda : print("Answer 4"),
        }
    },
    "Documentation":{
        "Interface Arguments": lambda : print(
"""Interface recives a tree that follows the follwoing format:
tree = {
    PromptString:FunctionOrTree
    }

PromptString is always a string
FunctionOrTree may be another tree or a function.

Example:
secondtree = {
    'Option 1': lambda : print('This is option one'),
    'Option 2':{
        'Option2-1':lambda : print('This is option two-one')
        'Option2-2':lambda : print('This is option two-two')
        }
    }

    Which will have the following effect:
    ================
    [0] Go back               --> Is implicit, no need to put this option in the tree
    [1] Option 1
    [2] Option 2
        - Option2-1
        - Option2-2
    ================"""
        ),'Interface functions':lambda : print("""
run():
    - Will activate the first batch of options. Ctrl-c or the option <[0] Exit> will terminate run().
    """),
    'Options Functions':lambda : print("""
activate(action=0,arguments=[])
    - works as a hub for all Options functions.
        - action 0 will run offer_options()
        - action 1 will wun print options()
    - arguments=[] will recive the arguments of each action and passed individually, which means the len(argumnets) must be rigth for each action.

print_options(identation='',depth=0,main=1)
    - Only depth should be specified. Will print Option's list of options and, if possible, go further depending on depth and also showing the nested options.

offer_options()
    - Will run print_options() and ask for a input() that is a number from 0 to len(Options.options). Will terminate if input is 0.
    """)
    }
}

example = Interface(tree_of_options)
example.run()