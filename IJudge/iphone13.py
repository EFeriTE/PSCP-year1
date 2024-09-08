"""Iphone"""
def iphone():
    """again"""
    series, capacity = input(),input()
    if series == "iPhone 13 mini":
        iphonemini(capacity)
    elif series == "iPhone 13":
        iphone13(capacity)
    elif series == "iPhone 13 Pro":
        iphonepro(capacity)
    elif series == "iPhone 13 Pro Max":
        iphonepromax(capacity)
    else:
        print("Not Available")

def iphonemini(capacity):
    """mini"""
    if capacity == "128 GB":
        print("25900")
    elif capacity == "256 GB":
        print("29900")
    elif capacity == "512 GB":
        print("37900")
    else:
        print("Not Available")

def iphone13(capacity):
    """13"""
    if capacity == "128 GB":
        print("29900")
    elif capacity == "256 GB":
        print("33900")
    elif capacity == "512 GB":
        print("41900")
    else:
        print("Not Available")

def iphonepro(capacity):
    """pro"""
    if capacity == "128 GB":
        print("38900")
    elif capacity == "256 GB":
        print("42900")
    elif capacity == "512 GB":
        print("50900")
    elif capacity == "1 TB":
        print("58900")
    else:
        print("Not Available")

def iphonepromax(capacity):
    """pro max"""
    if capacity == "128 GB":
        print("42900")
    elif capacity == "256 GB":
        print("46900")
    elif capacity == "512 GB":
        print("54900")
    elif capacity == "1 TB":
        print("62900")
    else:
        print("Not Available")

iphone()
