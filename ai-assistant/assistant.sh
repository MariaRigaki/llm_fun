#!/bin/bash

source .env

read -rsp $'Press r to record and Ctrl-C to stop recording.\n' -n1 key

if [ "$key" = 'r' ]; then
    echo "Your wish is my command"
    pw-record question.wav
else
    echo $key
    echo "This is not the correct key"
    exit
fi


text=$(cat question.txt | tr '\n' ' ')
echo $text 


python submit_question.py --num_tokens 100 --text "$(echo $text)" > answer.txt
answer=$(cat answer.txt | tr '\n' ' ')

echo $answer

# rm response.wav
curl -G -s --output - --data-urlencode "text=$answer" "http://localhost:5002/api/tts" > response.wav
aplay response.wav
