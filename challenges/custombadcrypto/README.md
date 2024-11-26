# Idea
The idea comes from "do not implement your own crypto." We are not supposed
to implement our own crypto because it is usually less secure than their widely
available alternatives. 

I also looked back at the slides to figure out a clever (yet crackable) own crypto
implementation, and saw that the ECB mode offered a very crackable crypto. I then
combined this with base64 to make sure that the output is printable, as opposed to 
non-printable codewords commonly prevelant in xor results. 

# Solution Approach
First, the encodings should be reverse base64'd, to find out that that the encoding
is in a format b'...'. By xoring this with the b'[plaintext]', we are able to figure
out that there is a pattern seen in the result. This is the repitition of the key, which
indicates that this encoding was a combination of a ECB + base64. By using this key, we are
able to xor it with the encoded flag to get the decoded flag.



