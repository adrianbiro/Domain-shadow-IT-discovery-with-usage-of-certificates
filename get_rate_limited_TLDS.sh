#!/bin/bash

awk '/Too Many Requests/{
        split(FILENAME, arr, "."); 
        hostnames[arr[2]] += 1
    }
    END{
        for (key in hostnames) 
            print key
    }' cert_info_*/*.json
