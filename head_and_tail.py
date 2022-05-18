import random

def flip_coin(count):
    '''
    :param count: 10
    :return: percentage of head and tail
    '''

    head_count = 0
    tail_count = 0
    i = 0

    if count >= 0:  #checking enterd value is positive integer are not

        for i in range(count):
            num = random.random()  #generating random number

            if num < 0.5:  #checking head or tail, if <= 0.5 then tail else head
                tail_count += 1

            else:
                head_count += 1
        tail_percentage = tail_count / count * 100  #calculating percentage of tail
        head_percentage = head_count / count * 100  #calculating percentage of head
        return tail_percentage, head_percentage


    else:  #if a negative integer entered
        print("Invalid input, please enter a positive integer")


if __name__ == "__main__":
    count = int(input("Enter number of times to flip the coin "))
    tail_percentage, head_percentage = flip_coin(count)
    print("Tail percentage is = ", tail_percentage)
    print("Head percentage is = ", head_percentage)