def freq_digit(num: int) -> int:
    return max(str(num),key=str(num).count)
    
    
    


if __name__ == '__main__':
   print(freq_digit(748791789189717891789))


    # (2020, 2), (177, 7), (1998, 9),
    # (12345, 1), (994145467, 4),
    # (748791789189717891789, 7)