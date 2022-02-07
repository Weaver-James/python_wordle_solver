import pandas as pd
import sqlite3

def intro():
    print('''
       
          __   __   __        ___     __   __             ___  __  
    |  | /  \ |__) |  \ |    |__     /__` /  \ |    \  / |__  |__) 
    |/\| \__/ |  \ |__/ |___ |___    .__/ \__/ |___  \/  |___ |  \ 
                                                                                                         
                 
    Directions:  Run after first attempt on Wordle or any Wordle clone.  
    Follow on-screen directions.
    
          ''')

playAgain = 'y'

# for input validation
yes_no = ["y", "n"]
nums = [1, 2, 3, 4, 5]

while playAgain == 'y':
    intro()
    df = pd.read_csv("words.txt", sep=" ", header=None, names=["word"])
    print("For your current game....")
   
    k1 = ''
    while k1 not in yes_no:
        k1 = input("Are there any excluded letters? (y/n): ")
    else:
        pass
    
    if k1 == "y":
        letters = ' '
        while letters.isalpha() == False:
            letters = input(
                "Which letters are excluded? (enter on one line with no spaces): ")
        else:
            letters = [char for char in letters]
        
        df1 = df[~df["word"].str.contains(letters[0])]
        for x in range(len(letters[1:])):
            df1 = df1[~df1["word"].str.contains(letters[x+1])]
    else:
        pass
    
    k1 = ''
    while k1 not in yes_no:
        k1 = input("Are there any included letters? (y/n): ")
    else:
        pass
    
    if k1 == "y":
        letters2 = '  '
        while letters2.isalpha() == False:
            letters2 = input(
                "Which letters are included? (enter on one line with no spaces): ")
        else:
            letters2 = [char for char in letters2]
        
        df1 = df1[df1["word"].str.contains(letters2[0])]
        for x in range(len(letters2[1:])):
            df1 = df1[df1["word"].str.contains(letters2[x+1])]
    
    k1 = ''
    while k1 not in yes_no:
        k1 = input("Are any positions known?: ")

    else:
        if k1 == 'y':
            known = []
            space = ''
            known_let = ''
            while space not in nums:
                space = input("Which position? (one at a time): ")
                try:
                    space = int(space)
                except:
                    pass
            else:
                pass
            
            while known_let.isalpha()== False:                    
                known_let = input("Which letter? (one at a time): ")
            else:
                pass       
            space = int(space)
            for spc in range(space-1):
                known.append('_')
            known.append(known_let)
            for spc in range(5):
                known.append('_')
            known1 = ''.join(str(i) for i in known)
            known1 = known1[:5]
        
            cnx = sqlite3.connect(':memory:')
            df1.to_sql(name='wordlist', con=cnx)
            cur = cnx.cursor()
            k_list = cur.execute(
                "SELECT * FROM wordlist WHERE word LIKE ?", (known1,)).fetchall()
            if len(k_list[0]) >= 3:
                k_list = [item[-1] for item in k_list]
                df1 = pd.DataFrame(k_list, columns=['word'])
            else:
                df1 = pd.DataFrame(k_list, columns=['0', 'word'])
                df1.drop(['0'], axis=1)
        else:
            pass
    
    while k1 == 'y':
        k1 = ''
        while k1 not in yes_no:
            k1 = input("Are any other positions known?: ")
        else:
            if k1 == 'y':
                known = []
                space = ''
                known_let = ''
                while space not in nums:
                    space = input("Which position? (one at a time): ")
                    try:
                        space = int(space)
                    except:
                        pass
                else:
                    pass
                while known_let.isalpha()== False:                    
                    known_let = input("Which letter? (one at a time): ")
                else:
                    pass
                space = int(space)
                for spc in range(space-1):
                    known.append('_')
                known.append(known_let)
                for spc in range(5):
                    known.append('_')
                known1 = ''.join(str(i) for i in known)
                known1 = known1[:5]
        
                cnx = sqlite3.connect(':memory:')
                df1.to_sql(name='wordlist', con=cnx)
                cur = cnx.cursor()
                k_list = cur.execute(
                    "SELECT * FROM wordlist WHERE word LIKE ?", (known1,)).fetchall()
                if len(k_list[0]) >= 3:
                    k_list = [item[-1] for item in k_list]
                    df1 = pd.DataFrame(k_list, columns=['word'])
                else:
                    df1 = pd.DataFrame(k_list, columns=['0', 'word'])
                    df1.drop(['0'], axis=1)
            else:
                pass
    
    
    k1 = ''
    while k1 not in yes_no:
        k1 = input("Are any impossible positions known?: ")
    else:    
        if k1 == 'y':
            imp = []
            space = ''
            imp_let = ''
            while space not in nums:
                space = input("Which position? (one at a time): ")
                try:
                    space = int(space)
                except:
                    pass
            else:
                pass
            while imp_let.isalpha()== False:                    
                imp_let = input("Which letter? (one at a time): ")
            else:
                   pass
            space = int(space)
            for spc in range(space-1):
                imp.append('_')
            imp.append(imp_let)
            for spc in range(5):
                imp.append('_')
            imp1 = ''.join(str(i) for i in imp)
            imp1 = imp1[:5]
        
            cnx = sqlite3.connect(':memory:')
            df1.to_sql(name='wordlist', con=cnx)
            cur = cnx.cursor()
            k_list = cur.execute(
                "SELECT * FROM wordlist WHERE word NOT LIKE ?", (imp1,)).fetchall()
            if len(k_list[0]) >= 3:
                k_list = [item[-1] for item in k_list]
                df1 = pd.DataFrame(k_list, columns=['word'])
            else:
                df1 = pd.DataFrame(k_list, columns=['0', 'word'])
                df1.drop(['0'], axis=1)
        else:
            pass
    

    while k1 == 'y':
        k1 = ''
        while k1 not in yes_no:
            k1 = input("Are any other impossible positions known?: ")
        else:
            if k1 == 'y':
                imp = []
                space = ''
                imp_let = ''
                while space not in nums:
                    space = input("Which position? (one at a time): ")
                    try:
                        space = int(space)
                    except:
                        pass
                else:
                   pass
                
                while imp_let.isalpha()== False:                    
                    imp_let = input("Which letter? (one at a time): ")
                else:
                    pass
                space = int(space)
                for spc in range(space-1):
                    imp.append('_')
                imp.append(imp_let)
                for spc in range(5):
                    imp.append('_')
                imp1 = ''.join(str(i) for i in imp)
                imp1 = imp1[:5]
        
                cnx = sqlite3.connect(':memory:')
                df1.to_sql(name='wordlist', con=cnx)
                cur = cnx.cursor()
                k_list = cur.execute(
                    "SELECT * FROM wordlist WHERE word NOT LIKE ?", (imp1,)).fetchall()
                if len(k_list[0]) >= 3:
                    k_list = [item[-1] for item in k_list]
                    df1 = pd.DataFrame(k_list, columns=['word'])
                else:
                    df1 = pd.DataFrame(k_list, columns=['0', 'word'])
                    df1.drop(['0'], axis=1)
            else:
                pass
    print()
    print(df1.to_string(index=False))
    
    solve = 'n'
    
    while solve == 'n':
        answer = ''
        while answer not in yes_no:
            answer = input("Did you win or lose the game on that turn (y/n):  ")
        else:
            pass
        
        if answer == 'n':
            k1 = ''
            while k1 not in yes_no:
                k1 = input("Are there any NEW excluded letters? (y/n): ")
            else:
                pass
            if k1 == 'y':
                letters = input(
                    "Which NEW letters are excluded? (enter on one line with no spaces):  ")
                letters = [char for char in letters]
   
    
                df1 = df1[~df1["word"].str.contains(letters[0])]
                for x in range(len(letters[1:])):
                    df1 = df1[~df1["word"].str.contains(letters[x+1])]
            else:
                pass
            k1 = ''
            while k1 not in yes_no:
                k1 = input("Are there any NEW included letters? (y/n): ")
            else:
                pass        
            if k1 == 'y':
                letters2 = input(
                "Which NEW letters are included? (enter on one line with no spaces):  ")
                letters2 = [char for char in letters2]

                df1 = df1[df1["word"].str.contains(letters2[0])]
                for x in range(len(letters2[1:])):
                    df1 = df1[df1["word"].str.contains(letters2[x+1])]
    
            k1 = ''
            while k1 not in yes_no:        
                k1 = input("Are any NEW positions known?: ")
            else:    
                if k1 == 'y':
                    known = []
                    space = ''
                    known_let = ''
                    while space not in nums:
                        space = input("Which position? (one at a time): ")
                        try:
                            space = int(space)
                        except:
                            pass
                    else:
                        pass
                    while known_let.isalpha()== False:                    
                        known_let = input("Which letter? (one at a time): ")
                    else:
                        pass
                    space = int(space)
                    for spc in range(space-1):
                        known.append('_')
                    known.append(known_let)
                    for spc in range(5):
                        known.append('_')
                    known1 = ''.join(str(i) for i in known)
                    known1 = known1[:5]
        
                    cnx = sqlite3.connect(':memory:')
                    df1.to_sql(name='wordlist', con=cnx)
                    cur = cnx.cursor()
                    k_list = cur.execute(
                        "SELECT * FROM wordlist WHERE word LIKE ?", (known1,)).fetchall()
                    if len(k_list[0]) >= 3:
                        k_list = [item[-1] for item in k_list]
                        df1 = pd.DataFrame(k_list, columns=['word'])
                    else:
                        df1 = pd.DataFrame(k_list, columns=['0', 'word'])
                        df1.drop(['0'], axis=1)
                else:
                    pass

            while k1 == 'y':
                k1 = ''
                known = []
                while k1 not in yes_no:
                    k1 = input("Are any other NEW positions known?: ")
                else:
                    if k1 == 'y':
                        space = ''
                        known_let = ''
                        while space not in nums:
                            space = input("Which position? (one at a time): ")
                            try:
                                space = int(space)
                            except:
                                pass
                        else:
                            pass
                        while known_let.isalpha()== False:                    
                            known_let = input("Which letter? (one at a time): ")
                        else:
                            pass
                        space = int(space)
                        
                        for spc in range(space-1):
                            known.append('_')
                        known.append(known_let)
                        for spc in range(5):
                            known.append('_')
                        known1 = ''.join(str(i) for i in known)
                        known1 = known1[:5]
        
                        cnx = sqlite3.connect(':memory:')
                        df1.to_sql(name='wordlist', con=cnx)
                        cur = cnx.cursor()
                        k_list = cur.execute(
                            "SELECT * FROM wordlist WHERE word LIKE ?", (known1,)).fetchall()
                        if len(k_list[0]) >= 3:
                            k_list = [item[-1] for item in k_list]
                            df1 = pd.DataFrame(k_list, columns=['word'])
                        else:
                            df1 = pd.DataFrame(k_list, columns=['0', 'word'])
                            df1.drop(['0'], axis=1)
                    else:
                        pass
        
            k1 = ''
            while k1 not in yes_no:   
                k1 = input("Are any NEW impossible positions known?: ")
            
            else:
                if k1 == 'y':
                    imp = []
                    space = ''
                    imp_let = ''
                    while space not in nums:
                        space = input("Which position? (one at a time): ")
                        try:
                            space = int(space)
                        except:
                            pass
                    else:
                       pass
                    
                    while imp_let.isalpha()== False:                    
                        imp_let = input("Which letter? (one at a time): ")
                    else:
                        pass
                    space = int(space)
                    for spc in range(space-1):
                        imp.append('_')
                    imp.append(imp_let)
                    for spc in range(5):
                        imp.append('_')
                    imp1 = ''.join(str(i) for i in imp)
                    imp1 = imp1[:5]
        
                    cnx = sqlite3.connect(':memory:')
                    df1.to_sql(name='wordlist', con=cnx)
                    cur = cnx.cursor()
                    k_list = cur.execute(
                        "SELECT * FROM wordlist WHERE word NOT LIKE ?", (imp1,)).fetchall()
                    if len(k_list[0]) >= 3:
                        k_list = [item[-1] for item in k_list]
                        df1 = pd.DataFrame(k_list, columns=['word'])
                    else:
                        df1 = pd.DataFrame(k_list, columns=['0', 'word'])
                        df1.drop(['0'], axis=1)
                else:
                    print()
                    print(df1.to_string(index=False))
    
            while k1 == 'y':
                k1 = ''
                while k1 not in yes_no:   
                    k1 = input("Are any other NEW impossible positions known?: ")
                else:
                    if k1 == 'y':
                        imp = []
                        space = ''
                        imp_let = ''
                        while space not in nums:
                            space = input("Which position? (one at a time): ")
                            try:
                                space = int(space)
                            except:
                                pass
                        else:
                           pass
                        
                        while imp_let.isalpha()== False:                    
                            imp_let = input("Which letter? (one at a time): ")
                        else:
                            pass
                        space = int(space)
                        for spc in range(space-1):
                            imp.append('_')
                        imp.append(imp_let)
                        for spc in range(5):
                            imp.append('_')
                        imp1 = ''.join(str(i) for i in imp)
                        imp1 = imp1[:5]
        
                        cnx = sqlite3.connect(':memory:')
                        df1.to_sql(name='wordlist', con=cnx)
                        cur = cnx.cursor()
                        k_list = cur.execute(
                            "SELECT * FROM wordlist WHERE word NOT LIKE ?", (imp1,)).fetchall()
                        if len(k_list[0]) >= 3:
                            k_list = [item[-1] for item in k_list]
                            df1 = pd.DataFrame(k_list, columns=['word'])
                        else:
                            df1 = pd.DataFrame(k_list, columns=['0', 'word'])
                            df1.drop(['0'], axis=1)
                    else:
                        print()
                        print(df1.to_string(index=False))
        else:
            solve = 'y'
            playAgain = input('Do you want to play again? (y/n): ')
    else:
        pass

# Not playing again
else:
    print()
    print("Maybe some other time then...  Goodbye.")
    raise SystemExit()
    
    
