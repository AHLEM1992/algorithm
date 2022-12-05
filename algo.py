ALGORITHM CHECK_SENTENCE

VAR
sent : STRING;
sent := ""
nb_espace,charact_count , word_count , vowels_count : INTEGER;
charact: CHAR;
vowels:["a","e","i","o","u"];
BEGIN

REPEAT
    Read(charact)
    write(charact)
    charact_count = charact_count++

    sent := sent+charact

    IF (charact == " ") THEN

    nb_espace:= nb_espace+1

    IF ( charact == vowels) THEN 

    vowels_count:= vowels_count++

UNTIL(charact == ".")

    write ("sent:",sent);
    write("word_count:",nb_espace+1);
    write("vowels_count:",vowels_count);
    write("charact_count:",charact_count);