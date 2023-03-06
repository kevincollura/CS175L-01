'''
Kevin Collura
AverageFromInput
CS-175L

'''

    
def main():
    
    numbers_file = open('numbers.txt', 'r')
    total=0
    count=0
    
    for line in numbers_file:
        
        total=total+float(line)
        count=count+1
        print (f'I read in {count} number(s) Current number is: {float(line)} Total is: {total}')
    average=total/count
    print(f'Average:',average)

    numbers_file.close()

if __name__ == '__main__':
    main()
