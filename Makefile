# ============================================================
# EPITECH_CONSOLE – Makefile
# ============================================================
# Usage:
#   make help
#   make install
#   make test
#   make demo
# ============================================================

# ------------------------------------------------------------
# CONFIGURATION
# ------------------------------------------------------------

PYTHON          ?= python3
PIP             ?= pip3
SHELL           := /bin/bash
SCRIPT_DIR      := script
PACKAGE_NAME    := epitech_console
VENV_DIR        := .venv

# Colors (safe for most terminals)
GREEN           := \033[0;32m
YELLOW          := \033[0;33m
RED             := \033[0;31m
NC              := \033[0m

# ------------------------------------------------------------
# DEFAULT TARGET
# ------------------------------------------------------------

.DEFAULT_GOAL := help

# ------------------------------------------------------------
# HELP
# ------------------------------------------------------------

help:
	@echo -e "$(GREEN)Available commands:$(NC)"
	@echo ""
	@echo -e "\tmake install\t\tInstall the package"
	@echo -e "\tmake uninstall\t\tUninstall the package"
	@echo -e "\tmake reinstall\t\tReinstall the package"
	@echo ""
	@echo -e "\tmake test\t\tRun test-package script"
	@echo -e "\tmake check\t\tRun check-package script"
	@echo ""
	@echo -e "\tmake demo\t\tRun full demo"
	@echo ""
	@echo -e "\tmake clean\t\tClean cache and build files"
	@echo -e "\tmake venv\t\tCreate a virtual environment"
	@echo -e "\tmake venv-install\tInstall package inside venv"
	@echo -e "\tmake info\t\tShow package info"
	@echo ""

# ------------------------------------------------------------
# PACKAGE MANAGEMENT
# ------------------------------------------------------------

install:
	@echo -e "$(GREEN)[INSTALL] Installing package$(NC)"
	@./$(SCRIPT_DIR)/install-package

uninstall:
	@echo -e "$(RED)[UNINSTALL] Uninstalling package$(NC)"
	@./$(SCRIPT_DIR)/uninstall-package

reinstall: uninstall install
	@echo -e "$(GREEN)[REINSTALL] Done$(NC)"

# ------------------------------------------------------------
# TESTS & CHECKS
# ------------------------------------------------------------

test:
	@echo -e "$(GREEN)[TEST] Running tests$(NC)"
	@./$(SCRIPT_DIR)/test-package

check:
	@echo -e "$(GREEN)[CHECK] Checking package$(NC)"
	@./$(SCRIPT_DIR)/check-package

# ------------------------------------------------------------
# DEMOS
# ------------------------------------------------------------

demo:
	@echo -e "$(GREEN)[DEMO] Running full demo$(NC)"
	@./$(SCRIPT_DIR)/full_demo

# ------------------------------------------------------------
# DEVELOPMENT UTILITIES
# ------------------------------------------------------------

venv:
	@echo -e "$(GREEN)[VENV] Creating virtual environment$(NC)"
	@$(PYTHON) -m venv $(VENV_DIR)
	@echo "Activate it with:"
	@echo "  source $(VENV_DIR)/bin/activate"

venv-install: venv
	@echo -e "$(GREEN)[VENV] Installing package in virtualenv$(NC)"
	@source $(VENV_DIR)/bin/activate && ./$(SCRIPT_DIR)/install-package

info:
	@echo -e "$(GREEN)[INFO] Package information$(NC)"
	@$(PIP) show $(PACKAGE_NAME) || echo "Package not installed"

# ------------------------------------------------------------
# CLEANUP
# ------------------------------------------------------------

clean:
	@echo -e "$(YELLOW)[CLEAN] Removing cache, test, log and build files$(NC)"
	@find . -type d -name "__pycache__" -exec rm -frd {} +
	@rm -frd *.egg-info *.xml trace htmlcov .pytest_cache epitech_console/log/*
	@echo -e "$(GREEN)[CLEAN] Done$(NC)"

# ------------------------------------------------------------
# SAFETY
# ------------------------------------------------------------

.PHONY: \
	help \
	install uninstall reinstall \
	test check \
	demo \
	venv venv-install \
	info clean