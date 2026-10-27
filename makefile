# Quarto slides (the existing container target is preserved below).
.DEFAULT_GOAL := slides
QUARTO ?= quarto
PYTHON ?= python3
NOTEBOOK := greenland_2016_slides.ipynb
HTML := greenland_2016_slides.html
# Keep Quarto state inside this writable project, including in containers.
export XDG_CACHE_HOME := $(CURDIR)/.cache
export XDG_DATA_HOME := $(CURDIR)/.local/share

.PHONY: all slides preview regenerate clean
all: slides
slides: $(HTML)

$(HTML): $(NOTEBOOK) slides.css makefile
	$(QUARTO) render $(NOTEBOOK) --to revealjs --output $(HTML)

preview: slides
	$(QUARTO) preview $(NOTEBOOK) --to revealjs

# Optional: overwrites notebook edits with the original authored version.
regenerate:
	$(PYTHON) scripts/create_notebook.py

clean:
	$(RM) $(HTML)

#--- codex
BUILD_TAG := 
PORT := 8484
CONTAINER_NAME := codex_biomath
IMAGE := gjhunt/codex:24.04$(BUILD_TAG)
CONTAINERFILE := Containerfile

codex_container:
	podman run -it \
		-p 127.0.0.1:$(PORT):8080 \
		--name $(CONTAINER_NAME) \
		-e USE_HTTPS=false \
		-e USE_PASS=true \
		-v $$(pwd):/home/repro/codex \
        --userns=keep-id \
		$(IMAGE)
