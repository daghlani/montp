FROM repo.admin.bs.bankmellat.ir/python:3.9

WORKDIR montp

COPY . .
RUN pip install --no-index --find-links pkg/ flask
CMD bash run.sh
