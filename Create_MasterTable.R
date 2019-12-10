
#****************************

#Written By : Chintan Pathak 

# This code basically parses & merges the two excel files and calculates summary stats.

# It generates two type of output files - 
# 1. Processed Mastered Data 
# 2. Summary Statistics

#Code Execution: This code can be run using R client. Make sure you change path of files accordingly

#******************************

#Reading the Data
file1 <- read.table("path/to/file/TestFile1_RCode.csv", header=True, sep = ",")
file2 <- read.table("path/to/file/TestFile2_RCode.csv", header=T, sep = ",")

#Merge the two data frame
#master_table <- merge(adsl, adef, by="USUBJID")
master_table <- merge(x = file2[,c("USUBJID", "TRT01P", "AGE", "SEX","COUNTRY", "DDUR", "WEIGHTBL", "HEIGHTBL")], y = file1[, c("USUBJID","AVISIT","AVAL")], by="USUBJID", all.x=TRUE)

#Remove duplicate records
index = which(duplicated(master_table))
table <- master_table[-index,]

#Calculate BMI
BMIBL <- (table$WEIGHTBL / (table$HEIGHTBL * table$HEIGHTBL)) * 10000
BMIBL <- round(BMIBL, digit = 2) # rounding to 2 decimal digits

#Add new col BMIBLto table and remove weightbl and heightBL
table < - cbind(table, BMIBL)
table[c("WEIGHTBL","HEIGHTBL")] <- NULL

#Screening where week of visit = 0 and adding that col to table
DAS_WEEK_0 <- ifelse(table$AVISIT == "WEEK 0", table$AVAL, NA)
table$DASWEEK_0 <- DAS_WEEK_0

#Screening where week of visit = 24 and adding that col to table
DAS_WEEK_24 <- ifelse(table$AVISIT == "WEEK 24", table$AVAL, NA)
table$DAS_WEEK_24 <- DAS_WEEK_24

# Category disease active score into 3 - short, long & intermediate and adding variable as new col in table
DDUR_group <- ifelse(table$DDUR > 7, "long",ifelse(table$DDUR > 3 & table$DDUR <= 7,"intermediate", ifelse(table$DDUR <= 3, "short", " ")))
table$DDUR_group <- DDUR_group

#renaming of col AVAL to DAS (reflecting filtered values)

#Rearranging column
# Use can also use the column name here.
table <- table[c(1,7,2,3,4,5,6,12,9,10,11,8)]

#Writing table to csv file
write.csv(table, "path/MasterData.csv", row.names=F)

#Summary Statistics - This can be done using several libraries such dplyr, platecs etc to get more details. But since summary calculation is mentioned, I used summary function

stat <- summary(table[c("AGE","SEX","BMIBL","DDUR","DAS_WEEK_0")])

#Note : 
#There can be visualization built around this data such  bar chart, box plot etc. portraying the significance of treatment. 
#As, mentioned above by using advanced statistical lib, one can perform deeper statistical analysis such as #correlate lot of variables like onset of disease with gender group, physical characteristics etc. 
#Lastly, one can use library - reshape and plyr to format the summary data as well

# Writing summary stat to output file csv file
write.csv(stat, "path/to/file/SummaryStatisitics.csv",row.names=F)
 






