# Makefile consists: 
# 	Install requirements 
#	Run script
#	pytest
# 	unittest 

# Variables
PYTHON = python
MAIN_SCRIPT = main.py

# Set default make option
.DEFAULT_GOAL:=menu

# Targets
.PHONY: menu install run pytest unittest

# Print Makefile menu
menu:
	@echo Makefile Menu:
	@echo 1. Install requirements (make install)
	@echo 2. Run the script (make run)
	@echo 3. Run pytest on all tests (make pytest)
	@echo 4. Run unittest (make unittest)

# Install dependencies
install:
	pip install -r requirements.txt

# Run the Python script
run:
	$(PYTHON) $(MAIN_SCRIPT)

# Run pytest on tests
pytest:
	$(PYTHON) -m pytest tests/

# Run unittest
unittest:
	$(PYTHON) -m unittest tests/test_do_sparql_qyery_unittest.py