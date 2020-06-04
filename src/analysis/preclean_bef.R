library(data.table)

dt_bef <- fread('../../gen/data-preparation/output/dataset-bef.csv')

# tag retweets
dt_bef[, retweet:=FALSE]
dt_bef[grepl('^RT', text), retweet:=TRUE] #every time it sees ^RT it sets retweet as true


#dir.create('../../gen/analysis/temp/', recursive = TRUE)
#dir.create('../../gen/analysis/output/', recursive = TRUE)
fwrite(dt_bef, '../../gen/analysis/temp/preclean_bef.csv')



