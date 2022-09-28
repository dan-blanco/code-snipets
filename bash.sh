# password should be defined

[[ `echo $password | grep -P "^(?=.*[a-z])(?=.*[0-9])(?=.*[A-Z]).{8,}$"` ]] && echo "Pass" || echo "Must contain one number, upper case, lower case, and min 8 characters"


# search for value of a key that can be in a different column position each row
while read line; do
        echo $line | awk -F"55=" '{print $2}' | awk '{print $1}' 
done < fixlog
exit 0
