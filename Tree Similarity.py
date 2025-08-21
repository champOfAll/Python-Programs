def is_mirror(n1,n2):
    if len(n1) != len(n2):
        return False
    for i in range(len(n1)):
        if (n1[i]==-999) != (n2[i]==-999):
            return False
    return True

user_input1=input("Enter 1st tree nodes in level-order (use -999 for missing): ")
node_values1=[int(val) for val in user_input1.strip().split()]

user_input2=input("Enter 2nd tree nodes in level-order (use -999 for missing): ")
node_values2=[int(val) for val in user_input2.strip().split()]

if is_mirror(node_values1,node_values2):
    print('They are same shape wise')
    if node_values1==node_values2:
        print('They are same value-wise')
else:
    print('They are not same')