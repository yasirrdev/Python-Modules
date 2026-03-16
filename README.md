# 🐍 Python Modules --- 42 School Curriculum

A structured collection of Python exercises completed as part of the
**42 School curriculum**.

These modules progressively introduce advanced Python concepts --- from
**Object-Oriented Programming fundamentals** to **production-grade data
validation and environment management**.

The goal of this repository is to demonstrate clean architecture, modern
Python practices, and scalable code design.

------------------------------------------------------------------------

# 📚 Curriculum Overview

## 🌱 Module 01 --- The Garden

**Object-Oriented Programming**

Introduction to Python classes and core OOP principles.

Concepts covered:

-   Class design and constructors
-   Instance methods
-   Encapsulation using properties
-   Inheritance chains
-   Class and static methods

Implemented through a **garden ecosystem simulation**.

------------------------------------------------------------------------

## 🧩 Module 02 --- Cyber Archives

**Exception Handling**

Understanding Python's error-handling mechanisms.

Concepts covered:

-   `try / except / finally`
-   Custom exception hierarchies
-   Raising meaningful errors
-   Designing fault-tolerant programs

Focus: building **robust applications that gracefully recover from
failures**.

------------------------------------------------------------------------

## ⚔️ Module 03 --- Command Quest

**Data Structures & CLI Arguments**

Working with Python's fundamental data structures in practical CLI
applications.

Concepts covered:

-   `sys.argv` argument parsing
-   List / dict / set comprehensions
-   Generators using `yield`
-   Command-line data analytics pipelines

------------------------------------------------------------------------

## 📂 Module 04 --- Cyber Archives II

**File I/O & Streams**

Managing data persistence and system streams.

Concepts covered:

-   Reading and writing files
-   Context managers with `with`
-   stdout vs stderr handling
-   Secure file manipulation patterns

------------------------------------------------------------------------

## 🔗 Module 05 --- Code Nexus

**Protocols & Processing Pipelines**

Advanced architecture and polymorphism.

Concepts covered:

-   Abstract Base Classes (ABC)
-   Python **Protocols** for structural typing
-   Multi-stage processing pipelines
-   Adapter pattern
-   Error-resilient stream processing

------------------------------------------------------------------------

## 📦 Module 06 --- The Codex

**Python Import System**

Deep dive into Python's module and package system.

Concepts covered:

-   `__init__.py`
-   Absolute vs relative imports
-   Public API exposure
-   Avoiding circular dependencies
-   Deferred imports

------------------------------------------------------------------------

## 🃏 Module 07 --- DataDeck

**Design Patterns & Multiple Inheritance**

Development of a **Trading Card Game engine** to explore advanced
patterns.

Concepts covered:

-   Abstract Factory Pattern
-   Strategy Pattern
-   Multiple inheritance with interfaces
-   Modular architecture across multiple layers

------------------------------------------------------------------------

## 🌐 Module 08 --- The Matrix

**Environment & Package Management**

Real-world Python tooling used in data engineering.

Concepts covered:

-   Virtual environments
-   Dependency management (`pip`, `Poetry`)
-   Environment variables
-   `.env` configuration using `python-dotenv`

------------------------------------------------------------------------

## 🪐 Module 09 --- Cosmic Data

**Pydantic v2 Data Validation**

Production-grade data validation using **Pydantic v2**.

Concepts covered:

-   `BaseModel` and `Field`
-   Enum-based type safety
-   `@model_validator`
-   Nested model relationships
-   Strict schema validation

------------------------------------------------------------------------

# ⚙️ Technical Requirements

  Requirement   Version
  ------------- ----------------------------------------------
  Python        **3.10+**
  Linting       **flake8 compliant**
  Type System   **Type hints required**
  Environment   Virtual environment recommended (Module 07+)

------------------------------------------------------------------------

# 📦 Dependencies

    pydantic>=2.0
    pandas
    numpy
    matplotlib
    python-dotenv
    requests

Install dependencies:

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

# ▶️ Execution

### Modules 07+ (package-based)

Run from the repository root:

``` bash
python3 -m exN.main
```

Example:

``` bash
python3 -m ex07.main
```

------------------------------------------------------------------------

### Earlier Modules

Executed as standalone scripts:

``` bash
python3 script_name.py [arguments]
```

------------------------------------------------------------------------

# 📂 Project Structure

    python-modules/
    │
    ├── ex01/
    ├── ex02/
    ├── ex03/
    ├── ex04/
    ├── ex05/
    ├── ex06/
    ├── ex07/
    ├── ex08/
    └── ex09/

Each module contains independent exercises focusing on specific Python
concepts.

------------------------------------------------------------------------

# 🎓 Author

**Yasir**\
42 School Student

------------------------------------------------------------------------

💡 *This repository represents a progressive journey through Python's
ecosystem --- from fundamental language mechanics to production-grade
development practices.*
