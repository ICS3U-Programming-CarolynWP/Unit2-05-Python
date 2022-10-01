#!/usr/bin/env python3
# Created by: Carolyn Webster Pless
# Created on: 2022/9/30
# Shows and displays a bunch of variables/assignment statements


def main():
    # variables
    classes = 4
    words = "You "
    words2 = "are "
    words3 = "cool!"

    # assignment statements
    classes = classes + 4
    nice_message = words + words2 + words3

    # printing out those statements
    print("There are {} classes in a semester".format(classes))
    print(nice_message)


if __name__ == "__main__":
    main()
