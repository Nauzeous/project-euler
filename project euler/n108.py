def compute(): #Ugliest code known to man
    minimum = 614889782588491410
    for e1 in range(1,60):
        print("e1", e1)
        divisors = (2*e1 + 1)
        number = 2**e1
        for e2 in range(1, 23):
            divisors = (2*e1 + 1)*(2*e2 + 1)
            number = 2**e1 * 3**e2
            if number > minimum:
                break 
            for e3 in range(1,12):
                divisors = (2*e1 + 1)*(2*e2 + 1)*(2*e3 + 1)
                number = 2**e1 * 3**e2 * 5**e3
                if number > minimum:
                    break
                for e4 in range(1,8):
                    divisors = (2*e1 + 1)*(2*e2 + 1)*(2*e3 + 1)*(2*e4 + 1)
                    number = 2**e1 * 3**e2 * 5**e3 * 7**e4
                    if number > minimum:
                        break
                    for e5 in range(1,6):
                        divisors = (2*e1 + 1)*(2*e2 + 1)*(2*e3 + 1)*(2*e4 + 1)*(2*e5 + 1)
                        number = 2**e1 * 3**e2 * 5**e3 * 7**e4 * 11**e5
                        if number > minimum:
                            break
                        for e6 in range(4):
                            divisors = (2*e1 + 1)*(2*e2 + 1)*(2*e3 + 1)*(2*e4 + 1)*(2*e5 + 1)*(2*e6 + 1)
                            number = 2**e1 * 3**e2 * 5**e3 * 7**e4 * 11**e5 * 13**e6
                            if number > minimum:
                                break
                            for e7 in range(4):
                                divisors = (2*e1 + 1)*(2*e2 + 1)*(2*e3 + 1)*(2*e4 + 1)*(2*e5 + 1)*(2*e6 + 1)*(2*e7 + 1)
                                number = 2**e1 * 3**e2 * 5**e3 * 7**e4 * 11**e5 * 13**e6 * 17**e7
                                if number > minimum:
                                    break
                                for e8 in range(3):
                                    divisors = (2*e1 + 1)*(2*e2 + 1)*(2*e3 + 1)*(2*e4 + 1)*(2*e5 + 1)*(2*e6 + 1)*(2*e7 + 1)*(2*e8 + 1)
                                    number = 2**e1 * 3**e2 * 5**e3 * 7**e4 * 11**e5 * 13**e6 * 17**e7 * 19**e8
                                    if number > minimum:
                                        break
                                    for e9 in range(3):
                                        divisors = (2*e1 + 1)*(2*e2 + 1)*(2*e3 + 1)*(2*e4 + 1)*(2*e5 + 1)*(2*e6 + 1)*(2*e7 + 1)*(2*e8 + 1)*(2*e9 + 1)
                                        number = 2**e1 * 3**e2 * 5**e3 * 7**e4 * 11**e5 * 13**e6 * 17**e7 * 19**e8 * 23**e9
                                        if number > minimum:
                                            break
                                        for e10 in range(2):
                                            divisors = (2*e1 + 1)*(2*e2 + 1)*(2*e3 + 1)*(2*e4 + 1)*(2*e5 + 1)*(2*e6 + 1)*(2*e7 + 1)*(2*e8 + 1)*(2*e9 + 1)*(2*e10 + 1)      
                                            number = 2**e1 * 3**e2 * 5**e3 * 7**e4 * 11**e5 * 13**e6 * 17**e7 * 19**e8 * 23**e9 * 29**e10
                                            if number > minimum:
                                                break
                                            for e11 in range(2):
                                                divisors = (2*e1 + 1)*(2*e2 + 1)*(2*e3 + 1)*(2*e4 + 1)*(2*e5 + 1)*(2*e6 + 1)*(2*e7 + 1)*(2*e8 + 1)*(2*e9 + 1)*(2*e10 + 1)*(2*e11 + 1)      
                                                number = 2**e1 * 3**e2 * 5**e3 * 7**e4 * 11**e5 * 13**e6 * 17**e7 * 19**e8 * 23**e9 * 29**e10 * 31**e11
                                                if number > minimum:
                                                    break
                                                for e12 in range(2):
                                                    divisors = (2*e1 + 1)*(2*e2 + 1)*(2*e3 + 1)*(2*e4 + 1)*(2*e5 + 1)*(2*e6 + 1)*(2*e7 + 1)*(2*e8 + 1)*(2*e9 + 1)*(2*e10 + 1)*(2*e11 + 1)*(2*e12 + 1)     
                                                    number = 2**e1 * 3**e2 * 5**e3 * 7**e4 * 11**e5 * 13**e6 * 17**e7 * 19**e8 * 23**e9 * 29**e10 * 31**e11 * 37**e12
                                                    if number > minimum:
                                                        break
                                                    for e13 in range(2):
                                                        divisors = (2*e1 + 1)*(2*e2 + 1)*(2*e3 + 1)*(2*e4 + 1)*(2*e5 + 1)*(2*e6 + 1)*(2*e7 + 1)*(2*e8 + 1)*(2*e9 + 1)*(2*e10 + 1)*(2*e11 + 1)*(2*e12 + 1)*(2*e13 + 1)   
                                                        number = 2**e1 * 3**e2 * 5**e3 * 7**e4 * 11**e5 * 13**e6 * 17**e7 * 19**e8 * 23**e9 * 29**e10 * 31**e11 * 37**e12 * 41**e13
                                                        if number > minimum:
                                                            break
                                                        for e14 in range(2):
                                                            divisors = (2*e1 + 1)*(2*e2 + 1)*(2*e3 + 1)*(2*e4 + 1)*(2*e5 + 1)*(2*e6 + 1)*(2*e7 + 1)*(2*e8 + 1)*(2*e9 + 1)*(2*e10 + 1)*(2*e11 + 1)*(2*e12 + 1)*(2*e13 + 1)*(2*e14 + 1)   
                                                            number = 2**e1 * 3**e2 * 5**e3 * 7**e4 * 11**e5 * 13**e6 * 17**e7 * 19**e8 * 23**e9 * 29**e10 * 31**e11 * 37**e12 * 41**e13 * 43**e14
                                                            if divisors > 8*10**6 and number < minimum:
                                                                minimum = number
    return minimum


print(compute())