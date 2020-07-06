# LongestPalindrome
This program takes in a string and return its longest palindromic substring.

The given file uses explanding around centre. We traverse through each letter in string and consider it the center of a palindrome string, Simultaneously, we consider the space between this and nexr letter to be center and whichever gives a longer palindrome we store it. Then we compare this with existing palindrome and find the bigger one. Then at last return it.

example: In "abba" the center of palindrome is between the two b, "ab|ba".
