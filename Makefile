# Makefile for the experiments template repository
# This Makefile provides commands for setting up the development environment,
# running formatting tools, and cleaning the repository.

# Set the default target to 'help' when running make without arguments
.DEFAULT_GOAL := help

# Create a Python virtual environment using uv (faster alternative to venv)
venv:
	@curl -LsSf https://astral.sh/uv/install.sh | sh  # Install uv if not already installed
	@uv venv  # Create a virtual environment in the current directory


# Mark 'help' as a phony target (not associated with a file)
.PHONY: help
help:  ## Display this help screen
	@echo -e "\033[1mAvailable commands:\033[0m"  # Print header in bold
	# Find all targets with comments (##) and display them as a help menu
	# This grep/awk command extracts target names and their descriptions from the Makefile
	@grep -E '^[a-z.A-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}' | sort


# Mark 'clean' as a phony target
.PHONY: clean
clean: ## clean the folder
	# Remove all files and directories that are ignored by git
	# -d: include directories, -X: only remove files ignored by git, -f: force
	@git clean -d -X -f


# Mark 'fmt' as a phony target
.PHONY: fmt
fmt: venv ## Run autoformatting and linting
	@uvx pre-commit install  # Install pre-commit hooks in the git repository
	@uvx pre-commit run --all-files  # Run all pre-commit hooks on all files
