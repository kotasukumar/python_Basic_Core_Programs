import random


def flip_coin():

    head_count = 0
    tail_count = 0
    i = 0
    print("Enter number of times to flip the coin")
    count = int(input())

    if count >= 0:  #checking enterd value is positive integer are not

        for i in range(count):
            num = random.random()  #generating random number

            if num < 0.5:  #checking head or tail, if <= 0.5 then tail else head
                tail_count = tail_count + 1

            else:
                head_count = head_count + 1
        tail_percentage = (tail_count / count) * 100  #calculating percentage of tail
        head_percentage = (head_count / count) * 100  #calculating percentage of head
        print("Tail percentage is = {0}".format(tail_percentage))
        print("Head percentage is = {0}".format(head_percentage))

    else:  #if a negative integer entered
        print("Enter a positive integer")


if __name__ == "__main__":
    flip_coin()