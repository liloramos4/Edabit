# Edabit

Reto1:

Given a string of digits, return the longest substring with alternating odd/even or even/odd digits. If two or more substrings have the same length, return the substring that occurs first.

Examples
longest_substring("225424272163254474441338664823") ➞ "272163254"
 substrings = 254, 272163254, 474, 41, 38, 23

longest_substring("594127169973391692147228678476") ➞ "16921472"
 substrings = 94127, 169, 16921472, 678, 476

longest_substring("721449827599186159274227324466") ➞ "7214"
 substrings = 7214, 498, 27, 18, 61, 9274, 27, 32
 7214 and 9274 have same length, but 7214 occurs first.
 
Notes
The minimum alternating substring size is 2, and there will always be at least one alternating substring.



Reto2:

An authentic vowel skewer is a skewer with a delicious and juicy mix of consonants and vowels. However, the way they are made must be just right:

Skewers must begin and end with a consonant.
Skewers must alternate between consonants and vowels.
There must be an even spacing between each letter on the skewer, so that there is a consistent flavour throughout.
Create a function which returns whether a given vowel skewer is authentic.

Examples
is_authentic_skewer("B--A--N--A--N--A--S") ➞ True

is_authentic_skewer("A--X--E") ➞ False
 Should start and end with a consonant.

is_authentic_skewer("C-L-A-P") ➞ False
 Should alternate between consonants and vowels.

is_authentic_skewer("M--A---T-E-S") ➞ False

 Should have consistent spacing between letters.


Notes:

All tests will be given in uppercase.
Strings without any actual skewer "-" or letters should return False.
