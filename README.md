# Mastermind-game
- Incomplete. Currently the count_exact_and_inexact_matches function is having issues.

Mastermind is a two-player code-breaking game, where one person sets a 4-character code, and the other person has to guess the code.

In this implementation, the 4-character code is made up of the letters A,B,C,D,E,F.  In the original game they used coloured pegs.

When the code-guesser makes a guess, they get given feedback of the number of characters they've guessed exactly correct (i.e. how many are the correct letter AND in the correct position), and also feedback of how many characters they have guessed inexactly correct (i.e. how many are the correct letter, but in the wrong position).

So for example, if the secret code is "AABC", and the guess is "DBDC", then the feedback is "1 exact match and 1 inexact match", since C is an exact match, and B is an inexact match (because B is guessed in the wrong position.)

In this implementation of the game, the computer will play the role of code setter, and the human player will play the code guesser.
