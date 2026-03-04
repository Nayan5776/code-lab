myArray=("text.txt" "text.txt" "text.txt" "text.txt" "image.jpg" "image.jpg" "image.jpg" "image.jpg")
for array in ${myArray[@]}
do
  if [[ "$array" == *.txt ]]; then
    echo "Moving $array to Text_Files folder"
  elif [[ "$array" == *.jpg ]]; then
    echo "Moving $array to Images folder"
  else
    echo "File not found"
  fi
done