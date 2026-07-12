#!/bin/bash

dbus-send --system --print-reply --dest=org.lingmo.Lastore1 /org/lingmo/Lastore1 org.lingmo.Lastore1.Manager.HandleSystemEvent string:"OsVersionChanged"
