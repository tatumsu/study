for f in *.c; 
do 
    gcc -o ${f%.c}.exe $f
done

