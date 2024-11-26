# mralchemist

- Namespace: yumam
- ID: mralchemist
- Type: custom
- Category: Forensics
- Points: 1
- Templatable: no
- MaxUsers: 0

## Description

A french diplomat/alchemist born in the year is trying to send his accomplish
secret messages using his own cipher method! Using a time machine, we were able
to intercept his message {{url_for("flag.txt","flag")}} and relevant
{{url_for("intercept.pcapng","network traffic")}}. Can you figure out the secret?

## Details

## Hints

- The french diplomat's name starts with a V
- Make sure to include a ' ' (space character) in your alphabet!

## Solution Overview
First, we realize from the pcap image that it is trying to send "The key is ..." but 
every character is being sent three times. We find the key from taking every 3rd character from
this network capture. Then we take the ciphertext in flag.txt and reverse it with by using a vigenere
cipher, which gives us the unencrypted flag? We also must include the ' ' character in the vigenere cipher 
to get the true flag.

## Challenge Options

```yaml
cpus: 0.5
memory: 128m
pidslimit: 20
ulimits:
  - nofile=128:128
diskquota: 64m
init: true
```

## Attributes

- author: Yuma 'yumam' Matsuoka 
- organization: 18-739
- event: 18-739 Problem Development Exercise #2
