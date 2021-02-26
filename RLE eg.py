to_compress = "WWWWWWWWUUUUUUGGGHHSKFGUMJJJJJJSSLCCCCCCCCCCCOOOOOOOAAAAAAANNNNNNNNNNNNSNNNNNNNNNNNNNNNNNNNNNNNSSSSSSSOOOOOEEEEOOQQQQQQWWQWWQWWQWWQWQWY"
previous_letter = ""
compressed_data = ""
count = ""
for letter in to_compress:
    # if letter is the same as previous letter, add 1 to count.
    if letter == previous_letter:
        count += 1
    else:
        # if letter is different, add previous letter and count to output,
        # reset count to 1
        compressed_data += previous_letter + str(count)
        count = 1

    # set previous letter to letter
    previous_letter = letter
#how to handle the very last letter?
compressed_data += previous_letter + str(count)
print(compressed_data)
