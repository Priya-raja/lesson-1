chai_type = "Tulasi"

def update_chai():

    print("this is local scope",chai_type)

    def frontdesk():

        global chai_type
        chai_type = "Ginger"
        

    frontdesk()    
    print("The updated one for frontdesk is", chai_type)
    
update_chai()        