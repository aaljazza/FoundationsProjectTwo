# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "Malabis.com"  # Give your site a name

def welcome():
    print("Welcome to %s.\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)


def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    # your code goes here!
    for store in stores:
        print("- %s" % store.name)


def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    # your code goes here!
    for store in stores:
        if store_name == store.name.lower():
            return store
        elif store_name == "checekout":
            return "checkout"
    return "NONE"


def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    # your code goes here!
    print_stores()
    print("Kindly choose a store from the options Above or type 'Checkout' to leave:")
    checkval2 = "NONE"
    while checkval2 == "NONE":
        store_name = input().lower()
        checkval2 = get_store(store_name)
        if store_name =="checkout":
            checkval2 = "done"
            return "checkout"
        if checkval2 == "NONE":
            print ("%s is not a valid store, please try again:" % store_name)
        else:
            checkval2 = "done"
            return get_store(store_name)


def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to cart.
    """
    # your code goes here!
    checkval4 = "notcomplete"
    while checkval4 == "notcomplete":
        print ("You have chosen %s. Below are the available items for purchase:")
        picked_store.print_products()
        print("Please select an item from the above list which you would like to purchase. Write in 'Checkout' to leave the store. Type 'Back' to go back to a different store.")
        checkval2 = "NONE"
        while checkval2 == "NONE":
            checkval3 = 0
            InputProd = str(input().lower())
            for product in picked_store.products:
                if InputProd == product.name.lower():
                    print ("%s has been added to your cart. Feel free to add more or type 'checkout' to leave." % InputProd)
                    cart.add_to_cart(product)
                    checkval3 = 1
                elif InputProd == "checkout":
                    checkval2 = InputProd
                    checkval3 = 1
                    print ("Your cart includes:")
                    for item in cart.products:
                        print (item)
                    return cart
                    checkval4 == "complete"
                elif InputProd == "back":
                    print ("Your cart includes: ")
                    for item in cart.products:
                        print ("%s, " % item) ,
                    checkval2 = InputProd
                    checkval3 = 1
                    checkval4 = "done"
            if checkval3 == 0:
                print ("%s is not available. Please choose a different product." % InputProd)


def shop():
    """
    The main shopping functionality
    """
    cart = Cart()
    # your code goes here!
    cartitems = []
    UserExitOption = "No"
    while UserExitOption != "yes":
        chosenstore = pick_store()
        if chosenstore != "checkout":
            pick_products(cart, chosenstore)
        print ("Are you ready to checkout? Type 'Yes' to pay or 'Exit' to leave. Type anything else to keep shopping.")
        UserExitOption = input().lower()
        if UserExitOption == "exit":
            print ("Your cart has been dropped. Goodbye.")
            UserExitOption = "No"
            break
    if cart.products == [] and UserExitOption == "yes":
        print ("Your Cart is Empty.")
    elif UserExitOption == "yes":
        cart.checkout()
        

def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
