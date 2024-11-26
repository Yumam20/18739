# Idea
The idea comes from seeing a modification of the Caesar cipher -- the Vegenere cipher.
I also took inspiration from the multiple network traffic intercept questions in the 
most recent hackcenter problem batch and figured I wanted to combine the two. This was
done by transmitting the key in the traffic intercept portion by sending each character
thrice (which should be evident by seeing 'TTThhheee kkkeeeyyy iiissss', normally being 
'The key is.') Users can also see that flag.txt has ...[space]....[space] which would point
them to realizing the first two words were The[space]Flag[space] so I decided to include the
space in the vigenere cipher alphabet as well.

# Solution Approach
First, we realize from the pcap image that it is trying to send "The key is ..." but 
every character is being sent three times. We find the key from taking 
every 3rd character from this network capture. Then we take 
the ciphertext in flag.txt and reverse it with by using a vigenere cipher,
which gives us the unencrypted flag (still looks like garbage?)
We must also include the ' ' character in the vigenere cipher to get the true flag.



