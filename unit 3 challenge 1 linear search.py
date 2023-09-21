def linear_search_product(product_list, target_product):
    indices = []
    for i, product in enumerate(product_list):
        if product == target_product:
            indices.append(i)
    return indices
        
from termcolor import colored,cprint
print(colored("\t\t\t\t LINEAR SCEARCH\n\n\n",'red'))
products = ["apple", "banana", "apple", "grape", "apple"]
cprint(products,'blue')
print("\n\n\n")
for i in range(0,10):
  num=int(input(colored("if you appand a word enter 1,not enter 2\n\n\n",'blue')))
  if num==1:
    a=input(colored("enter the word\n",'blue'))
    products.append(a)
    print(colored("append successfully \n\n\n",'blue'))
    print(products,"\n\n\n")
  else:
    print(colored("no word you apppend\n\n\n",'blue'))
    break
cprint("the products are:\n\n{}\n\n".format(products))
target = input(colored("enter the target word\n\n\n",'blue'))
result=None
result = linear_search_product(products, target)
if result ==[]:
    print(colored("\n\n\n unavailable word",'red'))
else:
  cprint("the {} product in {} index". format(target,result),'green')