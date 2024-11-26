# custombadcrypto

- Namespace: yumam
- ID: custombadcrypto
- Type: custom
- Category: Forensics
- Points: 1
- Templatable: no
- MaxUsers: 0

## Description

Dr.Evil tried to roll out his own crypto. Unfortunately
Dr.Evil didn't take 18-739 and reused his key. 
He encoded a {{url_for("scriptencoded.txt","few lines from the Bee Movie Script")}},
 and his {{url_for("encodedflag.txt","super duper secret")}}.
Can you figure out the secret and tell Dr.Evil to use a better encryption algorithm?

## Details

## Hints

- Do you see any patterns in the output?
- The output is base64 encoded

## Solution Overview
First, the encodings should be reverse base64'd, to find out that that the encoding
is in a format b'...'. By xoring this with the b'[plaintext]', we are able to figure
out that there is a pattern seen in the result. This is the repitition of the key, which
indicates that this encoding was a combination of a ECB + base64. By using this key, we are
able to xor it with the encoded flag to get the decoded flag.

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

## Learning Objective

Test and verify your connectivity to our CTF

## Attributes

- author: Yuma 'yumam' Matsuoka 
- organization: 18-739
- event: 18-739 Problem Development Exercise #1
