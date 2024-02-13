# README for WordPress Backup Server Scripts

This README outlines the use of a set of Python scripts designed for automating the setup of a WordPress backup server. These scripts are crucial for extracting a WordPress `.tbz` archive, importing a MySQL database dump, and updating domain names in the database and WordPress files to correspond with the new environment of the backup server.

## Prerequisites

- Python 3 installed on your system
- MySQL Server installed and operational
- Terminal or command prompt access

## Script Overview

The `master_script.py` orchestrates the execution of several scripts to streamline the preparation of a WordPress backup server. This process includes the extraction of WordPress site files, database importation, and the updating of domain names within both the database and site files.

## Master Script: Automated Execution

**Purpose:** Facilitates the execution of a sequence of scripts for setting up a WordPress backup server, including tasks such as file extraction, database importation, and domain updating.

**Usage Steps:**
1. Ensure the WordPress `.tbz` file and MySQL dump file are placed in the appropriate directory.
2. Update script variables with your database credentials, paths, and domain names as needed.
3. Execute the master script via Python 3:

'''python3 master_script.py'''

This execution will:
- Extract the WordPress `.tbz` archive.
- Import the MySQL database dump.
- Update all instances of the old domain to the new domain in the database.
- Replace the old domain with the new domain in WordPress files, including `.php`, `.js`, `.css`, and `.txt`.

## Script Details

- **Extract WordPress Archive:** Handles the extraction of the WordPress site from a `.tbz` file.
- **Import SQL Dump:** Manages the importation of the WordPress database dump into MySQL, ensuring the data is replicated on the backup server.
- **Update Domain in Database:** Adjusts references from the old domain to the new domain within the database, aligning links and references with the new environment.
- **Update Domain in Files:** Searches through WordPress files, updating any occurrence of the old domain with the new domain to ensure site consistency.

## General Guidelines

- Confirm you have the necessary permissions for script execution and database/file access.
- Conduct a backup of your database and files before running scripts that alter data.
- Customize the script variables (e.g., database credentials, file paths, domain names) to suit your backup server's specific configuration.

This guide aims to provide a clear method for utilizing the provided scripts to establish a WordPress backup server. For additional information or guidance, feel free to reach out.
