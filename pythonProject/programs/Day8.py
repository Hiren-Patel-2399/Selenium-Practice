
#xpath by traversing

# xpath to inspect no. of subscribers of a video in youtube
# (//yt-formatted-string[.='CarryMinati'])[3]/../../../..//span[5]

# xpath to inspect no. of likes of videos in youtube
# ((//yt-formatted-string[.='CarryMinati'])[3]/ancestor::div)[4]//div[2]

# # xpath to inspect price of a phone in filpcart
# (//div[.='Samsung Galaxy S21 FE 5G with Snapdragon 888 (Lavender, 128 GB)']/../../div)[2]//div[3]

# xapth to inspect ratings and review pf a phone in filpcart
# (//div[.='Samsung Galaxy S21 FE 5G with Snapdragon 888 (Lavender, 128 GB)']/../../div//span)[2]

# xapth to inspect offer % of a mobile in amazon
# (//span[contains(.,'Redmi 12 5G Pastel Blue 6GB RAM 128GB ROM')]/../../../..//span)[6]

##############################################################################################################

# xpath by sibling
#***************************************

# # xpath to inspect no. of subscribers of a video in youtube
# (//a[.='CarryMinati'])[4]/../../../../following-sibling::yt-formatted-string
