# https://rocker-project.org/images/versioned/rstudio.html#quick-reference
FROM rocker/rstudio:latest

# https://rocker-project.org/use/extending.html
RUN install2.r --error \
  dbplyr \
  DT \
  Rcpp \
  reticulate \
  RPostgres
