### Exercise 2 - Summing Numbers ###

def mysum(*nums):
    sum = 0
    for num in nums:
        sum = sum + num

    return sum

if __name__ == "__main__":
    print(mysum(5,1,17,*[21,4,8],-7))