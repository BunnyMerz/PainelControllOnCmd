class Interface():
    def option_creator(tree_of_options):
        options = []
        functions = []
        for key in tree_of_options:
            options.append(key)
            if isinstance(tree_of_options[key],dict):
                o = Interface.option_creator(tree_of_options[key])
                functions.append(o.activate)
            else:
                functions.append(tree_of_options[key])
        
        return Options(options,functions)

    def __init__(self,tree_of_options):
        self.tree_of_options = tree_of_options
        self.main_menu = Interface.option_creator(tree_of_options)
        self.main_menu.exit_message = 'Exit'
    
    def run(self):
        print("Starting")
        try:
            self.main_menu.activate()
        except:
            print("\n#############\nGracefully Stopping.")

class Options():
    def __init__(self,options=[],functions=[],exit_message="Go Back",depth=1):
        self.options = options
        self.functions = functions
        self.exit_message = exit_message
        self.depth = depth

    def activate(self,action=0,arguments=[]):
        if action == 0:
            self.offer_options()
        elif action == 1:
            self.print_options(arguments[0],arguments[1],arguments[2])
    
    def print_options(self,identation='',depth=0,main=1):
        x=1
        for option in self.options:
            #####
            print(identation,end='')
            if main:
                print("["+str(x)+"]",end=" ")
            else:
                print('-',end=' ')
            print(option)
            #####
            if depth > 0 and (self.functions[x-1].__name__ == Options.activate.__name__):
                self.functions[x-1](1,[identation+"      ",depth-1,0])
            x+=1
            
    def offer_options(self):
        y=-1
        while(y != 0):
            print("=============================")
            print("Which option do you want?")
            print("[0]",self.exit_message)
            self.print_options("",self.depth)
            print("=============================")
            y = int(input("Type in a number: \n"))
            if(y >= 1 and y <= len(self.options)):
                self.functions[y-1]()
                if not((self.functions[y-1].__name__ == Options.activate.__name__)):
                    input("Press enter to continue")
            elif y != 0:
                print("Input a valid option.")