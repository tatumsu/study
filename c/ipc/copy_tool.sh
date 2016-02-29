for folder in `find . -type d`
do
    if [ $folder != '.' ];
    then
        cp copy_tool.sh ./$folder
        cp make.sh ./$folder     
        cp clean.sh ./$folder
    fi
done

