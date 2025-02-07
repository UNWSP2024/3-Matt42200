BEGIN
    DISPLAY "Enter your age: "
    INPUT age


    IF age >= 0 AND age <= 12 THEN
        DISPLAY "You are a Child."
    ELSE IF age >= 13 AND age <= 19 THEN
        DISPLAY "You are a Teenager."
    ELSE IF age >= 20 AND age <= 64 THEN
        DISPLAY "You are an Adult."
    ELSE IF age >= 65 THEN
        DISPLAY "You are a Senior."
    ELSE
        DISPLAY "Invalid age entered."
    ENDIF
END