import pandas as pd
import sqlite3

def intro():
    print('''
      .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
    | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
    | | _____  _____ | || |     ____     | || |  _______     | || |  ________    | || |   _____      | || |  _________   | |
    | ||_   _||_   _|| || |   .'    `.   | || | |_   __ \    | || | |_   ___ `.  | || |  |_   _|     | || | |_   ___  |  | |
    | |  | | /\ | |  | || |  /  .--.  \  | || |   | |__) |   | || |   | |   `. \ | || |    | |       | || |   | |_  \_|  | |
    | |  | |/  \| |  | || |  | |    | |  | || |   |  __ /    | || |   | |    | | | || |    | |   _   | || |   |  _|  _   | |
    | |  |   /\   |  | || |  \  `--'  /  | || |  _| |  \ \_  | || |  _| |___.' / | || |   _| |__/ |  | || |  _| |___/ |  | |
    | |  |__/  \__|  | || |   `.____.'   | || | |____| |___| | || | |________.'  | || |  |________|  | || | |_________|  | |
    | |              | || |              | || |              | || |              | || |              | || |              | |
    | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
     '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
     .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
    | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
    | |    _______   | || |     ____     | || |   _____      | || | ____   ____  | || |  _________   | || |  _______     | |
    | |   /  ___  |  | || |   .'    `.   | || |  |_   _|     | || ||_  _| |_  _| | || | |_   ___  |  | || | |_   __ \    | |
    | |  |  (__ \_|  | || |  /  .--.  \  | || |    | |       | || |  \ \   / /   | || |   | |_  \_|  | || |   | |__) |   | |
    | |   '.___`-.   | || |  | |    | |  | || |    | |   _   | || |   \ \ / /    | || |   |  _|  _   | || |   |  __ /    | |
    | |  |`\____) |  | || |  \  `--'  /  | || |   _| |__/ |  | || |    \ ' /     | || |  _| |___/ |  | || |  _| |  \ \_  | |
    | |  |_______.'  | || |   `.____.'   | || |  |________|  | || |     \_/      | || | |_________|  | || | |____| |___| | |
    | |              | || |              | || |              | || |              | || |              | || |              | |
    | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
     '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'      
    
        
    Directions:  Run after first attempt on Wordle or any Wordle clone.  Follow Directions.
    
          ''')


playAgain = 'y'
while playAgain == 'y':
    intro()
    df = pd.read_csv("words.txt", sep=" ", header=None, names=["word"])
    print("For your current game....")
    letters = input(
        "Which letters are excluded? (enter on one line with no spaces): ")
    letters = [char for char in letters]
    
    df1 = df[~df["word"].str.contains(letters[0])]
    for x in range(len(letters[1:])):
        df1 = df1[~df1["word"].str.contains(letters[x+1])]
    
    letters2 = input(
        "Which letters are included? (enter on one line with no spaces): ")
    letters2 = [char for char in letters2]
    
    df1 = df1[df1["word"].str.contains(letters2[0])]
    for x in range(len(letters2[1:])):
        df1 = df1[df1["word"].str.contains(letters2[x+1])]
    
    k1 = input("Are any positions known?: ")
    if k1 == 'y':
        known = []
        space = int(input("Which position? (one at a time): "))
        known_let = input("Which letter? (one at a time): ")
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
        k1 = input("Are any other positions known?: ")
        if k1 == 'y':
            known = []
            space = int(input("Which position? (one at a time): "))
            known_let = input("Which letter? (one at a time): ")
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
       
    k1 = input("Are any impossible positions known?: ")
    if k1 == 'y':
        imp = []
        space = int(input("Which position? (one at a time): "))
        imp_let = input("Which letter? (one at a time): ")
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
        k1 = input("Are any other impossible positions known?: ")
        if k1 == 'y':
            imp = []
            space = int(input("Which position? (one at a time): "))
            imp_let = input("Which letter? (one at a time): ")
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
        answer = input("Did you win or lose the game on that turn (y/n):  ")
        if answer == 'n':
    
            letters3 = input(
                "Which NEW letters are excluded? (enter on one line with no spaces):  ")
            letters3 = [char for char in letters3]
            letters = letters + letters3
    
            df1 = df1[~df1["word"].str.contains(letters[0])]
            for x in range(len(letters[1:])):
                df1 = df1[~df1["word"].str.contains(letters[x+1])]
    
            letters4 = input(
                "Which NEW letters are included? (enter on one line with no spaces):  ")
            letters4 = [char for char in letters4]
            letters2 = letters2 + letters4
    
            df1 = df1[df1["word"].str.contains(letters2[0])]
            for x in range(len(letters2[1:])):
                df1 = df1[df1["word"].str.contains(letters2[x+1])]
    
            k1 = input("Are any NEW positions known?: ")
            if k1 == 'y':
                known = []
                space = int(input("Which position? (one at a time): "))
                known_let = input("Which letter? (one at a time): ")
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
                k1 = input("Are any other NEW positions known?: ")
                if k1 == 'y':
                    known = []
                    space = int(input("Which position? (one at a time): "))
                    known_let = input("Which letter? (one at a time): ")
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
    
            k1 = input("Are any NEW impossible positions known?: ")
            if k1 == 'y':
                imp = []
                space = int(input("Which position? (one at a time): "))
                imp_let = input("Which letter? (one at a time): ")
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
                k1 = input("Are any other NEW impossible positions known?: ")
                if k1 == 'y':
                    imp = []
                    space = int(input("Which position? (one at a time): "))
                    imp_let = input("Which letter? (one at a time): ")
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
    
