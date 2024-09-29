"""
Write a user defined function find_mean to find the mean of all the values of given dictionary.
"""
def find_mean(k):
    s=0
    p=k.values()
    s=sum(p)
    mean=s//len(k)
    return mean
mean_dict=eval(input("Enter the values: "))
mean=find_mean(mean_dict)
print(mean)