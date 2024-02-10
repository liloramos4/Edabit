def is_authentic_skewer(s):
 return bool(re.match(r'^[^AEIOU]((-+)[AEIOU]\2[^AEIOU])+$', s)) 

