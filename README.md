# Python Modules — 42 School Curriculum

A structured collection of Python exercises completed as part of the 42 School curriculum.
Each module introduces progressively advanced concepts, from object-oriented fundamentals
to production-grade data validation and environment management.

---

## Curriculum Overview

### Module 01 — The Garden · *Object-Oriented Programming*
Introduction to Python classes and OOP principles. Covers constructors, instance methods,
encapsulation with properties, inheritance chains, and class/static methods through a
garden simulation.

### Module 02 — Cyber Archives · *Exception Handling*
Mastery of Python's error system. Covers try/except/finally blocks, custom exception
hierarchies, raising errors with meaningful messages, and building fault-tolerant programs
that recover gracefully from unexpected input.

### Module 03 — Command Quest · *Data Structures & Arguments*
Working with Python's core data structures in practical scenarios. Covers sys.argv
argument parsing, list/dict/set comprehensions, generators with yield, and analytics
pipelines processing command-line input.

### Module 04 — Cyber Archives II · *File I/O & Streams*
Managing data persistence and system streams. Covers reading and writing files, context
managers with the `with` statement, stdout/stderr separation, and building secure
file-handling systems.

### Module 05 — Code Nexus · *Protocols & Pipelines*
Advanced OOP architecture. Covers abstract base classes, Python Protocols for structural
typing, multi-stage processing pipelines, adapter patterns, and polymorphic stream
processing with error recovery.

### Module 06 — The Codex · *Python Import System*
Deep dive into Python's module system. Covers `__init__.py` and package initialization,
absolute vs relative imports, controlling public interfaces, and resolving circular
dependencies using deferred imports.

### Module 07 — DataDeck · *Design Patterns & Multiple Inheritance*
Building a trading card game engine to explore advanced OOP patterns. Covers the Abstract
Factory and Strategy patterns, multiple inheritance with ABC interfaces, and progressive
architecture across five interconnected exercise layers.

### Module 08 — The Matrix · *Environment & Package Management*
Real-world Python tooling for data engineering. Covers virtual environment creation and
detection, dependency management with pip and Poetry, and secure configuration using
environment variables and `.env` files with python-dotenv.

### Module 09 — Cosmic Data · *Pydantic v2 Data Validation*
Production-grade data validation using Pydantic v2. Covers BaseModel and Field
constraints, custom validation logic with `@model_validator`, enum-based type safety,
and nested model relationships for complex data structures.

---

## Technical Requirements

- Python 3.10 or later
- flake8 linter compliance across all modules
- Type hints on all functions and methods
- Virtual environment recommended for modules 07+

## Dependencies
```
pydantic>=2.0    pandas    numpy    matplotlib    python-dotenv    requests
```

## Execution

Modules 07+ use Python's package system and must be run from the repository root:
```bash
python3 -m exN.main
```

Earlier modules run as standalone scripts:
```bash
python3 script_name.py [arguments]
```

---

## Author

**Yasir** — 42 School Student
