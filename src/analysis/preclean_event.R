library(data.table)

dt_event <- fread('../../gen/data-preparation/output/dataset-event.csv')

# tag retweets
dt_event[, retweet:=FALSE]
dt_event[grepl('^RT', text), retweet:=TRUE] #every time it sees ^RT it sets retweet as true


#dir.create('../../gen/analysis/temp/', recursive = TRUE)
#dir.create('../../gen/analysis/output/', recursive = TRUE)
fwrite(dt_event, '../../gen/analysis/temp/preclean_event.csv')

 