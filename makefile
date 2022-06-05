
# Python Verification
$(info Verifying python installation...)

PYTHON=$(shell which python)

ifeq ($(PYTHON), )
  $(error "`python` not found in path")
endif

PYTHON_VERSION_MIN_MAJOR=3
PYTHON_VERSION_MIN_MINOR=10

PYTHON_VERSION_OK="$(shell $(PYTHON) -c 'import sys; print(all(map(lambda _: _[0] >= _[1], zip(sys.version_info[:2], ($(PYTHON_VERSION_MIN_MAJOR), $(PYTHON_VERSION_MIN_MINOR)) ))))' )"

ifeq ($(PYTHON_VERSION_OK), "False")
  $(error "Need python >= $(PYTHON_VERSION_MIN_MAJOR).$(PYTHON_VERSION_MIN_MINOR)")
endif

$(info )

init:
	@echo "Installing requirements.txt file..."
	$(PYTHON) -m pip install -r requirements.txt


.PHONY: init
