#!/bin/bash

# Function to tell a random joke
tell_joke() {
    joke_file="jokes.txt"
    if [ -f "$joke_file" ]; then
        joke=$(shuf -n 1 "$joke_file")
        echo -e "Here's a joke for you:\n$joke"
        espeak "$joke"
    else
        echo "I'm sorry, I can't find any jokes right now."
    fi
}

# Function to tell the time
tell_time() {
    current_time=$(date +"%H:%M:%S")
    echo "The current time is $current_time."
    espeak "The current time is $current_time."
}

# Function to fetch weather information
fetch_weather() {
    weather_info=$(curl -s wttr.in)
    echo -e "Here's the current weather:\n$weather_info"
    espeak "$weather_info"
}

# Function to perform simple calculations
calculate() {
    result=$(echo "$1" | bc)
    echo "The result of '$1' is $result."
    espeak "The result of '$1' is $result."
}

# Interactive mode
interactive_mode() {
    echo "Hello! I'm your friend bot. How can I assist you today?"
    while true; do
        read -p "> " input
        case "$input" in
            "tell me a joke")
                tell_joke;;
            "what's the time")
                tell_time;;
            "what's the weather")
                fetch_weather;;
            "exit")
                echo "Goodbye!"
                break;;
            *)
                if echo "$input" | grep -qP '^[0-9+\-*/().[:space:]]+$'; then
                    calculate "$input"
                else
                    echo "I'm not sure how to respond to that."
                fi
        esac
    done
}

# Non-interactive mode
non_interactive_mode() {
    case "$1" in
        "tell me a joke")
            tell_joke;;
        "what's the time")
            tell_time;;
        "what's the weather")
            fetch_weather;;
        *)
            if echo "$1" | grep -qP '^[0-9+\-*/().[:space:]]+$'; then
                calculate "$1"
            else
                echo "I'm not sure how to respond to that."
            fi
    esac
}

# Main program
if [ $# -eq 0 ]; then
    interactive_mode
else
    non_interactive_mode "$1"
fi
