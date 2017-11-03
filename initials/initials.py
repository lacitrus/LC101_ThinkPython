def get_initials(fullname):
    """Given a person's name, return the person's initials (uppercase)"""
    #TODO you code here
    
    name_list = fullname.split()
    initials = ""
    
    for name in name_list:  
        initials = initials + name[0].upper()  

    return initials
