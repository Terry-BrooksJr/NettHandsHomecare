#!/bin/bash

if poetry install --without dev; then
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
