# python_wordle_solver

This is a simple wordle (or wordle clone) solver written in python.  This was a Saturday project and is fairly rough, yet completely functional.  There are undoubtedly much faster and more pythonic ways to build a wordle solver, but this was my quick and easy way to do it.  

**Idea:**   A five-letter word list is imported into a dataframe and then queried to remove words that contain excluded letters, and/or only include words that include known letters.  The resulting dataframe is read into a sqlite database in memory, and then queried based on known letter/position combinations and impossible letter/position combinations.  The results of these queries are read back into a dataframe for future guesses and printed out to the screen.  This process continues until the user solves the puzzle or runs out of guesses.

**Updates needed:**  
<li>Input validation (y/n, positional nunbers, and alphabetic entries)</li>
<li>Code commenting for better readablity</li><br>

**Directions:**  Run this program any time after your first guess in Wordle.  Follow on-screen directions.

