a_tuple = (10,20,30,40,50)

element = 30
def element_exists(element,a_tuple):
    if element in a_tuple:
        print (f"{element} exists in the tuple.")
    else:
        print (f"{element} does not exist in the tuple.")

element_exists(element,a_tuple)