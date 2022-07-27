my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20]

def find_missing(my_list,n):
    sum_obj = (n*(n+1))/2
    my_list_sum = sum(my_list)
    print(sum_obj-my_list_sum)
    

find_missing(my_list,len(my_list)+1)
    