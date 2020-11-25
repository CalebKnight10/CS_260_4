# Reversing a String: str = Good Morning
# Output should be = gninroM dooG


def reverse(stri): # Used stri so it doesn't use str because of same naming.  Just for my own mental sake
    if len(stri) == 1:
        return stri
    else:
        return reverse(stri[1:]) + stri[0]  # Apply Slicing to the string


def main():
    print(reverse("Good Morning"))


if __name__ == '__main__':
    main()