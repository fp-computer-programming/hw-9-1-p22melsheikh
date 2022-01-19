# MEE 1/18/22


def ft(list_or_string, to_be_found):
    for i, v in enumerate(list_or_string):
        try:
            if to_be_found in v:
                print(i)
                break
            elif to_be_found not in list_or_string:
                print(-1)
                break
                
        except: print("Invalid Input")
                
ft("apple", "p")