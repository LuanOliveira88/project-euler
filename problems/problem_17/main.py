import os        

def main():
    numbers_strings = [
        "one", "two", "three", "four", "five", "six", "seven", "eight", 
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", 
        "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "thirty", 
        "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
    ]
    numbers_keys = list(range(1, 20))
    numbers_keys.extend(list(range(20, 100, 10)))

    numbers_map = {key: value for key, value in zip(numbers_keys, numbers_strings)}

    def get_string(num):
        if num in numbers_map:
            return numbers_map[num]
        
        if 10 < num < 100 and num%10:
            d, u = [int(digit) for digit in str(num)]
            d = 10*d
            return f"{numbers_map[d]}{numbers_map[u]}"
        
        if 100 < num < 1000 and num%100:
            c = int(str(num)[0])
            d_u = int(str(num)[1:])
            c = 100*c
            return f"{numbers_map[c]}and{numbers_map[d_u]}"
        
    for num in range(1, 100):
        if num not in numbers_map:
            numbers_map[num] = get_string(num)
        else:
            continue    

    for num in range(1, 10):
        numbers_map[100*num] = f"{numbers_map[num]}hundred" 

    for num in range(100, 1000):
        if num not in numbers_map:
            
            numbers_map[num] = get_string(num)

    numbers_map[1000] = "onethousand"
    string_lens = [len(value) for value in numbers_map.values()]
    
    


    return sum(string_lens)

if __name__ == '__main__':
    main()
