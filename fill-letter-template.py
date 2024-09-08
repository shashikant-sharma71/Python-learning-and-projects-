# Write a progrm to fill in a letter template given below with name and date 

letter= '''
    Dear <|Name|>,
    You are selected!
    <|Date|>
'''
replace=letter.replace("<|Name|>","Shashikant Sharma").replace("<|Date|>"," 01-July-2050")

print(replace)