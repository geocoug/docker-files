ARG BASE_CONTAINER=jupyter/scipy-notebook:2023-01-09
FROM $BASE_CONTAINER

USER root

# install the locales you want to use
RUN set -ex \
    && sed -i 's/^# en_US.UTF-8 UTF-8$/en_US.UTF-8 UTF-8/g' /etc/locale.gen \
    && locale-gen en_US.UTF-8 \
    && update-locale LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8

# Install Python 3 packages
RUN mamba install --quiet --yes \
    'netCDF4' \
    && mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

RUN pip install --no-cache-dir \
    'execsql==1.111.0' \
    'plotly==5.11.0'

USER ${NB_UID}

WORKDIR "${HOME}"
