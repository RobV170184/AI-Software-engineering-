#!/bin/bash

# if statement: create if_folder if new_folder already exists
if [ -d "new_folder" ]; then
    mkdir if_folder
fi

# if-else statement: check if if_folder exists
if [ -d "if_folder" ]; then
    # if_folder exists, create hyperionDev folder
    mkdir hyperionDev
else
    # if_folder does not exist, create new-projects folder
    mkdir new-projects
fi
