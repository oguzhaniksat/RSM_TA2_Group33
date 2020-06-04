# Makefile
# requires GNUMake32
# Installation instructions: http://tilburgsciencehub.com/setup


analyze: ../../gen/analysis/output/analysis_after.html

../../gen/analysis/temp/preclean_after.csv: preclean_after.R ../../gen/data-preparation/output/dataset-after.csv
	R --vanilla --args "" < "preclean_after.R"

../../gen/analysis/output/analysis_after.html: analysis_after.Rmd ../../gen/analysis/temp/preclean_after.csv
	R -e "rmarkdown::render('analysis_after.Rmd', output_file = '../../gen/analysis/output/analysis_after.html')"

analyze: ../../gen/analysis/output/analysis_bef.html

../../gen/analysis/temp/preclean_bef.csv: preclean_bef.R ../../gen/data-preparation/output/dataset-bef.csv
	R --vanilla --args "" < "preclean_bef.R"

../../gen/analysis/output/analysis_bef.html: analysis_bef.Rmd ../../gen/analysis/temp/preclean_bef.csv
	R -e "rmarkdown::render('analysis_bef.Rmd', output_file = '../../gen/analysis/output/analysis_bef.html')"

analyze: ../../gen/analysis/output/analysis_event.html

../../gen/analysis/temp/preclean_event.csv: preclean_event.R ../../gen/data-preparation/output/dataset-event.csv
	R --vanilla --args "" < "preclean_event.R"

../../gen/analysis/output/analysis_event.html: analysis_event.Rmd ../../gen/analysis/temp/preclean_event.csv
	R -e "rmarkdown::render('analysis_event.Rmd', output_file = '../../gen/analysis/output/analysis_event.html')"

wipe:
	python wipe.py
