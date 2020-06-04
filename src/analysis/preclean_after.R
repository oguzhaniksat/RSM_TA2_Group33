library(data.table)


dt_after <- fread('../../gen/data-preparation/output/dataset-after.csv')

# tag retweets
dt_after[, retweet:=FALSE]
dt_after[grepl('^RT', text), retweet:=TRUE] #every time it sees ^RT it sets retweet as true

dir.create('../../gen/analysis/temp/', recursive = TRUE)
dir.create('../../gen/analysis/output/', recursive = TRUE)
fwrite(dt_after, '../../gen/analysis/temp/preclean_after.csv')

 