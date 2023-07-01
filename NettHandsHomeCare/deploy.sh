#!/bin/bash

if poetry install --only main; then
    # if cd NettHandsHomeCare; then
        if python manage.py collectstatic --noinput; then
            if python manage.py makemigrations; then
                if python manage.py migrate; then
                    if ! python manage.py runserver; then
                        exit 1
                    fi
                fi

            fi

    fi
fi
