

class HotelRoomType():
    """Python class to implement an enumeration for the attribute Hotel Room Type.

    This Python class implements an enumeration for the attribute Hotel Room Type.

    Syntax
    ------
      obj = HotelRoomType.Enum

    Parameters
    ----------

    Returns
    -------
      obj : HotelRoomType
          Python object output parameter that represents an instance
          of the class HotelRoomType.

    Attributes
    ----------
    """
    #Here you start your code.









def main():
    #TESTING
    print("=================================================================.")
    print("Test Case 1: Check Class HotelRoomType.")
    print("=================================================================.")

    if isinstance(HotelRoomType.INDIVIDUAL, HotelRoomType):
        print("Test PASS. The enum for Individual has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(HotelRoomType.DOBLE, HotelRoomType):
        print("Test PASS. The enum for Doble has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(HotelRoomType.SUITE, HotelRoomType):
        print("Test PASS. The enum for Suite has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


if __name__ == "__main__":
    main()
