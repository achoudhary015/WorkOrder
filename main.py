#######################################
'''------------------------------------
#Programming Language used :: Python
#Author :: Anubhav Choudhary
#Email :: anubhavchoudhary009@gmail.com
#Website ::https://anubhavchoudhary009.github.io/portfolio.me/
---------------------------------------'''
########################################

#-----------------code-----------------#




#import libraries and modules
import pandas as pd 
import direction    #module 
import Structure    #module 

 
def init_orders():
    
    id_depend = []
    direction.write_new_file("output.txt")                      #output Result 
    Depend_file = direction.read_file('dependencies.txt')       #Reading dependencies from file
    ordered_file= Depend_file.sort_values(by=['id'])            #Sorting values by id 

    for row in Depend_file.itertuples():
        id_depend.append([row.id, row.dependency_id])

    Work_orders = Structure.Tree()
    
    for pair in id_depend:
        id, depend = pair[0], pair[1]
        Work_orders.insert(id,depend)
        
        if Work_orders.insert(id,depend) is not None:
            new_tree = Work_orders.insert(id,depend)
 
    Work_orders.depth_tree_order()
    
    new_tree.depth_tree_order()
    
    
init_orders()
