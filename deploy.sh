#!/bin/bash

if pip install -r requirements.txt; then
    if cd NettHandsHomeCare; then
        if ! python manage.py runserver; then
            exit 1
        fi
    fi
fi
